---
title: "3.3 Risk Assessment at Sentencing (COMPAS)"
date: 2026-05-21
description: "Examining the COMPAS recidivism risk score, ProPublica's mathematical bias investigation, and the fundamental incompatibility of algorithmic fairness criteria."
tags: ["criminal-justice", "predictive-analytics", "compas", "algorithmic-fairness", "civil-rights"]
draft: false
---

# Risk Assessment at Sentencing (COMPAS)

## Context & Systems Architecture
The Correctional Offender Management Profiling for Alternative Sanctions (COMPAS) is a proprietary machine learning classification tool developed by Northpointe (now Equivant). It is widely integrated into the United States criminal justice apparatus, specifically used by judges, parole officers, and corrections departments in states like Wisconsin, Florida, and New York to guide pre-sentencing reports, bail amounts, and parole determinations. The system is designed to predict a defendant's risk of recidivism—the statistical likelihood that an individual will commit another crime within a specified window (typically two years)—by computing an automated risk rating.

## DTPA Lens Breakdown

### Data
The foundational data layer relies on an expansive intake questionnaire consisting of **137 items**. These questions are answered via a mix of official administrative files and an interview with the defendant. The core structural flaw of the dataset lies in its systemic confounding variables. Rather than isolating innate behavioral patterns, the questionnaire captures social determinants of health and structural poverty. 

Questions investigate childhood residential instability ("How often did you move as a child?"), educational disruption, parental or family arrest records, employment history, and peer associations. Because centuries of systemic housing segregation, economic disinvestment, and racialized over-policing are concentrated within these exact socio-economic variables, the algorithm codifies poverty and structural racism as objective indicators of personal criminogenic risk.

### Tools
The tool itself is a closed-source, proprietary classification algorithm that processes the 137 features to output a score ranging from 1 (lowest risk) to 10 (highest risk). Because the software is guarded under trade-secret protections, the specific feature weightings, coefficients, and mathematical parameters are completely withheld from public scrutiny. 

In 2016, a landmark data journalism investigation by *ProPublica* audited two years of COMPAS scores for over 7,000 individuals in Broward County, Florida. The statistical analysis revealed a severe racial disparity in error rates: Black defendants who did not go on to reoffend were **falsely flagged as high-risk at twice the rate (44.9%)** of white defendants (23.5%). Conversely, white defendants who did go on to reoffend were far more likely to be **falsely flagged as low-risk (47.7%)** compared to Black recidivists (28.0%).

This sparked a historic academic debate in computer science. Equivant published a statistical rebuttal proving that the tool achieved **predictive parity**—meaning that a score of 7 carries the same statistical probability of reoffending whether the defendant is Black or white. Academic researchers, including Kleinberg et al. (2016), mathematically proved that it is **physically impossible** for an algorithm to satisfy both predictive parity (calibration) and equalized error rates (false positive/negative balance) simultaneously when the base rates of arrest differ between two populations. The tool's mathematical definition of "fairness" is fundamentally incompatible with civil rights definitions of equity.

### Practices
In active courtrooms, judges receive the automated COMPAS decimal score printed directly on pre-sentencing packets. This practice induces a powerful cognitive bias known as **anchoring**. Even when judges are explicitly instructed that the score is merely an auxiliary reference tool, the presentation of a clean, mathematical metric heavily biases their subsequent sentencing deliberations. 

The due process implications of this practice reached the Wisconsin Supreme Court in ***State v. Loomis* (2016)**. Eric Loomis challenged his six-year prison sentence, arguing that the judge's reliance on a closed-source algorithm violated his constitutional right to due process because he was barred from reviewing or cross-examining the software's internal logic. The Court upheld the use of COMPAS, ruling that while the tool's opacity is deeply concerning, it is permissible as long as the score is not the *sole* determinant of the sentence—a standard that is practically impossible to police given internal cognitive anchoring.

### Actions
The systemic action driven by COMPAS is the automation of mass incarceration under a veneer of mathematical objectivity. Because the algorithm treats structural disadvantages as individual criminality vectors, it locks marginalized populations into an inescapable judicial loop. High scores drive longer sentences and higher bail, which strips individuals of employment and housing stability, which in turn elevates their risk variables for subsequent assessments. This mechanism converts historical institutional bias into an immutable, forward-looking mathematical projection, rendering systemic inequality legally un-challengeable at the individual sentencing gate.

---

## Connections to Perspective Markers
* **🏛️ STATE**: Weaponized by judicial architectures to streamline the processing of human bodies while insulating institutional actors from the political accountability of sentencing decisions.
* **⬛ BOX**: The software operates inside a trade-secret black box, ensuring that criminal defense attorneys cannot audit the code that directly influences their clients' loss of liberty.
* **🌳 SYSTEM**: Highlights how algorithms scale systemic racism by substituting structural poverty and historical policing biases as objective proxies for individual recidivism risks.

## Cross-Cutting Themes
* **Theme 1: Feedback Loops**: High risk scores cause higher bail and longer sentences, which destroys familial and economic stability, creating the exact social decay that drives future arrests and validates the algorithm's initial guess.
* **Theme 3: The Benchmark Illusion**: The vendor boasts a high overall area under the curve (AUC) metric for predictive accuracy, concealing the fact that this performance is built on a highly inequitable distribution of false positive costs borne entirely by Black defendants.

---

## References & Investigative Journalism
* **Angwin, J., Larson, J., Mattu, S., & Kirchner, L.** (2016, May 23). *Machine Bias: There’s software used across the country to predict future criminals. And it’s biased against blacks.* ProPublica.
* **Larson, J., Mattu, S., Kirchner, L., & Angwin, J.** (2016, May 23). *How we analyzed the COMPAS recidivism algorithm.* ProPublica.
* **Dieterich, W., Mendoza, C., & Brennan, T.** (2016). *COMPAS Risk Scales: Demonstrating Accuracy Equity and Predictive Parity.* Northpointe Inc. Research Department.
* **Kleinberg, J., Mullainathan, S., & Raghavan, M.** (2016). *Inherent Trade-Offs in the Fair Determination of Risk Scores.* Proceedings of Innovations in Theoretical Computer Science (ITCS). arXiv:1609.05807.
* ***State v. Loomis***, 881 N.W.2d 749 (Wis. 2016).