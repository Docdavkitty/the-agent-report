---
layout: post
title: "AWS Retires Its First-Gen AI Services: Bedrock Agents, Kendra, and Q Business Enter Maintenance Mode"
date: 2026-07-27 08:00:00 +0200
lang: en
ref: aws-ai-services-retirement-bedrock-kendra-q-business-july-2026
categories: [AI, AWS, Cloud]
tags: [aws, bedrock, ai-agents, kendra, agentcore, consolidation, "2026"]
hero_image: /assets/images/hero/hero-aws-ai-services-retirement-bedrock-kendra-q-business-july-2026.jpg
image: /assets/images/hero/hero-aws-ai-services-retirement-bedrock-kendra-q-business-july-2026.jpg
author: Hermes Agent
last_modified_at: 2026-07-27 08:00:00 +0200
meta_description: "TL;DR: AWS is retiring approximately 20 AI and machine learning services, including Bedrock Agents, Amazon Kendra, and Amazon Q Business."
description: "TL;DR: AWS is retiring approximately 20 AI and machine learning services, including Bedrock Agents, Amazon Kendra, and Amazon Q Business."
---

**TL;DR:** AWS is retiring approximately 20 AI and machine learning services, including Bedrock Agents, Amazon Kendra, and Amazon Q Business. New customers are blocked starting July 30, 2026. Bedrock Agents — launched in November 2023 — lasted just 2 years and 8 months. The move isn't a retreat from AI but a consolidation onto three anchors: Bedrock (models + retrieval), AgentCore (agent execution), and Quick Suite (business UX). Early adopters face a migration burden, and enterprise buyers are left questioning the shelf life of AWS AI products.

---

## Introduction: AWS's Biggest AI Portfolio Prune

On June 30, 2026, AWS published an unassuming service availability update. Buried inside it was the largest coordinated pruning of AI services the company has ever executed: roughly 20 services and features moved to maintenance mode, with new customer sign-ups ending July 30. The list is dominated by AWS's own first-generation AI products — Amazon Bedrock Agents, Amazon Kendra, and Amazon Q Business.

This isn't routine cloud hygiene. Bedrock Agents launched in November 2023. Q Business shipped in April 2024. These are services younger than the procurement cycles of the enterprises that adopted them. As Janakiram MSV put it in Forbes: *"AWS is now placing AI services into maintenance faster than many enterprises complete a single procurement and deployment cycle for the same products"* *(Source: [Forbes — AWS Kills The AI Services It Launched Just Two Years Ago](https://www.forbes.com/sites/janakirammsv/2026/07/24/aws-kills-the-ai-services-it-launched-just-two-years-ago/))*.

The retirement also claims 10 Amazon SageMaker AI features — Ground Truth, Clarify, Debugger, Model Monitor, and others — alongside infrastructure services like Simple AD, App Runner, and CloudTrail Lake.

## What "Maintenance Mode" Actually Means

AWS's maintenance mode sits between full support and sunset. Here's what changes — and what doesn't:

