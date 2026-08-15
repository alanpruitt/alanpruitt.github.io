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

function generateStaticHtml(article) {
  const { title, slug, summary, canonicalUrl, body } = article;
  const shareButtonsHtml = generateShareButtonsHtml({ ...article, url: canonicalUrl });

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
    ${shareButtonsHtml}
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

  // Resolves directly to the root /essays directory for GitHub Pages
  const outDir = resolve(`essays/${slug}`);
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
  console.log(`✅ Build Complete: essays/${slug}/index.html`);
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
