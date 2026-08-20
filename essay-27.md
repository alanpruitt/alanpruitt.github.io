# Essay 27: Curriculum-as-Code, ADA Title II Compliance, and Fleet-Wide Accessibility Refactoring

### Introduction
In modern instructional design, scaling course materials across a multi-course fleet requires a rigorous engineering approach. At Arizona Western College, my approach to building robust, equitable, and accessible learning environments for courses like EXW 101, 150, 245, and 265 relies on a **Curriculum-as-Code (C-as-C)** methodology. By treating curriculum files as version-controlled code, I can automate quality assurance, enforce strict institutional standards, and rapidly execute critical compliance refactors across live production shells.

### The Intersection of Curriculum-as-Code and the POUR Framework
Digital accessibility is frequently treated as an afterthought—a manual remediation checklist applied after a course goes live. However, by embedding accessibility guidelines directly into my repository structures, I operationalize compliance from inception. 

My integration of the **POUR framework (Perceivable, Operable, Understandable, and Robust)** into my C-as-C pipeline transforms accessibility from a static policy into an active, automated engineering standard:
*   **Perceivable:** I enforce high-contrast color palettes (such as Creme and Navy) and automated checks for descriptive alt text across all physiological diagrams and nutritional charts.
*   **Operable:** I ensure that my mobile-first Markdown and HTML layouts provide predictable, consistent navigation that works seamlessly across devices and assistive technologies.
*   **Understandable:** I utilize my consistent **Mission Loop** (Pattern / Rule / Solve) framework and my professional, supportive **Narrator voice** to maintain cognitive accessibility and clear readability.
*   **Robust:** I implement strict semantic HTML hierarchies (mandating that my content starts at `<h2>` and nests sequentially without skipping levels) so that screen readers interpret my course code reliably.

### Edge Use Case: Fleet-Wide Emoji and Icon Stripping for ADA Title II
A prime example of Curriculum-as-Code agility occurred during an active semester rollout in EXW 150. Recognizing that screen readers voice non-text symbols—such as decorative emojis and pictographs—as disruptive audio clutter (e.g., announcing "open book emoji" mid-sentence), and anticipating stricter upcoming **ADA Title II** mandates for public higher education, I identified a potential screen reader friction point. 

Rather than manually editing hundreds of pages across live Canvas production shells, I treated the issue as an infrastructure edge case:
1.  **Automated Scripting:** I engineered a recursive Python stripping utility (`scripts/strip_emojis.py`) designed to target and purge decorative unicode symbols and emoticons across all Markdown and HTML files in the repository.
2.  **Pipeline Integration:** I paired this with automated validation tools like `scripts/pour_audit.py` to continuously check semantic structures and heading hierarchies.
3.  **Synchronized Deployment:** I committed the refactor and force-pushed the synchronized updates across both `master` and `main` remote branches, instantly sanitizing the production environment before any student assistive technology friction could occur.

### Conclusion
Aligning my Curriculum-as-Code workflows with the POUR framework and automated refactoring scripts ensures that my wellness and physical education programs remain fully accessible under updated ADA Title II regulations. By engineering accessibility directly into our infrastructure, I guarantee that all of my students—regardless of ability or device—have equitable access to foundational kinesiology and nutrition principles.
