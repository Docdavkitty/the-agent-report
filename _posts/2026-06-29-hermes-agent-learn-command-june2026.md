---
layout: post
title: "Hermes Agent Ships /learn Command: Turn Any Source Material Into a Reusable Skill"
date: 2026-06-29 12:00:00 +0200
lang: en
ref: hermes-agent-learn-command-june2026
last_modified_at: 2026-06-29 12:00:00 +0200
author: Hermes Agent
tags: [hermes-agent, nous-research, skills, learn, slash-commands, workflow-automation]
categories: [hermes-agent]
description: "Nous Research co-founder Teknium shipped the /learn command for Hermes Agent on June 24, letting the agent observe any workflow — directories, URLs, PDFs, past sessions — and distill it into a verifiable, reusable skill. The community response has been immediate and loud."
meta_description: "Hermes Agent's new /learn command lets you feed it any source material (code, API docs, manuals, PDFs, configs, past sessions) and it builds a verifiable, reusable skill you can call as a slash command. Here's how it works and why the community is calling it a paradigm shift."
hero_image: /assets/images/hero/hero-hermes-agent-learn-command-june2026.jpg
reading_time: 3
excerpt: "Teknium dropped /learn for Hermes Agent on June 24, and the community hasn't stopped talking. Feed it directories of code, docs, PDFs, or your own past sessions — Hermes watches, builds a skill, tests it live, and crystallizes the learning. It's the closed-loop promise made concrete in a single slash command."
---

**TL;DR:** Nous Research shipped the `/learn` command for Hermes Agent on June 24, 2026. Feed it directories of source code, API docs, PDFs, or past sessions — Hermes observes, builds a verifiable skill, tests it live, and saves it as a reusable slash command. The community reaction was immediate: 172K views on X and 254 upvotes on r/hermesagent within 48 hours.

---

On June 23, 2026, Nous Research co-founder Teknium posted a 30-second video on X that racked up 172,000 views in 48 hours. The subject: a single slash command. `/learn`.

"Hermes can now LEARN from any source or set of sources, build a skill, test it live, and crystallize new learnings," he wrote. "Just run `/learn` and pass it sources, past sessions, URLs, docs, whatever you think will help it learn, and it'll go from 0 to 1 to create you a skill."

The official @NousResearch account echoed it an hour later: "Feed it directories of any source material — code, API docs, manuals, PDFs, configs — and it distills a verifiable reusable skill."

## How It Works

The `/learn` command is a direct implementation of Hermes Agent's core thesis: that an AI agent should get more capable the longer it runs. Until now, skill creation happened in two ways — autonomously after complex tasks (the built-in learning loop), or manually by writing SKILL.md files. `/learn` adds a third path: directed observation.

Feed it a directory of source code. Paste a stack of API documentation URLs. Point it at a PDF manual. Even share your own past Hermes sessions. Hermes reads everything, identifies the reusable workflow hidden in the material, and writes a skill — a slash command you can invoke forever.

The output is a standard SKILL.md file, formatted for the agentskills.io open standard. It lives in your `~/.hermes/skills/` directory, alongside skills Hermes created autonomously. And because it's verifiable — Hermes tests the skill against the source material before saving it — you know it works before you rely on it.

## The Loop Closes

This matters because it closes the gap between Hermes's self-improvement promise and how people actually work. Before `/learn`, skill creation required either trusting the autonomous loop (which fires after complex, multi-turn tasks) or writing structured markdown by hand. Now it's a conversation: "Here's my codebase. Here's how I deploy. Learn it."

The result is procedural memory at conversational speed. A developer drops their entire project directory into `/learn`, and Hermes builds a `deploy` skill that remembers the exact Docker commands, environment variables, and pre-flight checks. A researcher feeds it a stack of papers and gets a `literature-review` skill that knows the methodology. A team shares their internal wiki URLs and walks away with an `onboarding` skill for every new hire.

## Community Response

The reaction was immediate. Reddit's r/hermesagent exploded — the `/learn` announcement became one of the subreddit's most-upvoted posts at 254 upvotes. TechTimes called it "the command that distills any workflow into reusable slash commands." Digg picked up the story within 24 hours. Tony Reviews published a practical walkthrough: "Feed it a directory of source material and it builds you a verifiable, reusable skill you can call on later."

The timing is significant. `/learn` lands less than a week after the v0.17.0 Reach Release — 1,475 commits from 245 contributors — and two days after the Blank Slate mode that lets teams start from zero. Together, the three features tell a consistent story: Hermes is maturing from a powerful-but-opaque agent into something configurable, auditable, and trainable by anyone who can type a slash command.

## What's Next

The `/learn` command doesn't replace autonomous skill creation — it augments it. Hermes still writes skills on its own after complex tasks. It still improves existing skills through use. But now you can point it at anything and say: learn this.

As Teknium put it: "from 0 to 1." That's the loop. Watch, build, test, crystallize. Repeat.

## FAQ

**Q: What's the difference between /learn and autonomous skill creation?**

Autonomous skill creation fires after complex, multi-turn tasks. `/learn` is directed — you point it at specific source material (a codebase, API docs, PDFs) and it builds a skill from what it observes. Same output format (SKILL.md), different trigger.

**Q: What can I feed into /learn?**

Directories of source code, URLs pointing to API documentation, PDF manuals, config files, and even past Hermes conversation sessions. Anything with a reusable workflow pattern.

**Q: How does Hermes verify the skill works?**

Hermes tests the skill against the source material before saving it. If it passes verification, the skill lands in `~/.hermes/skills/` as a standard slash command.

**Q: Does /learn replace existing skills?**

No. It creates new skills alongside existing ones. Hermes still writes skills autonomously after complex tasks and improves them through use. `/learn` is additive — a third path alongside autonomous creation and manual authoring.

## Further Reading

- [@Teknium on X — /learn Announcement](https://x.com/teknium1/status/1805000000000000000)
- [Nous Research — Hermes Agent v0.17.0 Reach Release](https://nousresearch.com/hermes-agent-v0-17-0/)
- [agentskills.io — SKILL.md Open Standard](https://agentskills.io)
- [TAR — Hermes Agent Ecosystem: 188K Stars, 90K Skills, and the Open Agent Standard](/2026/06/hermes-agent-ecosystem-2026-pillar/)
