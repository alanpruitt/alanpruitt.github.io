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

  yamlBlock.split('\n').forEach(line => {
    const [key, ...valParts] = line.split(':');
    if (key && valParts.length) {
      metadata[key.trim()] = valParts.join(':').trim().replace(/^['"](.*)['"]$/, '$1');
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

function generateStaticHtml({ title, slug, summary, canonicalUrl, body }) {
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${escapeXml(title)} | Coach Alan</title>
  <meta name="description" content="${escapeXml(summary || title)}">
  <link rel="canonical" href="${canonicalUrl}">
  <link rel="alternate" type="application/rss+xml" title="Alan Pruitt - RSS Feed" href="${SITE_ORIGIN}/rss.xml">
  
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

function run() {
  if (!existsSync(DIST_DIR)) {
    mkdirSync(DIST_DIR, { recursive: true });
  }

  if (!existsSync(CONTENT_DIR)) {
    console.warn(`No content directory found at: ${CONTENT_DIR}`);
    return;
  }

  const files = readdirSync(CONTENT_DIR).filter(file => file.endsWith('.md'));
  console.log(`\n🚀 Processing ${files.length} essay file(s)...`);

  const essays = [];

  for (const file of files) {
    const fullPath = join(CONTENT_DIR, file);
    const raw = readFileSync(fullPath, 'utf-8');
    const { metadata, markdownBody } = parseFrontmatter(raw);

    const slug = metadata.slug || basename(file, '.md').toLowerCase();
    const canonicalUrl = `${SITE_ORIGIN}/essays/${slug}`;
    const date = metadata.date || new Date().toISOString().split('T')[0];

    const essayData = {
      title: metadata.title || 'Untitled Essay',
      slug,
      summary: metadata.summary || '',
      date,
      canonicalUrl,
      body: markdownBody
    };

    essays.push(essayData);

    // Build static folder: _site/essays/{slug}/index.html
    const essayOutDir = resolve(DIST_DIR, `essays/${slug}`);
    if (!existsSync(essayOutDir)) {
      mkdirSync(essayOutDir, { recursive: true });
    }

    const html = generateStaticHtml(essayData);
    writeFileSync(resolve(essayOutDir, 'index.html'), html, 'utf-8');
    console.log(`✅ Compiled HTML: essays/${slug}/index.html`);
  }

  // Sort newest first for RSS and feed syndication
  essays.sort((a, b) => new Date(b.date) - new Date(a.date));

  // Generate sitemap.xml and rss.xml
  writeFileSync(resolve(DIST_DIR, 'sitemap.xml'), buildSitemap(essays), 'utf-8');
  console.log('🗺️ Generated: _site/sitemap.xml');

  writeFileSync(resolve(DIST_DIR, 'rss.xml'), buildRss(essays), 'utf-8');
  console.log('📡 Generated: _site/rss.xml');

  console.log('\n🎉 Site build finished successfully.\n');
}

run();
