---
layout: post
title: "Openclaw v2026.5.22 Ships 4,100× Faster Model Listing, Meeting Notes Plugin, and Major Packaging Overhaul"
date: 2026-05-26 10:00:00 +0000
last_modified_at: 2026-05-26 10:00:00 +0000
meta_description: "Openclaw v2026.5.22 delivers a 4,100x speedup in model-listing calls, a Meeting Notes plugin with Discord voice capture, and a comprehensive packaging."
categories: [openclaw]
tags: [openclaw, claw-controller, agent-autonomy, performance-optimization, enterprise-packaging]
reading_time: 7
excerpt: "Openclaw v2026.5.22 delivers a staggering 4,100× speedup in model-listing calls, a brand-new Meeting Notes plugin with Discord voice capture, and a comprehensive packaging overhaul including shrinkwrap integrity checks and smaller npm tarballs. The star count crosses 375,000."
hero_image: /assets/images/hero/hero-openclaw-v2026-5-22-4100x-model-listing-meeting-notes.jpg
author: The Agent Report
---

Openclaw's release train shows no signs of slowing. On May 24, 2026, the project shipped **v2026.5.22** — a stable release that packs what may be the most technically impressive performance optimization in the project's history alongside a new Meeting Notes plugin and a sweeping packaging and security overhaul.

With **375,000+ GitHub stars**, **78,000+ forks**, and **381 contributors** in this release alone (including many first-time names), Openclaw's trajectory from buzzy open-source project to serious agent infrastructure platform continues to accelerate.

## The 4,100× Performance Milestone

The headline number in v2026.5.22 is hard to ignore: **model-listing calls dropped from ~20 seconds to ~5 milliseconds** — a 4,100× improvement. Here's how the team achieved it:

| Optimization | Description |
|---|---|
| **Auth-state pre-warming** | Provider authentication state maps are now pre-warmed at gateway startup, so `/models` calls short-circuit per-provider discovery instead of blocking on live API calls |
| **Immutable plugin metadata snapshots** | Plugin catalog, channel config, and SDK alias maps are cached as immutable snapshots reused across startup, config, model, and secret readers |
| **Lazy-loaded startup work** | Core handlers, embedded ACPX runtime, and startup-idle plugins are no longer loaded before health/ready signals — the gateway reports healthy *before* finishing plugin tree initialization |
| **Cached SDK alias maps** | Public-surface alias maps are cached, and irrelevant macOS Linuxbrew PATH probes are skipped entirely |
| **Avoided redundant channel checks** | Process-stable channel catalog reads eliminate repeated bundled-channel boundary checks during gateway dispatch |

For developers and teams running Openclaw in production, this means **near-instant model enumeration** — no more staring at a spinner while the gateway probes every provider. The `/models` endpoint now feels like a local cache lookup rather than a distributed discovery operation.

## Meeting Notes Plugin: Agent-Powered Transcription

A brand-new **Meeting Notes plugin** debuts in v2026.5.22 as a source-only external plugin with a defined SDK source-provider contract living outside the core npm package. Key capabilities include:

- **Auto-start capture** — Automatically begins recording meeting transcripts when a Discord voice session joins
- **Manual transcript imports** — Import existing meeting transcripts for search and retrieval
- **CLI access** — Full `openclaw meeting-notes` command with read-only operations
- **Discord as first live source** — Discord voice channels are the initial live capture source, with the SDK contract allowing third-party providers to build additional integrations

The plugin architecture is notable: it ships as a **source-only plugin outside the core distribution**, following the externalization pattern established in the v2026.5.12-beta cycle. This keeps the core npm package lean while allowing rich functionality through the plugin ecosystem.

```bash
# Install the meeting-notes plugin
openclaw plugins add openclaw/meeting-notes

# View captured notes
openclaw meeting-notes list
```

## Plugin SDK Advances

Beyond the Meeting Notes plugin, the Plugin SDK received several foundational upgrades:

- **Generic poll sender** — A new channel-message poll sender enables plugins to create and manage polls across any channel
- **Embedding providers API** — Plugins can now declare and register embedding provider capabilities through a formal contract
- **Row-level session workflow helpers** — Deprecating `loadSessionStore` in favor of granular, row-level session management that's more composable and testable
- **Compatible plugin registry reuse** — The gateway now reuses compatible plugin registries during dispatch, avoiding redundant loading

