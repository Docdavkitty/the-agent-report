---
layout: post
title: "Only 11% of Production AI Agents Pass Security Tests — The AIRQ Report Paints a Grim Picture"
date: 2026-06-11 08:00:00 +0200
last_modified_at: 2026-06-11 08:00:00 +0200
meta_description: "The independent AIRQ report evaluated 100 production AI agents and found only 11% meet security thresholds. Coding agents and computer-use agents are the riskiest — 98% of agents combine private data access, untrusted content ingestion, and outbound action capability."
description: "The independent AIRQ report evaluated 100 production AI agents and found only 11% meet security thresholds. Coding agents and computer-use agents are the riskiest — 98% of agents combine data access, untrusted content, and outbound actions."
categories: [security]
tags: ["ai-security", "ai-agents", "airq", "security-report", "prompt-injection", "agent-safety", "cybersecurity", "governance", "enterprise", "2026"]
hero_image: /assets/images/hero/hero-ai-agent-security-airq-report.jpg
reading_time: 10
excerpt: "The AIRQ 2026 Q2 report evaluated 100 production AI agents and found only 11% pass security thresholds. Coding agents and computer-use agents rank highest in attack surface and lowest in defenses. 98% exhibit the 'lethal trifecta' — and 83% of claimed defenses lack independent verification."
author: The Agent Report
---

**TL;DR:** The independent AIRQ (AI Risk Quadrant) 2026 Q2 report assessed 100 commercial and publicly available AI agents running in production. Only **11%** landed in the "Fortified Leaders" quadrant where strong defenses match their high attack surface. **98% of agents** exhibit the "lethal trifecta": private data access combined with exposure to untrusted content and the ability to take outbound actions. Coding agents and computer-use agents are the riskiest categories — highest attack surface, largest blast radius, and thinnest defenses. Computer-use agents scored an average of **zero** on output guardrails.

---

## Introduction

The AI agent market is growing faster than security can keep up. By early 2026, over 3 million agents were operating across enterprise environments, according to Gravitee's survey of 919 organizations — and 88% of those enterprises reported at least one AI agent security incident. *(Source: [Gravitee — State of AI Agent Security 2026](https://www.gravitee.io/blog/state-of-ai-agent-security-2026-report-when-adoption-outpaces-control))*

