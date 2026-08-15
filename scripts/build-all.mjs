import { readFileSync, writeFileSync, readdirSync, existsSync, mkdirSync } from 'fs';
import { resolve, join, basename } from 'path';

const SITE_ORIGIN = 'https://alanpruitt.com';
const CONTENT_DIR = resolve('content/essays');
const DIST_DIR = resolve('_site');

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

function generateStaticHtml({ title, summary, canonicalUrl, body }) {
  return `<!DOCTYPE html>
<html lang="en">
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
    h1, h2, h3 { color: var(--navy-dark); }
    a { color: var(--link-accent); text-decoration: underline; font-weight: 600; }
  </style>
</head>
<body>
  <main>
    <h2>${escapeXml(title)}</h2>
    <div class="content">
      ${body.replace(/\n\n/g, '<p>').replace(/\n/g, '<br>')}
    </div>
  </main>
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

function buildJsonFeed(essays) {
  const feed = {
    version: "https://jsonfeed.org/version/1.1",
    title: "Coach Alan Pruitt — Essays & Curriculum Architecture",
    home_page_url: SITE_ORIGIN,
    feed_url: `${SITE_ORIGIN}/feed.json`,
    description: "Algorithmic pedagogy, curriculum architecture, and generative AI strategy.",
    authors: [
      {
        name: "Coach Alan Pruitt",
        url: SITE_ORIGIN
      }
    ],
    items: essays.map(essay => ({
      id: essay.canonicalUrl,
      url: essay.canonicalUrl,
      title: essay.title,
      summary: essay.summary,
      date_published: new Date(essay.date).toISOString(),
      content_html: essay.body.replace(/\n\n/g, '<p>').replace(/\n/g, '<br>')
    }))
  };

  return JSON.stringify(feed, null, 2);
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
      body: markdownBody
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
  console.log('🛡️ Generated: _site/404.html (Universal routing safeguard)');

  // 1. Sitemap
  writeFileSync(resolve(DIST_DIR, 'sitemap.xml'), buildSitemap(essays), 'utf-8');
  console.log('🗺️ Generated: _site/sitemap.xml');

  // 2. RSS Feed (v2.0)
  writeFileSync(resolve(DIST_DIR, 'rss.xml'), buildRss(essays), 'utf-8');
  console.log('📡 Generated: _site/rss.xml');

  // 3. JSON Feed (v1.1)
  writeFileSync(resolve(DIST_DIR, 'feed.json'), buildJsonFeed(essays), 'utf-8');
  console.log('📄 Generated: _site/feed.json');

  // 1. Build Primary Archive: _site/essays/index.html
  const essaysDir = resolve(DIST_DIR, 'essays');
  if (!existsSync(essaysDir)) mkdirSync(essaysDir, { recursive: true });
  writeFileSync(resolve(essaysDir, 'index.html'), generateArchiveHtml(essays), 'utf-8');
  console.log('📚 Generated Archive: _site/essays/index.html');

  // 2. Build Alias / Backward-Compatible Archive: _site/articles/index.html
  const articlesDir = resolve(DIST_DIR, 'articles');
  if (!existsSync(articlesDir)) mkdirSync(articlesDir, { recursive: true });
  writeFileSync(resolve(articlesDir, 'index.html'), generateArchiveHtml(essays), 'utf-8');
  console.log('📚 Generated Alias Archive: _site/articles/index.html');

  console.log('\n🎉 Dual-Route generation and syndication builds complete.\n');
}

run();
