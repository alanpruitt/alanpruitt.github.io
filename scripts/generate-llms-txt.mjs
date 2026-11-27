import { readFileSync, writeFileSync, existsSync } from 'fs';
import { dirname, resolve } from 'path';
import { fileURLToPath } from 'url';

const REPO_ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');

/**
 * S-A-R v2.2 Guarded LLMs.txt Synchronizer
 * Prevents legacy pre-Hugo `articles/*.html` redirect stubs from clobbering
 * the canonical 42-essay + 11-PWA `llms.txt` and `llms-full.txt` manifests.
 */
function syncManifestPair(rootRel, staticRel) {
  const rootPath = resolve(REPO_ROOT, rootRel);
  const staticPath = resolve(REPO_ROOT, staticRel);
  if (!existsSync(rootPath) && !existsSync(staticPath)) {
    console.error(`Missing both ${rootRel} and ${staticRel}`);
    process.exit(1);
  }
  const sourcePath = existsSync(rootPath) ? rootPath : staticPath;
  const content = readFileSync(sourcePath, 'utf-8');
  if (content.includes('Redirecting to https://alanpruitt.com/essays/')) {
    console.error(`Refusing to sync redirect-stub clobbered ${sourcePath}`);
    process.exit(1);
  }
  writeFileSync(rootPath, content, 'utf-8');
  writeFileSync(staticPath, content, 'utf-8');
  console.log(`Synchronized canonical ${rootRel} <-> ${staticRel} (${content.length} chars)`);
}

syncManifestPair('llms.txt', 'static/llms.txt');
syncManifestPair('llms-full.txt', 'static/llms-full.txt');
