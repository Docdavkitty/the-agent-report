---
layout: post
title: "Frontier AI Has Broken the Open CTF Format — And the Scoreboard Will Never Be the Same"
date: 2026-05-17 10:00:00 +0200
last_modified_at: 2026-05-17 10:00:00 +0200
meta_description: "Claude Opus 4.5 and GPT-5.5 Pro have shattered the open Capture The Flag format as agentic solvers make the old game obsolete, threatening the next generation."
categories: [research]
tags: [ctf, cybersecurity, frontier-models, agentic-security, ai-impact]
reading_time: 8
excerpt: "Claude Opus 4.5, GPT-5.5 Pro, and the rise of agentic solvers have quietly shattered the open Capture The Flag competition format — one facet of the [broader state of AI agents in May 2026](/2026/05/state-of-ai-agents-may-2026/). A top-tier CTF veteran explains why the old game is gone — and why pretending otherwise hurts the next generation of security talent."
hero_image: /assets/images/hero/hero-ctf-frontier-ai-may17.jpg
author: The Agent Report
---

# Frontier AI Has Broken the Open CTF Format — And the Scoreboard Will Never Be the Same

**Capture The Flag competitions — the crucible where generations of cybersecurity talent forged their skills — are quietly collapsing under the weight of AI agents. Not because the challenges are being solved by humans using LLMs as a crutch, but because agentic systems can now churn through entire challenge categories without human intervention.**

