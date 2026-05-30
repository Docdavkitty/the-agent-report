---
layout: post
title: "Claude Platform on AWS Goes GA — Anthropic's Full Agent Stack Now Available to Every AWS Customer"
date: 2026-05-12 10:30:00 +0200
last_modified_at: 2026-05-12 10:30:00 +0200
meta_description: "Anthropic launches Claude Platform on AWS GA: Managed Agents, code execution, skills, and advisor with IAM auth, CloudTrail logging, and commitment retirement."
description: "Anthropic launches Claude Platform on AWS GA: Managed Agents, code execution, skills, and advisor with IAM auth, CloudTrail logging, and commitment"
categories: [tools-frameworks]
tags: [anthropic, claude, aws, cloud, managed-agents, enterprise, infrastructure]
reading_time: 6
excerpt: "Anthropic launches the Claude Platform on AWS in general availability — bringing Claude Managed Agents, code execution, skills, and the advisor strategy to AWS with IAM authentication, CloudTrail audit logging, and commitment retirement."
hero_image: /assets/images/hero/hero-claude-platform-aws-general-availability.jpg
author: The Agent Report
---

# Claude Platform on AWS Goes GA — Anthropic's Full Agent Stack Now Available to Every AWS Customer

**Anthropic has launched the Claude Platform on AWS in general availability, bringing the company's complete agent stack — including Claude Managed Agents, code execution, skills, and the advisor strategy — directly into the AWS ecosystem with native IAM authentication, CloudTrail audit logging, and commitment-based billing.**

---

## The Big Picture

