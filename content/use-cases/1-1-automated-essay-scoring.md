---
title: "1.1 Automated Essay Scoring (AES)"
date: 2026-05-21
description: "An analysis of automated text evaluation tools, surface feature proxies, and the systemic risks of algorithmic grading in high-stakes education."
tags: ["education", "nlp", "grading", "automated-essay-scoring"]
draft: false
---

# Automated Essay Scoring (AES)

## Context & Systems Architecture
Automated Essay Scoring (AES) systems utilize natural language processing (NLP) pipelines—ranging from traditional feature-extraction regression models (such as ETS's *e-rater*) to fine-tuned transformer networks (such as BERT variants)—to evaluate student writing. These systems are widely deployed by major assessment corporations, including Pearson, ETS, and Turnitin, to grade high-volume standardized tests, admissions essays, and placement exams. 

In a significant recent escalation of this technology, the Texas Education Agency deployed an automated scoring engine in 2024 to grade the State of Texas Assessments of Academic Readiness (STAAR) exams. The agency projected that the system would save **$15–$20 million annually** by reducing the number of human temporary graders from roughly 6,000 to under 2,000. However, the rollout resulted in widespread school district complaints after a dramatic surge in zero-scores for responses that did not fit the model's expected syntax paths.

## DTPA Lens Breakdown

### Data
Training datasets consist of historic student essays previously scored by human graders. These corpora are heavily skewed toward mainstream American academic English syntax, spelling conventions, and rhetorical patterns. Writing that features non-dominant regional variants, non-native syntax, or dialectical expressions (such as African American Vernacular English or Chicano English) is historically underrepresented in high-scoring tiers. The definition of "analytical writing" is implicitly baked into the corpus without structural transparency.

### Tools
The core tools are statistical regression and classification models optimized to map surface-level features to holistic human scores. Key variables include:
* Average sentence length variation
* Lexical density (vocabulary variety)
* Frequency of transitional markers (e.g., "therefore," "however")
* Spelling and grammatical error counts

Modern systems integrate large language models (LLMs) to perform semantic vector mapping, but the foundational optimization target remains the alignment with historic human score patterns rather than the comprehension of argumentation or truth.

### Practices
In low-stakes settings, AES tools serve as formative feedback mechanisms within Learning Management Systems (LMS). In high-stakes settings, the algorithmically generated score acts either as the final score or as an anchor that human reviewers must explicitly override. Research demonstrates an anchoring effect where human readers, facing high volume quotas, rarely challenge an algorithmic baseline score if it falls within an expected confidence band.

### Actions
Students writing unconventional but structurally sound or creative prose are systematically penalized by the model's inability to parse non-standard semantic transitions. Conversely, students can actively game the system. Dr. Les Perelman (MIT, 2012) demonstrated that his "BABEL Generator" could produce entirely nonsensical essays—constructed of complex, low-frequency vocabulary arranged in grammatically flawless but logically empty strings—that consistently received top marks from the commercial *e-rater* engine.

---

## Connections to Perspective Markers
* **🚀 HYPE**: Driven by administrative narratives of absolute grading consistency, elimination of human fatigue, and instant scalability across millions of students.
* **⬛ BOX**: The underlying feature weights and proprietary transformer embeddings are closely held trade secrets, preventing students or teachers from auditing why a specific writing sample failed.

## Cross-Cutting Themes
* **Theme 2: Proxy Variables**: Lexical complexity, sentence length, and transition word counts are treated as direct proxies for critical thinking and rigorous logical argumentation.
* **Theme 3: The Benchmark Illusion**: High statistical correlation between machine scores and human scores ($r \geq 0.85$) is used to claim system competence, masking the reality that both the machine and the human may be rewarding surface conformity rather than depth of understanding.

---

## References & Investigative Journalism
* **Perelman, L.** (2012). *Critique of Mark My Words* and the BABEL Generator Project. MIT Writing Across the Curriculum. [https://writing.mit.edu/wac/node/247](https://writing.mit.edu/wac/node/247)
* **Texas Tribune.** (2024). *Texas is using AI to grade STAAR written answers, saving money but sparking concern among educators.*
* **Deane, P.** (2013). On the relation between automated essay scoring and modern views of the writing construct. *Assessing Writing*, 18(1), 7–24.