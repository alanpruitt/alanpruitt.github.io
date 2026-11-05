<!-- tests/fixtures/test_suite_failing.md -->

## EXW150: Nutrition for Sports & Exercise

This module examines dietary standards and athletic performance calculations based on federal nutritional benchmarks.

<!-- VIOLATION 1: RULE_HEAD_NO_SKIP (Skipped from h2 to h5) -->
<h5>Macronutrient Distribution Ranges</h5>

<p>Review the target carbohydrate intake guidelines below.</p>

<!-- VIOLATION 2: RULE_TABLE_CAPTION & RULE_TABLE_TH_SCOPE -->
<table class="nutrition-matrix">
  <thead>
    <tr>
      <th>Athlete Category</th>
      <th>Recommended CHO (g/kg/day)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Endurance</td>
      <td>6 - 10 g/kg</td>
    </tr>
  </tbody>
</table>

<!-- VIOLATION 3: RULE_ALT_EXISTS (Embedded HTML img tag missing alt) -->
<img src="glycogen_resynthesis_graph.png" width="600" height="400">

## Summary Checklist

- [ ] Complete dietary intake log
- [ ] Calculate relative carbohydrate ratios
