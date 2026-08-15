#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..');

// Publication Metadata Configuration
const SITE_URL = 'https://alanpruitt.com';
const SITE_TITLE = 'Alan Pruitt | Curriculum-as-Code & AI Strategy';
const SITE_DESCRIPTION = 'Curriculum architecture, algorithmic pedagogy, sovereign AI strategies, and compliance frameworks by Alan Pruitt (Coach Alan).';
const AUTHOR_NAME = 'Alan Pruitt';
const AUTHOR_EMAIL = 'contact@webcognita.com';
const BUILD_DATE = new Date('2026-08-14T22:30:00Z');

// 1. Authoritative Essay Catalogue (SSoT Metadata Registry)
const ESSAYS = [
  {
    id: '19',
    slug: '19-hybrid-ergometer-scaffold',
    title: 'The Hybrid Ergometer Scaffold: Guided Simulation & Precision Testing (EXW245 Case Study)',
    date: '2026-08-15T12:00:00Z',
    summary: 'A clinical case study detailing how hybrid recumbent ergometry pacing protocols and digital predictive calculators isolate metabolic equations under ACSM 12th Ed guidelines.',
    tags: ['Kinesiology', 'Ergometry', 'ACSM', 'Pedagogy']
  },
  {
    id: '18',
    slug: '18-the-illusion-of-the-feed',
    title: 'The Illusion of the Feed: Upstream SSoT & Feed Link Rot Governance',
    date: '2026-08-14T12:00:00Z',
    summary: 'How relying on dynamic external feeds inside an LMS introduces link rot vulnerabilities, and how upstream SSoT configuration control resolves accessibility issues at the source.',
    tags: ['CurriculumAsCode', 'Compliance', 'Pedagogy', 'SSoT']
  },
  {
    id: '17',
    slug: '17-resolving-array-parsing-script-failures',
    title: 'Engineering Resilience: Resolving False-Positive Contrast Errors & Array Failures',
    date: '2026-08-07T12:00:00Z',
    summary: 'How automated accessibility checkers fail under WYSIWYG visual-editor DOM pollution and how Curriculum-as-Code resolves array parsing failures.',
    tags: ['CurriculumAsCode', 'Accessibility', 'DOM']
  },
  {
    id: '16',
    slug: '16-canvas-lms-3-track-ai-branch',
    title: 'Canvas LMS 3-Track Self-Guided AI Branch and Bilingual Scaffolding',
    date: '2026-07-31T12:00:00Z',
    summary: 'Transforming traditional online discussion boards into active, interdisciplinary clinical case conferences across all 16 EXW modules.',
    tags: ['CanvasLMS', 'Pedagogy', 'Bilingual']
  },
  {
    id: '15',
    slug: '15-algorithmic-pedagogy-ci',
    title: 'Algorithmic Pedagogy & Continuous Integration: Zero-Regression Learning',
    date: '2026-07-24T12:00:00Z',
    summary: 'Treating learning outcomes and compliance rules as executable code monitored by CI/CD.',
    tags: ['AlgorithmicPedagogy', 'CICD', 'CurriculumAsCode']
  },
  {
    id: '14',
    slug: '14-guided-learning-trifecta',
    title: 'The Guided Learning Trifecta: AI Simulation, Application & Auditing',
    date: '2026-07-17T12:00:00Z',
    summary: "Deploying Google's Guided Learning principles in Curriculum-as-Code via system prompts.",
    tags: ['GuidedLearning', 'AI', 'Prompts']
  },
  {
    id: '13',
    slug: '13-vibe-coding-paradigm',
    title: 'The Vibe-Coding Paradigm: Speed & Full-Stack Execution in EdTech',
    date: '2026-07-10T12:00:00Z',
    summary: 'Translating domain expertise directly into production-grade web applications using AI orchestration.',
    tags: ['VibeCoding', 'PWA', 'EdTech']
  },
  {
    id: '12',
    slug: '12-mission-loop-architecture',
    title: 'The Mission Loop Architecture: Pattern, Rule, and Solve in Coded Instruction',
    date: '2026-07-03T12:00:00Z',
    summary: 'Structuring deterministic health science problem-solving pipelines that enforce pattern identification.',
    tags: ['MissionLoop', 'Pedagogy', 'Kinesiology']
  },
  {
    id: '11',
    slug: '11-two-part-scaffold-framework',
    title: 'The Two-Part Scaffold Framework: Guided Simulation & Precision Testing',
    date: '2026-06-26T12:00:00Z',
    summary: 'Integrating AI simulation sandboxes with research-grade laboratory equipment.',
    tags: ['Scaffolding', 'Kinesiology', 'AI']
  },
  {
    id: '10',
    slug: '10-ai-safety-auditor-pattern',
    title: 'The AI Safety Auditor Pattern: Guardrailing In-LMS Student Simulations',
    date: '2026-06-19T12:00:00Z',
    summary: 'Deterministic verification protocols to prevent hallucination drift in academic environments.',
    tags: ['AISafety', 'AuditorPattern', 'Compliance']
  },
  {
    id: '09',
    slug: '09-immutable-learning-analytics',
    title: 'Immutable Learning Analytics: Privacy-Preserving Student Verification',
    date: '2026-06-12T12:00:00Z',
    summary: 'Auditing student engagement metrics with sovereign data privacy boundaries.',
    tags: ['Analytics', 'Privacy', 'Compliance']
  },
  {
    id: '08',
    slug: '08-bilingual-localization-pipelines',
    title: 'Bilingual Localization Pipelines in Higher Education',
    date: '2026-06-05T12:00:00Z',
    summary: 'Automating English/Spanish curriculum parity without semantic drift.',
    tags: ['Localization', 'Bilingual', 'Pedagogy']
  },
  {
    id: '07',
    slug: '07-continuous-integration-pedagogy',
    title: 'Continuous Integration in Course Pedagogy',
    date: '2026-05-29T12:00:00Z',
    summary: 'Automating curriculum deployment with GitHub Actions and Canvas API integrations.',
    tags: ['CICD', 'Automation', 'CurriculumAsCode']
  },
  {
    id: '06',
    slug: '06-canvas-ai-course-design',
    title: 'Canvas AI Course Design & Modular Architecture',
    date: '2026-05-22T12:00:00Z',
    summary: 'Designing high-touch student interaction tracks within learning management systems.',
    tags: ['CanvasLMS', 'Architecture', 'Pedagogy']
  },
  {
    id: '05',
    slug: '05-instructional-engineering',
    title: 'Instructional Engineering: Treating Pedagogy as Code',
    date: '2026-05-15T12:00:00Z',
    summary: 'Applying software engineering principles to academic curriculum design and maintenance.',
    tags: ['InstructionalEngineering', 'CurriculumAsCode']
  },
  {
    id: '04',
    slug: '04-ada-title-ii-accessibility',
    title: 'ADA Title II Compliance & WCAG 2.2 AA in Digital Classrooms',
    date: '2026-05-08T12:00:00Z',
    summary: 'Enforcing sovereign accessibility standards and programmatic contrast auditing across LMS pages.',
    tags: ['ADATitleII', 'WCAG', 'Accessibility']
  },
  {
    id: '03',
    slug: '03-air-gapped-sovereign-ai',
    title: 'Air-Gapped Sovereign AI in Community Colleges',
    date: '2026-05-01T12:00:00Z',
    summary: 'Deploying local open-weight models for zero-cost, private student compute.',
    tags: ['SovereignAI', 'AirGapped', 'CommunityColleges']
  },
  {
    id: '02',
    slug: '02-curriculum-as-code',
    title: 'Curriculum-as-Code: Version Control for Education',
    date: '2026-04-24T12:00:00Z',
    summary: 'Establishing Git as the Single Source of Truth for instructional design.',
    tags: ['CurriculumAsCode', 'Git', 'SSoT']
  },
  {
    id: '01',
    slug: '01-ai-assessment-design',
    title: 'AI Assessment Design: Beyond the Multiple Choice Question',
    date: '2026-04-17T12:00:00Z',
    summary: 'Designing authentic, interactive problem-solving evaluations using AI prompts.',
    tags: ['AIAssessment', 'Pedagogy', 'Prompts']
  }
];

