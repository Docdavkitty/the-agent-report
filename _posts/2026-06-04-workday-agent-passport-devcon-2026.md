---
layout: post
title: "Workday Launches Agent Passport — Independent Safety Verification for Enterprise AI Agents"
date: 2026-06-04 08:00:00 +0200
last_modified_at: 2026-06-04 08:00:00 +0200
categories: [industry]
tags: [workday, enterprise-ai, ai-agents, ai-safety, agent-passport, nist-ai-rmf]
reading_time: 4
hero_image: /assets/images/hero/hero-workday-agent-passport.jpg
author: The Agent Report
excerpt: "Workday unveiled Agent Passport at DevCon 2026 — an independent third-party verification system that tests AI agents against OWASP, NIST AI RMF, and MITRE ATLAS standards before deployment, with continuous runtime monitoring."
meta_description: "Workday launches Agent Passport at DevCon 2026 — an independent verification system that tests AI agents against OWASP LLM Top 10, NIST AI RMF, and MITRE ATLAS standards before deployment, with continuous runtime monitoring from Cisco."
description: "Enterprise AI agents are proliferating rapidly, but a fundamental question remains unanswered: how do you know an agent is safe to let loose on your HR..."
---

## The Trust Gap in Enterprise AI Agents

Enterprise AI agents are proliferating rapidly, but a fundamental question remains unanswered: **how do you know an agent is safe to let loose on your HR and finance data?**

One misconfigured agent sitting on top of payroll, benefits, or org chart data is all it takes for a missed paycheck, an exposed employee record, or a call from a regulator. Traditional API security doesn't apply — autonomous agents make independent decisions, execute multi-step workflows, and interact with systems in unpredictable ways.

At DevCon 2026 on June 2, Workday unveiled what may be the most direct answer yet: **Agent Passport**, an independent, third-party verification system for every AI agent running in the enterprise.

## Agent Passport: How It Works

Agent Passport tests and verifies every AI agent — whether built by Workday, the customer, or a third party — before it goes into production, and continuously monitors it after deployment.

Each agent receives a **digital passport** containing:

- **Which security and compliance tests** the agent passed
- **Who performed** the verification (an independent attestation partner)
- **Which public standards** were used as the testing framework

The verification ties directly to established industry standards: **OWASP LLM Top 10**, **NIST AI Risk Management Framework**, and **MITRE ATLAS**. Every attestation is signed and auditable, so security teams have a clear, comparable record across agents from any vendor.

> "Agents are going to be everywhere in the enterprise, and that only works if security teams have a clear, signed record of what each one has been tested for."
> — **Workday**, Agent Passport announcement

## Cisco as Launch Partner

Cisco is the first attestation partner for Agent Passport. Cisco AI Defense independently tests AI agents against leading security standards before deployment, and provides continuous runtime protection against:

- Prompt injection attacks
- Data leakage
- Jailbreak attempts
- Unsafe autonomous actions

This partnership is strategic — Cisco's existing enterprise security relationships give Agent Passport immediate credibility in the Fortune 500 security teams that Workday counts as its core customer base.

## More Than Just Verification

Workday also launched two companion tools at DevCon:

**Developer Agent** — lets developers build AI apps and agents using natural language from the agentic tools they already use: Claude Code, Cline, Codex, Cursor, and Google Antigravity. A developer can type "Build an agent that alerts finance when a department is trending to go over budget this quarter," and Developer Agent handles the rest — selecting the right tools, connecting data sources, and pulling documentation.

**Agent-Ready Tools** — a new class of enterprise connectors built specifically for autonomous agents, using open standards like Model Context Protocol (MCP). Hundreds of these tools span HR, finance, and IT domains, each inheriting Workday's security model, delegation controls, and audit trail automatically.

> "Platforms win when they make the hard thing disappear for the developer," said **Gabe Monroy**, CTO of Workday. "Anyone can give an agent speed — the hard part is letting it act on the org chart or ledger and trusting every step."

## What This Means for the Industry

Agent Passport addresses what has been called the **"permissioning wall"** — the finding that technical capability in AI agents has far outpaced enterprise trust infrastructure. Companies can build agents that do remarkable things, but deploying them on sensitive HR and finance data requires a level of confidence that most IT security teams don't yet have.

Workday's approach is notable because it doesn't try to solve the verification problem alone. By bringing in third-party attestation partners, tying to public standards, and making the results auditable, Agent Passport creates a **verification ecosystem** rather than a proprietary lock-in.

For the broader enterprise AI agent market, this sets a precedent. If Workday's approach gains traction, expect ERP and HCM competitors like SAP, Oracle, and UKG to follow with their own verification frameworks — and expect security vendors like CrowdStrike, Palo Alto Networks, and Zscaler to compete with Cisco for attestation partnerships.

## Availability

| Feature | Early Access | General Availability |
|---------|-------------|---------------------|
| Developer Agent | Now (Workday Extend Professional) | H2 2026 |
| Agent-Ready Tools | Now (Workday Extend Professional) | H2 2026 |
| Agent Passport | H2 2026 | Before end of 2026 |
