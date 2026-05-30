---
layout: post
title: "The First AI-Written Zero-Day — Google Confirms Criminal Hackers Used AI to Find a Critical Software Flaw"
date: 2026-05-12 10:00:00 +0200
last_modified_at: 2026-05-12 10:00:00 +0200
meta_description: "Google confirms the first documented case of criminal hackers using AI to discover and weaponize a zero-day vulnerability, marking a watershed for offensive AI."
description: "Google confirms the first documented case of criminal hackers using AI to discover and weaponize a zero-day vulnerability, marking a watershed for"
categories: [industry]
tags: [google, ai-security, zero-day, cyber-crime, ai-agents, vulnerability, mandiant]
reading_time: 8
excerpt: "Google Threat Intelligence Group confirms the first documented case of criminal hackers using AI to discover and weaponize a zero-day vulnerability. The finding marks a watershed moment for offensive AI agents — and a wake-up call for every security team."
hero_image: /assets/images/hero/hero-google-confirms-criminal-hackers-ai-zero-day.jpg
author: The Agent Report
---

# The First AI-Written Zero-Day — Google Confirms Criminal Hackers Used AI to Find a Critical Software Flaw

**For the first time, Google's Threat Intelligence Group (GTIG) has documented a criminal threat actor using an AI model to discover a zero-day vulnerability — and developing a working exploit for what would have been a mass-exploitation event. The finding, published Monday, confirms what security researchers have feared for months: agentic AI is no longer just a defensive tool — as the [CISA/NSA Five Eyes guidance]({% post_url 2026-05-03-cisa-nsa-five-eyes-ai-agent-security-guidance %}) warned just weeks earlier.**

---

## The Watershed Moment

In its [latest threat intelligence report](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access), GTIG revealed that it identified "a threat actor using a zero-day exploit that we believe was developed with AI." The criminal group planned to use it in a mass exploitation campaign, though Google's "proactive counter discovery may have prevented its use."

The exploit wasn't a simple script kiddie tool. According to the report, the AI-powered approach went beyond what most penetration testing tools can achieve — it didn't just scan for known signatures, but *reasoned* about the codebase to identify logic flaws that would be invisible to traditional scanners.

> "For the first time, GTIG has identified a threat actor using a zero-day exploit that we believe was developed with AI."
> — Google Threat Intelligence Group

This is the moment the theoretical threat of "AI-powered cybercrime" became concrete. The report documents a full spectrum of AI-augmented offensive operations, from vulnerability discovery to autonomous malware orchestration.

## How Criminal Hackers Are Using AI Agents

The Google report details several alarming developments:

### 1. AI-Augmented Zero-Day Discovery

The criminal group behind the zero-day used large language models to perform deep code analysis — identifying a flaw that had eluded both human reviewers and traditional static analysis tools. The model was fed vulnerability datasets to prime its reasoning, allowing it to spot edge cases and logic errors that standard fuzzing would miss.

### 2. State-Sponsored Actors Are Doing It Too

Google observed threat actors linked to the People's Republic of China (PRC) and the Democratic People's Republic of Korea (DPRK) pursuing sophisticated AI-augmented vulnerability research. These groups employed "persona-driven jailbreaking attempts" and integrated specialized security datasets — including a distilled knowledge base of over **85,000 real-world vulnerability cases** from the Chinese bug bounty platform WooYun — to train models for code analysis.

### 3. Autonomous Malware Operations

Google documented **PROMPTSPY**, an AI-enabled malware that represents a shift toward fully autonomous attack orchestration. Rather than following a fixed playbook, PROMPTSPY interprets system states to dynamically generate commands and manipulate victim environments. It operates like an AI agent — but with malicious intent.

### 4. Agentic Frameworks in the Hands of Adversaries

Perhaps most striking for the agent community: Google directly observed threat actors experimenting with **OpenClaw** and **OneClaw** — popular open-source agent frameworks — alongside intentionally vulnerable testing environments. They're using these tools to refine AI-generated payloads in controlled settings before deployment.

> "In their pursuit of this vulnerability research, we see clear indications of automation and scaled research... actors are also experimenting with [agentic tools such as OpenClaw and OneClaw]({% post_url 2026-05-14-openclaw-plugin-externalization-security-hardening-beta7 %}) alongside intentionally vulnerable testing environments."
> — Google Threat Intelligence Group

## The Defense One Perspective

The Google report aligns with a [separate analysis from Defense One](https://www.defenseone.com/threats/2026/05/pentagon-leaders-love-agentic-ai-its-giving-cyber-criminals-nation-state-powers/413379/), which notes that while Pentagon leaders are enthusiastic about agentic AI for defense, the same technology is giving cybercriminals nation-state-level capabilities.

Jackson Reed, founder of AI startup Barding Defense, put it bluntly: **"We're going to see criminal groups look a lot more like state actors."**

The Pentagon is reportedly evaluating Anthropic's **Mythos** — the same model that recently shattered METR's time-horizon benchmark — for vulnerability discovery. But the same capabilities are being turned against everyone.

## Google Strikes Back With AI Defenders

The report isn't all doom and gloom. Google detailed its own defensive AI agent arsenal:

| Agent | Role |
|-------|------|
| **Big Sleep** | AI agent for automated vulnerability discovery in Google's codebase |
| **Gemini + CodeMender** | Automated fix generation using AI reasoning |
| **SAIF Framework** | Secure AI Framework for protecting ML supply chains |

The message is clear: the same technology enabling offensive agents is also powering defensive ones. The question is which side moves faster.

## Why This Matters for the AI Agent Ecosystem

This is not just a security story — it's an **agent story**. The key development isn't that AI can find bugs (we've known that for a while). It's that:

1. **Agentic workflows** — the ability for AI to autonomously iterate, test, and refine exploits — are what made this zero-day possible
2. **Open-source agent frameworks** like OpenClaw are being repurposed for offensive operations
3. The **defense-offense gap** is narrowing: the same agent architectures that power Hermes Agent, Claude Code, and OpenClaw are being used on both sides

## What Comes Next

The security community is entering a new phase. The era of AI-versus-AI cyber conflict is no longer hypothetical. Security teams need to assume that adversaries have access to the same frontier models and agent frameworks they do.

**For developers and security teams:**

- Assume AI-powered attacks are already targeting your infrastructure
- Invest in AI-augmented defensive agents (Big Sleep, CodeMender, and open-source alternatives)
- Monitor agent supply chains — Google found attackers compromising AI software dependencies as an initial access vector
- Treat your agent skill repositories and MCP servers as critical security surfaces

**For the agent community:**

The same skills that make agents powerful — tool use, autonomous reasoning, multi-step planning — make them dangerous in the wrong hands. This report is a reminder that security isn't just about sandboxing agents. It's about the global arms race between defensive and offensive agentic AI.

---

*Read the full Google Threat Intelligence report [here](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access).*

*Coverage also from: [The New York Times](https://www.nytimes.com/2026/05/11/us/politics/google-hackers-attack-ai.html), [Defense One](https://www.defenseone.com/threats/2026/05/pentagon-leaders-love-agentic-ai-its-giving-cyber-criminals-nation-state-powers/413379/), [Hacker News discussion (170 pts)](https://news.ycombinator.com/item?id=48094641)*
