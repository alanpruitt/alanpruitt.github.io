import { readFileSync, writeFileSync, readdirSync, existsSync } from 'fs';
import { resolve, join } from 'path';

const SITE_ORIGIN = 'https://alanpruitt.com';
const ARTICLES_DIR = resolve('articles');

function cleanHtmlToMarkdown(htmlContent) {
  let md = htmlContent
    .replace(/<h2[^>]*>([\s\S]*?)<\/h2>/gi, '\n\n## $1\n\n')
    .replace(/<h3[^>]*>([\s\S]*?)<\/h3>/gi, '\n\n### $1\n\n')
    .replace(/<p[^>]*>([\s\S]*?)<\/p>/gi, '\n$1\n')
    .replace(/<ul[^>]*>([\s\S]*?)<\/ul>/gi, '\n$1\n')
    .replace(/<li[^>]*>([\s\S]*?)<\/li>/gi, '* $1\n')
    .replace(/<strong[^>]*>([\s\S]*?)<\/strong>/gi, '**$1**')
    .replace(/<em[^>]*>([\s\S]*?)<\/em>/gi, '*$1*')
    .replace(/<code[^>]*>([\s\S]*?)<\/code>/gi, '`$1`')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&raquo;/g, '»')
    .replace(/&laquo;/g, '«')
    .replace(/&apos;/g, "'")
    .replace(/<[^>]+>/g, ''); // strip any remaining tags
  
  // Trim spaces and normalize double newlines
  return md.trim().replace(/\n{3,}/g, '\n\n');
}

function run() {
  if (!existsSync(ARTICLES_DIR)) {
    console.error('Articles directory not found!');
    return;
  }

  const files = readdirSync(ARTICLES_DIR)
    .filter(file => file.endsWith('.html') && file !== 'index.html' && !file.startsWith('essay-'));

  // Sort chronologically/numerically by essay number prefix (e.g. "01", "02"..."18")
  files.sort((a, b) => a.localeCompare(b));

  const essays = [];

  for (const file of files) {
    const fullPath = join(ARTICLES_DIR, file);
    const html = readFileSync(fullPath, 'utf-8');

    // Extract title
    const titleMatch = html.match(/<title>([\s\S]*?) \| Alan Pruitt<\/title>/i) || html.match(/<title>([\s\S]*?)<\/title>/i);
    let title = titleMatch ? titleMatch[1].trim() : file;
    // Clean potential prefix from title (e.g. "Essay 15: ")
    title = title.replace(/^(Essay \d+:\s*)+/i, '');

    // Extract English body
    const bodyMatch = html.match(/<div class="article-body" data-lang="en">([\s\S]*?)<div class="article-body[^"]*?" data-lang="es">/) ||
                      html.match(/<div class="article-body" data-lang="en">([\s\S]*?)<\/article>/);
    let body = '';
    if (bodyMatch) {
      body = bodyMatch[1].trim();
    } else {
      // Fallback for simple article structures (like Essays 15 and 16)
      const articleBodyMatch = html.match(/<article>([\s\S]*?)<\/article>/);
      if (articleBodyMatch) {
        body = articleBodyMatch[1].trim();
        // Remove header tags like h1
        body = body.replace(/<h1>[\s\S]*?<\/h1>/gi, '');
      }
    }

    // Extract summary
    const descMatch = html.match(/<meta name="description" content="([\s\S]*?)"/i);
    let summary = descMatch ? descMatch[1].trim() : '';
    if (!summary) {
      // Find the first paragraph that doesn't start with Author/Target
      const paragraphs = body.match(/<p[^>]*>([\s\S]*?)<\/p>/gi) || [];
      for (const p of paragraphs) {
        const text = p.replace(/<[^>]+>/g, '').trim();
        if (text && !text.startsWith('Author:') && !text.startsWith('Target:') && !text.startsWith('Curricular:')) {
          summary = text;
          break;
        }
      }
    }

    // Clean body HTML tags
    const cleanBody = cleanHtmlToMarkdown(body);

    const essayNum = file.match(/^(\d+)/)?.[1] || '';

    essays.push({
      number: essayNum,
      title,
      summary,
      url: `${SITE_ORIGIN}/articles/${file}`,
      body: cleanBody
    });
  }

  // 1. Generate llms.txt
  let llmsTxt = `# Alan Pruitt

> Personal portfolio, research hub, and sovereign Curriculum-as-Code (CaC) repository of Alan Pruitt.

## Essays

`;

  essays.forEach(essay => {
    llmsTxt += `- [Essay ${essay.number}: ${essay.title}](${essay.url}): ${essay.summary}\n`;
  });

  writeFileSync(resolve('llms.txt'), llmsTxt, 'utf-8');
  console.log('📚 Generated: llms.txt');

  // 2. Generate llms-full.txt
  let llmsFullTxt = `# Alan Pruitt Full Corpus

This file contains the complete text corpus of all essays and curriculum architecture articles by Alan Pruitt.

`;

  essays.forEach(essay => {
    llmsFullTxt += `\n---\n\n# Essay ${essay.number}: ${essay.title}\nURL: ${essay.url}\n\n${essay.body}\n`;
  });

  writeFileSync(resolve('llms-full.txt'), llmsFullTxt, 'utf-8');
  console.log('📚 Generated: llms-full.txt');
}

run();
