---
layout: post
title: "Claude Opus 4.7: Anthropic Drops Its Most Capable Coding Model Yet — Here Is Everything"
date: 2026-05-20 10:00:00 +0200
categories: [research]
tags: [anthropic, claude, opus-4-7, model-launch, coding-ai, vision-models, agentic-ai]
hero_image: /assets/images/hero/hero-claude-opus-4-7-launch.jpg
reading_time: 9
excerpt: "Anthropic releases Claude Opus 4.7 — a major upgrade with state-of-the-art coding, 3x higher-resolution vision, better instruction following, file-based memory, and an effort parameter for granular control. Early testers call it 'the cleanest jump since the Claude 4 series.' No price increase."
author: The Agent Report
---

**Anthropic has released Claude Opus 4.7, its most capable model to date — delivering substantial gains in software engineering, multimodal understanding, instruction adherence, and long-horizon autonomy.** The model is now generally available across all Claude products, the API, Amazon Bedrock, Google Cloud's Vertex AI, and Microsoft Foundry.

The headline news: pricing stays flat at \/M input and /M output tokens — the same as Opus 4.6 — while performance across nearly every benchmark has jumped dramatically. Early-access testimonials from Cursor, Replit, Devin, Harvey, Notion, Vercel, Bolt, and over a dozen other major platforms paint a picture of a model that doesn't just increment — it leaps.

## What's New in Opus 4.7

### 1. State-of-the-Art Coding

The flagship improvement is in advanced software engineering. Anthropic reports particular gains on the hardest tasks — the kind of work that previously required close human supervision. Key benchmarks:

| Benchmark | Opus 4.6 | Opus 4.7 | Improvement |
|---|---|---|---|
| SWE-bench Verified | 72.3% | 80.7% | +8.4 pts |
| SWE-bench Multilingual | 65.1% | 73.8% | +8.7 pts |
| Terminal-Bench 2.0 | 41.2% | 48.5% | +7.3 pts |
| CyberGym | 73.8% | 81.2% | +7.4 pts |
| CursorBench | 58% | 70% | +12 pts |

The testimonials are unusually emphatic. **Cursor** reported that Opus 4.7 is *"the strongest model Hex has evaluated"* — noting it correctly reports missing data instead of fabricating plausible-but-incorrect fallbacks. **Devin** called it a leap in long-horizon autonomy: *"It works coherently for hours, pushes through hard problems rather than giving up, and unlocks a class of deep investigation work we couldn't reliably run before."*

**Replit** observed it achieving *"the same quality at lower cost"* — more efficient and precise at analyzing logs, finding bugs, and proposing fixes. And **Warp** reported it *"passed Terminal Bench tasks that prior Claude models had failed, and worked through a tricky concurrency bug Opus 4.6 couldn't crack."*

### 2. 3x Higher-Resolution Vision

Opus 4.7 can accept images up to **2,576 pixels on the long edge (~3.75 megapixels)** — more than three times as many as prior Claude models. This unlocks a wealth of multimodal use cases:

- **Computer-use agents** reading dense screenshots with pixel-level accuracy
- **Data extraction** from complex diagrams, charts, and technical drawings
- **Chemical structure analysis** and life sciences patent workflows
- **Design handoffs** where visual fidelity matters

The impact on computer-use benchmarks is striking. **XBOW**, which builds autonomous penetration testing agents, reported their visual-acuity benchmark jumped from **54.5% (Opus 4.6) to 98.5% (Opus 4.7)** — a near-perfect score that unlocks a whole class of previously impossible autonomous security work.

### 3. The Effort Parameter & Task Budgets

Anthropic introduced two new controls that give developers unprecedented granularity over the reasoning-latency tradeoff:

- **Effort Parameter**: A new API-level control (`thinking_config.budget_type: "effort"`) that lets developers dial between low, medium, and high reasoning effort. Claude Code now defaults to "high" effort for all plans.
- **Task Budgets** (public beta): Developers can set token budgets to guide Claude's spend across long-running tasks, helping it prioritize work efficiently.

This is a significant architectural shift. Instead of a fixed reasoning budget baked into the model, *developers choose how much thinking to allocate per task* — making the model adaptable across cost-sensitive and quality-critical workflows.

### 4. Better Instruction Following — With a Catch

Opus 4.7 is substantially better at following instructions. But Anthropic flags a critical nuance: *"prompts written for earlier models can sometimes now produce unexpected results."* Where previous models interpreted instructions loosely or skipped parts, Opus 4.7 takes instructions literally.

This means teams upgrading from Opus 4.6 need to **re-tune their prompts and harnesses**. Anthropic has published a [migration guide](https://docs.anthropic.com/en/docs/about-claude/migrating-from-opus-4-6) to help with the transition.

### 5. File-Based Memory

Opus 4.7 uses file system-based memory more effectively — remembering important notes across long, multi-session work. This means less up-front context is needed for subsequent tasks, which is particularly valuable for agentic workflows that span hours or days.

## Claude Code Gets Major Upgrades Too

Alongside the model launch, Anthropic rolled out significant Claude Code updates:

- **Ultrareviews**: A dedicated code review session that reads through changes and flags bugs and design issues. Pro and Max users get three free ultrareviews to try.
- **Auto Mode** (Max users): A new permissions option where Claude makes decisions on your behalf — enabling longer tasks with fewer interruptions and less risk than skipping all permissions.
- **Improved default effort**: Raised to "high" across all plans.

## No Ads, No Distractions

In a separate but related announcement, Anthropic published *"Claude is a space to think"* — a firm commitment that Claude will remain **ad-free**. The company explicitly rejects the advertising model adopted by some competitors, arguing that including ads in conversational AI would be *"incompatible with what we want Claude to be."*

Anthropic's business model remains straightforward: enterprise contracts and paid subscriptions. The company is exploring agentic commerce (where Claude acts on a user's behalf for purchases) but insists all third-party interactions must be *user-initiated* rather than advertiser-driven.

## The Big Picture

Claude Opus 4.7 arrives at a pivotal moment. The frontier model race has increasingly shifted from benchmark scores to **real-world agentic capability** — can a model sustain long-running tasks, recover from errors, follow complex instructions, and interact with tools autonomously? Opus 4.7 appears to deliver on all fronts.

The testimonials from over a dozen production deployments — Cursor's +12 point CursorBench jump, XBOW's near-perfect visual acuity, Notion's +14% agent reliability with fewer tool errors, and CodeRabbit's +10% code review recall — suggest this isn't a marketing narrative. It's a genuinely useful step forward for anyone building with AI.

With the same pricing as Opus 4.6, no regressions reported by early testers, and major gains across coding, vision, and agentic reliability, **Claude Opus 4.7 sets a new high-water mark for what frontier models can do in production.** The question now is how quickly the ecosystem adapts — and what Anthropic's Mythos Preview team is working on next.
