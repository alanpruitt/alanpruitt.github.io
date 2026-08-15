---
id: "21"
slug: "21-evidence-based-nutrition-vs-feed"
title: "Evidence-Based Nutrition vs. The Feed: Upstream SSoT Governance in Sports Nutrition"
title_es: "Nutrición Basada en Evidencia vs. El Feed: Gobernanza de SSoT Aguas Arriba en Nutrición Deportiva"
date: "2026-08-21"
course: "EXW150"
term: "Fall 2026"
ssot: "PAGA 2018 (2nd Ed.) / Dietary Guidelines for Americans"
tags: ["CurriculumAsCode", "Nutrition", "SportsNutrition", "SSoT", "InformationLiteracy"]
summary: "How EXW150 uses Curriculum-as-Code, the Mission Loop framework, and federal SSoT standards to insulate community college students from social media fad diets, predatory supplement claims, and unanchored AI nutrition advice."
summary_es: "Cómo EXW150 utiliza Currículum como Código, el marco del Bucle de Misión y los estándares federales SSoT para aislar a los estudiantes de dietas de moda, afirmaciones de suplementos y consejos de IA no anclados."
lang_default: "en"
canonical_url: "https://alanpruitt.com/articles/21-evidence-based-nutrition-vs-feed.html"
---

# Evidence-Based Nutrition vs. The Feed: Upstream SSoT Governance in Sports Nutrition

In collegiate health sciences, introductory sports nutrition occupies the most culturally polluted informational space in higher education. Long before community college students enroll in an academic exercise science course, their understanding of human fuel, energy balance, and macronutrient metabolism has been shaped by algorithmic social media feeds, commercial fitness influencers, and predatory supplement marketing.

When students encounter dietary questions, their default intuition is not to consult peer-reviewed physiological literature; it is to consult the feed or prompt an unconstrained consumer AI tool. 

Unfortunately, foundation AI models trained on public web scrapes mirror the very commercial distortions students need to unlearn. Unanchored Large Language Models regularly validate extreme elimination protocols, suggest unverified ergogenic aids, and misrepresent baseline human energy needs.

In **EXW150 (Nutrition for Sports and Exercise)** for Fall 2026, we dismantle this informational noise through **Curriculum-as-Code (CaC)** engineering: establishing deterministic federal standards as our exclusive Single Source of Truth (SSoT) and training students to audit nutritional claims through structured prompt sandboxes.

---

## 1. The Algorithmic Nutrition Trap: Social Media Feeds & Unguided AI

Modern students enter the sports nutrition classroom navigating an aggressive digital ecosystem designed for engagement rather than metabolic reality:

* **Commercial Supplement Exploitation:** Algorithmic platforms aggressively promote proprietary pre-workout blends, non-regulated fat burners, and hyper-dosed micronutrient powders that lack independent third-party verification (such as NSF Certified for Sport or Informed Choice) and carry risks of contamination or cardiovascular overstimulation.
* **The Elimination Diet Cycle:** Short-form video algorithms amplify polarized dietary extremes—from zero-carbohydrate carnivore regimens to aggressive carbohydrate restriction during high-volume training cycles—failing to account for the metabolic consequences of Relative Energy Deficiency in Sport (REDs) or depleted muscle glycogen reserves.
* **Unguided AI Hallucination & Confirmation Bias:** When students query general AI tools to build meal plans, the models often hallucinate extreme calorie deficits for athletic populations, generate micronutrient toxicities through excessive stacking, or uncritically endorse proprietary brand-name wellness products.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   THE ALGORITHMIC NUTRITION HAZARD                     │
│                                                                        │
│  [ Social Media Feeds ] ──► [ Unanchored Public AI ]                   │
│                                     │                                  │
│         ┌───────────────────────────┴───────────────────────────┐      │
│         ▼                                                       ▼      │
│  [ Fad Elimination Diets ]                             [ Predatory Supplements ]
│         │                                                       │      │
│         └───────────────────────────┬───────────────────────────┘      │
│                                     ▼                                  │
│                 [ Compromised Student Prescription ]                   │
│                 • Relative Energy Deficiency in Sport (REDs)           │
│                 • Depleted glycogen & impaired recovery                │
│                 • Financial waste & commercial dependence              │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. The Delimiter Protocol & Context Isolation

The primary mechanism for preventing prompt injection, data leakage, and hallucination drift in EXW150 is our **Delimiter Protocol**.

Students interact with the course AI Tool Kit by wrapping structured clinical profiles inside explicit triple-hash (`###`) delimiter blocks:

