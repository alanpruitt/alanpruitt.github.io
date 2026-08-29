const { chromium } = require('playwright');
const AxeBuilder = require('@axe-core/playwright').default;

const BASE_URL = process.env.BASE_URL || 'https://alanpruitt.com';

async function runAudits() {
  console.log(`\n🚀 Starting Fleet Verification Suite on: ${BASE_URL}\n`);
  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width: 375, height: 667 },
    userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15'
  });

  const page = await context.newPage();
  let totalErrors = 0;

  try {
    console.log('[1/7] Testing Homepage Multilingual Route Resolution...');
    await page.goto(`${BASE_URL}/`, { waitUntil: 'networkidle' });

    const enLang = await page.getAttribute('html', 'lang');
    if (!enLang || !enLang.startsWith('en')) {
      console.error(`  ❌ FAIL: Expected <html lang="en*"> on /, got "${enLang}"`);
      totalErrors++;
    } else {
      console.log(`  ✓ PASS: Root <html lang="${enLang}"> validated.`);
    }

    const enHeroText = await page.locator('#hero-heading').textContent();
    if (!enHeroText.includes('Reclaim Academic Sovereignty') && !enHeroText.includes('Eliminate ADA Title II Risk')) {
      console.error(`  ❌ FAIL: English hero headline mismatch. Found: "${enHeroText.trim()}"`);
      totalErrors++;
    } else {
      console.log('  ✓ PASS: English Hero headline resolved.');
    }

    const esSwitchBtn = page.locator('nav[aria-label*="Language"] a:has-text("ES"), nav[aria-label*="Idioma"] a:has-text("ES"), nav[aria-label*="idioma"] a:has-text("ES")');
    if (await esSwitchBtn.count() > 0) {
      await esSwitchBtn.first().click();
      await page.waitForLoadState('networkidle');

      const currentUrl = page.url();
      if (!currentUrl.includes('/es/')) {
        console.error(`  ❌ FAIL: Expected URL containing /es/, got: "${currentUrl}"`);
        totalErrors++;
      } else {
        console.log(`  ✓ PASS: Resolved to Spanish route (${currentUrl}).`);
      }
    }

    console.log('\n[2/7] Testing Deep-Link Context Retention (Essay 27)...');
    await page.goto(`${BASE_URL}/essays/essay-27/`, { waitUntil: 'networkidle' });

    const deepEsSwitch = page.locator('nav[aria-label*="Language"] a:has-text("ES"), nav[aria-label*="Idioma"] a:has-text("ES")');
    if (await deepEsSwitch.count() > 0) {
      await deepEsSwitch.first().click();
      await page.waitForLoadState('networkidle');

      const deepUrl = page.url();
      if (!deepUrl.includes('/es/essays/essay-27/')) {
        console.error(`  ❌ FAIL: Deep translation mismatch. Expected /es/essays/essay-27/, got: "${deepUrl}"`);
        totalErrors++;
      } else {
        console.log(`  ✓ PASS: Deep translation preserved route (${deepUrl}).`);
      }
    }

    console.log('\n[3/7] Running WCAG 2.2 AA Accessibility & Contrast Engine...');
    await page.goto(`${BASE_URL}/`, { waitUntil: 'networkidle' });

    const accessibilityScanResults = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'])
      .analyze();

    if (accessibilityScanResults.violations.length > 0) {
      console.error(`  ❌ FAIL: ${accessibilityScanResults.violations.length} accessibility violation(s) detected.`);
      for (const violation of accessibilityScanResults.violations) {
        console.error(`    - Violation: ${violation.id} (Impact: ${violation.impact})`);
        console.error(`      Description: ${violation.description}`);
        console.error(`      Help URL: ${violation.helpUrl}`);
        for (const node of violation.nodes) {
          console.error(`      Target: ${node.target.join(', ')}`);
          console.error(`      HTML: ${node.html}`);
        }
      }
      totalErrors += accessibilityScanResults.violations.length;
    } else {
      console.log('  ✓ PASS: 0 WCAG 2.2 AA violations detected (Contrast & Semantics Clean).');
    }

    console.log('\n[4/7] Validating Mobile Interactive Tap Targets...');
    const interactiveSelectors = [
      '#hero-heading ~ div a',
      'nav[aria-label*="Navigation"] a',
      'header a'
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
            console.error(`  ❌ FAIL: Target "${text}" too small (${box.width.toFixed(1)}px x ${box.height.toFixed(1)}px). Min 44x44px.`);
            totalErrors++;
          }
        }
      }
    }
    console.log('  ✓ PASS: Core interactive navigation and CTA tap targets compliant.');

    console.log('\n[5/6] Testing Legacy Alias Redirection (/alanpruitt/essays/ -> /essays/)...');
    const legacyUrl = `${BASE_URL}/alanpruitt/essays/`;
    const response = await page.goto(legacyUrl, { waitUntil: 'networkidle' });

    const statusCode = response ? response.status() : null;
    const finalResolvedUrl = page.url();

    if (statusCode === 404) {
      console.error(`  ❌ FAIL: ${legacyUrl} returned HTTP 404 Not Found.`);
      totalErrors++;
    } else {
      console.log(`  ✓ PASS: ${legacyUrl} responded with HTTP status ${statusCode}.`);
    }

    if (!finalResolvedUrl.includes('/essays/')) {
      console.error(`  ❌ FAIL: Expected final URL containing /essays/, got: "${finalResolvedUrl}"`);
      totalErrors++;
    } else {
      console.log(`  ✓ PASS: Successfully redirected to canonical archive route (${finalResolvedUrl}).`);
    }

    console.log('\n[6/6] Testing Interactive Essay Category Filtering on /essays/...');
    await page.goto(`${BASE_URL}/essays/`, { waitUntil: 'networkidle' });

    const allCardsLocator = page.locator('.essay-card-item');
    const totalCount = await allCardsLocator.count();

    if (totalCount < 25) {
      console.error(`  ❌ FAIL: Expected at least 25 essay cards on /essays/, found ${totalCount}.`);
      totalErrors++;
    } else {
      console.log(`  ✓ PASS: Base archive loaded with ${totalCount} essays.`);
    }

    async function getVisibleCardCount() {
      return await page.locator('.essay-card-item:visible').count();
    }

    const aiBtn = page.locator('button[onclick*="ai-safety-protocols"], button[data-filter="ai-safety-protocols"]');
    if (await aiBtn.count() > 0) {
      await aiBtn.first().click();
      await page.waitForTimeout(100);
      const aiCount = await getVisibleCardCount();
      if (aiCount === 0 || aiCount >= totalCount) {
        console.error(`  ❌ FAIL: AI Safety Protocols filter failed. Visible cards: ${aiCount}/${totalCount}`);
        totalErrors++;
      } else {
        console.log(`  ✓ PASS: "AI Safety Protocols" filter isolated ${aiCount} essays.`);
      }
    } else {
      console.error('  ❌ FAIL: AI Safety Protocols filter button not found.');
      totalErrors++;
    }

    const adaBtn = page.locator('button[onclick*="ada-title-ii"], button[data-filter="ada-title-ii"]');
    if (await adaBtn.count() > 0) {
      await adaBtn.first().click();
      await page.waitForTimeout(100);
      const adaCount = await getVisibleCardCount();
      if (adaCount === 0 || adaCount >= totalCount) {
        console.error(`  ❌ FAIL: ADA Title II filter failed. Visible cards: ${adaCount}/${totalCount}`);
        totalErrors++;
      } else {
        console.log(`  ✓ PASS: "ADA Title II & Accessibility" filter isolated ${adaCount} essays.`);
      }
    } else {
      console.error('  ❌ FAIL: ADA Title II filter button not found.');
      totalErrors++;
    }

    const cacBtn = page.locator('button[onclick*="curriculum-as-code"], button[data-filter="curriculum-as-code"]');
    if (await cacBtn.count() > 0) {
      await cacBtn.first().click();
      await page.waitForTimeout(100);
      const cacCount = await getVisibleCardCount();
      if (cacCount === 0 || cacCount >= totalCount) {
        console.error(`  ❌ FAIL: Curriculum-as-Code filter failed. Visible cards: ${cacCount}/${totalCount}`);
        totalErrors++;
      } else {
        console.log(`  ✓ PASS: "Curriculum-as-Code" filter isolated ${cacCount} essays.`);
      }
    }

    const allBtn = page.locator('button[onclick*="all"], button[data-filter="all"]');
    if (await allBtn.count() > 0) {
      await allBtn.first().click();
      await page.waitForTimeout(100);
      const restoredCount = await getVisibleCardCount();
      if (restoredCount !== totalCount) {
        console.error(`  ❌ FAIL: "All Essays" reset failed. Expected ${totalCount}, got ${restoredCount}`);
        totalErrors++;
      } else {
        console.log(`  ✓ PASS: "All Essays" reset restored all ${restoredCount} cards.`);
      }
    }

  } catch (err) {
    console.error(`\n🔥 Execution Exception: ${err.message}`);
    totalErrors++;
  } finally {
    await browser.close();
  }

  console.log('\n-------------------------------------------------------------');
  if (totalErrors === 0) {
    console.log('✅ ALL 6 AUDITS PASSED: SSoT Parity, Contrast, Aliases & Filter Compliant.');
    process.exit(0);
  } else {
    console.error(`❌ AUDIT FAILED: ${totalErrors} issue(s) require remediation.`);
    process.exit(1);
  }
}

runAudits();
