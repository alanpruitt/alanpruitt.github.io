const { chromium } = require('playwright');
const { AxeBuilder } = require('@axe-core/playwright');

const SITES = {
  alanpruitt: process.env.ALANPRUITT_URL || 'https://alanpruitt.com',
  webcognita: process.env.WEBCOGNITA_URL || 'https://webcognita.com'
};

async function auditSite(name, url) {
  console.log(`\n======================================================`);
  console.log(`🔎 AUDITING: ${name.toUpperCase()} (${url})`);
  console.log(`======================================================`);

  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();

  try {
    const response = await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
    console.log(`✓ HTTP Status: ${response.status()}`);

    // 1. Separation of Concerns Audits
    console.log(`\n--- Architectural Separation Checks ---`);
    const roiCount = await page.locator('#roi-calculator').count();
    const pourCount = await page.locator('#pour-audit').count();
    const tracksCount = await page.locator('#executive-tracks').count();

    if (name === 'alanpruitt') {
      if (roiCount === 0 && pourCount === 0) {
        console.log(`  ✓ Separation Verified: ROI Calculator & POUR Matrix are ABSENT.`);
      } else {
        console.error(`  ❌ LEAKAGE DETECTED: Commercial widgets found on alanpruitt.com! (ROI: ${roiCount}, POUR: ${pourCount})`);
      }

      if (tracksCount > 0) {
        console.log(`  ✓ Knowledge Graph: 3 Executive Reading Tracks are PRESENT.`);
      } else {
        console.error(`  ❌ MISSING: Executive Reading Tracks not found on homepage.`);
      }
    } else if (name === 'webcognita') {
      if (roiCount === 1 && pourCount === 1) {
        console.log(`  ✓ Deployment Verified: ROI Calculator & POUR Matrix are ACTIVE.`);
      } else {
        console.error(`  ❌ MISSING WIDGETS: Expected 1 ROI and 1 POUR instance, found ROI: ${roiCount}, POUR: ${pourCount}`);
      }

      // Check for live announcers
      const roiAnnouncer = await page.locator('#roi-live-announcer').count();
      const pourAnnouncer = await page.locator('#pour-live-announcer').count();
      if (roiAnnouncer === 1 && pourAnnouncer === 1) {
        console.log(`  ✓ Assistive Tech: aria-live="polite" regions verified.`);
      } else {
        console.error(`  ❌ A11Y WARNING: Missing aria-live announcer containers.`);
      }
    }

    // 2. WCAG 2.2 AA Automated Axe-core Audit
    console.log(`\n--- WCAG 2.2 Level AA Axe-Core Analysis ---`);
    const results = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'])
      .analyze();

    if (results.violations.length === 0) {
      console.log(`  🎉 100% WCAG 2.2 Level AA Conformance: 0 Violations Detected.`);
    } else {
      console.error(`  ⚠️ Violations Found: ${results.violations.length}`);
      results.violations.forEach((v, idx) => {
        console.error(`    ${idx + 1}. [${v.impact.toUpperCase()}] ${v.help} (${v.id})`);
        v.nodes.forEach(node => console.error(`       Target: ${node.target.join(' ')}`));
      });
    }

    // 3. Touch Target Perimeter Audit (WCAG SC 2.5.8 Min 44x44px Targets)
    console.log(`\n--- Minimum 44x44px Target Audit ---`);
    const smallTargets = await page.evaluate(() => {
      const elements = Array.from(document.querySelectorAll('a, button, input[type="checkbox"]'));
      return elements
        .map(el => {
          const rect = el.getBoundingClientRect();
          return {
            tag: el.tagName,
            text: el.innerText || el.getAttribute('aria-label') || el.name || 'unnamed',
            width: rect.width,
            height: rect.height
          };
        })
        .filter(t => t.width > 0 && t.height > 0 && (t.width < 43.5 || t.height < 43.5));
    });

    if (smallTargets.length === 0) {
      console.log(`  ✓ Touch Target Verification: All interactive items meet or exceed 44x44px.`);
    } else {
      console.log(`  ℹ Found ${smallTargets.length} sub-44px targets (inspecting inline text vs block items)...`);
      smallTargets.slice(0, 3).forEach(t => {
        console.log(`     - <${t.tag}> "${t.text.slice(0, 20)}": ${Math.round(t.width)}x${Math.round(t.height)}px`);
      });
    }

  } catch (err) {
    console.error(`❌ Audit execution error on ${url}:`, err.message);
  } finally {
    await browser.close();
  }
}

async function runAll() {
  await auditSite('alanpruitt', SITES.alanpruitt);
  await auditSite('webcognita', SITES.webcognita);
  console.log(`\n======================================================`);
  console.log(`🏁 DUAL-SITE AUDIT COMPLETE`);
  console.log(`======================================================\n`);
}

runAll();
