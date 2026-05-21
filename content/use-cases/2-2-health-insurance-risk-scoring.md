---
title: "2.2 Health Insurance Risk Scoring"
date: 2026-05-21
description: "A landmark study analysis of proxy variable bias, commercial care management algorithms, and systemic racial discrimination in healthcare resource allocation."
tags: ["healthcare", "predictive-analytics", "racial-bias", "proxy-variables"]
draft: false
---

# Health Insurance Risk Scoring & Care Management

## Context & Systems Architecture
Commercial health insurance companies and integrated health networks rely heavily on predictive scoring algorithms to manage large patient populations. These tools generate a "risk score" for each patient to identify individuals with complex, chronic needs for enrollment in high-risk care management programs. These programs grant patients access to dedicated nursing staff, home health visits, and prioritized primary care appointments to prevent sudden hospitalization.

## DTPA Lens Breakdown

### Data
In a landmark 2019 study published in *Science*, Ziad Obermeyer and his research team analyzed a widely used commercial algorithm (Optum’s Impact Pro system, which evaluated over **200 million patients nationwide**). The algorithm utilized historical healthcare cost data—specifically, total prior-year insurance claim expenditures—as its primary data proxy for health need. This proxy variable was chosen because financial transaction logs are highly standardized, clean, and readily accessible at scale.

### Tools
The system used proprietary regression modeling to predict a patient's future medical expenditures. The resulting percentile score served as a direct indicator of clinical urgency. Because the system was commercial software, it operated as an un-auditable black box within clinical settings, insulating its underlying logic from independent validation.

### Practices
Hospital administrators and care coordination teams received ranked lists of patients. Individuals whose scores fell above the 97th percentile were automatically fast-tracked into the extra-care program, while those between the 55th and 97th percentiles were flagged for manual clinical review. The algorithm's internal mechanics were invisible to the doctors and nurses utilizing the output; it appeared as a neutral, objective technical optimization tool.

### Actions
Obermeyer’s team uncovered severe, systemic racial bias within the algorithm's outputs. Because of deeply entrenched structural racism and economic barriers, Black patients in the United States face lower access to health insurance, fewer local clinics, and systemic clinical bias, resulting in significantly lower medical spending relative to white patients with the same level of illness. 

As a direct result of using *cost* as a proxy for *health need*, the algorithm systematically underscored Black patients. The study revealed that at any given risk score, Black patients were substantially sicker than white patients, suffering from a higher burden of uncontrolled diabetes, hypertension, and renal failure. 

**The concrete impact:** If the algorithm had been corrected to evaluate actual health indicators (such as chronic conditions) rather than financial cost, the percentage of Black patients eligible for immediate care management enrollment would have risen from **17.7% to 46.5%**, nearly tripling their access to critical medical resources.

---

## Connections to Perspective Markers
* **🏛️ STATE / CORP**: Prioritizes financial predictability, corporate resource control, and cost minimization over equitable patient outcomes.
* **⬛ BOX**: The proprietary software architecture shielded its discriminatory impacts from hospital compliance teams until independent academics reverse-engineered the claims data.
* **🌳 SYSTEM**: Illustrates how long-standing historical inequalities are codified into software, transforming a history of poor medical access into an algorithmic declaration that marginalized patients require less care.

## Cross-Cutting Themes
* **Theme 2: Proxy Variables**: Explores the systemic failure of using financial expenditure as an unadjusted proxy for an individual's physical health needs.
* **Theme 1: Feedback Loops**: Denying preventative care management to sick, low-cost patients ensures they only receive emergency interventions, reinforcing unstable health profiles and driving erratic, fragmented cost data back into institutional systems.

---

## References & Investigative Journalism
* **Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S.** (2019). Dissecting racial bias in an algorithm used to manage the health of populations. *Science*, 366(6464), 447–453. [https://doi.org/10.1126/science.aax2342](https://doi.org/10.1126/science.aax2342)
* **Nature News.** (2019). *Millions of Black people affected by racial bias in health-care algorithms.* [https://www.nature.com/articles/d41586-019-03228-6](https://www.nature.com/articles/d41586-019-03228-6)
* **Benjamin, R.** (2019). Assessing risk, automating racism. *Science*, 366(6464), 421–422.