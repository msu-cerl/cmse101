---
title: "Case Design & Template"
date: 2026-08-24
draft: false
weight: 50
description: "Semester-long, scaffolded team project designing a proactive AI solution or a targeted AI restriction, with a built-in template."
tags: ["AI", "society", "assignments", "education"]
author: "Danny Caballero"
---

* **Students:** Teams of 3-4
* **Framework:** Data-Tools-Practices-Actions (DTPA)

The Case Design project is the principal assessment for the course. Your team develops one case, in stages, over the whole semester. Your chosen topic must be substantial enough in scope to warrant a group effort.

Unlike Case Studies, this is not three separate documents. It is **one document that grows**: your Final Case Design is a direct expansion of your Scaffold 2, which is a direct expansion of your Scaffold 1. Each scaffold gets instructor feedback, and the next scaffold must respond to that feedback in a separate document.

## Case Studies vs. Case Design

In your Case Studies, you **analyze** something that already happened. In the Case Design, you **propose** something that should happen. The DTPA framework is the same; the direction is reversed.

| | Case Study | Case Design |
|---|---|---|
| **Question** | What happened, and why? | What should be built, or what should be stopped? |
| **Evidence** | Documents a past deployment | Justifies a future decision |
| **DTPA** | Describes the case | Designs (Pathway I) or constrains (Pathway II) the system |
| **Format** | Structured template with prompts | Narrative report that grows over the semester |

Your Case Studies are the best preparation you have. Many strong Case Designs start from a case a group has already analyzed: if you studied a system that failed, Pathway II asks what restriction would have prevented it; if you studied a problem that went unsolved, Pathway I asks what a better system would look like.

## Choose a Pathway

| Pathway | Goal | What you must deliver |
|--------|------|------------------------|
| **I. Proactive AI Solution** | Design an AI application that directly addresses a societal problem. | Description of the application; explanation of how it works through Data, Tools, Practices, and Actions; analysis of its bias, ethical boundaries, and impact |
| **II. Targeted AI Restriction** | Propose a limit, safeguard, or policy constraint on an existing AI system whose deployment poses documented or predictable harm. | Identification of the risky system; evidence-based rationale for the restriction; DTPA analysis of why it's needed and how it would be implemented |

