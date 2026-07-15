---
layout: post
title: >
  "Sprint Post-Fondation d'Hermes Agent : OAuth du Tableau de Bord, Mémoire Kynver, Qwen 3.7-Max et 30+ PR Fusionnées"
date: 2026-05-27 14:00:00 +0200
lang: fr
ref: hermes-agent-post-foundation-sprint-may27
permalink: /fr/2026/05/hermes-agent-post-foundation-sprint-may27/
translation_of: /2026/05/hermes-agent-post-foundation-sprint-may27/
author: The Agent Report
categories: ["hermes-agent"]
tags: ["hermes-agent", "nous-research", "open-source", "dashboard-oauth", "kynver-memory", "qwen-37-max", "api-server", "security-plugins", "codex-reliability", "traduction-francaise"]
last_modified_at: 2026-07-15 15:03:10 +0000
hero_image: /assets/images/hero/hero-hermes-agent-post-foundation-sprint-may27.jpg
meta_description: >
  "Découvrez le sprint post-Fondation d'Hermes Agent avec OAuth du tableau de bord, pont mémoire Kynver, support de Qwen 3.7-Max, contrôles de session API et plus de 30 PR fusionnées en 11 jours."
description: >
  "Découvrez le sprint post-Fondation d'Hermes Agent avec OAuth du tableau de bord, pont mémoire Kynver, support de Qwen 3.7-Max, contrôles de session API et plus de 30 PR fusionnées."
reading_time: 6
---

## 🏠 Connexion OAuth au tableau de bord (#30156)

Le changement le plus visible pour les utilisateurs dans ce lot est le **flux de connexion OAuth du tableau de bord**. Auparavant, les utilisateurs du tableau de bord devaient configurer manuellement leurs identifiants de fournisseur via des fichiers de configuration. Désormais, le tableau de bord prend en charge un flux complet de connexion OAuth — les opérateurs peuvent se connecter via leur fournisseur d'identité directement depuis l'interface utilisateur du tableau de bord.

L'implémentation repose sur la nouvelle option de configuration `dashboard.public_url` ([commit par @benbarclay](https://github.com/NousResearch/hermes-agent/commit/a890389b69575916dfaf3980556f31f7f25c9871)), qui permet aux opérateurs derrière des proxys inverses de définir l'URL de base absolue pour les callbacks OAuth. Cela résout un problème courant pour les déploiements auto-hébergés derrière nginx, les contrôleurs d'entrée sur site et les configurations Fly.io avec domaine personnalisé où les en-têtes `X-Forwarded-Host` ne sont pas transmis de manière fiable.

> « Lorsqu'elle est définie, il s'agit de l'autorité complète — schéma + hôte + préfixe de chemin optionnel — et elle devient la base de l'`redirect_uri` OAuth. »
> — Message de commit sur `HERMES_DASHBOARD_PUBLIC_URL`

La configuration suit une chaîne de priorité claire : **variable d'environnement > `config.yaml` > détection automatique depuis les en-têtes de requête**, en cohérence avec le modèle existant `dashboard.oauth.client_id`.

---

## 🧠 Fournisseur de mémoire Kynver + pont AgentOS (#33158)

La mémoire est l'un des sous-systèmes les plus critiques pour tout agent capable de s'améliorer, et aujourd'hui Hermes a gagné un nouveau backend. La PR [#33158](https://github.com/NousResearch/hermes-agent/pull/33158) ajoute le **fournisseur de mémoire Kynver** ainsi qu'un **pont AgentOS**.

Kynver est un substrat de mémoire spécialisé pour les agents d'IA, offrant un stockage persistant et interrogeable optimisé pour les charges de travail agentiques. Le pont AgentOS signifie qu'Hermes peut désormais exploiter les outils et infrastructures mémoire compatibles avec AgentOS. Il s'agit d'une expansion significative de l'écosystème mémoire déjà riche d'Hermes, qui dépendait auparavant de backends basés sur le système de fichiers, les bases vectorielles et d'autres solutions.

---

## 🤖 Qwen 3.7-Max rejoint le catalogue de modèles (#32806, #33129)

