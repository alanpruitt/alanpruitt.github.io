import { readFileSync, writeFileSync, readdirSync, existsSync, mkdirSync } from 'fs';
import { resolve, join, basename } from 'path';

const SITE_ORIGIN = 'https://alanpruitt.com';
const CONTENT_DIR = resolve('content/essays');
const DIST_DIR = (process.env.GITHUB_ACTIONS === 'true') ? resolve('_site') : resolve('.');

function parseFrontmatter(rawContent) {
  const match = rawContent.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) return { metadata: {}, markdownBody: rawContent.trim() };

  const [, yamlBlock, markdownBody] = match;
  const metadata = {};

  let currentKey = null;
  yamlBlock.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) return;

    if (trimmed.startsWith('- ') && currentKey) {
      if (!Array.isArray(metadata[currentKey])) metadata[currentKey] = [];
      metadata[currentKey].push(trimmed.replace(/^- \s*/, '').replace(/^['"](.*)['"]$/, '$1'));
      return;
    }

    const [key, ...valParts] = line.split(':');
    if (key && valParts.length) {
      currentKey = key.trim();
      const val = valParts.join(':').trim();
      if (val) {
        metadata[currentKey] = val.replace(/^['"](.*)['"]$/, '$1');
      }
    }
  });

  return { metadata, markdownBody: markdownBody.trim() };
}

function escapeXml(unsafe) {
  return (unsafe || '').replace(/[<>&'"]/g, c => {
    switch (c) {
      case '<': return '&lt;';
      case '>': return '&gt;';
      case '&': return '&amp;';
      case '\'': return '&apos;';
      case '"': return '&quot;';
    }
  });
}

function generateShareButtonsHtml(article) {
  const canonicalUrl = encodeURIComponent(article.url || `https://alanpruitt.com/articles/${article.slug}.html`);
  const encodedTitle = encodeURIComponent(article.title);

  const linkedInUrl = `https://www.linkedin.com/sharing/share-offsite/?url=${canonicalUrl}`;
  const xUrl = `https://x.com/intent/post?text=${encodedTitle}&url=${canonicalUrl}&via=alanpruitt`;
  const redditUrl = `https://reddit.com/submit?url=${canonicalUrl}&title=${encodedTitle}`;
  const mailtoUrl = `mailto:?subject=${encodedTitle}&body=Read%20this%20Curriculum-as-Code%20architecture:%20${canonicalUrl}`;

  return `
    <!-- Zero-JS Semantic Social Share -->
    <div style="margin-top: 32px; padding-top: 24px; border-top: 1px solid var(--bg-creme-200, #E6E6DC); display: flex; flex-direction: column; gap: 16px;" aria-label="Social sharing options">
      <span style="font-family: monospace; font-size: 0.75rem; font-weight: bold; color: var(--navy-dark); text-transform: uppercase; tracking-wider">
        Share this Architecture:
      </span>
      <div style="display: flex; flex-wrap: wrap; gap: 8px; align-items: center;">
        <a href="${linkedInUrl}" target="_blank" rel="noopener noreferrer" aria-label="Share on LinkedIn" style="font-family: monospace; font-size: 0.75rem; font-weight: 600; text-decoration: none; padding: 6px 12px; border-radius: 8px; border: 1px solid var(--bg-creme-200, #E6E6DC); color: var(--navy-dark); background-color: var(--bg-cream);">
          LinkedIn
        </a>
        <a href="${xUrl}" target="_blank" rel="noopener noreferrer" aria-label="Share on X" style="font-family: monospace; font-size: 0.75rem; font-weight: 600; text-decoration: none; padding: 6px 12px; border-radius: 8px; border: 1px solid var(--bg-creme-200, #E6E6DC); color: var(--navy-dark); background-color: var(--bg-cream);">
          X
        </a>
        <a href="${redditUrl}" target="_blank" rel="noopener noreferrer" aria-label="Share on Reddit" style="font-family: monospace; font-size: 0.75rem; font-weight: 600; text-decoration: none; padding: 6px 12px; border-radius: 8px; border: 1px solid var(--bg-creme-200, #E6E6DC); color: var(--navy-dark); background-color: var(--bg-cream);">
          Reddit
        </a>
        <a href="${mailtoUrl}" aria-label="Share via Email" style="font-family: monospace; font-size: 0.75rem; font-weight: 600; text-decoration: none; padding: 6px 12px; border-radius: 8px; border: 1px solid var(--bg-creme-200, #E6E6DC); color: var(--navy-dark); background-color: var(--bg-cream);">
          Email
        </a>
      </div>
    </div>`;
}

function renderMarkdown(md) {
  // Simple markdown renderer
  return (md || '')
    .replace(/^## (.*$)/gim, '<h2>$1</h2>')
    .replace(/^### (.*$)/gim, '<h3>$1</h3>')
    .replace(/^# (.*$)/gim, '<h1>$1</h1>')
    .replace(/^\* (.*$)/gim, '<li>$1</li>')
    .replace(/```(bibtex|text)?\n([\s\S]*?)\n```/g, '<pre><code>$2</code></pre>')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>')
    .split(/\n\n+/).map(p => {
      const trimmed = p.trim();
      if (!trimmed) return '';
      if (trimmed.startsWith('<h') || trimmed.startsWith('<pre') || trimmed.startsWith('<li')) return trimmed;
      return `<p>${trimmed.replace(/\n/g, '<br>')}</p>`;
    }).join('\n');
}

function generateStaticHtml(article) {
  const { title, summary, canonicalUrl, body } = article;
  
  // Split at the Academic Citation & Attribution section header to isolate it
  const parts = body.split(/(?:##\s+Academic Citation|##\s+Citación\s+Académica)/i);
  const mainMarkdown = parts[0];
  const citationMarkdown = parts.length > 1 ? '## Academic Citation & Attribution\n' + parts.slice(1).join('## Academic Citation') : '';

  const renderedContent = renderMarkdown(mainMarkdown);
  const shareButtonsHtml = generateShareButtonsHtml({ ...article, url: canonicalUrl });
  const renderedCitation = citationMarkdown ? `<section style="margin-top: 32px; padding-top: 24px; border-top: 1px solid var(--bg-creme-200, #E6E6DC);">${renderMarkdown(citationMarkdown)}</section>` : '';

  return `<!DOCTYPE html>
<html lang="en" class="h-full scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${escapeXml(title)} | Coach Alan</title>
  <meta name="description" content="${escapeXml(summary || title)}">
  <link rel="canonical" href="${canonicalUrl}">
  
  <!-- Feed Discovery -->
  <link rel="alternate" type="application/rss+xml" title="Alan Pruitt - RSS Feed" href="${SITE_ORIGIN}/rss.xml">
  <link rel="alternate" type="application/feed+json" title="Alan Pruitt - JSON Feed" href="${SITE_ORIGIN}/feed.json">
  
  <!-- OpenGraph Metadata -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="${escapeXml(title)}">
  <meta property="og:description" content="${escapeXml(summary || title)}">
  <meta property="og:url" content="${canonicalUrl}">
  <meta property="og:site_name" content="alanpruitt.com">

  <!-- Premium Style Guard -->
  <style>
    :root {
      --bg-creme-50: #FAFBF7;
      --bg-creme-100: #F5F5F0;
      --bg-creme-200: #E6E6DC;
      --text-navy-800: #1E3E62;
      --text-navy-900: #0B192C;
      --text-navy-950: #060E1A;
      --link-accent: #0E3D73;
    }
    *, ::before, ::after { box-sizing: border-box; }
    html { line-height: 1.5; font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; height: 100%; }
    body { margin: 0; min-height: 100%; display: flex; flex-direction: column; justify-content: space-between; background-color: var(--bg-creme-100); color: var(--text-navy-900); }
    
    header { width: 100%; background-color: #ffffff; border-bottom: 1px solid var(--bg-creme-200); padding: 24px; box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05); }
    main { width: 100%; max-width: 780px; margin: 40px auto; padding: 0 20px; flex-grow: 1; }
    
    .content h2 { font-size: 1.5rem; font-weight: 700; color: var(--text-navy-900); margin-top: 2rem; margin-bottom: 1rem; }
    .content h3 { font-size: 1.25rem; font-weight: 700; color: var(--text-navy-900); margin-top: 1.5rem; margin-bottom: 0.75rem; }
    .content p { font-size: 1rem; color: #1a1a1a; line-height: 1.75; margin-bottom: 1.25rem; }
    .content ul, .content ol { margin-bottom: 1.25rem; padding-left: 1.5rem; }
    .content li { margin-bottom: 0.5rem; line-height: 1.6; }
    .content a { color: var(--link-accent); text-decoration: underline; font-weight: 600; }
    .content pre { background-color: var(--bg-creme-50); border: 1px solid var(--bg-creme-200); padding: 1rem; border-radius: 0.5rem; overflow-x: auto; margin-bottom: 1.25rem; font-family: monospace; font-size: 0.875rem; }
  </style>
</head>
<body class="bg-creme-100 text-navy-900 font-sans antialiased min-h-full flex flex-col justify-between">
  <!-- Navigation Header -->
  <header>
    <div style="max-width: 780px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between;">
      <a href="/" style="font-size: 1.125rem; font-weight: 700; color: var(--text-navy-900); text-decoration: none;">Alan Pruitt</a>
      <nav style="display: flex; gap: 24px;">
        <a href="/" style="font-size: 0.875rem; font-weight: 600; color: var(--text-navy-800); text-decoration: none;">Home</a>
        <a href="/articles/" style="font-size: 0.875rem; font-weight: 600; color: var(--text-navy-900); text-decoration: underline;">Articles</a>
      </nav>
    </div>
  </header>

  <main>
    <article class="content">
      <h1 style="font-size: 2rem; font-weight: 700; color: var(--text-navy-900); margin-top: 1rem; margin-bottom: 1.5rem;">${escapeXml(title)}</h1>
      ${renderedContent}
    </article>

    <!-- INJECT SOCIAL SHARE BLOCK -->
    ${shareButtonsHtml}

    <!-- Academic Citation & BibTeX Section -->
    ${renderedCitation}
  </main>

  <!-- Footer -->
  <footer style="width: 100%; padding: 32px 24px; text-align: center; font-size: 0.75rem; border-top: 1px solid var(--text-navy-950); background-color: var(--text-navy-900); color: var(--bg-creme-100);">
    <p style="margin-bottom: 8px;">© 2026 Alan Pruitt • All Rights Reserved.</p>
    <p style="opacity: 0.75; margin: 0;">Instructional Design, AI Pedagogy & Curriculum Architecture</p>
  </footer>
</body>
</html>`;
}

function generateRedirectHtml(targetCanonicalUrl) {
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=${targetCanonicalUrl}">
  <link rel="canonical" href="${targetCanonicalUrl}">
  <title>Redirecting to ${targetCanonicalUrl}</title>
  <script>window.location.replace('${targetCanonicalUrl}' + window.location.search + window.location.hash);</script>
</head>
<body style="font-family: sans-serif; padding: 20px; color: #1B2A4A;">
  <p>Redirecting to <a href="${targetCanonicalUrl}">${targetCanonicalUrl}</a>...</p>
</body>
</html>`;
}

function deriveAllSlugs(filename, metadata) {
  const fileBase = basename(filename, '.md').toLowerCase();
  const primarySlug = metadata.slug || fileBase;
  
  const slugs = new Set([primarySlug]);

  // Extract essay number if present (matches "18", "essay-18", "essay18", "18-the-title")
  const numberMatch = fileBase.match(/^(?:essay[-_]?)?(\d+)/i) || primarySlug.match(/^(?:essay[-_]?)?(\d+)/i);
  if (numberMatch) {
    const num = numberMatch[1];
    slugs.add(num);
    slugs.add(`essay-${num}`);
    slugs.add(`essay${num}`);
  }

  // Include explicit frontmatter aliases
  if (Array.isArray(metadata.aliases)) {
    metadata.aliases.forEach(alias => slugs.add(alias.toLowerCase().trim()));
  }

  return { primarySlug, allSlugs: Array.from(slugs) };
}

function buildGlobal404(routingMap) {
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Redirecting...</title>
  <script>
    (function() {
      var path = window.location.pathname.toLowerCase().replace(/^\/+|\/+$/g, '');
      var search = window.location.search || '';
      var hash = window.location.hash || '';
      
      var routingTable = ${JSON.stringify(routingMap, null, 2)};
      
      // Match direct path or nested essay paths
      if (routingTable[path]) {
        window.location.replace(routingTable[path] + search + hash);
        return;
      }
      
      // Fuzzy match essay number patterns (e.g. /essays/18 or /essay-18)
      var essayMatch = path.match(/(?:essays?\/)?(?:essay[-_]?)?(\d+)/);
      if (essayMatch && essayMatch[1]) {
        var num = essayMatch[1];
        if (routingTable['essays/' + num] || routingTable['essays/essay-' + num]) {
          var dest = routingTable['essays/' + num] || routingTable['essays/essay-' + num];
          window.location.replace(dest + search + hash);
          return;
        }
      }

      // Default fallback
      window.location.replace('https://alanpruitt.com/');
    })();
  </script>
</head>
<body style="font-family: sans-serif; padding: 20px; color: #1B2A4A; background-color: #FDFBF7;">
  <p>Locating resource and redirecting...</p>
</body>
</html>`;
}

function buildSitemap(essays) {
  const urls = [
    `  <url>\n    <loc>${SITE_ORIGIN}/</loc>\n    <changefreq>weekly</changefreq>\n    <priority>1.0</priority>\n  </url>`,
    ...essays.map(essay => `  <url>\n    <loc>${essay.canonicalUrl}</loc>\n    <lastmod>${essay.date}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>`)
  ];

  return `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.join('\n')}
</urlset>`;
}

function buildRss(essays) {
  const items = essays.map(essay => `    <item>
      <title>${escapeXml(essay.title)}</title>
      <link>${essay.canonicalUrl}</link>
      <guid isPermaLink="true">${essay.canonicalUrl}</guid>
      <pubDate>${new Date(essay.date).toUTCString()}</pubDate>
      <description>${escapeXml(essay.summary)}</description>
    </item>`).join('\n');

  return `<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Coach Alan Pruitt — Essays &amp; Curriculum Architecture</title>
    <link>${SITE_ORIGIN}</link>
    <description>Algorithmic pedagogy, curriculum architecture, and generative AI strategy.</description>
    <language>en-us</language>
    <atom:link href="${SITE_ORIGIN}/rss.xml" rel="self" type="application/rss+xml" />
${items}
  </channel>
</rss>`;
}

function generateJsonFeed(essays) {
  return JSON.stringify({
    version: "https://jsonfeed.org/version/1.1",
    title: "Coach Alan | Curriculum-as-Code Essays",
    home_page_url: "https://alanpruitt.com/",
    feed_url: "https://alanpruitt.com/feed.json",
    description: "Algorithmic pedagogy, CaC frameworks, and sovereign AI strategies.",
    items: essays.map(e => ({
      id: e.canonicalUrl,
      url: e.canonicalUrl,
      title: e.title,
      content_html: e.htmlContent,
      date_published: new Date(e.date).toISOString()
    }))
  }, null, 2);
}

function generateArchiveHtml(essays) {
  const essayListHtml = essays.map(essay => `
    <article style="margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid #E5E0D8;">
      <h3 style="margin-bottom: 6px;">
        <a href="${essay.canonicalUrl}" style="color: #0E3D73; text-decoration: underline; font-weight: 700;">
          ${escapeXml(essay.title)}
        </a>
      </h3>
      <p style="margin: 0 0 8px 0; color: #555555; font-size: 0.85rem;">
        Published: ${essay.date}
      </p>
      <p style="margin: 0; color: #222222; font-size: 0.95rem; line-height: 1.5;">
        ${escapeXml(essay.summary)}
      </p>
    </article>
  `).join('\n');

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>All Essays & Articles | Coach Alan</title>
  <meta name="description" content="Complete archive of essays, curriculum architecture frameworks, and algorithmic pedagogy writings.">
  <link rel="canonical" href="${SITE_ORIGIN}/essays/">
  
  <style>
    :root {
      --bg-cream: #FDFBF7;
      --navy-dark: #1B2A4A;
      --text-main: #222222;
      --link-accent: #0E3D73;
    }
    body {
      background-color: var(--bg-cream);
      color: var(--text-main);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      line-height: 1.6;
      max-width: 780px;
      margin: 40px auto;
      padding: 0 20px;
    }
    h2, h3 { color: var(--navy-dark); }
    a { color: var(--link-accent); }
    nav a { margin-right: 15px; font-weight: 600; }
  </style>
</head>
<body>
  <header style="margin-bottom: 30px;">
    <nav style="margin-bottom: 20px;">
      <a href="/">← Home</a>
    </nav>
    <h2>All Essays &amp; Articles</h2>
    <p style="color: #555555; font-size: 1rem;">
      Curriculum Architecture, Algorithmic Pedagogy &amp; Generative AI Strategy.
    </p>
  </header>
  <main>
    ${essayListHtml}
  </main>
</body>
</html>`;
}

function run() {
  if (!existsSync(DIST_DIR)) mkdirSync(DIST_DIR, { recursive: true });
  if (!existsSync(CONTENT_DIR)) {
    console.warn(`No content directory found at: ${CONTENT_DIR}`);
    return;
  }

  const files = readdirSync(CONTENT_DIR).filter(file => file.endsWith('.md'));
  console.log(`\n🚀 Initializing Dual-Route Generation across ${files.length} essay(s)...`);

  const essays = [];
  const routingMap = {};

  for (const file of files) {
    const fullPath = join(CONTENT_DIR, file);
    const raw = readFileSync(fullPath, 'utf-8');
    const { metadata, markdownBody } = parseFrontmatter(raw);

    const { primarySlug, allSlugs } = deriveAllSlugs(file, metadata);
    const canonicalUrl = `${SITE_ORIGIN}/essays/${primarySlug}`;
    const date = metadata.date || new Date().toISOString().split('T')[0];

    const essayData = {
      title: metadata.title || `Essay: ${primarySlug}`,
      slug: primarySlug,
      summary: metadata.summary || '',
      date,
      canonicalUrl,
      body: markdownBody,
      htmlContent: markdownBody.replace(/\n\n/g, '<p>').replace(/\n/g, '<br>')
    };
    essays.push(essayData);

    // 1. Generate Primary Canonical Page
    const primaryDir = resolve(DIST_DIR, `essays/${primarySlug}`);
    if (!existsSync(primaryDir)) mkdirSync(primaryDir, { recursive: true });
    writeFileSync(resolve(primaryDir, 'index.html'), generateStaticHtml(essayData), 'utf-8');

    // 2. Generate Physical Alias Fallback Directories
    for (const altSlug of allSlugs) {
      routingMap[`essays/${altSlug}`] = canonicalUrl;
      routingMap[altSlug] = canonicalUrl;

      if (altSlug !== primarySlug) {
        const aliasDir = resolve(DIST_DIR, `essays/${altSlug}`);
        if (!existsSync(aliasDir)) mkdirSync(aliasDir, { recursive: true });
        writeFileSync(resolve(aliasDir, 'index.html'), generateRedirectHtml(canonicalUrl), 'utf-8');
      }
    }

    console.log(`✅ Indexed ${primarySlug} -> [${allSlugs.join(', ')}]`);
  }

  // Sort newest first for chronological feed delivery
  essays.sort((a, b) => new Date(b.date) - new Date(a.date));

  // Register Archive Routes in Universal Router Table
  routingMap['articles'] = `${SITE_ORIGIN}/essays/`;
  routingMap['articles/index.html'] = `${SITE_ORIGIN}/essays/`;
  routingMap['essays'] = `${SITE_ORIGIN}/essays/`;
  routingMap['essays/index.html'] = `${SITE_ORIGIN}/essays/`;

  // Generate Global SPA 404 Fallback Router
  writeFileSync(resolve(DIST_DIR, '404.html'), buildGlobal404(routingMap), 'utf-8');
  console.log('🛡️ Generated: 404.html (Universal routing safeguard)');

  // 1. Sitemap
  writeFileSync(resolve(DIST_DIR, 'sitemap.xml'), buildSitemap(essays), 'utf-8');
  console.log('🗺️ Generated: sitemap.xml');

  // 2. RSS Feed (v2.0)
  writeFileSync(resolve(DIST_DIR, 'rss.xml'), buildRss(essays), 'utf-8');
  console.log('📡 Generated: rss.xml');

  // 3. JSON Feed (v1.1)
  writeFileSync(resolve(DIST_DIR, 'feed.json'), generateJsonFeed(essays), 'utf-8');
  console.log('📄 Generated: feed.json');

  // 1. Build Primary Archive: essays/index.html
  const essaysDir = resolve(DIST_DIR, 'essays');
  if (!existsSync(essaysDir)) mkdirSync(essaysDir, { recursive: true });
  writeFileSync(resolve(essaysDir, 'index.html'), generateArchiveHtml(essays), 'utf-8');
  console.log('📚 Generated Archive: essays/index.html');

  // 2. Build Alias / Backward-Compatible Archive: articles/index.html
  const articlesDir = resolve(DIST_DIR, 'articles');
  if (!existsSync(articlesDir)) mkdirSync(articlesDir, { recursive: true });
  writeFileSync(resolve(articlesDir, 'index.html'), generateArchiveHtml(essays), 'utf-8');
  console.log('📚 Generated Alias Archive: articles/index.html');

  console.log('\n🎉 Dual-Route generation and syndication builds complete.\n');
}

run();