// Helper: Escape XML Characters
function escapeXml(unsafe) {
  return unsafe.replace(/[<>&'"]/g, (c) => {
    switch (c) {
      case '<': return '&lt;';
      case '>': return '&gt;';
      case '&': return '&amp;';
      case '\'': return '&apos;';
      case '"': return '&quot;';
    }
  });
}

// 2. Generator: RSS 2.0 Feed (feed.xml & rss.xml)
function generateRss(essays) {
  const itemsXml = essays.map((essay) => {
    const url = `${SITE_URL}/articles/${essay.slug}.html`;
    const pubDate = new Date(essay.date).toUTCString();
    const categories = essay.tags.map(t => `      <category>${escapeXml(t)}</category>`).join('\n');

    return `    <item>
      <title>${escapeXml(essay.title)}</title>
      <link>${url}</link>
      <guid isPermaLink="true">${url}</guid>
      <pubDate>${pubDate}</pubDate>
      <description>${escapeXml(essay.summary)}</description>
      <author>${AUTHOR_EMAIL} (${AUTHOR_NAME})</author>
${categories}
    </item>`;
  }).join('\n');

  return `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>${escapeXml(SITE_TITLE)}</title>
    <link>${SITE_URL}/</link>
    <description>${escapeXml(SITE_DESCRIPTION)}</description>
    <language>en-us</language>
    <lastBuildDate>${BUILD_DATE.toUTCString()}</lastBuildDate>
    <atom:link href="${SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>
${itemsXml}
  </channel>
</rss>
`;
}

