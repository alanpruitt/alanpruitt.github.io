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
  const { title, slug, summary, canonicalUrl, body } = article;
  
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
  <title>${title} | Coach Alan</title>
  <meta name="description" content="${summary || title}">
  <link rel="canonical" href="${canonicalUrl}">
  
  <!-- OpenGraph Metadata -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="${title}">
  <meta property="og:description" content="${summary || title}">
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
      <h1 style="font-size: 2rem; font-weight: 700; color: var(--text-navy-900); margin-top: 1rem; margin-bottom: 1.5rem;">${title}</h1>
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