Both pathways require evidence-based arguments and APA-style citations: peer-reviewed journals, scientific reports, news coverage, empirical studies, economic projections, or historical documentation. See the [APA formatting guide](https://apastyle.apa.org/style-grammar-guidelines/references/examples).

### What a good topic looks like

As with Case Studies, a domain is not a topic. "AI in healthcare" is too broad for either pathway. Narrow until you can name who would use the system (Pathway I) or which system you would restrict and who would enforce the restriction (Pathway II).

The examples below show the level of specificity we are looking for. They are illustrations, not a menu.

* **Pathway I (too broad):** "Use AI to improve city services."
* **Pathway I (workable):** "A model that helps a mid-sized Michigan city predict which homes have lead service lines, designed so residents can see and challenge their home's prediction." *(Builds on the Flint case from Full Case I.)*
* **Pathway II (too broad):** "Regulate AI in insurance."
* **Pathway II (workable):** "A requirement that any Medicare prior-authorization denial flagged by an algorithm be reviewed by a clinician in the same specialty before the patient is notified, with denial and reversal rates published quarterly." *(Builds on the nH Predict and WISeR cases.)*

A useful test: could someone who disagrees with you argue against your proposal specifically? If the only possible objection is "AI is good" or "AI is bad," your topic is still too general.

## Milestones *(tentative dates)*

| Milestone | Due | Focus | Minimum length |
|-----------|-----|-------|-----------------|
| Teams formed | Week 5 (by Fri, Oct 2) | Pick a pathway and topic; meet with Danny (if needed) | — |
| **Scaffold 1** | Fri, Oct 9 | Problem, stakeholders, initial DTPA scoping | 750 words - [Google Doc Template](https://docs.google.com/document/d/1SYQ4dbPWlU8J2yQq3-Pgw-q28ODSqG9u2oDb8h-3pjI/edit?tab=t.zhren5lcocyh) (MSU Login required)|
| **Scaffold 2** | Fri, Nov 6 | Evidence base, full DTPA analysis, design direction, response to Scaffold 1 feedback | 1500 words & response-to-feedback document (>250 words) - [Google Doc Template](https://docs.google.com/document/d/1U8DhPCFB4Ji7uVfMtpzF0F-kyvGgnDHGswzVjE2Hjm0/edit?tab=t.zhren5lcocyh#heading=h.wj7uoxrbgnw1) (MSU Login required) |
| **Final Case Design** | Fri, Dec 4 | Full *draft* solution or restriction, response to Scaffold 2 feedback | 3000 words & response-to-feedback document (>250 words) |
| **Class Showcase** | Dec 7–11 | Team presentations & class feedback | 10 minutes + 2–3 min for questions |
| **Final deliverable** | Tue, Dec 15 | Final Case Design edited based on class feedback | 3000 words (due 11:59pm on the day of the final exam) |

Note: Word minimums exclude the separate response-to-feedback document, the reference list, and tables.

> There is no in-class final exam for CMSE 101; the class showcase and feedback (during the last week of classes) is intended to guide any final edits before Dec 15. **You may not turn in your final case design until after your group presents to the class.**

## Submission

All work is submitted using D2L. See the [syllabus](/syllabus/#case-design) for how Case Design factors into your final grade. Note that, unlike most assignments, the Final Case Design is not eligible for a second attempt; get as much value as you can out of the Scaffold feedback before then.

---

# How to Use the Template

Copy the whole template below into one shared document for your team. Complete **Part 1** for Scaffold 1. When Scaffold 2 is due, don't delete Part 1; expand it into **Part 2**, and address your instructor's feedback in a separate response document. Do the same again for **Part 3** at the final deadline. By the end, your one document tells the whole story of your case, start to finish.

## Writing a narrative report

Each Part is a **formal report written in paragraphs**, not a list of answers to prompts. The prompts in each section tell you what the section must cover; they are not questions to answer one by one. Use the section headings below, and write connected prose under each.

Tables are welcome where they genuinely help (comparing stakeholders, summarizing a plan), but the argument lives in the paragraphs.

The difference looks like this:

> **List-style (avoid):**
> *Data: Patient records. Collected by hospitals. Could be biased.*

> **Narrative (aim for):**
> *The model would be trained on five years of prior-authorization requests and outcomes from a single regional insurer. Because these records capture only patients who were insured and who sought care, they exclude people who never submitted a request, a group the Obermeyer et al. (2019) study suggests may be disproportionately Black and lower-income. Any denial pattern the model learns will reflect that insurer's past decisions, including its mistakes.*

The narrative version makes a specific claim, supports it with a source, and explains why it matters for the design. That is the habit we have practiced since Week 1.

## Keeping the document growing

Because each Part expands the previous one, you will revise earlier sections as you go. A few rules keep this manageable:

* **Revise in place.** When Part 2 improves your problem statement, update the Part 1 text rather than writing a second version. Your response-to-feedback document explains what changed.
* **Keep a running reference list** at the bottom of the document from day one.
* **Use Section 0** (below) for notes, links, and drafts. It does not count toward word minimums and is not graded, but it keeps useful work from getting lost.

---

## Case Design Template

* **Team members:**
* **Pathway chosen (I or II):**
* **Working title / topic:**

### Section 0: Your Notes and Research

Use this space for planning, links, notes, and early drafts. It is not graded and does not count toward word minimums. Keep it at the top of the document all semester.

---

### Part 1: Scoping (Scaffold 1) — Due Fri, Oct 9

**Goal:** Convince a reader that your problem or system is real, specific, and worth a semester of work, and show that you know where you will look next.

**Minimum:** 750 words, not counting the research map or team roles.

#### 1.1 Introduction: the problem or system (about 200 words)

Describe the societal problem you want to address (Pathway I) or the AI system you want to restrict (Pathway II). Be concrete: where does this happen, to whom, and how do you know?

* *Pathway I:* What is the problem, who experiences it, and what is currently done about it? Why hasn't the current approach solved it?
* *Pathway II:* What is the system, who built it, who deploys it, and what does it decide? What harm has it caused or is it likely to cause?

End the section with one sentence stating what your team intends to propose, even if it is tentative. For example: *"We propose a restriction requiring..."* or *"We propose a tool that would help..."*

#### 1.2 Why it matters (about 150 words)

Make the case that this problem or risk is significant, using **at least two cited sources**. Numbers help: how many people are affected, how much money is involved, how often the harm occurs. Say where each number comes from.

#### 1.3 Stakeholders (about 100 words)

Who has something at stake? Name at least three groups, and for each, say what they stand to gain or lose. Include at least one group with little power over the outcome: the people a system is used *on*, not just the people who use it. A short table is fine here, followed by a paragraph on which stakeholder your design will prioritize and why.

#### 1.4 Preliminary DTPA lens (about 300 words)

Write **one paragraph for each component**. At this stage, you are identifying what you will need to find out, not answering everything.

* **Data.** What data is involved (or would be), where it comes from, and who might be missing from it.
* **Tools.** What kind of system this is (a classifier, a predictive model, a generative model, a rule-based system) and what you already know about how it can fail.
* **Practices.** Who builds, buys, operates, and oversees the system, and whose labor it depends on.
* **Actions.** What the system decides or does, who benefits, who pays, and what behavior it rewards.

It is fine to end each paragraph with the question you most need to answer next.

#### 1.5 Research map (not counted toward word minimum)

List **4–6 sources** you plan to use, in APA format. Label each as *reporting*, *official record*, *organization's own account*, *research*, *advocacy*, or *first-hand account*, the same categories from the Full Case Update. Aim for at least two different kinds.

#### 1.6 Team roles (not counted toward word minimum)

Name a lead for each DTPA component and one person responsible for coordination (deadlines, consistency of voice, final proofreading). Every member should write; a lead is responsible for making sure their section is complete, not for writing it alone.

#### Before you submit Part 1

- [ ] Could a classmate state your problem or system in one sentence after reading 1.1?
- [ ] Does 1.2 include at least two cited sources with specific numbers or claims?
- [ ] Does 1.3 name at least one stakeholder with little power over the outcome?
- [ ] Does each DTPA paragraph in 1.4 say something specific to *your* case?
- [ ] Is the document written in paragraphs, proofread, and consistent in voice?

---

### Part 2: DTPA Analysis (Scaffold 2, expands Part 1) — Due Fri, Nov 6

**Goal:** Build the evidence base your final design will stand on, and commit to a direction.

**Minimum:** 1500 words across Parts 1 and 2 (revised), not counting the annotated bibliography, plus a separate response-to-feedback document (>250 words).

The level of detail for Part 2 should increase in both depth and sophistication; you have now completed two Full Case Studies. The [Case Study template](case-studies) is a good model for the depth expected in each DTPA section.

#### 2.0 Revise Part 1

Before writing new sections, revise Part 1 in response to instructor feedback. Your problem statement, stakeholders, and intended proposal should now be sharper than they were in October.

#### 2.1 Data (about 300 words)

Describe the dataset(s) involved in detail: how they are (or would be) collected, by whom, what is included and excluded, and how the data is categorized or encoded. Identify at least one specific way the data could encode bias, and cite evidence for it.

* *Pathway I:* What data would your system need? Does it exist, and who owns it? What would you do about groups the data misses?
* *Pathway II:* What data does the existing system use? What does the evidence show about who it misrepresents?

#### 2.2 Tools (about 300 words)

Describe the algorithm or model (classifier, predictive model, LLM, neural network, rule-based system), what it assumes, and its technical limits. Report accuracy or error figures where they exist, and say what they were measured on and compared to. Remember Week 2: accuracy alone tells you almost nothing.

* *Pathway I:* What kind of model would you use, and why that kind rather than another (or rather than no model at all)?
* *Pathway II:* What is known about how the system fails, and for whom?

#### 2.3 Practices (about 300 words)

Describe who creates, curates, deploys, and oversees the tool; whose labor it depends on; and what regulatory or institutional rules already apply. Distinguish critique (people objecting) from constraint (something that actually limits the system).

#### 2.4 Actions (about 300 words)

Describe what the system decides or does, who benefits, who may be harmed, and what incentives it creates. For Pathway II, describe the harm your restriction targets as concretely as possible. For Pathway I, describe what success would look like and how you would know.

#### 2.5 Design direction (about 200 words)

Describe, in a first draft, the solution or restriction you intend to propose. It does not need to be complete, but it must be specific enough for feedback. What does it do? Who implements it? Which part of your DTPA analysis does it respond to?

This section exists so that Part 3 is an expansion, not a leap. Instructor feedback on this section will be the most useful feedback you receive all semester.

#### 2.6 Annotated bibliography (not counted toward word minimum)

Full APA citations with a two-sentence annotation per source: the first sentence says what the source is and what it found; the second says how your team is using it. Aim for at least eight sources, drawing on at least three different kinds.

*(Attach separately: response to Scaffold 1 feedback.)*

#### Before you submit Part 2

- [ ] Did you revise Part 1 based on feedback, and does your response document point to each change?
- [ ] Does each DTPA section make specific claims with citations, not general statements?
- [ ] Does each accuracy or error figure say what it was measured on and compared to?
- [ ] Is your design direction specific enough that someone could disagree with it?
- [ ] Is the whole document proofread and consistent in voice?

---

### Part 3: Full Case Design (Final, expands Part 2) — Due Fri, Dec 4

**Goal:** Present a complete, evidence-based proposal: what should be built or restricted, how it would work, and what could go wrong.

**Minimum:** 3000 words across the whole report (revised), not counting references, plus a separate response-to-feedback document (>250 words).

Your final Case Design should read as one continuous report, from executive summary to conclusion. Earlier sections should be revised so they lead naturally into your proposal. The recommended structure below reorganizes Parts 1 and 2 into a final report.

#### 3.1 Executive summary (about 150 words)

A reader who stops here should know the problem, your proposed solution or restriction, and its expected impact. Write this section last.

#### 3.2 Introduction and significance (about 350 words)

Your revised Part 1 sections 1.1–1.3: the problem or system, why it matters, and who has a stake.

#### 3.3 DTPA analysis (about 1,200 words)

Your revised Part 2 sections 2.1–2.4, deepened with concrete evidence and direct citations. Each section should now point forward: what does this part of the analysis mean for your design?

#### 3.4 The proposal (about 500 words)

Describe your solution or restriction in full.

* *Pathway I:* What does the system do, for whom, and how? Walk through how it works in DTPA terms: what data it uses, what kind of model, who operates it, and what it decides or recommends. Explain what it deliberately does *not* do.
* *Pathway II:* What exactly is restricted, required, or prohibited? Who does it apply to? Write the core of the restriction as precisely as a policy would state it, then explain it in plain language.

#### 3.5 Implementation or policy plan (about 400 words)

* *Pathway I:* Rollout steps, stakeholder engagement, and monitoring metrics. How would you know in a year whether it is working, and what would make you shut it down?
* *Pathway II:* Enforcement mechanism, compliance checks, and mitigation strategies. Who enforces the restriction, how would violations be detected, and what happens then?

#### 3.6 Risk and ethical assessment (about 300 words)

What could go wrong with your own proposal? Address remaining uncertainties, unintended consequences, and how you would mitigate them. Use the Four Pillars of AI Literacy (Data, Quantitative, Ethical, and Critical) as lenses. The strongest designs take their own weaknesses seriously; Amsterdam's welfare algorithm is a reminder that following every best practice does not guarantee a fair outcome.

#### 3.7 Conclusion (about 100 words)

Explain why your design reflects a critically pragmatic view of AI: neither assuming technology will solve the problem nor assuming it can only cause harm.

#### 3.8 References

Full APA list for every source cited in the report.

*(Attach separately: response to Scaffold 2 feedback.)*

#### Before you submit Part 3

- [ ] Does the executive summary stand on its own?
- [ ] Does the report read as one argument, from problem to proposal, rather than as stacked sections?
- [ ] Is the proposal specific enough to implement or enforce?
- [ ] Does the risk assessment take your own proposal's weaknesses seriously?
- [ ] Is every factual claim traceable to the reference list?

---

### Feedback Response Document (attach at Scaffold 2 and Final)

For each piece of instructor feedback:

1. Quote or reference the comment.
2. State the change you made, or explain why you did not make it.
3. Point to where the revision appears (for example, "Part 2, Data section").

A table works well:

| Feedback | What we changed (or why we didn't) | Where |
|---|---|---|
| "Your stakeholder section doesn't include patients." | Added patients as a stakeholder group and revised our design priority to address them. | 1.3, 2.5 |

"We disagreed and kept our approach" is an acceptable response, as long as you explain why.

---

### Class Showcase — Dec 7–11

To ensure each member of our class has the opportunity to see your work and provide feedback, the last week of classes will consist of in-class presentations of your Case Design. Your team will lead the class through your complete case in **about 10 minutes**, followed by **2–3 minutes of questions**. Slides are highly recommended.

While the Showcase itself is not graded, you will not be able to turn in your Final Case Design without presenting your case and considering the class's feedback and questions.

#### What the presentation is (and isn't)

The presentation is **not** a reading of your report. Your report is written for a reader who has time; your presentation is for a room that has ten minutes. Pick the most important evidence and the clearest version of your proposal, and trust the report to hold the rest.

#### Suggested structure

| Section | Time | What to cover |
|---|---|---|
| The problem or system | ~1.5 min | One concrete example that makes the audience care. A person, a number, or an incident works better than a definition. |
| Why it matters | ~1 min | Your strongest one or two pieces of evidence. |
| DTPA analysis | ~3 min | The single most important finding from each component, about 45 seconds each. |
| The proposal | ~2.5 min | What you propose, who implements it, and how it works. This is the heart of the talk. |
| Risks and trade-offs | ~1 min | What could go wrong with your own proposal, and what you would do about it. |
| Closing | ~1 min | The one thing you want the audience to remember. |

Eight to ten slides is usually enough. Put a source on every slide that shows a number or a claim.

#### Presentation guidelines

* **Every team member should speak.** Divide the talk by section, and practice the handoffs.
* **Rehearse with a timer at least once.** Ten minutes goes quickly; we will keep time so every team gets its full slot.
* **Prepare for questions.** Before the Showcase, write down the three questions you most expect, and agree on who will answer each.
* **Design for the back of the room.** Large text, few words per slide, and charts with labeled axes.

#### Giving and using class feedback

After each presentation, audience members will respond to three questions:

1. What was the most convincing part of this proposal?
2. What is the biggest weakness or unanswered question?
3. If you were implementing (or affected by) this proposal, what would you want to know?

Your team will receive this feedback after the Showcase. Use it to make final edits before the Dec 15 deadline. We recommend adding a short paragraph (about 150 words) at the end of your report, titled **"Changes after the Showcase,"** describing what you revised in response to the class and why.

---