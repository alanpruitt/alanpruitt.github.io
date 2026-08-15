import { readdirSync, existsSync, mkdirSync } from 'fs';
import { resolve, join } from 'path';
import { execSync } from 'child_process';

const CONTENT_DIR = resolve('content/essays');
const DIST_DIR = resolve('_site');

if (!existsSync(DIST_DIR)) {
  mkdirSync(DIST_DIR, { recursive: true });
}

if (existsSync(CONTENT_DIR)) {
  const files = readdirSync(CONTENT_DIR).filter(file => file.endsWith('.md'));
  
  console.log(`Found ${files.length} essay(s) to process...`);
  
  for (const file of files) {
    const fullPath = join(CONTENT_DIR, file);
    console.log(`Building: ${file}`);
    execSync(`node scripts/publish-essay.mjs "${fullPath}"`, { stdio: 'inherit' });
  }
} else {
  console.warn(`No content directory found at ${CONTENT_DIR}`);
}
