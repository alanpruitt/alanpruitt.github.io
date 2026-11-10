---
title: "Essay 34: From GSU Demo Day to Vibe-Coding – What Happens When You Stop Scrolling and Start Building"
slug: "essay-34-prompt-per-mile"
date: 2026-09-17T17:40:00-07:00
publishDate: 2026-09-17T17:40:00-07:00
draft: false
author: "Alan Pruitt"
categories:
  - "Curriculum-as-Code"
  - "Vibe-Coding"
  - "AI Literacy"
tags:
  - "Prompt-per-Mile"
  - "Rapid Prototyping"
  - "Sustainability"
  - "S-A-R Standard"
description: "From a LinkedIn question about GSU Demo Day train transit to shipping the live Prompt-per-Mile Offset Calculator in ten minutes using Curriculum-as-Code and rapid prototyping."
summary: "From a LinkedIn question about GSU Demo Day train transit to shipping the live Prompt-per-Mile Offset Calculator in ten minutes using Curriculum-as-Code and rapid prototyping."
aliases:
  - "/essays/34/"
  - "/essays/essay-34/"
  - "/essays/essay34/"
substack_url: "https://alanpruitt.substack.com/p/from-gsu-demo-day-to-vibe-coding"
---

## Turning Fleeting Curiosity into Shipped Architecture

It started with a simple, scroll-stopping question on LinkedIn:

> *"I took the train to the GSU Demo Day that showcased entrepreneurship in our business department. So now I'm wondering, does anyone have an ecology offset calculator for how many AI prompts I can get for a 10 mile train ride instead of a 10 mile drive? If that doesn't exist yet, which one of you will build one in the next ten minutes?"*

Most people read a prompt like that, smile at the clever analogy, drop a quick comment comparing carbon footprints, and keep scrolling.

**What if I didn't?**

What if, instead of treating a real-world quantitative question as fleeting social media banter, I treated it as an immediate engineering challenge? What happens when I refuse to let an engaging pedagogical opportunity get buried in the feed, and instead use my operational stack to ship a fully functional web utility in ten minutes?

When I apply my **Curriculum-as-Code (CaC)** philosophy, I do not wait for permission, a committee review, or a semester-long software procurement cycle. I build. Within minutes, I transformed that question into a responsive, live web application: my **[Prompt-per-Mile Offset Calculator](https://prompt-mile-hero.lovable.app)**.

Here is how I use a nimble, software-driven approach to content and ideation to make rapid prototyping repeatable, and why this agility changes instructional design and digital literacy.

---

## The Anatomy of the Thought Experiment: Transit vs. Compute

To build the calculator accurately on the fly, I first anchored the underlying algebra in transparent environmental and compute benchmarks rather than guesswork:

1. **The Transport Baseline:** Under standard EPA and passenger-rail emissions estimates, driving a conventional gasoline vehicle `10` miles emits roughly **`4.0 lbs` of CO2**, whereas a commuter rail trip emits roughly **`0.75 lbs`** over the same distance—yielding a net carbon savings of approximately **`3.25 lbs` of CO2**.
2. **The LLM Inference Factor:** A standard frontier large language model text query consumes roughly **`0.3 watt-hours (Wh)`** of electricity (comparable to running an LED bulb for a couple of minutes). Factoring in average U.S. grid carbon intensity (`~0.00085 lbs CO2/Wh`), I established a direct algebraic bridge between active transit and AI inference.
3. **The Conversion Equation:**

```text
P = (M * (E_car - E_train)) / (e_prompt * C_grid)
```

When I plug in a `10`-mile train commute, the equation reveals an intuitive comparison: a single low-carbon rail trip offsets roughly **`12,745` standard text prompts** or more than **`2,500` multi-step code-debugging queries**.

---

## Why Curriculum-as-Code Changes the Velocity of Teaching

In traditional higher education settings, translating an emerging classroom question into an interactive learning resource can take months of vendor tickets, LMS embeds, and administrative bottlenecks.

**What if I didn't rely on rented infrastructure and slow-moving pipelines?**

By applying my **Curriculum-as-Code** workflow—treating instructional ideas like repositories, authoring specifications in plain-text Markdown, and orchestrating rapid prototyping agents under human verification—I eliminate that friction:

* **Speed to Prototype:** I structure qualitative questions directly into explicit variables, algebraic constraints, and accessible UI specifications rather than static slide decks.
* **Modular Agility:** Just as I manage my multi-course `EXW` fleet and automated deployments, I can prototype a standalone zero-login Progressive Web App, verify contrast and keyboard accessibility, and publish it in minutes.
* **Experiential AI Literacy:** For my students and faculty peers, watching a real-world question become an interactive calculator demonstrates **The Centaur Protocol** in action—pairing human problem framing and domain math with high-velocity AI execution.

---

## Bridging Sustainability and Quantitative Digital Literacy

Beyond the rapid build itself, this exercise highlights a healthier way to teach digital sustainability. As generative AI becomes part of everyday occupational workflows, students rightly ask about its energy footprint.

By framing compute energy through concrete physical comparisons—such as walking, cycling, or riding transit instead of driving solo—I demystify watt-hours without alarmism and turn abstract energy metrics into verifiable, everyday decisions.

### Key Takeaways for Educators & Technologists

* **Capture Live Curiosity:** Some of the highest-engagement micro-simulations begin as spontaneous questions from colleagues or students.
* **Anchor Vibes in Deterministic Math:** Rapid prototyping ("vibe-coding") only holds educational value when the human architect defines and verifies the underlying equations first.
* **Ship Open Tools:** With modern AI-assisted engineering and sovereign CaC pipelines, faculty can build and share `$0 ZTC` interactive tools the same day a question arises.

* **Launch the Live Utility:** [Prompt-per-Mile Offset Calculator (`prompt-mile-hero.lovable.app`)](https://prompt-mile-hero.lovable.app)
* **Read the Substack Edition:** [From GSU Demo Day to Vibe-Coding (Substack)](https://alanpruitt.substack.com/p/from-gsu-demo-day-to-vibe-coding)

---

> **Disclaimer:** The Curriculum-as-Code architecture, S-A-R Standard, and open-source software tools described in this essay represent my independent faculty engineering and research through Webcognita LLC and do not represent official policy or endorsement by Arizona Western College or The University of Arizona.
