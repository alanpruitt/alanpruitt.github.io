import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'fs';
import { resolve, basename } from 'path';

const SITE_ORIGIN = 'https://alanpruitt.com';

function parseFrontmatter(rawContent) {
  const match = rawContent.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) {
    throw new Error('Frontmatter missing or invalid YAML block.');
  }

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

function generateStaticHtml({ title, slug, summary, canonicalUrl, body }) {
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title} | Coach Alan</title>
  <meta name="description" content="${summary || title}">
  <link rel="canonical" href="${canonicalUrl}">
  
  <!-- OpenGraph Metadata -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="${title}">
  <meta property="og:description" content="${summary || title}">
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
    <h2>${title}</h2>
    <div class="content">
      ${body.replace(/\n\n/g, '<p>').replace(/\n/g, '<br>')}
    </div>
  </main>
</body>
</html>`;
}

function run() {
  const targetFile = process.argv[2];
  if (!targetFile) {
    console.error('Usage: node scripts/publish-essay.mjs <path-to-markdown-file>');
    process.exit(1);
  }

  const raw = readFileSync(resolve(targetFile), 'utf-8');
  const { metadata, markdownBody } = parseFrontmatter(raw);

  const slug = metadata.slug || basename(targetFile, '.md').toLowerCase();
  const canonicalUrl = `${SITE_ORIGIN}/essays/${slug}`;
  metadata.canonicalUrl = canonicalUrl;

  // Build target static directory: dist/essays/{slug}/index.html
  const outDir = resolve(`dist/essays/${slug}`);
  if (!existsSync(outDir)) {
    mkdirSync(outDir, { recursive: true });
  }

  const html = generateStaticHtml({
    title: metadata.title || 'Untitled Essay',
    slug,
    summary: metadata.summary || '',
    canonicalUrl,
    body: markdownBody
  });

  writeFileSync(resolve(outDir, 'index.html'), html, 'utf-8');

  // Print standardized distribution copy blocks
  console.log('\n======================================================');
  console.log(`✅ Build Complete: dist/essays/${slug}/index.html`);
  console.log(`🔗 Canonical SSoT: ${canonicalUrl}`);
  console.log('======================================================\n');

  console.log('### CANVAS / LMS EMBED SNIPPET ###');
  console.log(`> **${metadata.title}**\n> ${metadata.summary || ''}\n> \n> 🔗 **Read Full Essay (SSoT):** [${canonicalUrl}](${canonicalUrl})`);
  console.log('###\n');

  console.log('### LINKEDIN DISTRIBUTION SNIPPET ###');
  console.log(`${metadata.summary || metadata.title}\n\nRead the full breakdown in ${metadata.title}:\n${canonicalUrl}\n\n#CurriculumArchitecture #AIEducation #HigherEd`);
  console.log('###\n');
}

run();
