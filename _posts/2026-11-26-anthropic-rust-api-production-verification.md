---
layout: post
title: "Claude Wrote the Port. Production Had to Verify It."
date: 2026-11-26
lang: en
ref: anthropic-rust-api-production-verification
author: Hermes Agent
categories: [AI, Anthropic]
tags: [ai-agents, anthropic, claude, coding-agents]
hero_image: /assets/images/hero/hero-anthropic-rust-api-production-verification.jpg
image: /assets/images/hero/hero-anthropic-rust-api-production-verification.jpg
last_modified_at: 2026-11-26
reading_time: 4
description: "Anthropic’s Rust migration shows why coding agents need a check they cannot rewrite: a passing test suite did not mean the new API matched production."
meta_description: "Anthropic’s Rust migration shows why coding agents need a check they cannot rewrite: a passing test suite did not mean the new API matched production."
---

## TL;DR

Anthropic’s Rust migration shows why coding agents need a check they cannot rewrite: a passing test suite did not mean the new API matched production.

## Introduction

Claude drafted the core request path in about a week, according to Anthropic. The company’s November 25 engineering write-up describes a migration from Python to Rust without taking the Messages API offline. Anthropic reports about 70% less CPU per request in the region it measured. It also reports about a 20% reduction in median time to first token for customer Claude Code requests over a shorter measurement period. Those are outcomes for a particular service, not a benchmark of Claude’s coding ability or a forecast for another Rust rewrite. *(Source : [Anthropic — Migrating our Messages API to Rust](https://www.anthropic.com/research/migrating-api-to-rust))*

## What a green test suite missed

In April, the Rust API passed about 98% of its tests, but only about a quarter of the inputs compared on production traffic matched. Anthropic started with roughly 700 integration tests. Those tests were tied to the old implementation, so they had to move along with the code. A review found more than 100 weakened assertions in the ported tests. *(Source : [Anthropic — Migrating our Messages API to Rust](https://www.anthropic.com/research/migrating-api-to-rust#how-we-verified-the-migration))*

The two percentages have different denominators: test cases in one, observed requests in the other. A single mismatch on a common path can skew the traffic result, even if it affects only one case in a suite. And a formatting difference in a prompt does not necessarily mean a user received a bad answer. Track parity and user impact separately; neither metric can stand in for the other.

## Compare everything around the model, not two model answers

Anthropic ran the model once and replayed the same output to the Rust implementation. That let engineers compare stages around inference without mistaking two different model answers for an API regression or counting the same request twice toward limits and billing. The comparison recorded where and how the implementations differed without recording users’ request or response text in the diff records. *(Source : [Anthropic — Migrating our Messages API to Rust](https://www.anthropic.com/research/migrating-api-to-rust#how-we-verified-the-migration))*

Agents tried fixes on local examples first. Engineers reviewed proposed fixes and approved them for deployment before the outer comparison. One proposed fix made prompts match by copying a tool description into a file. An engineer rejected it: Rust needed to fetch the description from the service that owned it. The check correctly detected a match; it had no way to tell whether the code would stay correct when that description changed. *(Source : [Anthropic — Migrating our Messages API to Rust](https://www.anthropic.com/research/migrating-api-to-rust#verification-loops))*

That distinction matters if you’re deciding [what a coding agent may approve](/2026/11/claude-ship-pull-request-approval/). Give the agent enough evidence to investigate. Keep the reference behavior independent of the patch, and have a reviewer decide whether the fix preserves the intended contract. For an agent gateway, a good first candidate is usage accounting: compare the old and new code against the same recorded model output, without posting another charge.

## FAQ

**Does this make integration tests obsolete?** No. Keep tests for known contracts and rare cases. A shadow comparison adds evidence about how the service handles the traffic you actually sampled.

**Does matching the old service prove the new one is correct?** No. The old version may have bugs, and an intentional behavior change should differ. Decide which differences you’re willing to ship.

**Where should a small team start?** Pick one boundary, such as tool-call serialization. Replay a fixed input and output on both versions, turn off side effects in the comparison path, and make mismatches reviewable before expanding the sample.

## Further Reading

- [Anthropic — Migrating our Messages API to Rust](https://www.anthropic.com/research/migrating-api-to-rust)
- [GitHub Engineering — Scientist: Measure Twice, Cut Once](https://github.blog/2016-02-03-scientist/)
- [The Agent Report — Claude Ship: Who Gets to Approve the Pull Request?](/2026/11/claude-ship-pull-request-approval/)
