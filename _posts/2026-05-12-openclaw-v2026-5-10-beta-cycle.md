---
title: "Openclaw v2026.5.10 Beta Cycle: Five Releases in Two Days, 371K Stars, and Agent-to-Agent Depth"
date: 2026-05-12 10:00:00 +0000
last_modified_at: 2026-05-12 10:00:00 +0000
categories: [openclaw]
tags: [openclaw, claw-controller, agent-autonomy, agent-to-agent, pnpm11]
reading_time: 6
hero_image: /assets/images/hero/hero-openclaw-v2026-5-10-beta-cycle.jpg
excerpt: "Openclaw shipped five beta releases across May 10-11 — v2026.5.10-beta.1 through beta.5 — in an aggressive weekend release train that touches every layer of the stack. Agent-to-agent ping-pong turns are now configurable up to 20, Slack gets unfurl controls and reply broadcast, Discord voice gains realtime diagnostics, and the project crosses 371,000 GitHub stars."
---

**Openclaw** — the open-source personal AI assistant sitting at **371,074 GitHub stars** with **76,742 forks** — unleashed a torrent of five beta releases over May 10-11, collectively branded **v2026.5.10-beta**. The weekend release cycle shipped changes across almost every subsystem: agent-to-agent protocols, Slack integration, Discord voice, Fal image generation, Fly Machines, the Control UI, and the build system's migration to pnpm 11.

The cadence is remarkable even by Openclaw's standards: **beta.1** on May 10 at 13:16 UTC, **beta.2** at 17:37, **beta.3** on May 11 at 03:05, **beta.4** at 15:40, and **beta.5** at 16:13. That's five releases in roughly 27 hours, each carrying production-quality changelogs spanning dozens of pull requests.

## Agent-to-Agent: Deeper Conversation Chains

The most architecturally significant change in the beta cycle is the relaxation of agent-to-agent limits. Previously capped at 5 ping-pong turns, `session.agentToAgent.maxPingPongTurns` can now be configured up to **20** (default remains at 5). This matters for complex multi-agent workflows where agents need sustained back-and-forth — collaborative debugging sessions, iterative code reviews, or negotiation tasks between specialized sub-agents.

Two companion features reinforce this direction:

- **`tools.message.crossContext` per-agent overrides** — sandboxed and public agents can now restrict message sends to the current conversation without changing the global bot policy. This is crucial for multi-tenant gateways where different agents need different isolation guarantees.
- **`tools.message.actions.allow` per-agent overrides** — agents can expose and enforce send-only message tools granularly, giving operators fine-grained control over what each agent can communicate.

> The message routing changes alone touch on safety patterns that enterprise deployments have been requesting since Openclaw crossed 300K stars.

## Slack Gets Unfurl Control and Thread Broadcast

Three Slack improvements landed in beta.3 that together make Openclaw a much more polished Slack citizen:

| Feature | Description | Issue |
|---------|-------------|-------|
| **`unfurlLinks` / `unfurlMedia`** | Per-account config to suppress link and media previews in bot replies without workspace-wide settings | #48435 |
| **`replyBroadcast`** | Agents can opt into Slack's parent-channel `reply_broadcast` behavior for thread replies | #64365 |
| **Mention metadata** | Bot now distinguishes direct mentions from implicit thread wakes that mention someone else | #79025 |

The canonicalization of outbound DM routes in beta.3 also fixes a subtle but painful bug: `message.send` calls to `D...` targets no longer split the same Slack DM thread into separate channel sessions. (#80091)

## Discord Voice Diagnostics and Telegram QA Automation

The beta cycle brought significant quality-of-life improvements for voice agents:

- **Discord/voice realtime diagnostics** — speaker turn timing, playback resets, barge-in detection, and audio cutoff analysis. These diagnostics make it feasible to debug voice interactions in production, a notoriously difficult problem.
- **`talk.realtime.instructions`** — operators can now append realtime voice style guidance while preserving Openclaw's built-in agent-consult defaults. (#79081)
- **Opus codec handling** — test and source installs default to the pure-JS `opusscript` decoder, avoiding slow native addon compiles outside dedicated voice-performance lanes. An opt-in native install script is available for production voice deployments.

On the QA side, a new **Telegram live PR evidence automation** system leases Convex credentials, captures Crabbox transcripts, generates motion GIF previews, and posts inline PR comments — a taste of Openclaw dogfooding its own platform for development workflows.

## Infrastructure: Fly Machines, pnpm 11, and Local Models

Three infrastructure changes deserve attention:

1. **Fly Machines container detection** — Openclaw now detects Fly Machines from runtime environment variables and adjusts gateway bind and Bonjour defaults accordingly. (#80209) This makes deploying Openclaw on Fly.io genuinely zero-config.

2. **pnpm 11 migration** — the workspace package manager was upgraded to pnpm 11, with all Docker, install, update, and release workflows aligned to the new config surface. (#79414, #80588) Thanks to @altaywtf for both.

3. **Local model server support** — a new `localService` startup option at the provider level allows on-demand local model servers to spin up before OpenAI-compatible requests, including one-shot model probes. This is a meaningful step toward fully offline agent operation.

## Fal Image Generation Gets GPT Image 2 and Nano Banana 2

Providers/fal received a substantial update: GPT Image 2 and Nano Banana 2 reference-image edit requests are now routed to `/edit` with proper `image_urls` arrays. Nano Banana 2 edit geometry is enforced using `aspect_ratio` and `resolution` params, and input-image caps are lifted to 10 for GPT Image 2 and 14 for Nano Banana 2. Aspect-ratio hints are now allowed in edit mode. (#77295)

## Control UI Recovery and Code Quality

The Control UI now shows a **plain HTML recovery panel** when the app module never registers — a small but critical fix for users who land on a blank dashboard. (#44107)

On the code quality front, the beta cycle enabled stricter Vitest lint rules (focused, disabled, conditional, hook, matcher hazards), additional oxlint rules for promise and TypeScript footguns, and stricter `tsc` compiler checks for implicit returns, side-effect imports, overrides, and unused production code. Logging saw targeted additions for model transport, payload, SSE, and code-mode diagnostics with redacted URL handling.

## The 371K Milestone

At **371,074 stars**, Openclaw has added approximately **2,600 stars since May 7** (when it was at 369,246). The growth rate shows no signs of slowing — the project now averages over 500 new stars per day, making it one of the fastest-growing open-source projects on GitHub by any measure.

The ecosystem around Openclaw continues to expand as well. The **awesome-openclaw-skills** list (VoltAgent) has passed 48,500 stars with 4,750 forks, and the official **ClawHub** skill directory sits at 8,574 stars with 1,324 forks — both indicators that the plugin and skill ecosystem is maturing alongside the core project.

## Looking Ahead

With the v2026.5.10 beta cycle concluding and the project pushing toward a stable release, the trajectory is clear: Openclaw is evolving from a Claude Code harness into a full personal AI operating system with its own build system, deployment targets, voice infrastructure, and agent communication protocols. The agent-to-agent depth improvements, combined with per-agent message isolation and local model support, suggest the project is quietly preparing for a world where users run fleets of specialized agents rather than a single general-purpose assistant.