// 3. Generator: Atom RFC 4287 Feed (atom.xml)
function generateAtom(essays) {
  const entriesXml = essays.map((essay) => {
    const url = `${SITE_URL}/articles/${essay.slug}.html`;
    const updated = new Date(essay.date).toISOString();
    const categories = essay.tags.map(t => `    <category term="${escapeXml(t)}"/>`).join('\n');

    return `  <entry>
    <title>${escapeXml(essay.title)}</title>
    <link href="${url}" rel="alternate" type="text/html"/>
    <id>${url}</id>
    <updated>${updated}</updated>
    <published>${updated}</published>
    <summary type="text">${escapeXml(essay.summary)}</summary>
    <author>
      <name>${escapeXml(AUTHOR_NAME)}</name>
      <email>${escapeXml(AUTHOR_EMAIL)}</email>
      <uri>${SITE_URL}</uri>
    </author>
${categories}
  </entry>`;
  }).join('\n');

  return `<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>${escapeXml(SITE_TITLE)}</title>
  <subtitle>${escapeXml(SITE_DESCRIPTION)}</subtitle>
  <link href="${SITE_URL}/atom.xml" rel="self" type="application/atom+xml"/>
  <link href="${SITE_URL}/" rel="alternate" type="text/html"/>
  <id>${SITE_URL}/</id>
  <updated>${BUILD_DATE.toISOString()}</updated>
  <author>
    <name>${escapeXml(AUTHOR_NAME)}</name>
    <email>${escapeXml(AUTHOR_EMAIL)}</email>
    <uri>${SITE_URL}</uri>
  </author>
${entriesXml}
</feed>
`;
}

// 4. Generator: JSON Feed v1.1 (feed.json)
function generateJsonFeed(essays) {
  const feedObject = {
    version: 'https://jsonfeed.org/version/1.1',
    title: SITE_TITLE,
    home_page_url: `${SITE_URL}/`,
    feed_url: `${SITE_URL}/feed.json`,
    description: SITE_DESCRIPTION,
    user_comment: 'This feed allows programmatic consumers to ingest Curriculum-as-Code essays cleanly.',
    favicon: `${SITE_URL}/assets/og-preview.png`,
    authors: [
      {
        name: AUTHOR_NAME,
        url: SITE_URL,
        avatar: `${SITE_URL}/assets/Coach-Alan-Sketch-Headshot.webp`
      }
    ],
    items: essays.map((essay) => ({
      id: `${SITE_URL}/articles/${essay.slug}.html`,
      url: `${SITE_URL}/articles/${essay.slug}.html`,
      title: essay.title,
      summary: essay.summary,
      date_published: new Date(essay.date).toISOString(),
      tags: essay.tags
    }))
  };

  return JSON.stringify(feedObject, null, 2) + '\n';
}

// 5. Output Coordinator
function buildFeeds() {
  console.log('🚀 Compiling syndication feeds (RSS 2.0, Atom, JSON Feed)...');

  const rssContent = generateRss(ESSAYS);
  const atomContent = generateAtom(ESSAYS);
  const jsonContent = generateJsonFeed(ESSAYS);

  // Targets in Repository Root
  const targets = [
    { file: 'feed.xml', content: rssContent },
    { file: 'rss.xml', content: rssContent },
    { file: 'atom.xml', content: atomContent },
    { file: 'feed.json', content: jsonContent }
  ];

  targets.forEach(({ file, content }) => {
    const dest = path.join(ROOT_DIR, file);
    fs.writeFileSync(dest, content, 'utf8');
    console.log(` ✅ Generated ${file} -> ${dest}`);
  });

  // Mirror to _site directory if it exists
  const siteDir = path.join(ROOT_DIR, '_site');
  if (fs.existsSync(siteDir)) {
    targets.forEach(({ file, content }) => {
      const dest = path.join(siteDir, file);
      fs.writeFileSync(dest, content, 'utf8');
    });
    console.log(' ✅ Mirrored feed files to _site/ directory.');
  }

  console.log(`\n🎉 Successfully published 3-format syndication feeds for ${ESSAYS.length} essays.`);
}

buildFeeds();
