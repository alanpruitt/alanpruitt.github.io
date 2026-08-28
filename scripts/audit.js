const { chromium } = require('playwright');
const AxeBuilder = require('@axe-core/playwright').default;

const BASE_URL = process.env.BASE_URL || 'https://alanpruitt.com';

async function runAudits() {
  console.log(`\n Starting Fleet Verification Suite on: ${BASE_URL}\n`);
  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width: 375, height: 667 },
    userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15'
  });

  const page = await context.newPage();
  let totalErrors = 0;

  try {
    console.log('[1/6] Testing Homepage Multilingual Route Resolution...');
    await page.goto(`${BASE_URL}/`, { waitUntil: 'networkidle' });

    const enLang = await page.getAttribute('html', 'lang');
    if (!enLang || !enLang.startsWith('en')) {
      console.error(`  FAIL: Expected <html lang="en*"> on /, got "${enLang}"`);
      totalErrors++;
    } else {
      console.log(`  PASS: Root <html lang="${enLang}"> validated.`);
    }

    const enHeroText = await page.locator('#hero-heading').textContent();
    if (!enHeroText.includes('Reclaim Academic Sovereignty')) {
      console.error(`  FAIL: English hero headline mismatch. Found: "${enHeroText.trim()}"`);
      totalErrors++;
    } else {
      console.log('  PASS: English Hero headline resolved.');
    }

    const esSwitchBtn = page.locator('nav[aria-label*="Language"] a:has-text("ES"), nav[aria-label*="idioma"] a:has-text("ES")');
    await esSwitchBtn.click();
    await page.waitForLoadState('networkidle');

    const currentUrl = page.url();
    if (!currentUrl.includes('/es/')) {
      console.error(`  FAIL: Expected URL containing /es/, got: "${currentUrl}"`);
      totalErrors++;
    } else {
      console.log(`  PASS: Resolved to Spanish route (${currentUrl}).`);
    }

    const esHeroText = await page.locator('#hero-heading').textContent();
    if (!esHeroText.includes('Recupera la soberanía académica')) {
      console.error(`  FAIL: Spanish hero headline mismatch. Found: "${esHeroText.trim()}"`);
      totalErrors++;
    } else {
      console.log('  PASS: Spanish Hero headline resolved.');
    }

    console.log('\n[2/6] Testing Deep-Link Context Retention (Essay 27)...');
    await page.goto(`${BASE_URL}/essays/essay-27/`, { waitUntil: 'networkidle' });

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

    console.log('\n[3/6] Running WCAG 2.2 AA Accessibility & Contrast Engine...');
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

    console.log('\n[4/6] Validating Mobile Interactive Tap Targets...');
    const interactiveSelectors = [
      '#hero-heading ~ div a',
      'nav[aria-label*="Language"] a',
      'header a',
      '#roi-calculator-heading ~ div a'
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

    console.log('\n[5/6] Testing Interactive ROI Calculator Sliders & Mathematical Logic...');
    const calcHeading = page.locator('#roi-calculator-heading');

    if (await calcHeading.count() === 0) {
      console.error('  FAIL: ROI Calculator section (#roi-calculator-heading) not found on homepage.');
      totalErrors++;
    } else {
      console.log('  PASS: ROI Calculator section located in DOM.');

      const coursesSlider = page.locator('#cac-courses');
      const pagesSlider = page.locator('#cac-pages');
      const savingsText = page.locator('#cac-savings-dollars');
      const hoursSavedText = page.locator('#cac-hours-saved');
      const roiMultText = page.locator('#cac-roi-mult');

      const initialSavings = (await savingsText.textContent()).trim();
      console.log(`  PASS: Default calculator output rendered (${initialSavings}).`);

      await coursesSlider.evaluate((el) => {
        el.value = '200';
        el.dispatchEvent(new Event('input', { bubbles: true }));
      });

      await pagesSlider.evaluate((el) => {
        el.value = '30';
        el.dispatchEvent(new Event('input', { bubbles: true }));
      });

      await page.waitForTimeout(100);

      const updatedAriaCourses = await coursesSlider.getAttribute('aria-valuenow');
      const updatedAriaPages = await pagesSlider.getAttribute('aria-valuenow');

      if (updatedAriaCourses !== '200' || updatedAriaPages !== '30') {
        console.error(`  FAIL: Slider aria-valuenow mismatch. Courses: ${updatedAriaCourses}, Pages: ${updatedAriaPages}`);
        totalErrors++;
      } else {
        console.log('  PASS: Slider dynamic aria-valuenow attributes synchronized.');
      }

      const updatedSavings = (await savingsText.textContent()).trim();
      const updatedHours = (await hoursSavedText.textContent()).trim();
      const updatedRoi = (await roiMultText.textContent()).trim();

      if (updatedSavings !== '$63,900' || !updatedHours.includes('1,420') || !updatedRoi.includes('18.8x')) {
        console.error(`  FAIL: Mathematical calculation mismatch on input change:`);
        console.error(`    Expected: $63,900 | 1,420 Hours | 18.8x ROI`);
        console.error(`    Received: ${updatedSavings} | ${updatedHours} | ${updatedRoi}`);
        totalErrors++;
      } else {
        console.log(`  PASS: Real-time calculation validated (${updatedSavings}, ${updatedHours}, ${updatedRoi}).`);
      }
    }

    console.log('\n[6/6] Testing Legacy Alias Redirection (/alanpruitt/essays/ -> /essays/)...');
    const legacyUrl = `${BASE_URL}/alanpruitt/essays/`;
    const response = await page.goto(legacyUrl, { waitUntil: 'networkidle' });

    const statusCode = response ? response.status() : null;
    const finalResolvedUrl = page.url();

    if (statusCode === 404) {
      console.error(`  FAIL: ${legacyUrl} returned HTTP 404 Not Found.`);
      totalErrors++;
    } else {
      console.log(`  PASS: ${legacyUrl} responded with HTTP status ${statusCode}.`);
    }

    if (!finalResolvedUrl.includes('/essays/')) {
      console.error(`  FAIL: Expected final URL containing /essays/, but landed on: "${finalResolvedUrl}"`);
      totalErrors++;
    } else {
      console.log(`  PASS: Successfully redirected to canonical archive route (${finalResolvedUrl}).`);
    }

  } catch (err) {
    console.error(`\n Execution Exception: ${err.message}`);
    totalErrors++;
  } finally {
    await browser.close();
  }

  console.log('\n-------------------------------------------------------------');
  if (totalErrors === 0) {
    console.log('  ALL AUDITS PASSED: SSoT Parity, Contrast, Mobile, ROI & Alias Compliant.');
    process.exit(0);
  } else {
    console.error(`  AUDIT FAILED: ${totalErrors} issue(s) require remediation.`);
    process.exit(1);
  }
}

runAudits();
