---
title: "3.1 Predictive Policing & Spatial-Temporal Risk Loops"
date: 2026-05-21
description: "Examining PredPol (Geolitica), historical arrest feedback loops, and mathematical distortions in urban crime prediction."
tags: ["criminal-justice", "surveillance", "predictive-policing", "geolitica"]
draft: false
---

# Predictive Policing & Spatial-Temporal Risk Loops

## Context & Systems Architecture
PredPol (later rebranded Geolitica) represents one of the most widely deployed predictive policing applications in the United States, integrated into major metropolitan departments including the LAPD and Chicago PD between 2011 and 2020. Marketed as an objective tool capable of identifying where crimes would occur before they happen, the software promised to optimize municipal resource allocation. However, the system's foundational architecture obscured a fundamental operational reality: the algorithm does not map actual criminal occurrences, but rather the historical deployment patterns of the law enforcement agency itself.

## DTPA Lens Breakdown

### Data
The model primarily ingests historical arrest records, official crime reports, and 911 emergency call dispatch logs. **Core Flaw:** This data represents an administrative reflection of police activity rather than an objective ground truth of human behavior. In practice, the historical over-policing of marginalized, lower-income neighborhoods and communities of color automatically populates the dataset with a disproportionate volume of arrests in those specific geographical zones. The data systematically treats police presence as an independent variable, confusing historical institutional focus with innate criminality.

### Tools
PredPol adapted the Epidemic-Type Aftershock Sequence (ETAS) model, a mathematical framework originally developed in seismology to predict earthquake aftershocks. The tool processes these spatial-temporal inputs to generate 500-foot by 500-foot tracking blocks on a digital map for upcoming shifts. Because the system utilizes non-linear machine learning pathways, the exact transactional criteria used to flag a specific block are hidden behind corporate trade secret boundaries, giving the output a false aura of clinical neutrality.

### Practices
On the operational level, patrol officers receive automated map-based hot-spot assignments at the beginning of their shifts. Because these grids are presented through an objective, data-driven software interface, human supervisors and field officers treat the targets with a high degree of automation bias. Officers are pushed to spend their uncommitted patrol time within these boxes, looking specifically for suspicious behaviors, which structurally ensures they will make more stops and arrests inside the designated zones.

### Actions
The structural action driven by this software is an aggressive, self-reinforcing **feedback loop**. The algorithm sends police officers to historically over-policed neighborhoods; because officers are concentrated there, they observe and arrest more individuals in those areas; these new arrests are then fed back into the training database as fresh "ground truth," prompting the model to generate the exact same hot-spot coordinates for the next shift. Independent statistical evaluations, including audits by the RAND Corporation, demonstrated no statistically significant reduction in crime attributable to the system, leading cities like Santa Cruz to explicitly ban the software.

---

## Connections to Perspective Markers
* **🏛️ STATE**: Deployed by institutional authorities to project systemic control and automate patrol surveillance under the banner of data-driven efficiency.
* **⬛ BOX**: The underlying proprietary weights and code parameters are closed off from criminal defense attorneys, preventing defendants from challenging the algorithmic justification for their initial stop.

## Cross-Cutting Themes
* **Theme 1: Feedback Loops**: The quintessential example of an algorithmic loop where output dictates the creation of its own future training data.
* **Theme 4: The Consent Gap**: Residents of targeted neighborhoods are subjected to heightened surveillance vectors without notification, oversight, or democratic recourse.

---

## References & Investigative Journalism
* **Lum, K., & Isaac, W.** (2016). *To predict and serve?* Significance, 13(5), 14–19.
* **Richardson, R., Schultz, J. M., & Crawford, K.** (2019). *Dirty Data, Bad Predictions: How Civil Rights Violations Impact Police Data, Predictive Policing Systems, and Justice.* New York University Law Review Online, 94.