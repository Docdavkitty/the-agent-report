---
layout: post
title: >
  "Hermes Agent v0.11.0 « Interface » — Ink TUI, AWS Bedrock, GPT-5.5 et 17 plateformes"
date: 2026-04-30 12:56:00 +0200
lang: fr
ref: hermes-agent-v0110-interface-release
permalink: /fr/2026/04/hermes-agent-v0110-interface-release/
translation_of: /2026/04/hermes-agent-v0110-interface-release/
author: The Agent Report
categories: ["hermes-agent"]
tags: [Hermes Agent, Nous Research, release, v0.11, TUI, AWS Bedrock, "GPT-5.5", QQBot, "traduction-francaise"]
last_modified_at: 2026-08-22 12:15:45 +0000
hero_image: /assets/images/hero/hero-04-30-hermes-agent-v0110-interface-release.jpg
meta_description: >
  "Hermes Agent v0.11.0 Interface propose une refonte TUI React/Ink, le support AWS Bedrock, GPT-5.5 via Codex OAuth, cinq nouveaux chemins d’inférence et QQBot."
description: >
  "Hermes Agent v0.11.0 Interface comprend une interface TUI React/Ink réécrite, AWS Bedrock, GPT-5.5 via Codex OAuth, cinq chemins d’inférence et QQBot."
reading_time: 4
---

Hermes Agent, le runtime IA open source de **Nous Research** qui a pris GitHub d’assaut (plus de 126 000 étoiles), vient de livrer **v0.11.0 « Interface »** — sa plus grosse version à ce jour. (Consultez notre [guide complet sur les agents IA]({% post_url 2026-05-26-complete-guide-to-ai-agents-2026 %}) pour situer cet écosystème.) Avec 1 556 commits, 761 PR fusionnées et les contributions de 29 membres de la communauté sur deux semaines de développement intensif, cette version redéfinit la manière dont les développeurs interagissent avec l’agent et l’étendent.

## ✨ Une toute nouvelle expérience terminal

La fonctionnalité phare est une réécriture complète de l’interface en ligne de commande interactive avec **React/Ink**, accessible via `hermes --tui` ou `HERMES_TUI=1`. La nouvelle TUI (environ 310 commits) comprend :

- Un **composeur persistant** qui reste en place pendant le défilement de l’historique de conversation
- La **diffusion en direct** avec prise en charge du presse-papiers OSC-52 pour copier à travers SSH
- Des **touches de sélection stables**, un **chronomètre par tour** dans la barre d’état et un **indicateur de branche git**
- Un **overlay d’observabilité du lancement de sous-agents** pour suivre les flux de travail parallèles
- Un thème clair prédéfini et une confirmation `/clear` pour éviter les réinitialisations accidentelles de session

Le backend JSON-RPC en Python (`tui_gateway`) rend la TUI entièrement extensible — attendez-vous bientôt à des thèmes et des plugins communautaires.

## 🏗️ Couche de transport enfichable et AWS Bedrock

Cette version introduit une classe de base abstraite **Transport ABC** qui extrait la conversion de format et le transport HTTP du fichier monolithique `run_agent.py` vers des modules dédiés :

- **AnthropicTransport** — API Anthropic Messages
- **ChatCompletionsTransport** — fournisseurs compatibles OpenAI
- **ResponsesApiTransport** — API OpenAI Responses + Codex
- **BedrockTransport** — AWS Bedrock natif via l’API Converse

Ce changement architectural simplifie considérablement l’ajout de nouveaux backends de fournisseurs et ouvre la porte aux transports contribués par la communauté.

## 🧠 Cinq nouvelles voies d’inférence

Hermes se connecte désormais à plus de modèles que jamais grâce à la prise en charge native de :

- **NVIDIA NIM** — exécutez les modèles Nemotron et d’autres modèles hébergés par NVIDIA
- **Arcee AI** — modèles de domaine spécialisés
- **Step Plan** — modèles de planification structurée
- **Google Gemini CLI OAuth** — authentifiez-vous et utilisez Gemini directement
- **Vercel ai-gateway** — avec tarification, attribution et découverte dynamique des modèles

De plus, **GPT-5.5** est disponible via Codex OAuth avec découverte dynamique des modèles : les nouvelles sorties OpenAI apparaissent dans le sélecteur de modèles sans mise à jour du catalogue.

## 📱 QQBot — Plateforme #17

Hermes fonctionne désormais sur **17 plateformes de messagerie**. La nouveauté est **QQBot**, construit sur l’API officielle QQ v2 avec configuration par scan de QR code, curseur de streaming, réactions emoji et application de politiques de groupes/messages directs, au même niveau que WeCom et Weixin.

Parmi les autres nouveautés de plateformes figurent la prise en charge d’un proxy Telegram, les salons de forum Discord, l’intelligence des commentaires de documents Feishu et l’envoi de messages vocaux WhatsApp.

## 🔌 Surface des plugins : d’extensible à entièrement hackable

Le système de plugins a connu une expansion massive. Les plugins peuvent désormais :

- **Enregistrer des commandes slash** (`register_command`)
- **Appeler directement des outils** (`dispatch_tool`)
- **Mettre un veto à l’exécution d’outils** via des hooks `pre_tool_call`
- **Réécrire les résultats d’outils** avec `transform_tool_result`
- **Transformer la sortie du terminal** (`transform_terminal_output`)
- **Fournir des backends personnalisés de génération d’images**
- **Ajouter des onglets personnalisés au tableau de bord**
- **Câbler des scripts shell comme hooks de cycle de vie** — sans avoir besoin de Python

Un **plugin de nettoyage de disque** fourni sert d’implémentation de référence, proposé en opt-in par défaut.

## 🤖 Autres améliorations notables

- **`/steer <prompt>`** — Injectez des instructions en cours d’exécution que l’agent verra après son prochain appel d’outil, sans casser le cache de prompt. Consultez notre [glossaire des agents IA]({% post_url 2026-05-27-ai-agent-glossary-55-terms %}) pour la définition de ces primitives d’agent.
- **Mode de livraison directe par webhook** — notifications push sans LLM pour les alertes et les flux d’événements
- **Délégation plus intelligente** — les sous-agents ont désormais un rôle `orchestrator` explicite avec une profondeur de lancement configurable et une coordination par système de fichiers
- **Système de plugins du tableau de bord** — onglets tiers, widgets et basculement de thème en direct pour le tableau de bord web
- **i18n** — le tableau de bord prend en charge l’anglais et le chinois avec un sélecteur de langue
- **Purge automatique des anciennes sessions** + VACUUM au démarrage pour maintenir `state.db` en bonne santé

## 📈 En chiffres

- **126 132 étoiles GitHub** et **18 854 forks**
- **1 556 commits** depuis la v0.9.0
- **29 contributeurs de la communauté** (290 en incluant les coauteurs)
- **224 174 lignes modifiées** dans 1 314 fichiers

## Prise en main

Hermes Agent fonctionne sur n’importe quelle machine Linux, un VPS à 5 $ ou une infrastructure serverless. Installez-le avec :

```bash
pip install hermes-agent
hermes setup
```

Exécutez ensuite `hermes --tui` pour découvrir la nouvelle interface, ou `hermes model` pour choisir parmi plus de 200 modèles sur OpenRouter, Nous Portal, NVIDIA NIM, AWS Bedrock et plus encore.

Consultez la [documentation](https://hermes-agent.nousresearch.com) et le [dépôt GitHub](https://github.com/NousResearch/hermes-agent) pour tous les détails. Le projet est sous licence MIT et les contributions de la communauté sont les bienvenues.