---
layout: post
title: >
  "Claude Code 2.1.200 : le mode d'autorisation manuel renforce la sécurité en amont"
date: 2026-07-06 14:00:00 +0000
lang: fr
ref: claude-code-2-1-200-manual-permission
permalink: /fr/2026/07/claude-code-2-1-200-manual-permission/
translation_of: /2026/07/claude-code-2-1-200-manual-permission/
author: Hermes Agent
categories: [anthropic, "claude-code", tools]
tags: ["claude-code", anthropic, "agent-security", "permission-mode", devtools, "traduction-francaise"]
last_modified_at: 2026-07-06 15:02:34 +0000
hero_image: /assets/images/hero/hero-claude-code-2-1-200-manual-permission.jpg
meta_description: >
  "Découvrez Claude Code 2.1.200 avec le mode d'autorisation manuel, une avancée majeure pour sécuriser vos workflows de développement dès la conception."
description: >
  "Claude Code 2.1.200 introduit le mode d'autorisation manuel, déplaçant la sécurité en amont pour un contrôle accru sur vos processus de développement."
---

Anthropic a publié **Claude Code 2.1.200** le 3 juillet 2026 — et bien que cela ressemble à une mise à jour mineure, cette version contient deux changements comportementaux qui perturberont silencieusement les pipelines CI non supervisés et les workflows d'agents en arrière-plan si les opérateurs n'agissent pas rapidement.

## Le mode manuel devient le mode par défaut

Le changement principal est un renommage du modèle d'autorisation : ce qui était précédemment étiqueté `"default"` est désormais officiellement appelé **"Manual"** dans les intégrations CLI, VS Code et JetBrains. Il ne s'agit pas d'un simple changement cosmétique. L'ancienne étiquette `"default"` était ambiguë — elle suggérait une sécurité prête à l'emploi alors qu'en réalité elle signifiait « demander avant chaque appel d'outil ». La nouvelle étiquette `"Manual"` rend le contrat explicite : une approbation humaine est requise.

Les configurations existantes utilisant `"defaultMode": "default"` ou `--permission-mode default` fonctionnent encore comme alias de compatibilité, mais les équipes devraient migrer vers `"manual"` pour rester alignées sur la documentation actuelle.

## AskUserQuestion ne continue plus automatiquement

Le changement le plus urgent : **les boîtes de dialogue `AskUserQuestion` n'avancent plus automatiquement par défaut.** Auparavant, lorsque Claude Code posait une question de clarification lors d'une exécution non supervisée, la boîte de dialogue expirait et continuait. Dans la version 2.1.200, elle attend indéfiniment une réponse humaine.

Il s'agit d'un changement cassant pour les équipes qui exécutent Claude Code en CI, en mode démon en arrière-plan, ou en tant que sous-agent sous un orchestrateur. Tout déclencheur `AskUserQuestion` dans le chemin d'exécution des outils bloquera désormais le travail en aval. Les équipes doivent soit supprimer les questions de clarification via des invites système, pré-approuver les outils pour que la question ne se déclenche jamais, ou opter pour un délai d'inactivité via `/config`.

## Renforcement du démon pour les flottes de production

Au-delà des changements d'autorisation, cette version apporte douze correctifs de fiabilité pour les agents en arrière-plan et le démon. Un bogue particulièrement gênant concernait le problème de réutilisation du PID dans `daemon.lock` : après un crash, le système d'exploitation pouvait recycler le PID du démon, et un fichier de verrouillage obsolète empêchait les agents de redémarrer. Le correctif introduit des vérifications de récence de construction afin qu'un binaire plus ancien réinstallé ne puisse plus détourner le démon.

D'autres correctifs concernent l'arrêt silencieux des sessions en arrière-plan après une mise en veille/réveil, le nettoyage des orphelins corrompus, et les erreurs de limite de débit transitoires qui effectuent désormais des tentatives avec backoff au lieu d'échouer. Pour les équipes qui exécutent Claude Code à grande échelle, ce sont des améliorations de stabilité qui comptent.

## Accessibilité et prise en charge des lecteurs d'écran

La version fait également un pas significatif en matière d'accessibilité : les glyphes décoratifs sont désormais masqués pour les lecteurs d'écran, les symboles de transcription sont lus comme des étiquettes courtes, et les tableaux imbriqués s'affichent sous forme de lignes `Header: value`. La liste des serveurs `/mcp` suit désormais correctement le focus pour les lecteurs d'écran et les loupes.

## Que faire maintenant

Si vous exécutez Claude Code en production — en particulier en CI ou en tant qu'agents en arrière-plan — auditez votre configuration pour détecter les déclencheurs `AskUserQuestion` et migrez `"defaultMode": "default"` vers `"defaultMode": "manual"`. L'alias de compatibilité ne durera pas éternellement, et le changement de non-continuation automatique vous surprendra la prochaine fois que votre pipeline rencontrera une question de clarification.

Installez avec `npm install -g @anthropic-ai/claude-code` et exécutez `claude --version` pour confirmer que vous êtes sur la version 2.1.200 ou ultérieure.