Deux PRs ajoutent aujourd'hui **Qwen 3.7-Max** — le dernier modèle de pointe d'Alibaba — aux catalogues de modèles d'Hermes. La PR [#32806](https://github.com/NousResearch/hermes-agent/pull/32806) l'ajoute à la liste des fournisseurs Alibaba, tandis que la [#33129](https://github.com/NousResearch/hermes-agent/pull/33129) l'ajoute au catalogue `alibaba-coding-plan`.

Qwen 3.7-Max fait des vagues dans la communauté de l'IA open source pour ses capacités de raisonnement solides et ses scores compétitifs sur les benchmarks. Les utilisateurs d'Hermes sur le fournisseur Alibaba peuvent désormais le sélectionner via `hermes model` et commencer immédiatement à construire des agents avec.

---

## 🔌 Contrôles de session du serveur API (#33134, #29302)

Le serveur API — l'interface HTTP d'Hermes pour l'accès programmatique — bénéficie d'une mise à niveau majeure avec les **API de contrôle de session**. La PR [#33134](https://github.com/NousResearch/hermes-agent/pull/33134) (récupérant la [#29302](https://github.com/NousResearch/hermes-agent/pull/29302)) introduit des endpoints pour :
- **Gestion des sessions** — créer, lister et gérer les sessions actives
- **Endpoints de chat** — envoyer des messages, récupérer l'historique des conversations
- **Support du fork** — bifurquer une session vers un nouveau contexte indépendant
- **Streaming SSE** — flux d'événements en temps réel pour les réponses en direct des agents

Cela transforme le serveur API d'une interface HTTP basique en une plateforme d'interaction agentique complète — permettant des interfaces utilisateur personnalisées, des intégrations CI/CD et une orchestration programmatique des agents.

---

## 🛡️ Plugins de sécurité : avertissements de code par correspondance de motifs (#33131)

Une nouvelle catégorie de plugins voit le jour aujourd'hui : les **plugins d'orientation de sécurité**. La PR [#33131](https://github.com/NousResearch/hermes-agent/pull/33131) introduit un système qui détecte par correspondance de motifs les schémas de code dangereux dans le code écrit par les agents et affiche des avertissements _avant_ l'exécution du code.

C'est particulièrement important pour les agents auto-améliorants qui écrivent et exécutent leur propre code — la proposition de valeur centrale d'Hermes. Le plugin d'orientation de sécurité détecte les motifs dangereux courants (`eval()` non sécurisé, traversée du système de fichiers, vecteurs d'injection shell) et les signale avec des conseils de correction exploitables.

---

## 🛠️ Cluster de fiabilité Codex

Une part significative des PRs fusionnées aujourd'hui se concentre sur la **fiabilité du fournisseur Codex (GitHub Copilot)** — le backend de travail pour de nombreux utilisateurs d'Hermes :

- **Synchronisation du pool d'identifiants lors de la ré-authentification** ([#33074](https://github.com/NousResearch/hermes-agent/pull/33074)) — corrige un bug où la ré-authentification Codex via `hermes setup` / `hermes model` écrivait de nouveaux jetons OAuth mais laissait le pool d'identifiants avec des entrées obsolètes, provoquant des erreurs 401 à chaque requête suivante
- **Raisonnement sur émetteur étranger lors de la relecture** ([#33156](https://github.com/NousResearch/hermes-agent/pull/33156), récupérant la [#31629](https://github.com/NousResearch/hermes-agent/pull/31629)) — empêche les erreurs `HTTP 400 invalid_encrypted_content` lors du changement de fournisseur de modèle en cours de conversation (par exemple, de Grok à GPT-5.5)
- **État de raisonnement transitoire rs_tmp** ([#33146](https://github.com/NousResearch/hermes-agent/pull/33146)) — supprime les éléments de raisonnement temporaires obsolètes qui pouvaient s'accumuler et provoquer des échecs
- **Gestion du flux de sortie nul** ([#33008](https://github.com/NousResearch/hermes-agent/pull/33008), [#33050](https://github.com/NousResearch/hermes-agent/pull/33050)) — normalise `response.output=None` en listes vides, évitant les plantages d'itération
- **Indices de contournement des blocages silencieux** ([#33133](https://github.com/NousResearch/hermes-agent/pull/33133), [#33034](https://github.com/NousResearch/hermes-agent/pull/33034)) — indices améliorés côté utilisateur lorsque des scénarios de blocage silencieux ChatGPT sont détectés
- **Incitations du poller CI Homebrew** ([#33142](https://github.com/NousResearch/hermes-agent/pull/33142)) — l'outil terminal détecte désormais les scripts de polling CI anti-modèles et incite les utilisateurs vers des extraits CI verts canoniques

---

## 💬 Nettoyage de l'expérience utilisateur Telegram

Un groupe de trois PRs traite du bruit opérationnel Telegram :
- [#31034](https://github.com/NousResearch/hermes-agent/pull/31034) — réduit le bruit de communication opérationnelle dans la passerelle Telegram
- [#31098](https://github.com/NousResearch/hermes-agent/pull/31098) — ignore les pings de plateforme `/start` sur Telegram
- [#31941](https://github.com/NousResearch/hermes-agent/pull/31941) — masque le bruit de l'état de compactage

Ce sont des améliorations UX petites mais importantes — réduire le bruit dans les canaux Telegram où Hermes opère en tant que bot rend la conversation plus naturelle et moins « robotique ».

---

## 📊 Ce que signifie ce sprint

Onze jours après la sortie Foundation, la vélocité de développement d'Hermes Agent s'accélère :

1. **Le tableau de bord devient un véritable produit** — la connexion OAuth et les API de contrôle de session indiquent qu'Hermes évolue au-delà d'un simple outil en ligne de commande vers une plateforme avec une interface web et des couches d'accès API appropriées
2. **La diversité mémoire s'accroît** — le pont Kynver + AgentOS signifie qu'Hermes peut se connecter à davantage de substrats mémoire d'entreprise et de recherche
3. **La sécurité est au premier plan** — les plugins de sécurité par correspondance de motifs pour l'écriture de code sont une réponse directe aux risques uniques des agents auto-améliorants
4. **La fiabilité quotidienne s'accumule** — le cluster Codex corrige à lui seul plus de 7 modes de défaillance distincts que les utilisateurs rencontraient réellement

Le rythme est remarquable : plus de 30 PRs fusionnées en une seule journée, couvrant l'infrastructure (authentification, configuration, API), les modèles (Qwen 3.7-Max), les systèmes mémoire, la sécurité et la fiabilité. Si la sortie Foundation portait sur la _surface fonctionnelle_, ce sprint porte sur la _profondeur_ — rendre chaque sous-système plus fiable, plus sécurisé et plus performant. La dynamique du projet reflète ce que nous avons documenté à travers l'[écosystème communautaire Hermes Agent]({% post_url 2026-05-25-hermes-agent-community-ecosystem-may25 %}), qui a atteint 276 cas d'usage documentés et 165K étoiles GitHub.

Avec **169,5K étoiles et en augmentation**, Hermes Agent continue d'être le framework d'agents open source à la croissance la plus rapide — et si le sprint d'aujourd'hui est une indication, la prochaine version (v0.15.0 ?) vaudra l'attente.