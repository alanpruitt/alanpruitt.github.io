/**
 * scripts/audit-lighthouse.js
 * Automated Multi-Route Lighthouse v13 CI Gate (Standard Slow-4G + 4x CPU Mobile)
 * Enforces Quad-100 (100/100/100/100) + zero label-content-name-mismatch across
 * /, /curriculum-as-code/, and /research-log/.
 */

const { launch } = require('chrome-launcher');

const BASE_URL = (process.env.BASE_URL || 'http://localhost:1313').replace(/\/+$/, '');
const ROUTES = ['/', '/curriculum-as-code/', '/research-log/'];

async function runAudit() {
  const lighthouse = (await import('lighthouse')).default;

  console.log(`\n======================================================`);
  console.log(` Starting Multi-Route Lighthouse CI Gate: ${BASE_URL}`);
  console.log(`======================================================\n`);

  const chrome = await launch({ chromeFlags: ['--headless=new', '--disable-gpu', '--no-sandbox'] });
  let failures = 0;

  try {
    for (const route of ROUTES) {
      const url = `${BASE_URL}${route}`;
      const runnerResult = await lighthouse(url, {
        logLevel: 'error',
        output: 'json',
        onlyCategories: ['performance', 'accessibility', 'best-practices', 'seo'],
        port: chrome.port,
      });

      const report = runnerResult.lhr;
      const perf = Math.round(report.categories.performance.score * 100);
      const a11y = Math.round(report.categories.accessibility.score * 100);
      const bp = Math.round(report.categories['best-practices'].score * 100);
      const seo = Math.round(report.categories.seo.score * 100);
      const labelMismatch = report.audits['label-content-name-mismatch'];
      const mismatchCount =
        labelMismatch && labelMismatch.score === 0 && labelMismatch.details && labelMismatch.details.items
          ? labelMismatch.details.items.length
          : 0;

      console.log(` [ROUTE: ${route}]`);
      console.log(`  - Scores: Perf ${perf} | A11y ${a11y} | BP ${bp} | SEO ${seo}`);
      console.log(
        `  - CWV:    FCP ${report.audits['first-contentful-paint'].displayValue} | LCP ${report.audits['largest-contentful-paint'].displayValue} | TBT ${report.audits['total-blocking-time'].displayValue} | CLS ${report.audits['cumulative-layout-shift'].displayValue}`
      );
      console.log(`  - WCAG SC 2.5.3 Label Mismatches: ${mismatchCount}\n`);

      if (perf < 100 || a11y < 100 || bp < 100 || seo < 100 || mismatchCount > 0) {
        failures++;
        console.error(`  FAIL: ${url} fell below Quad-100 / zero-mismatch gate.\n`);
      }
    }
  } catch (err) {
    console.error(` Execution Error: ${err.message}`);
    process.exit(1);
  } finally {
    await chrome.kill();
  }

  if (failures > 0) {
    console.error(`FAIL: ${failures} route(s) failed the Quad-100 Lighthouse CI gate.`);
    process.exit(1);
  }

  console.log(`PASS: All ${ROUTES.length} pillar routes achieved 100/100/100/100 with 0 label mismatches.`);
  process.exit(0);
}

runAudit();