Starting today, any AWS customer can deploy Claude agents at enterprise scale without leaving the AWS console. The announcement, published on [Claude's blog](https://claude.com/blog/claude-platform-on-aws), marks Anthropic's most aggressive push yet into enterprise infrastructure — and it signals a clear strategy: **meet enterprises where they already are — a strategy also reflected in Anthropic's [Claude for Small Business]({% post_url 2026-05-14-claude-for-small-business-agentic-workflows %}) launch.**

The Claude Platform on AWS gives customers access to the "full set of Claude Platform features with AWS authentication, billing, and commitment retirement." In plain English: enterprises can now use their existing AWS budgets to pay for Claude agents, manage access through IAM policies they already control, and audit every agent action through CloudTrail.

## What's Included

The platform ships with everything Anthropic has built over the past six months:

### Claude Managed Agents (Beta)
The headline feature. Enterprises can deploy AI agents that operate autonomously over long time horizons — planning, executing, and iterating — building on Anthropic's [Managed Agents platform]({% post_url 2026-05-25-anthropic-managed-agents-platform-dreaming-orchestration-may25 %}) on complex tasks. Managed Agents support:
- **Code execution** — agents can write, test, and deploy code
- **Skills** — reusable agent capabilities (similar to Hermes Agent's skill system)
- **Advisor strategy** — multi-agent orchestration where specialized agents collaborate on complex problems

### Full Feature Parity
Anthropic is making a point: every feature that ships on the native Claude API ships on AWS the same day. No lag. No "AWS edition" with fewer capabilities.

> "The Claude Platform on AWS brings the full set of Claude API features to AWS customers for the first time, with all new features and betas shipping the same day they go live on the native Claude API."
> — Anthropic

### Enterprise-Grade Controls
- **Authentication**: AWS IAM — customers use their existing credentials and policies
- **Audit logging**: CloudTrail integration for complete visibility
- **Billing**: Single AWS invoice with commitment retirement against existing agreements

## Claude on AWS vs. Claude on Bedrock — What's the Difference?

This launch creates two parallel paths for AWS customers:

| Feature | Claude Platform on AWS | Claude on Amazon Bedrock |
|---------|----------------------|-------------------------|
| **Operator** | Anthropic | AWS |
| **Data processing** | Outside AWS boundary | Inside AWS boundary |
| **Feature parity** | Full, day-one | Core model access |
| **Best for** | Full platform features, cutting-edge capabilities | Strict data residency, regulated industries |

The distinction matters. The Claude Platform on AWS is **operated by Anthropic** — data flows through Anthropic's infrastructure — while Bedrock keeps AWS as the data processor. This means:
- **Platform on AWS**: Get the latest features instantly. Good for teams that want the full Claude experience.
- **Bedrock**: Data stays entirely within AWS's boundary. Good for regulated industries with strict data residency requirements.

Anthropic is clear: "This is a first of its kind offering for Anthropic, giving you all native Claude API features from day one."

## Early Customer Reactions

Enterprise customers are already on board. **OpenRouter**'s AI Platform Engineer Tomas Oliva noted: "Using Claude Platform on AWS gives OpenRouter and our users direct access to the latest and greatest features of the native Claude API."

Jonathan Echavarria, Principal Research Scientist at an unnamed cybersecurity firm, added: "Claude Platform on AWS helped simplify how we access Claude, improved the experience for key users like our Claude Code engineers, and gave us a practical path to integrate further frontier AI capabilities into our cybersecurity and engineering work."

## Agent View in Claude Code — Also New

In a separate but related [announcement](https://claude.com/blog/agent-view-in-claude-code), Anthropic released **Agent View** in Claude Code — a new interface for managing multiple concurrent agent sessions from the terminal.

Key features:
- **Session dashboard**: See all running Claude Code agents at a glance
- **Background agents**: Launch agents with `claude --bg [task]` and check in only when they need input
- **Multi-agent workflow**: Dispatch several ideas simultaneously, each paired with a skill, and return to a list of PRs ready for review
- **Research Preview**: Available now on Pro, Max, Team, Enterprise, and API plans

This is part of a broader pattern: Anthropic is shipping agent infrastructure at every layer — from the CLI (Agent View) to the cloud platform (AWS GA).

## What This Means for the Agent Ecosystem

The Claude Platform on AWS is significant for several reasons:

### 1. Enterprise Validation
Six months ago, deploying AI agents at scale meant stitching together open-source tools, managing your own inference infrastructure, and praying nothing broke. Today, it's an AWS Marketplace checkbox. That's an extraordinary acceleration.

### 2. MCP and the Connector Economy
Anthropic's launch comes alongside its aggressive expansion of the Model Context Protocol (MCP) and the "connector" ecosystem. The [DataDome analysis](https://datadome.co/agent-trust-management/why-anthropics-connector-expansion-makes-mcp-security-a-business-imperative/) notes that "the AI agent economy is going mainstream" — and with it, security considerations around how agents connect to enterprise data.

### 3. Pressure on Competitors
With Claude available at AWS scale, OpenAI and Google face pressure to deliver equivalent enterprise agent experiences. AWS's massive enterprise salesforce is now effectively selling Claude agents — and that changes the competitive landscape overnight.

### 4. The Hermes Agent Connection
For the open-source agent community, this launch validates the thesis that agents need first-class infrastructure support. Projects like [Hermes Agent](https://github.com/NousResearch/hermes-agent), which pioneered the skill-based agent architecture, and OpenClaw are proving that the open-source ecosystem can innovate faster — but Anthropic is showing that enterprise adoption requires cloud-native integration.

## Getting Started

The Claude Platform on AWS is available today in most AWS commercial regions. To get started:
1. Visit the [Claude Platform on AWS](https://claude.com/blog/claude-platform-on-aws)
2. Configure IAM policies for your team
3. Deploy Managed Agents with code execution and skills
4. Monitor everything through CloudTrail

For existing Bedrock private offer holders, Anthropic recommends contacting your account executive before switching to ensure discounts are applied correctly.

---

*Read the full announcement [here](https://claude.com/blog/claude-platform-on-aws).*

*Also announced today: [Agent View in Claude Code](https://claude.com/blog/agent-view-in-claude-code).*

*Hacker News discussion: [121 points](https://news.ycombinator.com/item?id=48112839)*
