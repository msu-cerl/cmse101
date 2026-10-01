---
title: "Week 9 and 10 Case Study III"
date: 2026-10-01
draft: false
description: "Week 9 and 10 Materials CMSE 101, Fall 2026"
tags: ["AI", "society", "education", "MSU", "schedule"]
author: "Danny Caballero"
---

> All of this material is also available on [Google Docs](https://docs.google.com/document/d/1ojQvteoKQ_oyffV1nCndgXFaxHJFtY9Q1W38PkmsTQ4/edit?tab=t.0) (*MSU login required*)

## Full Case III

This is the last of the three two-week cases, and it runs the same way as the first two: pick a domain, settle on **one specific, documented case**, complete the **Update** at the end of Week 9, and complete the **Full Case** at the end of Week 10. The domains for this round are:

* **Agriculture**
* **Transportation**
* **Retail & Consumer**
* **Entertainment & Gaming**
* **Environmental & Climate Science**
* **An undiscussed area of your choosing** — any domain not covered in Full Cases I or II

For a refresher on how the two weeks work, see [Weeks 5 and 6](../week5and6/) and the [Two Week Case Analyses Explainer](../../assignments/two-week-cases).

**Two things are different this round:**

* **Week 9 is short.** There is no class on Monday, Oct 26 (Fall Break), so you have two class meetings before the Update is due. Settle on a case by Wednesday.
* **Scaffold 2 of your Case Design is due Fri, Nov 6**, in the same week as the Full Case. Plan for both. See [Case Design: Scaffold 2](#case-design-scaffold-2-due-fri-nov-6) below.

| Week | Individually | As a group |
|:----:|--------------|------------|
| 9 | Review one domain below; summarize; write preliminary DTPA questions → [Forum Post](../../assignments/forum-posts) | Pick a domain, narrow to a case, find sources → **Update** (Sun Nov 1) |
| 10 | Review a *different* domain below; summarize; write preliminary DTPA questions → [Forum Post](../../assignments/forum-posts) | Complete the full DTPA analysis → **Full Case** (Sun Nov 8) |

## Prep reading & resources

*You only need to review **one domain per week**, and we expect you to spend at least 90 minutes with the materials in that domain. If your group chooses an undiscussed area, your individual review can still come from the domains below.*

### 🌾 Agriculture

Farming is one of the most data-intensive industries in the country, and Michigan farmers are part of the story. Many cases in this domain turn on **who owns the data and the machine**: the farmer who generates the data, or the company that sells the equipment.

<!-- Instructor key (not shown to students): + promising, − problematic, ± mixed, constraint -->

#### Equipment, data, and the right to repair

* 📖 [Deere: See & Spray users saving nearly 60% on herbicides](https://www.michiganfarmnews.com/deere-see-spray-users-saving-nearly-60-on-herbicides) (*Michigan Farm News*, 2024) — sprayers use cameras and computer vision to spray only where they detect weeds. Deere reports average herbicide savings of 59% across more than a million acres in 2024. Note that these figures come from the company. <!-- + -->
* 📖 [FTC, States Sue Deere & Company to Protect Farmers from Unfair Corporate Tactics, High Repair Costs](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-states-sue-deere-company-protect-farmers-unfair-corporate-tactics-high-repair-costs) (Federal Trade Commission, 2025) — the same software that makes modern tractors "smart" also locks out farmers and independent mechanics. **Michigan** joined the lawsuit. <!-- constraint -->
* 📖 [FTC, States Secure Settlement with Deere & Company, Advancing Farmers' Right to Repair](https://www.ftc.gov/news-events/news/press-releases/2026/07/ftc-states-secure-settlement-deere-company-advancing-farmers-right-repair) (Federal Trade Commission, 2026) — **this summer.** Under a 10-year settlement, Deere must give farmers and independent repair shops the same diagnostic software that its dealers have. <!-- constraint -->
* 📖 [A Hidden Crop for Corporate Tech: Farm Data](https://civileats.com/2026/03/23/a-hidden-crop-for-corporate-tech-farm-data/) (*Civil Eats*, 2026) — precision-ag platforms from Deere, Bayer, Corteva, and others collect field-level data on seeding, spraying, and yield. The article asks who profits when that data is combined across farms, and describes Nebraska's attempt to give farmers rights over it. <!-- ± -->

#### Forecasts and advice for farmers

* 📖 [AI-based monsoon forecasts help 38 million Indian farmers make planting decisions](https://climate.uchicago.edu/news/ai-based-monsoon-forecasts-help-38-million-indian-farmers-make-planting-decisions/) (University of Chicago Institute for Climate and Sustainable Growth, 2025) — researchers combined AI weather models, including Google's NeuralGCM, to forecast when the monsoon would arrive up to a month ahead. India's agriculture ministry sent the forecasts by text message to 38 million farmers. <!-- + -->
* 📖 [Beyond the Chat: AI-Powered Advice for Women Farmers](https://www.cgap.org/blog/beyond-chat-ai-powered-advice-for-women-farmers) (CGAP, 2025) — Farmer.Chat, a generative AI advice tool from the nonprofit Digital Green, answers farmers' questions by voice and text in India, Kenya, and Nigeria. The article reports early quality-of-life gains and names the barriers for women farmers: digital literacy, language accuracy, data costs, and bias. <!-- ± -->

#### Livestock and labor

* 📖 [The dairy farm of the future could employ robotics](https://www.wpr.org/news/dairy-farm-future-wisconsin-research-center) (Wisconsin Public Radio, 2024) — Wisconsin farms and a new $55 million research center use robotic milkers, sensors, and automated alerts to track each cow's health and production. The article says robots "save a lot of labor" but doesn't say whose. <!-- ± -->

---

### 🚗 Transportation

Michigan built the car industry, and the debate over who is responsible when a car drives itself is happening now. Read for the difference between *driver-assist* systems, where a human is supposed to be watching, and *driverless* systems, where no human is. Many of the failures happen in the gap between those two.

#### Self-driving and driver-assist

* 📖 [NTSB Investigation Into Deadly Uber Self-Driving Car Crash Reveals Lax Attitude Toward Safety](https://spectrum.ieee.org/ntsb-investigation-into-deadly-uber-selfdriving-car-crash-reveals-lax-attitude-toward-safety) (*IEEE Spectrum*, 2019) — in 2018, an Uber test vehicle killed Elaine Herzberg in Tempe, Arizona. The car detected her nearly six seconds before impact but never classified her correctly, and Uber had disabled the Volvo's built-in emergency braking. <!-- − -->
* 📖 [GM self-driving car subsidiary withheld video of a crash, California DMV says](https://www.cnn.com/2023/10/24/business/california-dmv-cruise-permit-revoke/) (CNN, 2023) — after a human driver knocked a pedestrian into its path, a Cruise robotaxi stopped on top of her and then dragged her about 20 feet. California suspended Cruise's permit, saying the company had not shown regulators the full video. <!-- − -->
* 📖 [GM exits robotaxi market, will bring Cruise operations in house](https://www.cnbc.com/2024/12/10/gm-halts-funding-of-robotaxi-development-by-cruise.html) (CNBC, 2024) — **a Michigan company.** Fourteen months later, Detroit-based GM shut down Cruise's robotaxi business. <!-- ± -->
* 📖 [Waymo shows 90% fewer claims than advanced human-driven vehicles: Swiss Re](https://www.reinsurancene.ws/waymo-shows-90-fewer-claims-than-advanced-human-driven-vehicles-swiss-re/) (*Reinsurance News*, 2024) — across 25.3 million driverless miles, Waymo had about 90% fewer injury and property-damage claims than human drivers, according to one of the world's largest reinsurers. <!-- + -->
* 📖 [Tesla hit with $243 million in damages after jury finds its Autopilot feature contributed to fatal crash](https://www.nbcnews.com/news/us-news/tesla-autopilot-crash-trial-verdict-partly-liable-rcna222344) (NBC News, 2025) — the first federal jury verdict holding Tesla partly responsible for a fatal crash involving Autopilot. The jury put a third of the responsibility on Tesla and the rest on the driver. A judge upheld the verdict in 2026. <!-- constraint -->

#### Ride-hail pricing

* 📖 [Uber's Algorithm and Driver Pay](https://business.columbia.edu/faculty/press/ubers-algorithm-and-driver-pay) (Columbia Business School, 2025) — researchers analyzed about 31,000 trips from one experienced driver and found that after Uber switched to algorithmic "upfront pricing," riders paid more, drivers were paid less, and Uber's share of each fare rose from about 32% to about 42%. <!-- − -->

---

### 🛒 Retail & Consumer

These are the systems you use every week, often without noticing: what you are shown, what price you are charged, who watches you in the store, and who answers when you complain. Several of the strongest cases ended with a regulator stepping in or a company reversing course.

#### Pricing

* 📖 [Instacart Stops AI Pricing Tests](https://www.consumerreports.org/money/questionable-business-practices/instacart-stops-ai-pricing-experiments-a1176475852/) (*Consumer Reports*, 2025) — Consumer Reports and Groundwork Collaborative found that shoppers ordering the same item, at the same store, at the same time could see prices up to 23% apart. Instacart ended the experiments within weeks. <!-- constraint -->
* 📖 [FTC Surveillance Pricing Study Indicates Wide Range of Personal Data Used to Set Individualized Consumer Prices](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-surveillance-pricing-study-indicates-wide-range-personal-data-used-set-individualized-consumer) (Federal Trade Commission, 2025) — the companies that set prices on retailers' behalf can use your location, browsing history, and even what you left in your cart. <!-- − -->

#### Stores, surveillance, and "automation"

* 📖 [Rite Aid Banned from Using AI Facial Recognition After FTC Says Retailer Deployed Technology without Reasonable Safeguards](https://www.ftc.gov/news-events/news/press-releases/2023/12/rite-aid-banned-using-ai-facial-recognition-after-ftc-says-retailer-deployed-technology-without) (Federal Trade Commission, 2023) — from 2012 to 2020, Rite Aid used facial recognition in hundreds of stores to flag suspected shoplifters, and the FTC says the system falsely flagged customers, especially women and people of color. Rite Aid is banned from using it for five years. <!-- constraint -->
* 📖 [Amazon's 'just walk out' checkout tech was powered by 1,000 Indian workers](https://www.business-standard.com/companies/news/amazon-s-just-walk-out-checkout-tech-was-powered-by-1-000-indian-workers-124040400463_1.html) (*Business Standard*, 2024) — Amazon's cashierless checkout relied on about 1,000 workers in India reviewing video, and in 2022 they reviewed about 700 of every 1,000 transactions. Amazon says the workers mainly label data to train the system. <!-- − -->
* 📖 [Afresh expands AI-powered tools for fresh](https://www.grocerydive.com/news/afresh-ai-solution-fresh-inventory-management-grocery/760795/) (*Grocery Dive*, 2025) — AI forecasting that tells grocery stores how much produce to order, aimed at the millions of tons of fresh food that U.S. grocers throw away. Its customers include Michigan-based Meijer. <!-- + -->

#### Customer-service chatbots

* 📖 [Air Canada found liable for chatbot's bad advice on bereavement rates](https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416) (CBC News, 2024) — Air Canada's chatbot invented a refund policy. The airline argued the chatbot was responsible for its own words, and a Canadian tribunal disagreed. <!-- constraint -->
* 📖 [Klarna Is Hiring Customer Service Agents After AI Couldn't Cut It on Calls](https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396) (*Entrepreneur*, 2025) — in 2024, Klarna said its AI assistant was doing the work of 700 agents. In 2025, its CEO said the company "went too far" on cost, quality suffered, and Klarna began hiring humans again. <!-- ± -->

---

### 🎮 Entertainment & Gaming

This domain overlaps with Art & Creative Industries from Full Case I, so focus on what is different: **platforms that run on algorithms** (matchmaking, moderation, recommendation) and the **performers whose voices and likenesses** those platforms use. Many of you are users of these systems, which makes you a source too.

#### Performers and synthetic content

* 📖 [Video Game Performers Secure AI Consent Rules in New SAG-AFTRA Deal](https://decrypt.co/329479/video-game-performers-ai-consent-rules) (Decrypt, 2025) — video game voice and motion-capture actors struck for nearly a year over AI. The July 2025 contract requires consent and disclosure before a studio makes a digital replica of a performer. <!-- constraint -->
* 📖 [SAG-AFTRA Files Unfair Labor Practice Charge Over AI Replica of Darth Vader's Voice in 'Fortnite'](https://www.hollywoodreporter.com/business/business-news/sag-aftra-labor-charge-fortnite-darth-vader-ai-voice-1236221492/) (*The Hollywood Reporter*, 2025) — James Earl Jones had approved recreating his voice, and his family agreed to the Fortnite use. The union still objected, arguing that consent from one performer does not settle whether the work should have gone to a working actor. <!-- ± -->
* 📖 [The Velvet Sundown's AI saga is 2025's weirdest music story](https://www.thefader.com/2025/07/07/the-velvet-sundown-ai-band-story-explained) (*The Fader*, 2025) — a "band" passed a million monthly Spotify listeners before admitting its music was AI-generated. Ask what role Spotify's recommendation algorithm played. <!-- − -->

#### Moderation, safety, and matchmaking

* 📖 [Call of Duty enlists AI to eavesdrop on voice chat and help ban toxic players](https://www.pcgamer.com/call-of-duty-enlists-ai-to-eavesdrop-on-voice-chat-and-help-ban-toxic-players-starting-today/) (*PC Gamer*, 2023) — Activision added Modulate's ToxMod, which listens to live voice chat and flags harassment for enforcement. Follow up with [the 2024 results](https://www.techradar.com/gaming/consoles-pc/call-of-dutys-ai-powered-anti-toxicity-voice-recognition-has-already-detected-2-million-accounts): more than 2 million accounts have faced enforcement. <!-- ± -->
* 📖 [Roblox to Require All Users to Verify Age With Facial Estimation Tech to Access Chat Features](https://variety.com/2025/gaming/news/roblox-launches-required-facial-age-checks-1236584050/) (*Variety*, 2025) — since January 2026, Roblox has required an AI face scan that estimates age before users can chat, and lets users chat only with people in nearby age groups. The goal is to protect children, and the method collects face scans from millions of users, many of them children. <!-- ± -->
* 📖 [Activision secretly experimented on 50% of Call of Duty players by 'decreasing' skill-based matchmaking](https://www.pcgamer.com/games/activision-secretly-experimented-on-50-of-call-of-duty-players-by-decreasing-skill-based-matchmaking-and-determined-players-like-sbmm-even-if-they-don-t-know-it/) (*PC Gamer*, 2024) — Activision ran a hidden experiment on half its North American players and published the results: most players played less when matchmaking paid less attention to skill. <!-- ± -->

---

### 🌍 Environmental & Climate Science

AI is both a tool for understanding the environment and a growing burden on it. In Week 3 you looked at the energy and water costs of data centers. This domain also includes cases where AI forecasts and detection systems may be saving lives.

#### Forecasting and early warning

* 📖 [Google's AI-powered Flood Hub expands to 80 countries](https://blog.google/company-news/outreach-and-initiatives/sustainability/flood-hub-ai-flood-forecasting-more-countries/) (Google, 2024) — the company's own account of a river-flood forecasting model, described in *Nature*, that gives up to seven days' warning, including in places with no river gauges. It covers about 460 million people. <!-- + -->
* 📖 [ECMWF – delivering forecasts over 10 times faster and cutting energy usage by 1000](https://www.eurekalert.org/news-releases/1088526) (European Centre for Medium-Range Weather Forecasts via EurekAlert!, 2025) — since February 2025, one of the world's leading forecasting centers has run a machine-learning weather model alongside its traditional physics-based model. <!-- + -->
* 📖 [Over 1,000 AI cameras help spot Calif. wildfires before the first 911 call](https://www.gov1.com/emergency-management/over-1-000-ai-cameras-help-spot-calif-wildfires-before-the-first-911-call) (*Gov1*, 2025) — UC San Diego and CAL FIRE run more than 1,200 mountaintop cameras that use AI to detect smoke. In one year, 38% of the fires they detected were spotted before anyone called 911. The article also describes the limits: dust, clouds, and geothermal steam set off false alarms. <!-- + -->
* 📺 [How satellites and AI cameras are detecting wildfires before they get out of control](https://www.pbs.org/newshour/show/how-satellites-and-ai-cameras-are-detecting-wildfires-before-they-get-out-of-control) (*PBS NewsHour*, 2026) — video companion to the article above. <!-- + -->

#### Monitoring emissions

* 📖 [More Than 70,000 of the Highest Emitting Greenhouse Gas Sources Identified in Largest Available Global Emissions Inventory](https://climatetrace.org/news/more-than-70000-of-the-highest-emitting-greenhouse-gas) (Climate TRACE, 2022) — a coalition uses satellite data and machine learning to estimate emissions from individual facilities, finding that oil and gas emissions are much higher than countries report. Independent researchers have found that some of its estimates are also off. <!-- ± -->

#### AI's own footprint: a Michigan case

* 📖 [$7 billion Saline Township data center reignites Michigan climate plan "off ramp" concerns](https://planetdetroit.org/2025/11/dte-openai-saline-township/) (*Planet Detroit*, 2025) — **a Michigan case,** on farmland just south of Ann Arbor. A 1.4-gigawatt data center for OpenAI and Oracle's "Stargate" project would need power from DTE equal to a large power plant. Advocates question whether it fits the state's clean-energy law. <!-- − -->
* 📖 [A Michigan farm town voted down plans for a giant OpenAI-Oracle data center. Weeks later, construction began](https://fortune.com/2026/05/06/ai-data-center-michigan-saline-politics-farmland/) (*Fortune*, 2026) — the township board rejected the rezoning, the developer sued, and the township settled within weeks. <!-- − -->
* 📖 [Michigan regulators approve DTE's Saline data center contracts](https://planetdetroit.org/2025/12/dte-data-center-contracts-approved/) (*Planet Detroit*, 2025) — the Michigan Public Service Commission approved the power contracts without a contested case, so ratepayer and environmental groups could not file testimony. It did attach conditions meant to protect other customers. <!-- constraint -->

---

### 🧭 An Undiscussed Area of Your Choosing

Any domain **not** covered in Full Cases I or II is fair game. Examples include housing and real estate, religion, social services and child welfare, dating and relationships, sports betting, libraries, insurance outside of healthcare, or accessibility and disability. The standard does not change: a named tool, a named organization, and a documented deployment.

**Name your domain and case in Question 1 of the Week 9 Update** so the instructional team can confirm it. If you are unsure whether a domain counts as "undiscussed," ask by Wednesday, Oct 28.

---

### Places to start looking for your own case

The places listed in [Weeks 5 and 6](../week5and6/#places-to-start-looking-for-your-own-case) and [Weeks 7 and 8](../week7and8/#places-to-start-looking-for-your-own-case) still apply. These are also useful for this round:

| Where | What you'll find |
|---|---|
| [AI Incident Database](https://incidentdatabase.ai/) | Structured, cross-domain, sourced |
| [FTC press releases](https://www.ftc.gov/news-events/news/press-releases) | Consumer-protection cases that name the company and the tool |
| [NHTSA Standing General Order crash reports](https://www.nhtsa.gov/laws-regulations/standing-general-order-crash-reporting) | Federal crash data for driver-assist and automated vehicles |
| [Planet Detroit](https://planetdetroit.org/) and [Bridge Michigan](https://bridgemi.com/) | Michigan environment, energy, and policy reporting |

## Your Individual Domain Review

This is the same assignment as in [Weeks 5 and 6](../week5and6/#your-individual-domain-review). Each week, pick one domain above (a different one in Week 10) and post to the [Forum](../../assignments/forum-posts) (~250 words, APA references):

1. **Summary.** What is happening in this domain? Name at least two specific tools, organizations, or deployments, with a source for each.
2. **Preliminary DTPA questions.** At least one question for each of Data, Tools, Practices, and Actions.
3. **A possible case.** One specific, documented case you *could* imagine analyzing.

## Class Meetings

| Day | Date | Focus |
|:---:|:----:|-------|
| M | ~~Oct 26~~ | 🚫 **No class** — Fall Break (Mon Oct 26 – Tue Oct 27) |
| W | **Oct 28** | Introducing Full Case III — Planning and Research |
| F | **Oct 30** | Full Case III — Planning and Research; Complete Part A of Template |
| M | **Nov 2** | Full Case III — Research and Drafting Case Analysis |
| W | **Nov 4** | Full Case III — Research and Drafting Case Analysis; Case Design Scaffold 2 check-in |
| F | **Nov 6** | Full Case III — Completing Case Analysis; Complete Part B of Template · 🎯 **Case Design Scaffold 2 due** |

* **Week 9:** You *may* select new groups for Full Case III, or stay in the same groups.
* **Week 10:** You must stay in your groups for Full Case III and for the Case Design.

## Focus for Weeks 9 and 10

The standard is the same as for Full Cases I and II. All four DTPA sections and all four Pillars of AI Literacy are evaluated. See [Focus for Weeks 5 and 6](../week5and6/#focus-for-weeks-5-and-6) for the full description.

By the third round, we expect your analysis to **compare**. Where it helps, connect your case to one from an earlier round, whether your own group's or one from the readings. For example, compare Rite Aid's facial recognition to Detroit's, Waymo's safety claims to Epic's sepsis model, or Saline Township to Pavilion Township. Comparing cases is one of the clearest ways to show Critical Literacy.

### Week 9 Update (due Sun Nov 1)

Answer the same eight questions as the [Week 5 Update](../week5and6/#week-5-update-due-sun-oct-4) in your group's tab, starting with **Section 0 (Your Notes/Research)**. Groups choosing an **undiscussed area** must name the domain and case in Question 1.

### Week 10 Full Case (due Sun Nov 8)

The complete Case Study, using the same template and DTPA framework. Where your group disagrees, write the disagreement down.

**Looking ahead:** starting in Week 11, groups may sign up to [lead half a class](../../assignments/lesson-planning/) by presenting one of their three Full Cases. If you think Full Case III might be that case, keep your sources and disagreements well organized.

## Case Design: Scaffold 2 (due Fri Nov 6)

Scaffold 2 expands your Scaffold 1 into **Part 2** of the [Case Design template](../../assignments/case-design): a revised Part 1, a full DTPA analysis, a design direction, and an annotated bibliography. **Minimum 1,500 words** across Parts 1 and 2, plus a separate **response-to-feedback document (>250 words)** that addresses your Scaffold 1 feedback.

A few reminders:

* **Revise in place.** Update the Part 1 text instead of writing a second version, and point to each change in your response document.
* **Section 2.5 (Design direction) matters most.** It must be specific enough that someone could disagree with it, and the feedback you get on it is the most useful feedback of the semester.
* **Use your Case Studies.** You have now analyzed two full cases, possibly three. Any of them can supply evidence, comparisons, or models for your design.
* Work through the **"Before you submit Part 2"** checklist in the template.

Use part of Wednesday's class (Nov 4) to check in with your Case Design team, especially if it differs from your Full Case III group.

## Turning In

Same as before: one group member downloads the Word or PDF version of your tab and submits it on D2L to **Week 9 Full Case III Update** and then **Week 10 Full Case III Complete**. Each of you also submits an **Individual Effort & Metacognitive Report** (~250 words) each week. One Case Design team member submits **Scaffold 2** and the **response-to-feedback document** on D2L.

**Due dates:**

* **Tuesday, October 27th at 11:59pm**
    * Week 9 Forum Post (domain review)
* **Sunday, November 1st at 11:59pm**
    * Week 9 Full Case III *Update* (Part A of Template)
    * Week 9 Individual Effort & Metacognitive Report
    * Week 10 Forum Post (domain review, *different* domain)
* **Friday, November 6th**
    * 🎯 Case Design Scaffold 2 and response to Scaffold 1 feedback
* **Sunday, November 8th at 11:59pm**
    * Week 10 Full Case III *Complete* (Part B of Template)
    * Week 10 Individual Effort & Metacognitive Report

## Reminders

Put your group's names at the top of the page, and do not copy from or to other groups' Case Studies.

Case Studies that do not meet the standard will be returned without credit, and your group will have one week from receiving it to revise and meet the standard.

---