The [AIRQ (AI Risk Quadrant) 2026 Q2 report](https://www.helpnetsecurity.com/2026/06/03/research-ai-agent-security-capability/), published June 3, is the first independent, open-methodology assessment of how production agents actually stack up on security. It evaluated 100 agents across 10 classes — from coding assistants to computer-use agents to enterprise copilots — scoring them on attack surface, blast radius, defense controls, and governance maturity.

The results are sobering.

---

## The Numbers That Matter

| Metric | Value |
|--------|-------|
| Agents passing security threshold ("Fortified Leaders") | **11%** |
| Agents exhibiting the "lethal trifecta" | **98%** |
| Agents in "Exposed Giants" quadrant (high attack surface, weak defense) | **40%** |
| Total risk budget held by Exposed Giants | **60%** |
| Agents with independently verified defenses | **17%** |
| Computer-use agents with any output guardrails | **0%** |

*(Source: [Help Net Security — Only 11% of Production Agents Pass the AI Agent Security Bar](https://www.helpnetsecurity.com/2026/06/03/research-ai-agent-security-capability/))*

---

## The Lethal Trifecta

The report identifies a pattern so common it earned its own label. The "lethal trifecta" consists of three capabilities that, when combined, create an **unacceptably high-risk profile**:

1. **Private data access** — The agent can read internal databases, documents, emails, or code repositories
2. **Exposure to untrusted content** — The agent ingests external data (web pages, user uploads, tickets, emails) that could contain malicious payloads
3. **Outbound action capability** — The agent can write files, send messages, execute code, modify infrastructure, or trigger API calls

**98% of agents** in the study exhibited all three. The remaining 2% — a single General Assistant Agent and a single Data Engineering Agent — are edge cases that happen to lack one element of the trifecta, not examples of intentional security design.

*"External data ingestion is the universal attack surface,"* the report notes. A single hostile document, email, or web page containing an indirect prompt injection can steer nearly any agent toward unauthorized actions — because nearly every agent reads untrusted content.

---

## Coding Agents and Computer-Use Agents: The Riskiest Category

The report ranks agent classes by attack surface and defense levels. The findings reveal a clear pattern: **the most capable agents are the least defended.**

| Agent Class | Capability Rank | Defense Rank | Key Finding |
|-------------|----------------|--------------|-------------|
| Coding agents | 2nd | 8th out of 10 | Bottom-up adoption bypasses procurement gates |
| Computer-use agents | High | **Last (10th)** | Average output guardrail score: **zero** |
| Work Copilot / Business Process | Moderate | 1st | Top-down adoption, platform-level governance |

*(Source: [AIRQ 2026 Q2 Report](https://www.helpnetsecurity.com/2026/06/03/research-ai-agent-security-capability/))*

### Coding Agents: Self-Serve Security Blindness

Coding agents are adopted bottom-up — developers install them individually, often without any security review. They have access to private code repositories, can read documentation from the open web, and can execute code or push commits. The report ranks them 2nd in attack surface and 8th in defense — a massive gap.

The problem is structural: the people deploying coding agents (developers) are not the people responsible for security (CISOs), and the tool is designed to maximize autonomy, not auditability.

### Computer-Use Agents: No Output Defenses at All

Computer-use agents — systems that can control a desktop or browser environment — represent the extreme case. Every agent in this class scored **zero** on output guardrails. No output validation, no exfiltration blocking, no rendering sanitization. Combined with the lethal trifecta (all computer-use agents have it at 100%), these agents are the highest-risk category in the study.

As Eugene Neelou, AIRQ Project Lead, puts it: *"Coding agents and computer agents rank as the top 2 highest attack surfaces, top 2 highest blast radius, and top 2 lowest defense controls."*

---

## Audit Without Defense: The False Comfort of Observability

One of the report's most surprising findings is that **37% of agents score well on logging and observability but poorly on harm prevention**. These agents can tell you exactly what went wrong — after the damage is done.

*"Audit is a forensic asset only,"* the report warns. Logs don't stop data exfiltration. They don't prevent an agent from deleting production data. They don't block a prompt injection from escalating to infrastructure compromise.

Adding to the concern: **38% of agents complete irreversible actions before monitoring can fire**. By the time the alert reaches a human operator, the damage is already done.

---

## Tool Execution: The Single Best Predictor of Risk

The AIRQ analysis identified **tool execution** as the dominant factor in determining an agent's blast radius — explaining **76% of the variance** across all agents. This single variable outperforms agent class, vendor reputation, and any individual defense control as a predictor of overall risk.

The practical implication: an agent that can execute tools is fundamentally different from one that cannot. Agent risk is **effectively bimodal** — tool-executing agents vs. non-tool-executing agents — and the two categories should be evaluated with entirely different threat models.

| Mitigation | Risk Reduction |
|------------|---------------|
| Sandboxed execution | ~2.6x reduction |
| Cloud/container isolation | ~6x reduction |
| Standing credentials (vs. brokered) | Unbounded risk increase |

*(Source: [AIRQ 2026 Q2 Report](https://www.helpnetsecurity.com/2026/06/03/research-ai-agent-security-capability/))*

---

## The Verification Gap: 83% of Claims Are Unverified

Perhaps the most troubling finding is the gap between claimed defenses and verified ones. **Only 17% of defense credits carry an independent verification mark.** The other 83% are based on vendor documentation, white papers, or self-reported security posture.

*"AIRQ is designed to reward vendor transparency,"* Neelou explains. *"Independent verification means evidence from public sources, as opposed to confidential vendor docs."*

Execution isolation is the **least verifiable** component — which is problematic because it's also the single most effective defense (6x risk reduction when properly implemented).

---

## What Buyers Should Do

The AIRQ report offers six actionable recommendations for organizations deploying or procuring AI agents:

1. **Treat the agent as the unit of risk** — above the underlying model. The model matters, but the agent's tools, data access, and execution environment determine the actual blast radius.

2. **Compare agents within the same class and quadrant** — a coding agent and a customer support agent operate under fundamentally different threat models.

3. **Separate compliance certifications from technical defense scoring** — SOC 2 compliance does not prevent prompt injection.

4. **Score every platform twice** — as shipped by the vendor and as configured by the buyer. The gap between these two scores can be wider than the gap between entire agent classes.

5. **Require documented and tested sandboxing** before deployment — it's the single most effective verified defense (2.6x risk reduction).

6. **Perform quarterly re-audits** — the CVE volume in the AI agent market is climbing quarter over quarter. Categories with low vulnerability counts are likely in a pre-discovery phase, not genuinely more secure.

*(Source: [Help Net Security — Recommendations](https://www.helpnetsecurity.com/2026/06/03/research-ai-agent-security-capability/))*

---

## The Shared Responsibility Problem

The report highlights a structural issue that echoes the early days of cloud security. A final deployed agent often has a different security posture than the vendor's default platform configuration, because:

- **Bottom-up adoption** (developers installing coding agents) bypasses procurement gates entirely
- **Vendor-shipped defaults** rarely match enterprise security requirements
- **Customer configuration** can introduce vulnerabilities the vendor never tested for

*"Similar to the shared responsibility model in cloud security, a final agentic product deployed by the buyer often has a different security posture than a default platform configuration,"* Neelou notes.

---

## FAQ

**Q: What is the AIRQ report?**
A: The AI Risk Quadrant report is an independent, open-methodology assessment of production AI agent security. The 2026 Q2 edition evaluated 100 agents across 10 classes. The full methodology is designed to be reproducible by any organization.

**Q: Which agents are safest?**
A: Work Copilot and Business Process agents rank highest on defenses, largely because they're adopted top-down through enterprise procurement and inherit platform-level governance. But even they don't escape the lethal trifecta.

**Q: What is the "lethal trifecta"?**
A: The combination of private data access, exposure to untrusted content, and outbound action capability. 98% of agents in the study exhibit all three.

**Q: Should I stop using coding agents?**
A: No — but you should ensure they run in sandboxed environments with network egress controls and ephemeral credentials. The risk is not the agent itself; it's the combination of standing credentials and unfettered tool execution.

**Q: How often should agents be re-audited?**
A: The report recommends quarterly re-audits. The AI agent vulnerability landscape is evolving rapidly, and categories with low CVE counts are likely in a pre-discovery phase.

---

## Further Reading

- [Help Net Security — Only 11% of Production Agents Pass the AI Agent Security Bar](https://www.helpnetsecurity.com/2026/06/03/research-ai-agent-security-capability/)
- [Gravitee — State of AI Agent Security 2026 Report](https://www.gravitee.io/blog/state-of-ai-agent-security-2026-report-when-adoption-outpaces-control)
- [Let's Data Science — Assessment Finds 11% of Production AI Agents Secure](https://letsdatascience.com/news/assessment-finds-11-of-production-ai-agents-secure-4a5057a6)
- [The Agent Report — AI Agent Finds 21 Zero-Days in FFmpeg for $1,000](https://the-agent-report.com/2026/06/ai-agent-21-zero-days-ffmpeg-1000-dollars/)
- [The Agent Report — Anthropic Mythos: Autonomous Zero-Day Chain](https://the-agent-report.com/2026/05/anthropic-project-glasswing-claude-mythos-preview-cybersecurity-may27/)
