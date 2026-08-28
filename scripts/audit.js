/**
 * scripts/audit.js
 * Automated Verification: Contrast, Touch Targets, and Multilingual Routing
 * SSoT Target: https://alanpruitt.com (or local http://localhost:1313)
 */

const { chromium } = require('playwright');
const AxeBuilder = require('@axe-core/playwright').default;

const BASE_URL = process.env.BASE_URL || 'https://alanpruitt.com';

async function runAudits() {
  console.log(`\n Starting Fleet Verification Suite on: ${BASE_URL}\n`);
  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width: 375, height: 667 }, // Mobile-first viewport (iPhone SE)
    userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15'
  });

  const page = await context.newPage();
  let totalErrors = 0;

  try {
    // -------------------------------------------------------------
    // TEST 1: Multilingual Homepage Routing & Switcher Parity
    // -------------------------------------------------------------
    console.log('[1/4] Testing Homepage Multilingual Route Resolution...');
    await page.goto(`${BASE_URL}/`, { waitUntil: 'networkidle' });

    // Check English Lang Attribute
    const enLang = await page.getAttribute('html', 'lang');
    if (!enLang || !enLang.startsWith('en')) {
      console.error(`  FAIL: Expected <html lang="en*"> on /, got "${enLang}"`);
      totalErrors++;
    } else {
      console.log(`  PASS: Root <html lang="${enLang}"> validated.`);
    }

    // Verify English Headline
    const enHeroText = await page.locator('#hero-heading').textContent();
    if (!enHeroText.includes('Reclaim Academic Sovereignty')) {
      console.error(`  FAIL: English hero headline mismatch. Found: "${enHeroText.trim()}"`);
      totalErrors++;
    } else {
      console.log('  PASS: English Hero headline resolved.');
    }

    // Trigger Spanish Switcher
    const esSwitchBtn = page.locator('nav[aria-label*="Language"] a:has-text("ES"), nav[aria-label*="idioma"] a:has-text("ES")');
    await esSwitchBtn.click();
    await page.waitForLoadState('networkidle');

    // Check Spanish Route Resolution
    const currentUrl = page.url();
    if (!currentUrl.includes('/es/')) {
      console.error(`  FAIL: Expected URL containing /es/, got: "${currentUrl}"`);
      totalErrors++;
    } else {
      console.log(`  PASS: Resolved to Spanish route (${currentUrl}).`);
    }

    const esLang = await page.getAttribute('html', 'lang');
    if (!esLang || !esLang.startsWith('es')) {
      console.error(`  FAIL: Expected <html lang="es*"> on /es/, got "${esLang}"`);
      totalErrors++;
    } else {
      console.log(`  PASS: Spanish <html lang="${esLang}"> validated.`);
    }

    // Verify Spanish Headline
    const esHeroText = await page.locator('#hero-heading').textContent();
    if (!esHeroText.includes('Recupera la soberanía académica')) {
      console.error(`  FAIL: Spanish hero headline mismatch. Found: "${esHeroText.trim()}"`);
      totalErrors++;
    } else {
      console.log('  PASS: Spanish Hero headline resolved.');
    }

    // -------------------------------------------------------------
    // TEST 2: Deep-Page Context Preservation (Essay 27 Route Pairing)
    // -------------------------------------------------------------
    console.log('\n[2/4] Testing Deep-Link Context Retention (Essay 27)...');
    await page.goto(`${BASE_URL}/essays/essay-27/`, { waitUntil: 'networkidle' });

    // Click Spanish toggle on Essay 27
    const deepEsSwitch = page.locator('nav[aria-label*="Language"] a:has-text("ES"), nav[aria-label*="idioma"] a:has-text("ES")');
    if (await deepEsSwitch.count() > 0) {
      await deepEsSwitch.first().click();
      await page.waitForLoadState('networkidle');

      const deepUrl = page.url();
      if (!deepUrl.includes('/es/essays/essay-27/')) {
        console.error(`  FAIL: Deep translation mismatch. Expected /es/essays/essay-27/, got: "${deepUrl}"`);
        totalErrors++;
      } else {
        console.log(`  PASS: Deep translation preserved route (${deepUrl}).`);
      }
    } else {
      console.warn('  WARN: Language switcher not found on Essay 27 template.');
    }

    // -------------------------------------------------------------
    // TEST 3: WCAG 2.2 AA Contrast & Accessibility Engine (Axe)
    // -------------------------------------------------------------
    console.log('\n[3/4] Running WCAG 2.2 AA Accessibility & Contrast Engine...');
    await page.goto(`${BASE_URL}/`, { waitUntil: 'networkidle' });

    const accessibilityScanResults = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'])
      .analyze();

    if (accessibilityScanResults.violations.length > 0) {
      console.error(`  FAIL: ${accessibilityScanResults.violations.length} accessibility violation(s) detected:`);
      accessibilityScanResults.violations.forEach((v) => {
        console.error(`    - [${v.id}] ${v.help} (Impact: ${v.impact})`);
        v.nodes.forEach((node) => console.error(`        Target: ${node.target}`));
      });
      totalErrors += accessibilityScanResults.violations.length;
    } else {
      console.log('  PASS: 0 WCAG 2.2 AA violations detected (Contrast & Semantics Clean).');
    }

    // -------------------------------------------------------------
    // TEST 4: Mobile Tap Target Size (WCAG 2.2 SC 2.5.8 - 44x44px min)
    // -------------------------------------------------------------
    console.log('\n[4/4] Validating Mobile Interactive Tap Targets...');
    const interactiveSelectors = [
      '#hero-heading ~ div a', // Hero CTAs
      'nav[aria-label*="Language"] a', // Language Switcher
      'header a' // Nav links
    ];

    for (const selector of interactiveSelectors) {
      const elements = page.locator(selector);
      const count = await elements.count();

      for (let i = 0; i < count; i++) {
        const el = elements.nth(i);
        const box = await el.boundingBox();
        const text = (await el.textContent()).trim();

        if (box) {
          const passesHeight = box.height >= 44;
          const passesWidth = box.width >= 44;

          if (!passesHeight || !passesWidth) {
            console.error(`  FAIL: Target "${text}" too small (${box.width.toFixed(1)}px x ${box.height.toFixed(1)}px). Min 44x44px.`);
            totalErrors++;
          } else {
            console.log(`  PASS: Target "${text}" size compliant (${box.width.toFixed(1)}px x ${box.height.toFixed(1)}px).`);
          }
        }
      }
    }

  } catch (err) {
    console.error(`\n Execution Exception: ${err.message}`);
    totalErrors++;
  } finally {
    await browser.close();
  }

  // Final Summary
  console.log('\n-------------------------------------------------------------');
  if (totalErrors === 0) {
    console.log('  ALL AUDITS PASSED: SSoT Parity, Contrast & Mobile Compliant.');
    process.exit(0);
  } else {
    console.error(`  AUDIT FAILED: ${totalErrors} issue(s) require remediation.`);
    process.exit(1);
  }
}

runAudits();
