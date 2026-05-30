---
layout: post
title: "Anthropic and OpenAI Finally Found Product-Market Fit — and It's All About Coding Agents"
date: 2026-05-28 09:00:00 +0200
last_modified_at: 2026-05-28 09:00:00 +0200
meta_description: "Simon Willison argues that Anthropic and OpenAI have found genuine product-market fit through coding agents like Claude Code and Codex — as enterprise pricing shifts to API rates and budgets balloon."
description: "Simon Willison argues that Anthropic and OpenAI have found genuine product-market fit through coding agents like Claude Code and Codex — as enterprise"
categories: [industry]
tags: [anthropic, openai, product-market-fit, coding-agents, claude-code, codex, ai-economics, enterprise-ai]
reading_time: 9
hero_image: /assets/images/hero/hero-anthropic-openai-pmf-coding-agents-april-2026.jpg
excerpt: "Simon Willison makes the case that Anthropic and OpenAI have finally found genuine product-market fit — through coding agents. With enterprise pricing switching to API rates and companies spending $200+/month per user, April 2026 marks a new revenue inflection point for frontier AI labs."
author: The Agent Report
---

# Anthropic and OpenAI Finally Found Product-Market Fit — and It's All About Coding Agents

**May 28, 2026** — Is the AI industry's massive infrastructure spend finally paying off? According to a [deeply researched analysis](https://simonwillison.net/2026/May/27/product-market-fit/) by Simon Willison, the answer is a resounding **yes** — and the driver is not chatbots, not image generators, but **coding agents**.

Willison's post, which rocketed to the top of Hacker News with over 830 points and 950 comments, argues that April 2026 marks a genuine inflection point for the frontier AI labs. "I think they've finally found product-market fit, with the coding/general-purpose agent products embodied by Claude Code/Cowork and Codex," he writes.

## Enterprise Customers Are Now Paying API Prices

The cornerstone of Willison's argument is a seismic shift in how Anthropic and OpenAI charge their enterprise customers. At some point in the last six months, Anthropic switched its Enterprise plan to **$20/seat/month plus API pricing for usage**. OpenAI followed suit in April 2026, aligning Codex pricing with API token costs.

This is a dramatic departure from the flat-rate enterprise deals that characterized the 2024–2025 era. Now, companies signing year-long contracts are locked into full API prices — **no more deep discounts**.

> "I currently subscribe to the $100/month Max plan from Anthropic and the $100/month Pro plan from OpenAI," Willison notes. "I just ran the ccusage tool on my laptop to get an estimate of how much I would have spent if I were to pay for API tokens in the past 30 days and got $1,199.79 for Anthropic Claude Code and $980.37 for OpenAI Codex."

That's **$2,180.16 worth of tokens for $200** — and Willison describes himself as a "moderately heavy user," not someone running agents around the clock.

The pricing becomes even starker when you consider the latest model releases. **GPT-5.5** (released April 23rd) costs 2× the API price of GPT-5.4. **Opus 4.7** (April 16th) runs around 1.4× the price of Opus 4.6 when accounting for a new tokenizer. Enterprise customers face a double whammy: higher model prices and the removal of bulk discounts.

## Why This Is Product-Market Fit

Willison draws a crucial distinction between popularity and profitability. ChatGPT boasts more than **900 million weekly active users**, but only **50 million** — 5.6% — are paying consumer subscribers.

"Charging $10–$20/month per user is an OK business, but you'd need 1–2 billion subscribers sticking around for four years to cover $1 trillion in infrastructure," he calculates.

Coding agents change this equation entirely. These tools burn vastly more tokens than chat interfaces, but they are quickly becoming **daily drivers for extremely well-compensated professionals**. Companies spending **$200+/month per user** — or in Willison's power-user case, **~$1,000/month per vendor** — generate revenue at a scale that can meaningfully offset infrastructure costs.

> "Coding agents really did change everything. These are tools which burn vastly more tokens, but are also quickly becoming daily drivers for the work carried out by extremely well-compensated professionals."

