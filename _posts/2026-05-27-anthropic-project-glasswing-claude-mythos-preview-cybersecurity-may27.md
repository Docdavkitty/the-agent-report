---
layout: post
title: "Anthropic Launches Project Glasswing — Claude Mythos Preview, $100M Cyber Defense Initiative with AWS, Apple, Google, Microsoft, and NVIDIA"
date: 2026-05-27 16:00:00 +0200
last_modified_at: 2026-05-27 16:00:00 +0200
meta_description: "Discover Project Glasswing, Anthropic's $100M cybersecurity initiative with AWS, Apple, Google, Microsoft, and NVIDIA, powered by Claude Mythos Preview for autonomous defense."
description: "Discover Project Glasswing, Anthropic's $100M cybersecurity initiative with AWS, Apple, Google, Microsoft, and NVIDIA, powered by Claude Mythos Preview"
categories: [industry]
tags: [anthropic, claude, cybersecurity, glasswing, mythos-preview, zero-day, ai-safety]
reading_time: 6
hero_image: /assets/images/hero/hero-anthropic-project-glasswing-claude-mythos-preview-cybersecurity-may27.jpg
excerpt: "Anthropic today announced Project Glasswing, a landmark cybersecurity initiative backed by $100M in model usage credits and partnerships with AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, NVIDIA, and Palo Alto Networks. At its core is Claude Mythos Preview — an unreleased frontier model that autonomously discovered a 27-year-old vulnerability in OpenBSD and a 16-year-old flaw in FFmpeg that had survived 5 million automated test passes."
author: The Agent Report
---