These SDK improvements lower the barrier for third-party developers while giving power users more granular control over session state and embedding strategies.

## Enterprise Packaging & Security Overhaul

One of the most consequential changes in v2026.5.22 is invisible to end users but critical for enterprise adopters: a complete **packaging and integrity overhaul**.

### Smaller npm Tarballs

The npm distribution package now **excludes documentation images and assets**, significantly reducing download size. For teams deploying Openclaw across fleets of servers, this translates to faster installs and less bandwidth consumption.

### Shrinkwrap Integrity

Every published Openclaw npm package now ships with a **generated shrinkwrap file**, pinning all transitive dependency versions:

```bash
# The shrinkwrap is included in the published tarball
npm install -g openclaw  # Guaranteed reproducible install
```

All lockfile and shrinkwrap changes now require explicit review before merge, preventing accidental dependency drift. The `pnpm check` stages run through a managed child runner to avoid Node.js shell-argv deprecation warnings.

### Package Integrity Checks

A new release validation step performs **package integrity checks before publication**, preventing private QA artifacts from leaking into the published npm package. This addresses a class of supply-chain concerns that enterprise security teams frequently raise.

## QA-Lab: Personal Agent Scenarios

The QA-Lab automated test harness continues its expansion with v2026.5.22, adding:

- **Curated mock JSONL replay fixtures** — Deterministic replay of provider API responses for reproducible testing
- **First-drift reporting** — Automatically identifies the first divergence in agent behavior during runtime parity checks
- **Personal-agent failure recovery scenarios** — Tests that agents can recover from runtime failures without human intervention
- **Codex plugin lifecycle coverage** — End-to-end tests for Codex plugin install, update, and removal paths
- **Opt-in self-upgrade sentinel** — `update.run` scenarios that validate the upgrade path doesn't break existing functionality

With each release, QA-Lab grows more comprehensive — signaling Openclaw's maturation toward enterprise-grade reliability engineering.

## Discord and Browser Fixes

Beyond the headline features, v2026.5.22 ships important quality-of-life fixes:

- **Discord callback lifetime caps** — `agentComponents.ttlMs` now enforces a 24-hour maximum on Discord callback registry lifetime, preventing stale callbacks from accumulating
- **WebChat deduplication** — Fixed a race condition where WebChat sessions could spawn duplicate message handlers
- **Gateway lifecycle cleanup** — Preserved lifecycle state during gateway channel resets, preventing stale subscriptions from surviving restarts
- **Browser image sanitization** — Limits now properly enforced for screenshots and labeled snapshots

## Documentation Sprint

The release includes a massive documentation update touching **Signal configPath, Telegram wildcard topic defaults, Termux home fallback, macOS VM auto-login, WhatsApp QR/408 recovery, cron output language prompts, CDP diagnostics, Plugin SDK allowlist imports, Bitwarden SecretRef setup, EasyRunner deployments, Upstash Box install guides, and more**. 164+ contributors are named in the changelog, highlighting the project's extraordinary community momentum.

## The Big Picture

Openclaw v2026.5.22 represents a release where **infrastructure maturity catches up with feature velocity**. The 4,100× performance improvement isn't just a benchmark trophy — it fundamentally changes how responsive the gateway feels during provider configuration. The Meeting Notes plugin opens a new product category for agent-powered productivity. And the packaging overhaul addresses the #1 blocker for enterprise deployment: supply-chain integrity. This release follows just days after the [Policy Plugin introduced compliance-as-code]({% post_url 2026-05-21-openclaw-v2026-5-20-beta1-policy-plugin-compliance %}) for agent orchestration.

The project now sits at **375,000+ GitHub stars** with **78,000+ forks**. The stable release is available immediately. For developers evaluating the open-source agent landscape, our [Complete Guide to AI Agents]({% post_url 2026-05-26-complete-guide-to-ai-agents-2026 %}) provides a comprehensive overview of how platforms like Openclaw fit into the broader ecosystem.

```bash
npm install -g openclaw
```

For those running beta builds, `npm update -g openclaw` pulls the latest stable directly.

---

*Openclaw v2026.5.22 is available now via `npm install -g openclaw`. Full release notes on [GitHub](https://github.com/openclaw/openclaw/releases/tag/v2026.5.22).*