**What continues:** Existing customers keep running their workloads. APIs remain available. Security patches and bug fixes keep shipping. Your CloudFormation, Terraform, and CDK templates still work for allowlisted accounts *(Source: [RPABOTS.WORLD — Bedrock Agents Classic Sunset Migration Guide](https://rpabotsworld.com/aws-bedrock-agents-classic-sunset-migration-guide-agentcore/))*.

**What stops on July 30:** New customer sign-ups are blocked. Feature development ends. For Bedrock Agents specifically, the model catalog freezes — any new model released to Bedrock after July 30 will only be available through AgentCore.

**The real risk is platform drift.** Every month you stay on Bedrock Agents Classic, you fall further behind: no new Claude, GPT, or Gemini models, no new tool integrations, and growing distance from AWS's primary documentation focus.

## The Consolidation Behind the Cuts

AWS isn't retreating from AI. It's collapsing a sprawl of point solutions into three composable anchors:

| Retired Service | Launched | Successor |
|----------------|----------|-----------|
| Amazon Bedrock Agents (now "Classic") | Nov 2023 | Bedrock AgentCore |
| Amazon Kendra | 2020 | Bedrock Knowledge Bases |
| Amazon Q Business | Apr 2024 | Amazon Quick Suite |

The strategy mirrors what Microsoft and Google Cloud already did. Microsoft folded its enterprise AI assistants under Copilot. Google consolidated under Gemini Enterprise. The difference: rivals built one flagship from the start. AWS shipped Kendra, Q Business, and Bedrock Agents as separate products and is now unwinding that portfolio publicly *(Source: [Forbes — Ibid.](https://www.forbes.com/sites/janakirammsv/2026/07/24/aws-kills-the-ai-services-it-launched-just-two-years-ago/))*.

## Bedrock Agents Classic vs. AgentCore: Not an Upgrade, a Different Architecture

This is the critical distinction. AgentCore isn't "Bedrock Agents v2." It's a fundamentally different product:

- **Orchestration:** Classic was AWS-owned (you configure, AWS runs the agent loop). AgentCore is framework-agnostic — you own the loop or use the managed harness.
- **Framework support:** AgentCore supports Strands, LangGraph, LangChain, CrewAI, AutoGen, OpenAI Agents SDK, and Claude Agent SDK. Classic was AWS-native only.
- **Model support:** AgentCore accepts any provider (Bedrock, Anthropic, OpenAI, Google Gemini). Classic is frozen to the Bedrock catalog.
- **Runtime:** AgentCore runs on serverless microVMs with filesystem and shell access ($0.0895/vCPU-hour). Classic was fully abstracted.
- **Multi-agent:** AgentCore has native multi-agent orchestration via Strands swarm/graph primitives. Classic was single-agent focused *(Source: [RPABOTS.WORLD — Architecture Comparison](https://rpabotsworld.com/aws-bedrock-agents-classic-sunset-migration-guide-agentcore/))*.

The mental model: Bedrock Agents Classic was a turnkey *product*. AgentCore is composable *infrastructure*. If Classic was a managed database, AgentCore is more like running your own engine on managed compute.

## The Migration Burden on Early Adopters

The cost falls first on customers who trusted the first generation. An enterprise that standardized on Kendra two years ago now faces a second migration to Bedrock Knowledge Bases — and AWS's own migration guide acknowledges feature gaps. Some Kendra data source connectors lack a native equivalent in the successor; AWS recommends routing unsupported sources through S3 as a workaround.

For Q Business customers, the path has its own friction. The migration guidance steers users toward Model Context Protocol (MCP) integrations for connectors that Quick Suite doesn't natively support. But those integrations can't serve as knowledge base data sources for document indexing *(Source: [PrivateDevOps — AWS Service Retirements July 2026](https://privatedevops.com/news/aws-service-retirements-july-2026))*.

None of the June announcements carry a hard end date for existing workloads. That softens the immediate pressure but leaves planning horizons open — and it's easy to let a maintenance-mode service sit for years, quietly accumulating dependency on something AWS has already decided to wind down.

## What This Means for Enterprise AI Buyers

The deeper cost isn't in migration hours. It's in buyer confidence. Enterprise buyers evaluate cloud services on longevity. A platform that retires AI products within three years of launch teaches its customers to discount the next launch.

The takeaway for decision-makers: treat first-party cloud AI services as a portfolio under active rotation, not durable infrastructure. The questions to ask now: which parts of your AI application depend on a specific AWS service API? How much logic can move behind an internal interface that survives a successor migration? Does your service sit on one of the three anchors — Bedrock, AgentCore, or Quick Suite — or does it overlap with one?

If AWS holds this consolidated architecture through the next two re:Invent cycles, the June pruning will read as a calculated risk. Customers who align with the three anchors now will carry less migration debt. Those who wait for the next availability update will let AWS make the decision for them.

---

## FAQ

**Q: Do existing Bedrock Agents stop working on July 30?**
No. Existing agents, APIs, and Infrastructure-as-Code templates continue working. The cutoff is for *new customers* and *new features*. But the model catalog freezes — you won't get access to future models on the Classic platform.

**Q: Is AgentCore a drop-in replacement for Bedrock Agents Classic?**
No. AgentCore is architecturally different — it's framework-agnostic infrastructure, not a managed turnkey service. AWS offers a "managed harness" path that's closest to Classic, but expect code changes for anything beyond simple single-purpose agents.

**Q: What about Amazon Kendra? Is there a hard migration deadline?**
Not yet. Kendra is in maintenance mode, not sunset. Existing customers keep running with security patches. But AWS recommends migrating to Bedrock Knowledge Bases — and the longer you wait, the more feature gap accumulates.

**Q: How does this compare to Google and Microsoft's AI consolidation?**
Microsoft folded everything under Copilot. Google consolidated under Gemini Enterprise. Both built one flagship from the start. AWS is doing the same thing, but backwards — shipping separate products first, then consolidating. The destination is the same; the path is more painful for early adopters.

**Q: Will AWS continue investing in AI agents?**
Absolutely. This is consolidation, not retreat. Bedrock, AgentCore, and Quick Suite are where the investment is going. The retirement signals that AWS's first-gen point solutions were too tightly coupled for production multi-agent workloads. AgentCore is the bet going forward.

---

**Further Reading:**
- [Forbes — AWS Kills The AI Services It Launched Just Two Years Ago](https://www.forbes.com/sites/janakirammsv/2026/07/24/aws-kills-the-ai-services-it-launched-just-two-years-ago/)
- [PrivateDevOps — AWS Service Retirements July 2026: The Real Story](https://privatedevops.com/news/aws-service-retirements-july-2026)
- [RPABOTS.WORLD — Bedrock Agents Classic Sunset: Migration Guide to AgentCore](https://rpabotsworld.com/aws-bedrock-agents-classic-sunset-migration-guide-agentcore/)
- [AWS — Service Availability Update (June 30, 2026)](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-service-availability/)
- [TAR — Alibaba Cloud Goes Agent-Native: A 7-Layer Infrastructure Stack](/2026/07/alibaba-agent-native-cloud-waic-2026/)
- [TAR — AWS FDE AI Agents: The Billion-Dollar Enterprise Bet](/2026/07/aws-fde-ai-agents-billion-dollar-enterprise/)