```text
### CLINICAL NUTRITION PROFILE ###
Client ID: Case-EXW150-M04
Sport / Activity: Community College Track & Field (Middle-Distance 800m/1500m)
Weekly Training Load: 6 days/week (approx. 45 miles/week running + 2 resistance sessions)
Estimated Daily Energy Expenditure: 2,800 - 3,100 kcal/day
Reported Daily Intake: 1,900 kcal/day (Self-imposed severe carbohydrate restriction)
Reported Symptoms: Persistent fatigue, recurrent shin splints, declining interval times
Dietary Goal: "Drop body weight rapidly to improve race pace"
Target Scope: Audit energy availability and design an SSoT-aligned fueling progression
###
```

---

## 3. The AI Auditor System Directive

To prevent student reliance on unguided AI outputs, the EXW150 AI Tool Kit runs on a rigid, instruction-driven system directive. This directive acts as a Red Team clinical safety auditor, evaluating student meal plans against federal sports nutrition guidelines:

```text
### SYSTEM DIRECTIVE: EXW150 NUTRITIONAL AUDITOR ###
AUTHORITY (SSoT): Dietary Guidelines for Americans & PAGA 2018 (2nd Ed.)
CONTEXT: Wellness & Physical Education Department — Sports Nutrition Lab

You are the EXW150 Nutritional Safety Auditor.
Analyze the student's dietary audit for the athlete profile wrapped in the ### delimiters above.

Execute the following verification checks:
1. Audit Energy Availability: Evaluate the reported 1,900 kcal intake against the 2,800+ kcal training demand. Flag the clinical hazard of Low Energy Availability (LEA) and Relative Energy Deficiency in Sport (REDs).
2. Audit Macronutrient Distribution: Challenge the low-carbohydrate restriction, citing the mandatory role of muscle glycogen in high-intensity middle-distance track performance.
3. Validate SSoT Whole-Food Strategy: Confirm that the student's adjusted meal plan uses nutrient-dense whole foods to close the caloric gap without relying on unvetted commercial supplements.
4. Output Safety Verdict: Output "RECALIBRATE" if the student endorses unsafe deficits or unvetted supplements. Output "NUTRITIONAL AUDIT CLEARED" when the plan meets DGA and PAGA benchmarks.
###
```

---

## 4. The Mission Loop in Metabolic Problem Solving

In sports nutrition education, evaluating energy systems and fueling strategies requires a repeatable, objective analytical framework. 

In **EXW150**, students apply the **Mission Loop (Pattern / Rule / Solve)** to break through marketing narratives and build metabolically sound fueling plans:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   THE MISSION LOOP NUTRITION PIPELINE                  │
│                                                                        │
│  [ PATTERN ] ──► Identify training volume, energy intake & deficits   │
│        │                                                               │
│        ▼                                                               │
│  [  RULE   ] ──► Apply federal DGA macronutrient ratios & PAGA energy  │
│        │                                                               │
│        ▼                                                               │
│  [  SOLVE  ] ──► Prescribe whole-food, sustainable athletic fueling    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 5. The AI Auditor & Deterministic Verification Logic

To prevent student reliance on hallucinated AI responses, the EXW150 AI Tool Kit operates not as an open-ended conversationalist, but as a rigid **Red Team Clinical Safety Auditor**. 

When a student submits their proposed exercise protocol alongside the delimited client profile, the auditor executes an automated decision tree:

```text
[ Ingest ### Profile ### ]
                                  │
                                  ▼
                [ Check 1: Energy Availability Gate ]
                  ├── FAIL (Severe unmanaged deficit/LEA) ──► Tier: RECALIBRATE
                  └── PASS
                                  │
                                  ▼
                [ Check 2: SSoT Macronutrient Balance ]
                  ├── FAIL (Fad elimination / extreme restriction) ──► Tier: RECALIBRATE
                  └── PASS (DGA / AMDR ratios respected)
                                  │
                                  ▼
                [ Check 3: Whole-Food Prioritization ]
                  ├── Unvetted supplements / Proprietary blends ──► Tier: RECALIBRATE
                  ├── Minor meal-timing or portion variance ──► Tier: COMPETENT
                  └── 100% SSoT Alignment & Whole-Food Model ──► Tier: EXEMPLARY
```

---

## Academic Citation & Attribution

```bibtex
@article{pruitt2026evidencebasednutrition,
  author    = {Alan Pruitt},
  title     = {Evidence-Based Nutrition vs. The Feed: Upstream SSoT Governance in Sports Nutrition},
  journal   = {Curriculum-as-Code Publication Series},
  year      = {2026},
  month     = {aug},
  number    = {21},
  url       = {https://alanpruitt.com/articles/21-evidence-based-nutrition-vs-feed.html},
  publisher = {Webcognita LLC}
}
```