In a [deeply personal and provocative essay](https://kabir.au/blog/the-ctf-scene-is-dead) published this weekend that rocketed to the top of Hacker News with over 370 points, Australian CTF veteran Kabir (username `frays`) makes a blunt declaration: *"The scoreboard does not measure human skill cleanly anymore, and the old game is not coming back."*

As an editor at *The Agent Report*, this story lands squarely at the intersection of two worlds we cover daily — frontier AI capability and the real-world disruption of agentic automation. This isn't a theoretical future: **it's happening right now, on live scoreboards, in real time.**

## The Ladder That Built a Generation

Kabir's credentials are not those of a casual observer. He started CTFs in 2021, won Australia's largest CTF (DownUnderCTF) multiple times with team Blitzkrieg, and later joined TheHackersCrew — an international top-tier team consistently ranked in the CTFTime global top 10. When he says CTFs "taught me how to learn, gave me a way to measure myself, and introduced me to many of the people I respect most in the field," he speaks for thousands.

CTF competitions were never just about the flags. They were a **ladder** — a structured progression where beginners could climb from simple web exploitation challenges to advanced binary exploitation and cryptography. You could see yourself improve, solve more challenges, place higher, join better teams. That feedback loop — *active struggle → learning → visible progress* — was the engine that produced a generation of security professionals.

> *"Even as a beginner, you had something to climb. You could see yourself improve, solve more challenges, place higher, join better teams, and become more competitive over time. That feedback loop is breaking."*
> — Kabir, "Frontier AI has broken the open CTF format"

## The Three Waves of AI Disruption in CTFs

### Wave 1: GPT-4 — The First Cracks

When GPT-4 first arrived, a significant percentage of **medium-difficulty** CTF challenges became "one-shottable" — a single prompt could produce the solve and flag. At the time, the community didn't panic. Hard challenges remained untouched, and the time savings weren't large enough to ruin the competitive experience. CTF players have always used tools, and this felt like a more powerful addition to the toolbox.

### Wave 2: Claude Opus 4.5 — The Tipping Point

The release of Claude Opus 4.5 changed everything. Kabir describes the shift bluntly:

> *"Almost every medium difficulty challenge, and some hard challenges, became agent-solvable. Claude Code packaged everything into a CLI and made it easy to connect other CLI and MCP tools. It became trivial to build an orchestrator that used the CTFd API to spin up a Claude instance for every challenge."*

Teams that refused to use AI weren't just missing a convenience — they were playing a fundamentally slower version of the game, reflecting the [agent safety trust gap]({% post_url 2026-05-23-agent-safety-trust-gap-may23 %}) between capability and understanding. The scoreboard started measuring **orchestration skill and willingness to use frontier models** alongside, and sometimes above, raw security expertise.

### Wave 3: GPT-5.5 Pro — The Nail in the Coffin

With GPT-5.5 and GPT-5.5 Pro, the situation has escalated further. Kabir reports that these models can **one-shot "Insane" difficulty active leakless heap pwn challenges on HackTheBox** — the kind of challenges that previously marked the pinnacle of competitive CTF difficulty.

> *"If you orchestrate Pro against Insane challenges in a 48-hour CTF, there is a good chance you get the flag before the event ends. That makes open CTFs pay-to-win. The more tokens you can throw at a competition, the faster you can burn down the board."*

## The Anti-Pattern Nobody Is Talking About

Perhaps the most troubling insight from Kabir's essay concerns the **beginners**. Veteran HN commenter `hoyd` distilled it perfectly:

> *"That feedback loop is breaking. If the visible scoreboard is dominated by teams using AI, a beginner is pushed toward using AI before they have built the instincts the AI is replacing. That is an anti-pattern. It prevents active learning, and active struggle is the bit that actually teaches you."*

This is a problem that extends far beyond CTFs. In interviews, software engineering hiring, and competitive programming, the same dynamic is emerging: beginners skip foundational struggle for immediate AI-powered results, **short-circuiting the very process that builds expertise**.

Thomas Ptacek of Hacker News — a legendary figure in CTF/security circles — added important nuance:

> *"A big fraction of the comments on this thread are about the impact of cheating on competitive games. It's important to understand that automating CTF challenges isn't usually cheating. It's normally part of CTF culture. The better teams have toolboxes ready to shred the early challenges."*

But the argument cuts both ways: when the "toolbox" becomes a frontier LLM that does the *reasoning* as well as the execution, the line between tool-assisted competition and automation dissolves entirely.

## What This Means for the Agent Age

The CTF story is a canary in the coal mine for a much broader phenomenon. **Any skill-assessment format that depends on solvable puzzles is vulnerable to agentic automation.** This includes:

- **Technical interviews** — LeetCode-style problems are already being solved in real-time by candidates using AI
- **Cybersecurity certifications** — practical exams that test tool usage are trivial for agentic systems
- **Bug bounty programs** — automated vulnerability discovery by AI agents is already a [documented phenomenon](https://arxiv.org/abs/2512.20798)
- **Competitive programming** — as HN commenter `lg5689` noted, "this is happening to other forms of competitive programming too"

The [δ-mem paper](https://arxiv.org/abs/2605.12357) (also trending on HN this weekend) points to a future where LLMs have efficient, persistent memory — making agentic solvers even more capable over longer time horizons. Combine that with frontier models approaching Claude Mythos-level capability at GPT-5.5 Pro pricing, and the trend line is clear.

## An Open Question

Kabir doesn't offer a solution, and neither can we. The CTF community is grappling with question that will soon face every domain that uses structured challenges for skill assessment:

**How do you design a meaningful test of human capability when a capable AI agent can solve the test?**

Some suggestions circulating in the HN thread include:

1. **In-person, supervised competitions** — but this eliminates the open, global nature of CTFs
2. **Challenges requiring physical-world interaction** — impractical at scale
3. **Challenges that test creativity and novel insight** — the hardest category for current models
4. **Accepting the new reality** — CTFs as AI-versus-AI spectacles, with human skill measured differently

None of these fully satisfy. But the debate itself is urgent — and it's happening right now, in every field touched by agentic AI.

---

*Featured image generated by The Agent Report. Read the original essay at [kabir.au/blog/the-ctf-scene-is-dead](https://kabir.au/blog/the-ctf-scene-is-dead). Join the discussion on [Hacker News](https://news.ycombinator.com/item?id=48157559).*
