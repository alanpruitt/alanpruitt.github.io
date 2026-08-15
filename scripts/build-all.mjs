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

  // Generate Global SPA 404 Fallback Router
  writeFileSync(resolve(DIST_DIR, '404.html'), buildGlobal404(routingMap), 'utf-8');
  console.log('🛡️ Generated: _site/404.html (Universal routing safeguard)');

  console.log('\n Dual-Route generation complete for Essays 1–18 and future modules.\n');
}

run();
