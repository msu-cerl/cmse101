---
title: "Week 3 Case Study: Transformers and Generating Text"
date: 2026-09-04
draft: false
description: "Week 3 Materials CMSE 101, Fall 2026"
tags: ["AI", "society", "education", "MSU", "schedule"]
author: "Danny Caballero"
---

> All of this material is also available on [Google Docs](#) (*MSU login required*)

![Placeholder: probability distribution over next tokens](../../images/next-token.png)

*Source: [add]*

## Predicting the Next Word

In June 2017, eight researchers at Google published an eleven-page paper called "Attention Is All You Need." It described a way for a computer to process an entire sequence of text at once — a sentence, a paragraph, a whole article — instead of walking through it word by word. They called the architecture a **transformer**. Five years later, in November 2022, that architecture reached the public as ChatGPT.

The thing it does is narrower than it looks. Given some text, it produces a **probability distribution over what comes next**, then picks from that distribution, then does it again. That's it. Everything else — the essay, the code, the apology, the fabricated legal citation — is that loop running a few hundred times.

On Monday we will run that loop by hand, with dice. You will produce fluent sentences that are confidently wrong, and nothing about your process will have malfunctioned.

This week we add **Practices**. A tool is only half the story. The other half is people: who built it, on whose words, with whose labor, using whose water and electricity — and who is now expected to use it, at what pace, with what checking step quietly removed. Practices asks who is doing this, who is paying for it, and who has managed to make anyone stop.

## Prep reading & resources (Complete by Wed, Sep 16)

*You do not individually have to review all materials. We expect that you will spend at least 90 minutes with these materials. Groups can discuss how to ensure all posted materials are reviewed each week.*

### How the tool works

* 📖 [Generative AI exists because of the transformer](https://ig.ft.com/generative-ai/) (Murgia and the Visual Storytelling Team, *Financial Times*, 2023) — open access, scroll-based, no mathematics. Transformers process an entire sequence at once, analyzing all its parts rather than individual words, which is the change that made everything after 2017 possible. Also covers where these systems go wrong. If you read one thing this week, read this.
* 📺 [But what is a GPT?](https://www.youtube.com/watch?v=wjZofJX0v4M) (3Blue1Brown via YouTube, Chapter 5) — predict, sample, repeat. Pay attention to the section on **softmax with temperature**, because that is precisely what we will be doing with dice on Monday (27 min).
* 📺 [Attention in transformers, visually explained](https://www.youtube.com/watch?v=eMlx5fFNoYc) (3Blue1Brown via YouTube, Chapter 6) — how context gets computed. The example to hold onto: the word "mole" in "American shrew mole," "one mole of carbon dioxide," and "a biopsy of the mole." Same word, three meanings, and the model has to work out which from everything around it. Harder than Chapter 5; optional (26 min).
* 🖱️ [Transformer Explainer](https://poloclub.github.io/transformer-explainer/) (Cho et al., Georgia Tech) — a real GPT-2 running in your browser. Type a sentence and watch the probability distribution over the next word change as you edit. There is a temperature slider. Play with it before class on Monday and the dice will make immediate sense.

### Where the words came from

* 📖 [We Tracked a Shipment of Rare Books. It Ended at an Amazon AI Training Facility](https://www.404media.co/we-tracked-a-shipment-of-rare-books-it-ended-at-an-amazon-ai-training-facility/) (Maiberg, *404 Media*) — reporters hid a tracking device inside a rare book they suspected would be bought for AI training data, then followed it across the country to an Amazon warehouse in Las Vegas. Employees there say the job is receiving pallets of printed books and cutting the bindings off so they can be scanned faster. Amazon's book-buying operation had never been reported before. Note the method: this is what it took to find out, and a four-person outlet had to do it.
* 📖 [The Unbelievable Scale of AI's Pirated Book Problem](https://www.theatlantic.com/technology/archive/2025/03/libgen-meta-openai/682093/) (Reisner, *The Atlantic*, 2025) — includes a search tool covering the 7.5 million books in LibGen. Search an author you love.
* 🖱️ [Anthropic Copyright Settlement Works List](https://secure.anthropiccopyrightsettlement.com/lookup) — the searchable list of roughly 500,000 books covered by a $1.5 billion settlement. Two things happened in that case and courts treated them oppositely: buying physical books, cutting the bindings, scanning them and destroying the originals was ruled fair use as a format conversion, while downloading millions of books from pirate libraries was not. Most people assume the destruction was the offense. It wasn't. Sit with that.
* 📖 [Common Crawl investigation](https://www.theatlantic.com/technology/archive/2025/11/common-crawl-ai-training-data/684567/) (Reisner, *The Atlantic*, 2025) — the nonprofit whose web scrape underpins much of this told publishers it respected paywalls and honored removal requests. Reporting found otherwise.

### Who did the labor

* 🖱️ [The Data Workers' Inquiry](https://data-workers.org/) (DAIR Institute, Weizenbaum Institute, TU Berlin) — nineteen data workers from Kenya, Venezuela, Syria, Brazil, France, Germany and elsewhere researched their own workplaces as co-researchers rather than as interview subjects, and each chose the form their report would take. The result is documentaries, zines, comics, podcasts, animations and essays. Pick one and go deep:
  * 📺 **Data Workers Organizing: The African Content Moderators Union** — Richard Mathenge, a former team leader, on the conditions at Sama in Nairobi that led workers to form a union in 2023. *Content warning: describes workplace violence, including sexual violence against women and children.*
  * 📺 **A day annotating in Syria** — Yasser Yousef Alrayes, who annotates images to pay for his education, on badly specified tasks and impossible client demands (8 min).
  * 📺 **Oskarina's and Ruba's animated videos** — platform-mediated data work in Latin America. The gentlest entry point here.
  * 📖 **The Emotional Labor Behind AI Intimacy** — Michael Geoffrey Abuyabo Asia worked for Sama, CloudFactory, TELUS, Appen and others, and part of his job was impersonating AI companions: doing emotional labor for users who believed they were talking to a machine. We assume human labor comes before the model. Sometimes the human labor *is* the model.
* 📖 [OpenAI Used Kenyan Workers on Less Than $2 Per Hour](https://time.com/6247678/openai-chatgpt-kenya-workers/) (Perrigo, *TIME*, 2023) — to build a filter that could catch descriptions of child sexual abuse, torture, self-harm and incest, someone first had to read tens of thousands of such passages and label them. Workers took home between roughly $1.32 and $2 an hour. OpenAI was billed about $12.50 an hour for that same labor. Sama ended the contract eight months early. *Content warning: the article describes the material workers had to read.*
* 📖 [Data workers detail exploitation by tech industry](https://techcrunch.com/2024/07/08/data-workers-detail-exploitation-by-tech-industry-in-dair-report) (*TechCrunch*, 2024) — short framing piece. Note the structural point: workers sit as subcontractors to subcontractors, so lines of responsibility blur if anything ever goes wrong.

### What it costs, and who lives next to it

* 🎧 [No AI data centers in my backyard!](https://www.npr.org/transcripts/nx-s1-5581445) (The Indicator from Planet Money) — **this one is down the road.** Pavilion Township, outside Kalamazoo, fighting a proposed data center. One resident: it brings no tourism, no jobs, nothing, only issues. Roughly 10 minutes, full transcript posted (10 min).
* 🎧 [Data Vampires](https://techwontsave.us/episode/241_data_vampires_going_hyperscale_episode_1) (Paris Marx, *Tech Won't Save Us*, four-part series) — the most sustained critical treatment of data centers available in audio. Episode 1 covers the push to hyperscale; Episode 2 covers communities organizing against it.
* 📖 [How to stop a data center](https://disconnect.blog/how-to-stop-a-data-center/) (Marx interviewing Sebastián Lehuedé, *Disconnect*) — read this for the complication rather than the argument. Many activists organizing against these facilities have Gmail accounts and hold their meetings on Google Meet. Opposing a company you depend on is genuinely hard, and pretending otherwise is not analysis.
* 📖 [Environmental cost of AI's energy use](https://unu.edu/inweh/news/environmental-cost-of-AIs-Enrgy-use-carbon-water-and-land-footprints) (United Nations University, 2026) — global data centers used an estimated 448 TWh of electricity in 2025; as a country that would rank 11th, behind France and ahead of Saudi Arabia. The correction most people need: **inference, not training, is the majority of it.** Training GPT-3 took roughly 1.3 GWh, once. Serving billions of daily queries accounts for an estimated 80 to 90 percent of a deployed model's energy. This is not a thing that was done. It is a thing being done, continuously, including by us.
* 🎧 [What AI data centers are doing to your electric bill](https://www.npr.org/2025/12/19/nx-s1-5649814/ai-data-center-electricity-bill) (Planet Money, Dec 2025) — traces a single Ohio electric bill back to its source (32 min).

### Why it makes things up

* 📖 [Why language models hallucinate](https://openai.com/index/why-language-models-hallucinate/) (OpenAI, 2025) — read the blog post, not the paper. The argument: models guess because training and evaluation reward guessing. If a wrong answer and "I don't know" score identically, a system optimized to score well will always guess — the same reason you bubble in a letter rather than leaving a question blank. **Read this after Monday's class** and it will feel obvious rather than technical.
* 🖱️ [AI Hallucination Cases Database](https://www.damiencharlotin.com/hallucinations/) (Damien Charlotin, HEC Paris) — live, searchable, updated daily. Over 2,000 court decisions worldwide where someone filed AI-fabricated citations. Filter by country, court, tool, outcome. **You can filter it to Michigan.**

### The practices being built right now

* 📖 [AI Is Supercharging the War on Libraries, Education, and Human Knowledge](https://www.404media.co/ai-is-supercharging-the-war-on-libraries-education-and-human-knowledge/) (Koebler, *404 Media*, 2025) — a school library catalog product added an AI "sensitive material marker" with traffic-light risk ratings, advertising that districts may cut manual review workload by more than 80 percent when complying with book-ban legislation. Librarians describe being flooded with AI-generated books they must screen while being handed AI tools to screen them. A complete Practices case in one article.
* 📖 [Your AI Use Is Breaking My Brain](https://www.404media.co/your-ai-use-is-breaking-my-brain/) (Koebler, *404 Media*, 2026) — on the cognitive load that other people's AI use imposes on everyone else. Is this AI? Do I care? Is this a person at all? Harms are not only distant.

## Monday: Rolling a Sentence

You are the model. Stay in your assigned group. You will need dice.

### Round 1 — the untrained model (~10 min)

Each group gets a sentence stem and a numbered list of six words. Roll one die, take that word, write it down. Repeat six times. Read your sentence out loud.

It will be nonsense. That is a **uniform distribution** — every word exactly as likely as every other. This is what a model knows before it is trained on anything.

### Round 2 — weights (~15 min)

Same stem, new rule: roll **two dice and use the sum**. Your table maps sums to words, and it is not evenly filled in. A sum of 7 comes up most often, so 7 holds the most plausible next word. Sums of 6 and 8 hold reasonable alternatives. Sums of 2 and 12 hold something absurd.

Roll six more times. Now most sentences work, and every so often one lurches somewhere strange.

Nothing changed except the **shape of the distribution**. No new words, no new rules, no cleverness. The weights are the training. That is the entire idea.

### Round 3 — temperature (~10 min)

Same table. Two different rules for using it.

* **Take 7 every time. Don't roll.** Write the sentence.
* **Roll and accept whatever comes up**, including 2 and 12. Write that one too.

Compare across the room. Under the first rule, every group in the class produces nearly the same sentence: fluent, safe, dull. Under the second, the sentences are surprising and some are unusable.

You have just built the temperature slider in the Transformer Explainer. Same model, same weights, different willingness to take the unlikely branch.

### Round 4 — the passage that changes meaning (~15 min)

Every group now gets the **same passage** and the **same tables**. One entry in those tables is a plausible-sounding claim that happens to be false.

Roll. Write. Read them aloud around the room.

Then the question: **whose model broke?**

Nobody's. Every group ran an identical procedure correctly. Some sentences came out true, some came out false, and the false ones sound exactly as confident as the true ones — because confidence was never something the procedure tracked. It sampled from a distribution. It did what it was built to do.

Last question before you leave: **your table had no entry for "I don't know."** Should it have? And what would have to change about how we score your sentences for that entry ever to get picked?

### One thing this activity gets wrong on purpose

Dice tables are a lookup. A transformer is not. The rolling shows you what the model does *with* the probabilities — the last step of a long process. The transformer is how those probabilities get computed in the first place, using everything in the context at once. That is what Chapter 5 and the FT explainer cover, and it is the piece the dice cannot show you.

## Wednesday and Friday: Find a Case

**Wednesday you find a case; Friday you analyze it in your group.**

You choose your own. It must be documented and specific enough to name who used the tool and when. "AI in healthcare" is not a case. "A hospital system that deployed an AI scribe to draft clinical notes" is.

Places to start looking:

| Where | What you'll find |
|---|---|
| [AI Hallucination Cases Database](https://www.damiencharlotin.com/hallucinations/) | 2,000+ court decisions, filterable to Michigan |
| [AI Incident Database](https://incidentdatabase.ai/) | Structured, cross-domain, sourced |
| [404 Media](https://www.404media.co/tag/ai-slop/) | Ongoing reporting on AI in workplaces, schools, libraries |
| [The Data Workers' Inquiry](https://data-workers.org/) | Worker-authored accounts of building these systems |
| [Atlantic LibGen search](https://www.theatlantic.com/technology/archive/2025/03/libgen-meta-openai/682093/) / [Settlement Works List](https://secure.anthropiccopyrightsettlement.com/lookup) | Search for a specific book |
| Local news: "data center" + any Michigan township | Pavilion Township, and others |

You are not required to pick something harmful. You are required to pick something **documented**, and then to follow the labor and the resources wherever they actually go.

## Focus for Week 3

This week we add **Practices**. You will still complete Data and Tools — we are building up, not moving on — but your evaluation this week focuses on the Practices parts. Data and Tools should be getting faster; be briefer there than you were in Weeks 1 and 2.

### What "meeting the standard" looks like this week

The habit carries over unchanged: a specific claim with a source, not a general statement. For Practices, "specific" means naming **people, workflows, and decisions** — not capabilities.

* **Use — how does the tool actually get used?** Describe the workflow, not the product. Who sits down and prompts it? Who receives the output? What did that person do before this tool existed, and what are they expected to do instead now? Where in the chain is someone supposed to check the result, and is that step written down anywhere or merely assumed?
    * Strong: *"A school library product markets an AI 'sensitive material marker' with traffic-light risk ratings and advertises that districts may reduce manual review workload by more than 80% when complying with book-ban legislation, which means a librarian's judgment about a book is replaced by a flag they are expected to accept (404 Media, 2025)."*
    * Weak: *"Schools are using AI to review books."*
* **Labor and resources — what did it take to build, and what does it take to run?** Both halves are required. For **labor**: who annotated, moderated, cleaned, wrote, or performed the material this system depends on — under what pay, what conditions, and through how many layers of subcontracting? For **resources**: what does it consume, and who lives next to that consumption? Name a specific input wherever you can.
    * Strong: *"Workers labeling descriptions of abuse for a content filter took home roughly $1.32 to $2 per hour while the client was billed about $12.50 (TIME, 2023), and workers report sitting as subcontractors to subcontractors, so responsibility is difficult to trace (TechCrunch, 2024). Separately, global data centers consumed an estimated 448 TWh in 2025, which would rank 11th among nations, and inference rather than training accounts for 80–90% of a deployed model's energy (UNU, 2026)."*
    * Weak: *"Training AI takes a lot of data and energy."*
* **Constraint and critique — what pushed back, and did anything actually change?** Keep these separate. **Critique** is someone saying this is wrong: reporting, a paper, an op-ed, a worker's testimony. **Constraint** is a change in what someone is now permitted to do: a union contract, a court ruling, a settlement, a zoning denial, a written policy. Name at least one of each where both exist, and state plainly whether the critique produced a constraint or didn't.
    * Strong: *"TIME's reporting was critique. Sama ended the contract, but roughly 200 Nairobi jobs ended with it, so the practice relocated rather than stopped. The African Content Moderators Union, formed in 2023, is the constraint, because it changes what an employer can decide unilaterally going forward (DAIR, 2024)."*
    * Weak: *"There has been a lot of criticism of AI labor practices."*

### The trap to avoid

**Critique is not constraint.** Being written about is not the same as being stopped. An article, a lawsuit, and a signed policy are three very different objects, and only one of them changes what someone may do tomorrow. We made this point in Week 2: Detroit's settlement did not make the algorithm more accurate, it changed what police were permitted to do with the output.

So answer directly for your case: **after the criticism, what can someone no longer do that they could do before?** If the answer is nothing, say so. That is a finding, not a hole in your research. A practice that absorbed its critique and carried on unchanged deserves more analysis than one that got fixed.

*If your Practices section only describes what the technology can do, you have written a Tools section. Practices is about people: who is doing this, who is paying for it, and who managed to make anyone stop.*

### Working through the materials

Divide the materials among yourselves and bring back what you found. Five threads this week:

1. How the model actually predicts a word (FT explainer, 3Blue1Brown)
2. Where the training text came from and how it was obtained (404 Media, The Atlantic, the settlement list)
3. Who did the labor of building it (Data Workers' Inquiry, TIME)
4. What running it consumes and who lives beside that (Planet Money, Marx, UNU)
5. Why it produces confident falsehoods (OpenAI, Charlotin database)

Thread 1 is the one nobody should skip entirely. Without it, your Practices section will describe a mysterious force rather than a mechanism, and mysterious forces cannot be constrained.

A note on threads 3 and 4: several of these materials carry content warnings, and they are marked. The Latin America animations and the Syria film cover the same ground without the moderation material. Choose accordingly, and tell your group what you took so the coverage still works.

Where your group disagrees, write the disagreement down. The Marx interview is designed to produce it — you will find yourselves arguing about a technology you are also using to argue about it.

## Citations

Cite all sources in **APA format** in the Research Resources section. Every factual claim in your Data, Tools, and Practices sections should be traceable to something on that list.

## Turning In

When you have completed your Case Study, download the Word or PDF version of your tab and turn it in on D2L to the assignment **Week 3 Case Study**. It is a group assignment, so only one member of the group needs to turn it in.

Each of you also submits an **Individual Effort & Metacognitive Report** (~250 words) as a separate individual upload on D2L. Describe what you contributed, what you learned, and any AI used in your work.

**Week 3's Case Study and Individual Reports are due by Sunday, September 20th at 11:59pm.**

## Reminders

Put your group's names at the top of the page, and do not copy from or to other groups' Case Studies.

Case Studies that do not meet the standard will be returned without credit, and your group will have one week from receiving it to revise and meet the standard.

---