The models released in **November 2025** — GPT-5.1 and Opus 4.5 combined with their respective coding agent harnesses — elevated agents to being genuinely useful. We've now had six months for organizations to integrate these tools into their workflows, and the spending is following.

## The Ramp-Up: Enterprise Sales Teams Are Growing Fast

As further evidence, Willison points to the open job listings at both companies:

- **OpenAI**: 703 open jobs, of which **229 (32.6%)** relate to enterprise sales and support — account executives, "Go To Market" roles, and Forward Deployed Engineers.
- **Anthropic**: 390 open jobs, with **105 (26.9%)** in enterprise-facing roles.

"It's pleasingly ironic that these AI labs have picked a business model with such a heavy demand on human labor — enterprise sales contracts don't close themselves without a whole lot of humans in the mix!" Willison observes.

Notably, he conducted this analysis **using Claude Code itself** — scraping job sites, piping data into Datasette Cloud, and analyzing with Datasette Agent. Full dogfooding.

## The "AI Failure" Stories Are Actually Evidence of PMF

The narrative around companies being "shocked" by their AI bills — most notably Uber reportedly maxing out its full-year AI budget just months into 2026 — is actually **evidence for the PMF thesis**, not against it.

> "The best advice I ever heard on pricing a product was that your customer should suck air through their teeth and then say yes. Uber's budget overrun and Microsoft's seat cancellations look like that effect playing out in practice."

Microsoft's decision to cancel Claude Code licenses — ostensibly to encourage dogfooding of Copilot CLI — was also reported to be a financial decision triggered by the June 30th end of Microsoft's fiscal year. When your customers are making billion-dollar budget allocation decisions about your product, you've found product-market fit.

## The Colossus Deal Changes Everything

Perhaps the most staggering data point comes from an unexpected source: **SpaceX's recent S-1 filing** revealed that Anthropic signed a deal for cloud services worth **$1.25 billion per month through May 2029** for access to compute capacity across the Colossus and Colossus II clusters.

The Anthropic announcement indicated this deal would allow them to "increase our usage limits for Claude Code and the Claude API," heavily implying Colossus is being used for inference, not training. Given that Anthropic already has vast compute from other providers, the willingness to spend $1.25 billion/month from just one vendor hints at the enormous scale of inference budgets today.

## A Two-Inflection-Point Story

Willison identifies two critical inflection points:

1. **November 2025** — The *capability* inflection point, when GPT-5.1 and Opus 4.5, combined with their coding agent harnesses, became genuinely useful for real work.

2. **April 2026** — The *revenue* inflection point, when the enterprise pricing shift and the resulting budget impacts made clear that these are real businesses, not just research projects.

> "We'll know for sure how real this moment is when the S-1 documents for the upcoming Anthropic and OpenAI IPOs give us some real, audited numbers to get our teeth into."

## What This Means for the Agent Ecosystem

For the broader AI agent ecosystem, the implications are profound:

- **Cursor and Copilot face direct competition** from Anthropic and OpenAI's own agent products. No wonder Cursor is investing in their own models.
- **Enterprise pricing at API rates** means the cost of running AI agents at scale is now transparent and predictable — but expensive.
- **The middleman squeeze** is real: Anthropic's Claude Code directly competes with the very tools that were previously Anthropic's biggest API customers (Cursor and GitHub Copilot were reportedly responsible for $1.2 billion of Anthropic's then-$4 billion revenue in 2025).
- **Infrastructure providers** (CoreWeave, Lambda, and now SpaceX) become critical — and their own IPOs will provide visibility into the AI industry's true scale.

For developers and enterprises building on AI agents, the message is clear: the era of cheap, flat-rate agentic automation is over. But the value these tools deliver is now proven enough that organizations are willing to pay real money. That's not a bug — it's product-market fit.

<p><em>Read the full original analysis: <a href="https://simonwillison.net/2026/May/27/product-market-fit/">"I think Anthropic and OpenAI have found product-market fit" by Simon Willison</a></em></p>
