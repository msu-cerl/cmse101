---
title: "Week 7 and 8 Case Study II"
date: 2026-10-01
draft: false
description: "Week 7 and 8 Materials CMSE 101, Fall 2026"
tags: ["AI", "society", "education", "MSU", "schedule"]
author: "Danny Caballero"
---

> All of this material is also available on [Google Docs](https://docs.google.com/document/d/1pwKz9a0XDEpbCGhGviQYAlS62Ncfc8fu0mKeXOqqKdw/edit?tab=t.0) (*MSU login required*)

## Full Case II

Full Case II works the same way as Full Case I. Your group picks one broad domain, settles on **one specific, documented case** inside it, completes the **Update** at the end of Week 7, and completes the **Full Case** at the end of Week 8. The domains for this round are:

* **Law & Criminal Justice**
* **Finance & Banking**
* **Journalism & Media**
* **Hiring & Employment**
* **Military & Defense**
* **Scientific Research**

As before, the materials below orient you to each domain. They are **not** a menu of pre-picked cases. If you need a refresher on how the two weeks work, how to choose a case, or what the Update asks, see [Weeks 5 and 6](../week5and6/) and the [Two Week Case Analyses Explainer](../../assignments/two-week-cases).

**What should be different this time:** you have done this once. Narrow from domain to case in the first two class meetings, not the first week. Aim for sources about your *case*, not your domain, and for more than one *kind* of source. The Full Case I feedback you receive is the standard for Full Case II.

| Week | Individually | As a group |
|:----:|--------------|------------|
| 7 | Review one domain below; summarize; write preliminary DTPA questions → [Forum Post](../../assignments/forum-posts) | Pick a domain, narrow to a case, find sources → **Update** (Sun Oct 18) |
| 8 | Review a *different* domain below; summarize; write preliminary DTPA questions → [Forum Post](../../assignments/forum-posts) | Complete the full DTPA analysis → **Full Case** (Sun Oct 25) |

## Prep reading & resources

*You only need to review **one domain per week**, and we expect you to spend at least 90 minutes with the materials in that domain. Groups can split members across domains so that, together, you have seen as much as possible.*

### ⚖️ Law & Criminal Justice

Criminal justice is where an AI output can most directly cost someone their freedom. Many of these tools are bought by local agencies with little public review, so the case is often in a city council record or a court filing rather than a press release. You met Detroit's facial recognition arrests in [Week 2](../week2/).

<!-- Instructor key (not shown to students): + promising, − problematic, ± mixed, constraint -->

#### Facial recognition, police reports, and gunshot detection

* 📖 ["It didn't make sense at all": Wrongful facial recognition arrest in Detroit leads to landmark settlement](https://www.michiganpublic.org/criminal-justice-legal-system/2024-06-28/it-didnt-make-sense-at-all-wrongful-facial-recognition-arrest-leads-to-landmark-settlement) (*Michigan Public*, 2024) — **a Michigan case.** Robert Williams's lawsuit ended with $300,000 and what the ACLU called the nation's strongest police policy on facial recognition. Detroit police can no longer arrest anyone based only on a facial recognition match. <!-- constraint -->
* 📖 [EFF Investigation: AI Product for Police Reports is Designed to Hinder Audits](https://www.eff.org/press/releases/eff-investigation-ai-product-police-reports-designed-hinder-audits) (Electronic Frontier Foundation, 2025) — Axon's Draft One writes the first draft of a police report from body-camera audio. The draft is not saved, so no record shows which words came from the AI and which from the officer. A King County, Washington, prosecutor told officers not to use it. <!-- − -->
* 📖 [Chicago Mayor Brandon Johnson Ends City's ShotSpotter Contract](https://www.thetrace.org/2024/02/chicago-police-shotspotter-gun-violence/) (*The Trace*, 2024) — Chicago dropped its gunshot-detection system after the city's Inspector General found that alerts rarely led to evidence of a gun crime. Supporters argued that it got officers to shootings faster. <!-- ± -->

#### Risk assessment and predictive policing

* 📖 [Machine Bias](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing) (Angwin et al., *ProPublica*, 2016) — the investigation that started the modern debate about algorithmic fairness. ProPublica checked COMPAS risk scores for about 10,000 people arrested in Broward County, Florida. Black defendants who did not reoffend were almost twice as likely as white defendants to be labeled high risk. <!-- − -->
* 📖 [Bias in Criminal Risk Scores Is Mathematically Inevitable, Researchers Say](https://www.propublica.org/article/bias-in-criminal-risk-scores-is-mathematically-inevitable-researchers-say) (*ProPublica*, 2016) — the vendor's reply was that COMPAS was equally *accurate* for Black and white defendants. Both claims were true. Researchers then showed that when two groups reoffend at different rates, a score cannot satisfy both definitions of "fair." Read this alongside the Week 2 lesson that accuracy alone tells you almost nothing. <!-- ± -->
* 📖 [Case Closed: Pasco Sheriff Admits "Predictive Policing" Program Violated Constitution](https://ij.org/press-release/case-closed-pasco-sheriff-admits-predictive-policing-program-violated-constitution/) (Institute for Justice, 2024) — a Florida sheriff's office used an algorithm to list people it predicted would commit crimes, then sent deputies to their homes more than 12,500 times, citing residents for things like overgrown grass. In a December 2024 settlement, the office admitted the program was unconstitutional. <!-- − -->

#### Automating relief

* 📖 [Nearly 1.6M criminal records cleared under Michigan 'clean slate' law](https://bridgemi.com/michigan-government/nearly-1-6m-criminal-records-cleared-under-michigan-clean-slate-law/) (*Bridge Michigan*, 2026) — **a Michigan case.** Since April 2023, a Michigan State Police system has flagged eligible convictions to courts every day, with no application required. One problem remains: private background-check companies sometimes keep records the courts have cleared. <!-- + -->
* 📖 [Code for America's Technology and Expertise Enable Utah to Automatically Clear Eligible Criminal Records of 500,000 People](https://codeforamerica.org/news/utah-record-clearance/) (Code for America, n.d.) — the organization's own account of an open-source algorithm that reads criminal records, checks them against clean-slate laws, and fills out the court paperwork. This is automation used to *reduce* the reach of the criminal legal system. <!-- + -->

*AI-fabricated citations in court filings also belong here. The [AI Hallucination Cases Database](https://www.damiencharlotin.com/hallucinations/) from Week 3 can be filtered to Michigan.*

---

### 🏦 Finance & Banking

Finance runs on models, and lending discrimination law in the U.S. dates to the 1970s, so this domain has an unusually long record of regulators testing algorithms against the law. 

#### Credit, lending, and underwriting

* 📖 [The Secret Bias Hidden in Mortgage-Approval Algorithms](https://themarkup.org/denied/2021/08/25/the-secret-bias-hidden-in-mortgage-approval-algorithms) (Martinez & Kirchner, *The Markup*, 2021) — after controlling for 17 factors across more than 2 million applications, lenders were 80% more likely to deny Black applicants than similar white applicants. The analysis traces part of the gap to the credit-scoring software that Fannie Mae and Freddie Mac require. <!-- − -->
* 📖 [Mass. AG reaches settlement with student loan firm for $2.5M over AI lending bias](https://bankingjournal.aba.com/2025/08/mass-ag-reaches-settlement-with-earnest-operations-for-2-5m-over-ai-lending-bias/) (*ABA Banking Journal*, 2025) — Massachusetts alleged that Earnest Operations' AI underwriting models put Black, Hispanic, and non-citizen applicants at a disadvantage. One problem it named was that the models were trained on past human decisions that were themselves arbitrary. <!-- constraint -->
* 📖 [Report on Apple Card Investigation](https://www.dfs.ny.gov/reports_and_publications/202103_report_apple_card_investigation) (New York State Department of Financial Services, 2021) — in 2019, viral posts claimed that the Apple Card gave women lower credit limits than their husbands. Regulators examined data on about 400,000 applicants and found **no** fair-lending violation, but they faulted Goldman Sachs for opaque decisions that customers could not get explained. <!-- ± -->

#### Insurance claims

* 📖 [State Farm accused of making it harder for Black customers to get payouts](https://www.courthousenews.com/state-farm-accused-of-making-it-harder-for-black-customers-to-get-payouts/) (*Courthouse News Service*, 2022) — a class action alleges that State Farm's automated fraud-flagging sent Black homeowners' claims through more delays and paperwork than white neighbors' claims for similar damage. A federal judge has allowed the core claim to proceed. <!-- − -->

#### Fraud, scams, and "AI washing"

* 📖 [AI helped Uncle Sam catch $1 billion of fraud in one year. And it's just getting started](https://www.cnn.com/2024/10/17/business/ai-fraud-treasury/index.html) (CNN, 2024) — the U.S. Treasury credits machine learning with recovering $1 billion in check fraud in fiscal year 2024, part of more than $4 billion in fraud prevented or recovered. <!-- + -->
* 🖱️ [Incident 634: Alleged Deepfake CFO Scam Reportedly Costs Multinational Engineering Firm Arup $25 Million](https://incidentdatabase.ai/cite/634/) (AI Incident Database, 2024) — an employee in Hong Kong joined a video call in which every other participant, including the "CFO," was a deepfake, and then made 15 transfers totaling $25 million. <!-- − -->
* 📖 [SEC Charges Two Investment Advisers with Making False and Misleading Statements About Their Use of Artificial Intelligence](https://www.sec.gov/news/press-release/2024-36) (U.S. Securities and Exchange Commission, 2024) — the SEC's first "AI washing" cases. Two advisers marketed AI-driven investing that, according to the SEC, they did not actually have. <!-- constraint -->
* 🖱️ [Incident 149: Zillow Shut Down Zillow Offers Division Allegedly Due to Predictive Pricing Tool's Insufficient Accuracy](https://incidentdatabase.ai/cite/149/) (AI Incident Database, 2021) — Zillow used its pricing model to buy homes directly, then shut the business down in November 2021 after losses of more than $500 million and cutting about 25% of its workforce. <!-- − -->

*Algorithmic rent pricing (RealPage) also fits here: the Justice Department sued RealPage in 2024 and settled in 2025.*

---

### 📰 Journalism & Media

AI shows up in the news in three places: in *writing* it, in *ranking* it (what you see in your feed), and in *policing* it (moderation and fact-checking). AI bots are often scraping articles; rewriting them; and re-posting them to boost [Search Engine Optimization (SEO)](https://en.wikipedia.org/wiki/Search_engine_optimization).

#### AI-written and AI-summarized news

* 📖 [How an AI-generated summer reading list got published in major newspapers](https://npr.org/2025/05/20/nx-s1-5405022/fake-summer-reading-list-ai) (NPR, 2025) — ten of the fifteen books on a syndicated summer reading list, printed in the *Chicago Sun-Times* and *The Philadelphia Inquirer*, do not exist. The freelancer who wrote it used AI, and neither the syndicator nor either newspaper checked it. <!-- − -->
* 📖 [Apple disables AI notifications for news in its beta iPhone software](https://www.cnbc.com/2025/01/16/apple-disables-ai-notifications-for-news-in-its-beta-iphone-software.html) (CNBC, 2025) — Apple Intelligence summarized a BBC story into a false headline saying the suspect in the UnitedHealthcare CEO killing had shot himself. After complaints from the BBC and press-freedom groups, Apple paused news summaries. <!-- − -->
* 🖱️ [Incident 616: Sports Illustrated Is Alleged to Have Used AI to Invent Fake Authors and Their Articles](https://incidentdatabase.ai/cite/616/) (AI Incident Database, 2023) — product reviews ran under invented bylines with AI-generated headshots. The publisher blamed a contractor, and within weeks its CEO was fired. <!-- − -->
* 📖 [Robot-writing increased AP's earnings stories by tenfold](https://www.poynter.org/reporting-editing/2015/robot-writing-increased-aps-earnings-stories-by-tenfold/) (Poynter, 2015) — Starting in 2014, the Associated Press automated corporate earnings stories from structured data, going from about 300 a quarter to more than 3,000. AP said this freed reporters for other work. <!-- + -->

#### Feeds, moderation, and fact-checking

* 📖 [Myanmar: Facebook's business model profits from 'echo chamber of hatred' which fuelled Rohingya atrocities](https://www.amnesty.org.uk/latest/myanmar-facebooks-business-model-profits-echo-chamber-hatred-which-fuelled-rohingya/) (Amnesty International, 2022) — drawing on leaked internal documents, Amnesty argues that Facebook's recommendation algorithms amplified anti-Rohingya hate before the 2017 violence that drove more than 700,000 people from Myanmar. *Content note: discusses mass atrocity.* <!-- − -->
* 📖 [Meta to end fact-checking program on Facebook and Instagram](https://www.npr.org/2025/01/07/nx-s1-5251151/meta-fact-checking-mark-zuckerberg-trump) (NPR, 2025) — Meta replaced third-party fact-checkers in the U.S. with user-written Community Notes and said it would scale back automated enforcement except for the most severe violations. <!-- ± -->
* 📖 [Generative AI is already helping fact-checkers. But it's proving less useful in small languages and outside the West](https://reutersinstitute.politics.ox.ac.uk/news/generative-ai-already-helping-fact-checkers-its-proving-less-useful-small-languages-and) (Reuters Institute for the Study of Journalism, 2024) — fact-checkers describe where AI tools such as Full Fact AI help (transcribing, monitoring, finding repeated claims) and where they fall short. <!-- ± -->

---

### 💼 Hiring & Employment

You will probably be screened by one of these systems within a year or two. Hiring tools often run before any human sees your application, and the person rejected rarely learns that a model was involved. Management tools go further and decide schedules, pay, and firing.

#### Screening and interviews

* 📖 [Amazon scraps secret AI recruiting tool that showed bias against women](https://www.irishtimes.com/business/technology/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-1.3658651) (Reuters via *The Irish Times*, 2018) — the classic case. Trained on ten years of mostly male résumés, Amazon's tool learned to penalize the word "women's." <!-- − -->
* 📖 [AI Screening Tools Under Scrutiny: Federal Court Preliminarily Certifies ADEA Collective Action](https://www.dwt.com/blogs/employment-labor-and-benefits/2025/05/ai-hiring-age-discrimination-federal-court-workday) (Davis Wright Tremaine, 2025) — in *Mobley v. Workday*, a federal judge allowed applicants over 40 nationwide to join an age-discrimination case against the *software vendor*, not just the employers that used it. <!-- constraint -->
* 📖 [iTutorGroup to Pay $365,000 to Settle EEOC Discriminatory Hiring Suit](https://www.eeoc.gov/newsroom/itutorgroup-pay-365000-settle-eeoc-discriminatory-hiring-suit) (U.S. Equal Employment Opportunity Commission, 2023) — the EEOC's first AI hiring settlement. The company's software automatically rejected women 55 and older and men 60 and older. <!-- constraint -->
* 📖 [HireVue stops using facial expressions to assess job candidates amid audit of its A.I. algorithms](https://fortune.com/2021/01/19/hirevue-drops-facial-monitoring-amid-a-i-algorithm-audit/) (*Fortune*, 2021) — a video-interview company dropped facial analysis after an outside audit and public criticism. <!-- ± -->
* 📖 [Does AI Beat Humans at Recruiting?](https://www.chicagobooth.edu/review/does-ai-beat-humans-recruiting) (*Chicago Booth Review*, 2026) — a randomized trial with about 70,000 applicants for customer-service jobs in the Philippines. Applicants interviewed by an AI voice agent were 12% more likely to get a job offer and more likely to stay in the job, and 80% chose the AI when given a choice. Humans still made the final hiring decisions. <!-- + -->

#### Algorithmic management and transparency rules

* 📖 [Fired by bot at Amazon: 'It's you against the machine'](https://www.seattletimes.com/business/amazon/fired-by-bot-at-amazon-its-you-against-the-machine/) (Bloomberg via *The Seattle Times*, 2021) — Amazon Flex delivery drivers were rated and deactivated largely by automated systems, including for problems like locked apartment gates. Former managers said Amazon judged it cheaper to trust the algorithm than to investigate mistakes. <!-- − -->
* 📖 [Studying How Employers Comply with NYC's New Hiring Algorithm Law](https://citizensandtech.org/research/2024-algorithm-transparency-law/) (Citizens and Technology Lab, Cornell, 2024) — New York City requires employers that use automated hiring tools to publish bias audits. Student researchers checked 391 employers and found 18 audit reports. <!-- constraint -->

---

### 🛡️ Military & Defense

Military AI is the hardest domain to document, because much of it is classified. Strong cases here usually rely on official records, investigative reporting with named sources, and statements from the companies involved. Read carefully for who is making each claim and how they would know. *Content note: this domain involves armed conflict and civilian deaths.*

#### Targeting and decision support

* 📖 [What Is Maven Smart System, and What Does It Do?](https://www.csis.org/analysis/what-maven-smart-system-and-what-does-it-do) (Mande & Allen, Center for Strategic and International Studies, 2026) — an explainer on the Pentagon's main AI targeting and intelligence platform. Palantir builds it, it draws on commercial AI models, and U.S. commands and NATO allies use it. The piece also covers a 2026 dispute between the Pentagon and one model provider over restrictions on use. <!-- ± -->
* 📖 [Google to halt controversial project aiding Pentagon drones](https://www.nbcnews.com/news/military/google-halt-controversial-project-aiding-pentagon-drones-n879471) (NBC News, 2018) — where Project Maven began. Thousands of Google employees protested its work analyzing drone footage, and Google declined to renew the contract. <!-- constraint -->
* 🖱️ [Incident 672: 'Lavender' and 'The Gospel' AI Systems Reportedly Used in Gaza Targeting Operations](https://incidentdatabase.ai/cite/672/) (AI Incident Database, 2024) — summarizes reporting by *+972 Magazine* and *Local Call*, based on Israeli intelligence officers, that an AI system marked tens of thousands of people as suspected militants and that human review was sometimes only seconds long. The Israeli military disputes how the system has been described. <!-- − -->

#### Autonomy and the rules for it

* 📖 [Russia-Ukraine war is accelerating the dangerous race toward fully autonomous drones](https://theconversation.com/russia-ukraine-war-is-accelerating-the-dangerous-race-toward-fully-autonomous-drones-290877) (*The Conversation*, 2024) — radio jamming cuts drones off from their operators, which pushes both sides toward drones that can find and hit targets on their own. <!-- − -->
* 📖 [Killer Robots: UN Vote Should Spur Treaty Negotiations](https://www.hrw.org/news/2024/12/05/killer-robots-un-vote-should-spur-treaty-negotiations) (Human Rights Watch, 2024) — in December 2024, 166 countries voted for a UN General Assembly resolution on lethal autonomous weapons. Human Rights Watch, an advocacy group, explains why the resolution stops short of starting treaty negotiations. <!-- constraint -->

#### Defense uses beyond weapons

* 📖 [DARPA's AI Cyber Challenge reveals winning models for automated vulnerability discovery and patching](https://cyberscoop.com/darpa-ai-cyber-challenge-winners-def-con-2025/) (CyberScoop, 2025) — in a two-year DARPA competition, AI systems found 77% of the planted software flaws and patched 61% of them, and also found 18 real flaws no one knew about. The winning systems were released as open source. <!-- + -->
* 📖 [Air Force selects AI-enabled predictive maintenance program as system of record](https://defensescoop.com/2023/05/10/air-force-selects-ai-enabled-predictive-maintenance-program-as-system-of-record/) (DefenseScoop, 2023) — the Air Force uses models to predict which aircraft parts will fail before they break. The case is less dramatic, but it shows where much of the military's AI spending goes. <!-- + -->

---

### 🔬 Scientific Research

AI has produced one of the biggest scientific advances of the decade and also new ways to fake science. This domain is also about *you*: universities, journals, and peer reviewers are deciding right now what counts as legitimate AI use in research.

#### Discovery

* 📖 [Chemistry Nobel goes to developers of AlphaFold AI that predicts protein structures](https://www.nature.com/articles/d41586-024-03214-7) (*Nature*, 2024) — the first Nobel Prize for an AI-enabled breakthrough. AlphaFold's predicted structures for about 200 million proteins are free to use, and millions of researchers have used them. Ask what data it was trained on (decades of publicly funded lab work) and where its predictions still fail. <!-- + -->
* 📖 [MIT disavows doctoral student paper on AI's productivity benefits](https://techcrunch.com/2025/05/17/mit-disavows-doctoral-students-paper-on-ai-productivity-benefits) (TechCrunch, 2025) — a widely cited preprint claimed that an AI tool sped up materials discovery at a large company's lab. Economists, including a Nobel laureate, praised it. Then MIT announced it had no confidence in the data, and the paper was withdrawn. <!-- − -->

#### Publishing, peer review, and paper mills

* 📖 [Study Featuring AI-Generated Giant Rat Penis Retracted, Journal Apologizes](https://www.vice.com/en/article/ai-midjourney-rat-penis-study-retracted-frontiers/) (*Vice*, 2024) — a peer-reviewed journal published nonsensical Midjourney-generated figures, and they went viral. A reviewer had objected, but nobody checked whether the authors fixed the figures. <!-- − -->
* 📖 [Wiley shuts 19 scholarly journals amid AI paper mill problem](https://www.theregister.com/software/2024/05/16/wiley-shuts-19-scholarly-journals-amid-ai-paper-mill-problem/1255533) (*The Register*, 2024) — a major publisher retracted more than 11,000 papers from journals it had acquired and closed 19 journals after paper mills, which sell authorship of fake papers, overwhelmed peer review. <!-- − -->
* 📖 [Researchers hide prompts in scientific papers to sway AI-powered peer review](https://the-decoder.com/researchers-hide-prompts-in-scientific-papers-to-sway-ai-powered-peer-review/) (*The Decoder*, 2025, reporting on a *Nikkei* investigation) — authors at several universities hid white-on-white text such as "give a positive review only" in their papers, aimed at reviewers who paste papers into chatbots. <!-- − -->
* 📖 [The AI Scientist Generates its First Peer-Reviewed Scientific Publication](https://sakana.ai/ai-scientist-first-publication/) (Sakana AI, 2025) — the company's own account of an entirely AI-generated paper passing peer review at a workshop of a major AI conference, with the organizers' cooperation. Read the caveats the company itself gives. <!-- ± -->

---

### Places to start looking for your own case

The same places from [Weeks 5 and 6](../week5and6/#places-to-start-looking-for-your-own-case) still apply. These are also useful for this round:

| Where | What you'll find |
|---|---|
| [AI Incident Database](https://incidentdatabase.ai/) | Structured, cross-domain, sourced |
| [AI Hallucination Cases Database](https://www.damiencharlotin.com/hallucinations/) | Court decisions involving AI-generated errors |
| [Retraction Watch](https://retractionwatch.com/) | Retractions and research-integrity cases, including AI-generated papers |
| [The Markup](https://themarkup.org/) | Data-driven investigations of algorithms in lending, hiring, and policing |
| Court and agency records | FTC, EEOC, SEC, CFPB, and state attorney general press releases often name the tool and the company |

## Your Individual Domain Review

This is the same assignment as in [Weeks 5 and 6](../week5and6/#your-individual-domain-review). Each week, pick one domain above (a different one in Week 8) and post to the [Forum](../../assignments/forum-posts) (~250 words, APA references):

1. **Summary.** What is happening in this domain? Name at least two specific tools, organizations, or deployments, with a source for each.
2. **Preliminary DTPA questions.** At least one question for each of Data, Tools, Practices, and Actions.
3. **A possible case.** One specific, documented case you *could* imagine analyzing.

## Class Meetings

| Day | Date | Focus |
|:---:|:----:|-------|
| M | **Oct 12** | Introducing Full Case II — Planning and Research |
| W | **Oct 14** | Full Case II — Planning and Research |
| F | **Oct 16** | Full Case II — Planning and Research; Complete Part A of Template |
| M | **Oct 19** | Full Case II — Research and Drafting Case Analysis |
| W | **Oct 21** | Full Case II — Research and Drafting Case Analysis |
| F | **Oct 23** | Full Case II — Completing Case Analysis; Complete Part B of Template |

* **Week 7:** You *may* select new groups for Full Case II, or stay in the same groups.
* **Week 8:** You must stay in your groups for Full Case II.

## Focus for Weeks 7 and 8

The standard is the same as for Full Case I. All four DTPA sections and all four Pillars of AI Literacy are evaluated. See [Focus for Weeks 5 and 6](../week5and6/#focus-for-weeks-5-and-6) for the full description and examples of weak answers.

Two things to push on this round:

* **Source variety.** Several domains this round (Law, Finance, Hiring) have strong *official records*: court filings, settlements, and regulator reports. A case built only on news coverage will be thinner than it needs to be.
* **Who could stop it.** Many of these cases involve a regulator, a court, or a union that acted, or didn't. In Actions, be specific about who had the power to constrain the system and what they actually did.

### Week 7 Update (due Sun Oct 18)

Answer the same eight questions as the [Week 5 Update](../week5and6/#week-5-update-due-sun-oct-4) in your group's tab, starting with **Section 0 (Your Notes/Research)**. If your Full Case I feedback flagged a problem (too few case-specific sources, a domain instead of a case, a thin DTPA section), say in **Question 8** how you are avoiding it this time.

### Week 8 Full Case (due Sun Oct 25)

The complete Case Study, using the same template and DTPA framework. Where your group disagrees, write the disagreement down.

## Keep the Case Design Moving

Your **Case Design** continues in the background. Scaffold 1 was due Oct 9, and **Scaffold 2 is due Fri Nov 6**. When you receive Scaffold 1 feedback, start a response-to-feedback document right away and add notes and sources to Section 0 of your Case Design. Several domains this round, especially Law, Finance, and Hiring, include settlements and policies that could serve as models for a Pathway II restriction. See the [Case Design & Template](../../assignments/case-design) for Part 2.

## Turning In

Same as Full Case I: one group member downloads the Word or PDF version of your tab and submits it on D2L to **Week 7 Full Case II Update** and then **Week 8 Full Case II Complete**. Each of you also submits an **Individual Effort & Metacognitive Report** (~250 words) each week.

**Due dates:**

* **Sunday, October 11th at 11:59pm**
    * Week 7 Forum Post (domain review)
* **Sunday, October 18th at 11:59pm**
    * Week 7 Full Case II *Update* (Part A of Template)
    * Week 7 Individual Effort & Metacognitive Report
    * Week 8 Forum Post (domain review, *different* domain)
* **Sunday, October 25th at 11:59pm**
    * Week 8 Full Case II *Complete* (Part B of Template)
    * Week 8 Individual Effort & Metacognitive Report

## Reminders

Put your group's names at the top of the page, and do not copy from or to other groups' Case Studies.

Case Studies that do not meet the standard will be returned without credit, and your group will have one week from receiving it to revise and meet the standard.

---