<style>
.highlight-box { background: #1a1a2e; border-left: 4px solid #fdcb6e; padding: 1.2rem 1.5rem; margin: 1.5rem 0; border-radius: 0 8px 8px 0; }
.highlight-box p { margin: 0; }
.stat-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin: 1.5rem 0; }
.stat-card { background: #1a1a2e; border-radius: 8px; padding: 1rem; text-align: center; border: 1px solid #2a2a3e; }
.stat-card .stat-value { font-size: 1.6rem; font-weight: bold; color: #fdcb6e; }
.stat-card .stat-label { font-size: 0.85rem; color: #888; margin-top: 0.3rem; }
</style>

**Anthropic today announced [Project Glasswing](https://www.anthropic.com/glasswing)**, the most ambitious cross-industry cybersecurity initiative ever mounted by an AI company. The project brings together **AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, NVIDIA, and Palo Alto Networks** around a single goal: securing the world's most critical software before AI-augmented attackers can exploit it.

At the heart of Glasswing is **Claude Mythos Preview** — a new, unreleased frontier model that Anthropic describes as having crossed a threshold where AI can "surpass all but the most skilled humans at finding and exploiting software vulnerabilities." The model has already discovered **thousands of high-severity vulnerabilities**, including critical flaws in every major operating system and web browser.

<div class="stat-grid">
<div class="stat-card"><div class="stat-value">$100M</div><div class="stat-label">Model Usage Credits</div></div>
<div class="stat-card"><div class="stat-value">$4M</div><div class="stat-label">Open Source Donations</div></div>
<div class="stat-card"><div class="stat-value">12</div><div class="stat-label">Launch Partners</div></div>
<div class="stat-card"><div class="stat-value">40+</div><div class="stat-label">Additional Participants</div></div>
</div>

---

## What Claude Mythos Preview Found

The model's capabilities were demonstrated through a series of striking vulnerability discoveries conducted entirely autonomously:

**🔴 A 27-year-old vulnerability in OpenBSD** — one of the most security-hardened operating systems in the world, used to run firewalls and critical infrastructure. The flaw allowed an attacker to remotely crash any machine running the OS just by connecting to it.

**🔴 A 16-year-old vulnerability in FFmpeg** — the ubiquitous video encoding library used by countless applications. The vulnerable line of code had been hit **five million times** by automated testing tools without ever triggering a detection.

**🔴 A chain of vulnerabilities in the Linux kernel** — the software powering most of the world's servers. Mythos autonomously found and chained together several flaws to escalate from ordinary user access to complete system control.

All reported vulnerabilities have been patched by the respective maintainers.

---

## Benchmark Performance

Claude Mythos Preview's security-specific capabilities far exceed any publicly evaluated model:

| Benchmark | Mythos Preview | Opus 4.6 | Improvement |
|---|---|---|---|
| CyberGym (Vulnerability Reproduction) | **83.1%** | 66.6% | +16.5 pp |
| SWE-bench Verified | **93.9%** | 80.8% | +13.1 pp |
| SWE-bench Pro (Agentic Coding) | **77.8%** | 53.4% | +24.4 pp |
| Terminal-Bench 2.0 | **82.0%** | 65.4% | +16.6 pp |
| GPQA Diamond (Reasoning) | **94.6%** | 91.3% | +3.3 pp |
| Humanity's Last Exam (with tools) | **64.7%** | 53.1% | +11.6 pp |
| OSWorld-Verified (Computer Use) | **79.6%** | 72.7% | +6.9 pp |

The model's **SWE-bench Pro score of 77.8%** is particularly notable — it represents a **24.4 percentage point leap** over Opus 4.6, reflecting Mythos' ability to handle complex, multi-step software engineering tasks autonomously.

---

## How Project Glasswing Works

The initiative is structured around **defensive deployment** of Claude Mythos Preview:

- **Launch partners** (AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, Microsoft, NVIDIA, Palo Alto Networks) receive direct access to Mythos Preview for scanning their foundational systems — codebases representing a large share of the world's shared cyberattack surface.
- **40+ additional organizations** that build or maintain critical software infrastructure can apply for access to scan both first-party and open-source systems.
- **$100M in model usage credits** from Anthropic covers substantial usage throughout the research preview period.
- **$4M in donations** to open-source security organizations: $2.5M to Alpha-Omega and OpenSSF (via the Linux Foundation) and $1.5M to the Apache Software Foundation.
- After the preview period, Mythos Preview will be available to participants at **$25/$125 per million input/output tokens** on the Claude API, Amazon Bedrock, Google Cloud's Vertex AI, and Microsoft Foundry.

---

## The Urgency: Why Now?

Anthropic's announcement makes a compelling case for urgency. The core argument:

> "Given the rate of AI progress, it will not be long before such capabilities proliferate, potentially beyond actors who are committed to deploying them safely."

The company notes that **Claude Mythos Preview is not yet generally available** and will not be made broadly accessible. Instead, the model's cyber capabilities are being channeled exclusively through Project Glasswing for defensive purposes. Anthropic plans to develop and refine safety safeguards with an upcoming Claude Opus model before considering broader deployment of Mythos-class capabilities.

---

## Industry Response

The breadth of industry participation is remarkable for a single AI company initiative:

- **Cisco** (Anthony Grieco, SVP & Chief Security & Trust Officer): "AI capabilities have crossed a threshold that fundamentally changes the urgency required to protect critical infrastructure from cyber threats, and there is no going back."
- **AWS** (Amy Herzog, VP and CISO): "Our teams analyze over 400 trillion network flows every day for threats, and AI is central to our ability to defend at scale."
- **Microsoft** (Igor Tsyganskiy, EVP of Cybersecurity): "When tested against CTI-REALM, our open-source security benchmark, Claude Mythos Preview showed substantial improvements compared to previous models."
- **Google** (Heather Adkins, VP of Security Engineering): "We have long believed that AI poses new challenges and opens new opportunities in cyber defense."
- **Linux Foundation** (Jim Zemlin, CEO): "By giving the maintainers of critical open source codebases access to a new generation of AI models that can proactively identify and fix vulnerabilities at scale, Project Glasswing offers a credible path to changing that equation."

---

## What This Means for the Agent Ecosystem

Project Glasswing has implications beyond cybersecurity:

1. **A new capability tier is confirmed.** Mythos Preview's benchmark scores — particularly the 24.4pp jump on SWE-bench Pro — validate that a significant capability leap exists beyond [Claude Opus 4.7]({% post_url 2026-05-20-claude-opus-4-7-launch %}). This is the model that will inform Anthropic's next general-purpose release.

2. **Agentic security is now a first-class use case.** Autonomous vulnerability discovery and patching is one of the highest-value agent applications yet demonstrated. The model found vulnerabilities without human steering, wrote exploits autonomously, and in some cases chained multiple bugs together — all capabilities that transfer directly to non-security agent tasks. This autonomous security capability underscores the concerns raised in our [agent safety trust gap analysis]({% post_url 2026-05-23-agent-safety-trust-gap-may23 %}), which found that only 14.4% of agents receive full security approval before deployment.

3. **The defensive vs. offensive AI debate gets real.** Anthropic is explicitly withholding Mythos from general release while deploying it defensively. This sets a precedent for how frontier AI companies might gate access to especially powerful capabilities.

4. **Cross-industry AI security coalitions become the norm.** The participation of virtually every major tech company signals that AI-powered cybersecurity is shifting from competitive differentiator to shared infrastructure problem.

5. **Open source maintainers get AI-powered help.** The $4M in donations and access program means that resource-constrained open-source projects — which power the vast majority of modern software — can now benefit from frontier AI vulnerability detection.

---

## The Bottom Line

Project Glasswing is the most significant AI security initiative to date — not just because of Claude Mythos Preview's capabilities, but because of the **unprecedented breadth of industry alignment** around a defensive AI deployment model. The partnership roster reads like a who's-who of global technology: every major cloud provider (AWS, Google Cloud, Microsoft Azure), every major chipmaker (Apple, Broadcom, NVIDIA), every major security vendor (Cisco, CrowdStrike, Palo Alto Networks), and the world's largest financial institution (JPMorganChase).

Anthropic has committed to reporting publicly within 90 days on vulnerabilities fixed, lessons learned, and practical recommendations for how security practices should evolve in the AI era. If Project Glasswing succeeds at its stated goals, it could fundamentally reshape how the industry approaches software security — from reactive patching to proactive, AI-driven vulnerability discovery at scale.

For agent builders, the key takeaway is clear: **the frontier of autonomous agent capability is advancing faster than most expected.** If a model can autonomously find a 27-year-old vulnerability in OpenBSD, it can autonomously handle far more than most production agent systems ask of it today.
