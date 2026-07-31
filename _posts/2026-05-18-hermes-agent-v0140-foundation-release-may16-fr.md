---
layout: post
title: >
  "Hermes Agent v0.14.0 « Foundation » : Grok OAuth, proxy compatible OpenAI, PyPI, bêta native Windows et 155K étoiles"
date: 2026-05-18 10:00:00 +0200
lang: fr
ref: hermes-agent-v0140-foundation-release-may16
permalink: /fr/2026/05/hermes-agent-v0140-foundation-release-may16/
translation_of: /2026/05/hermes-agent-v0140-foundation-release-may16/
author: The Agent Report
categories: ["hermes-agent"]
tags: [Hermes Agent, Nous Research, "open-source", v0.14.0, "foundation-release", "grok-oauth", "local-proxy", pypi, "windows-beta", "microsoft-teams", "traduction-francaise"]
last_modified_at: 2026-07-31 15:12:06 +0000
hero_image: /assets/images/hero/hero-hermes-agent-v0140-foundation-release-may16.jpg
meta_description: >
  "Hermes Agent v0.14.0 Foundation livre Grok OAuth avec contexte 1M, proxy compatible OpenAI, packaging PyPI, la bêta native Windows et 155K étoiles GitHub."
description: >
  "Hermes Agent v0.14.0 Foundation livre Grok OAuth avec contexte 1M, proxy compatible OpenAI, packaging PyPI, bêta native Windows et 155K étoiles GitHub."
reading_time: 8
---

## 🤖 xAI Grok via SuperGrok OAuth — Avec une fenêtre de contexte de 1M tokens

La fonctionnalité phare. Si vous payez pour SuperGrok, vous pouvez désormais utiliser **xAI Grok dans Hermes Agent** — positionnant le projet parmi les [meilleurs frameworks d'agents IA open source]({% post_url 2026-05-27-ultimate-guide-open-source-ai-agent-frameworks %}) — en vous connectant avec votre compte xAI — sans clé API, sans facturation séparée. L'intégration passe par OAuth, vos identifiants d'abonnement sont gérés de manière sécurisée sans exposer de tokens bruts.

Mais la vraie surprise : **la fenêtre de contexte de Grok passe à 1M tokens** grâce à ce passage direct. Cela signifie que vous pouvez déposer des bases de code entières ou des corpus de recherche dans une seule invite Grok — une capacité qui place Grok au niveau de Gemini 2.5 Pro pour les cas d'usage à long contexte. ([#26534](https://github.com/NousResearch/hermes-agent/pull/26534), [#26664](https://github.com/NousResearch/hermes-agent/pull/26664), [#26644](https://github.com/NousResearch/hermes-agent/pull/26644))

> *"Gestion appropriée des erreurs de droits et une page de documentation pour le tunnel SSH pour lorsque vous êtes connecté en SSH sur une machine distante et devez terminer le flux OAuth."* — Notes de version

Pour les utilisateurs de serveurs distants, le flux OAuth inclut également un **guide de tunnel SSH** afin que vous puissiez vous authentifier depuis une machine sans interface graphique via votre navigateur local.

---

## 🏪 Proxy local compatible OpenAI : un seul abonnement, tous les outils

**[PR #25969](https://github.com/NousResearch/hermes-agent/pull/25969)** introduit `hermes proxy` — un serveur HTTP local qui parle le format de l'API OpenAI mais qui est alimenté par le fournisseur OAuth auquel vous êtes connecté. C'est trompeusement puissant :

| Abonnement | Devient disponible pour | Sans |
|-------------|---------------------|---------|
| Claude Pro | Codex CLI, Aider, Cline, Continue | Une clé API Anthropic |
| ChatGPT Pro | Tout outil compatible OpenAI | Une clé API OpenAI |
| SuperGrok | Tout outil compatible OpenAI | Une clé API xAI |

Exécutez `hermes proxy`, obtenez un point de terminaison `http://localhost:port`, et pointez tout outil qui attend une API compatible OpenAI vers lui. **Un seul abonnement, tous les outils** — aucune clé API supplémentaire requise. Cela transforme effectivement votre abonnement Hermes Agent en une passerelle API universelle pour tout l'écosystème des outils d'agents.

---

## 🐦 x_search : une recherche X (Twitter) de première classe

L'agent peut désormais rechercher directement sur X/Twitter — sans installation de compétence, sans câblage d'intégration personnalisé. **[PR #26763](https://github.com/NousResearch/hermes-agent/pull/26763)** ajoute `x_search` en tant qu'outil intégré conditionné avec deux modes d'authentification :

- **Connexion OAuth X** — utilisez votre session Twitter existante
- **Clé API** — authentification traditionnelle par jeton Bearer

Recherchez dans la timeline, trouvez des fils de discussion, faites apparaître des posts spécifiques — le tout depuis l'interface de chat. Pour les journalistes, les chercheurs et les analystes des médias sociaux qui utilisent Hermes Agent comme interface principale, cela élimine toute une catégorie de flux de travail manuel.

---

## 🏢 Microsoft Teams : de bout en bout

Hermes Agent parle désormais **Microsoft Teams** nativement. Il ne s'agit pas d'une intégration partielle — l'ensemble de la pile arrive ensemble :

1. **Authentification Microsoft Graph + base client** ([#21922](https://github.com/NousResearch/hermes-agent/pull/21922))
2. **Écouteur webhook** qui reçoit les événements Teams ([#21969](https://github.com/NousResearch/hermes-agent/pull/21969))
3. **Runtime de plugin pipeline** pour traiter les messages Teams ([#22007](https://github.com/NousResearch/hermes-agent/pull/22007))
4. **Livraison sortante** pour publier en réponse ([#22024](https://github.com/NousResearch/hermes-agent/pull/22024))

Connectez le bot une fois, puis discutez avec votre agent depuis n'importe quel canal Teams, DM ou groupe. C'est une avancée majeure pour l'adoption en entreprise — Microsoft Teams est le standard des entreprises, et maintenant Hermes Agent y réside en citoyen de première classe.

---

## 📦 Packaging PyPI : `pip install hermes-agent && hermes`

L'une des fonctionnalités les plus demandées est arrivée : **Hermes Agent est désormais un véritable package PyPI**. Plus besoin de cloner le dépôt ou d'exécuter des installateurs shell. Une seule commande `pip install hermes-agent` et vous voilà opérationnel. Le wheel est livré avec le bundle Ink TUI et le lanceur shell, de sorte que l'expérience interactive complète est disponible immédiatement. ([#26593](https://github.com/NousResearch/hermes-agent/pull/26593))

Cela s'accompagne d'une **vague d'allègement** complète ([#24220](https://github.com/NousResearch/hermes-agent/pull/24220), [#24515](https://github.com/NousResearch/hermes-agent/pull/24515)) :

- Les backends lourds (SDK Slack/Matrix/Feishu, génération d'images, fournisseurs voix/TTS) sont désormais **installés paresseusement à la première utilisation**
- Les extras `[all]` suppriment tout ce qui est couvert par les dépendances paresseuses
- **Repli d'installation par paliers** lorsque le wheel ne correspond pas à votre plateforme
- **Vérificateur d'avis de sécurité de la chaîne d'approvisionnement** analyse chaque installation à la recherche de versions non sécurisées

L'effet net : des installations plus rapides, un encombrement disque réduit, moins de vulnérabilités transitives et une barrière à l'entrée considérablement abaissée.

---

## ⚡ Performance : cache, démarrage à froid et navigateur

### Cache de prompt Claude inter-sessions d'une heure

**[PR #23828](https://github.com/NousResearch/hermes-agent/pull/23828)** apporte la mise en cache de prompt inter-sessions pour Claude (via Anthropic, OpenRouter ou le portail Nous). Le préfixe du prompt (prompt système, compétences, mémoire) est désormais mis en cache pendant **une heure entière entre les sessions**. Lancez une session `/new` et la première réponse revient plus rapidement et à moindre coût car le cache est encore chaud. La révision de mémoire en arrière-plan profite également du cache — pas de tours au prix plein. ([#25434](https://github.com/NousResearch/hermes-agent/pull/25434))

### Vague d'optimisation du démarrage à froid : ~19 secondes de gagnées au lancement de `hermes`

Une série d'optimisations coordonnées sur le chemin de lancement :

| Optimisation | Amélioration |
|-------------|-------------|
| Adaptateurs lourds différés à la première utilisation | Réduction majeure du temps d'importation |
| Catalogues de modèles depuis le cache disque en priorité | Élimine l'attente réseau |
| Vérifications doctor exécutées en parallèle | Sondes de connectivité concurrentes |
| `chat -q` saute la bannière de bienvenue | Prompt instantané |
| Écran Toutes les plateformes de `hermes tools` | **14s → moins de 1,5s** |

### Évaluations de console navigateur 180× plus rapides

**[PR #23226](https://github.com/NousResearch/hermes-agent/pull/23226)** achemine les évaluations de la console du navigateur via le WebSocket CDP persistant du superviseur au lieu de lancer une nouvelle session DevTools par appel. Ce qui prenait auparavant des secondes revient maintenant en millisecondes — les interactions réelles avec les pages semblent instantanées.

---

## 💬 Deux nouvelles plateformes : LINE + SimpleX Chat

Hermes Agent ajoute **deux nouvelles plateformes de messagerie**, portant le total à **22** :

- **LINE** ([#23197](https://github.com/NousResearch/hermes-agent/pull/23197)) — très populaire au Japon, en Corée et à Taïwan. Intégration native avec l'API de messagerie LINE.
- **SimpleX Chat** ([#26232](https://github.com/NousResearch/hermes-agent/pull/26232)) — le messager décentralisé axé sur la confidentialité sans identifiants d'utilisateur, sans serveur, sans annuaire.

Tous deux sont des plateformes de première classe complètes avec messagerie entrante et sortante.

---

## 🪟 Beta native Windows

**[PR #21561](https://github.com/NousResearch/hermes-agent/pull/21561)** amène Hermes Agent sur **Windows natif** — fonctionnant sur `cmd.exe` et PowerShell **sans WSL**. Un installateur PowerShell complet gère l'installation automatique de MinGit, la détection du stub Python du Microsoft Store et la gestion de Ctrl+C. Il reste des aspérités (c'est une bêta précoce), mais la boucle de base fonctionne de bout en bout sur une machine Windows propre.

---

## 🧠 Agent plus intelligent : diagnostics LSP, transfert de session et vérification de fichiers

Trois améliorations qui rendent l'agent considérablement plus fiable :

| Fonctionnalité | Ce qu'elle fait | PR |
|---------|-------------|-----|
| **Diagnostics sémantiques LSP** | Après chaque `write_file`/`patch`, exécute un véritable serveur de langage sur le fichier et fait remonter les erreurs (erreurs de type, symboles non définis, importations manquantes) | [#24168](https://github.com/NousResearch/hermes-agent/pull/24168) |
| **Transfert de session en direct `/handoff`** | Déplace la session active — chaque message, appel d'outil et contexte — vers un modèle/persona/profil différent en cours de conversation | [#23395](https://github.com/NousResearch/hermes-agent/pull/23395) |
| **Vérificateur de mutation de fichiers par tour** | Après chaque tour qui a écrit/modifié des fichiers, un pied de page résume exactement ce qui a changé sur le disque — chemins, nombre de lignes, deltas | [#24498](https://github.com/NousResearch/hermes-agent/pull/24498) |

Les diagnostics LSP sont une amélioration particulièrement importante. La v0.13.0 avait un linting basique pour Python/JSON/YAML/TOML ; la v0.14.0 passe à une **analyse sémantique réelle** — le même type de détection d'erreurs que votre IDE vous offre, désormais au sein de la boucle de l'agent.

---

## 🖥️ Utilisation de l'ordinateur pour les modèles non Anthropic

L'outil `computer_use` (souris + clavier contrôlés par l'agent pour les applications GUI) était auparavant verrouillé au SDK d'Anthropic. Le nouveau **backend cua-driver** ([#21967](https://github.com/NousResearch/hermes-agent/pull/21967)) fonctionne également avec des fournisseurs non Anthropic, avec des opérations sécurisées au niveau du focus et un rafraîchissement automatique sur `hermes update`. Désormais, tout modèle capable de vision peut piloter votre bureau.

---

## 🎥 Nouvelles capacités : génération vidéo, pixels de vision et recherche web

Un trio de nouvelles capacités complète la Foundation Release :

- **`video_generate` avec des backends enfichables** ([#25126](https://github.com/NousResearch/hermes-agent/pull/25126)) — un outil, n'importe quel modèle vidéo, avec une architecture de plugins pour les futurs fournisseurs
- **`vision_analyze` renvoie des pixels bruts** ([#22955](https://github.com/NousResearch/hermes-agent/pull/22955)) — les modèles capables de vision (GPT-5, Claude, Gemini, Grok-vision) reçoivent désormais de véritables pixels au lieu d'allers-retours de résumés textuels
- **Brave Search (niveau gratuit) + DuckDuckGo** ([#21337](https://github.com/NousResearch/hermes-agent/pull/21337)) — deux nouveaux backends de recherche web gratuits rejoignent Tavily, SearXNG et Exa

---

## 🔒 Sécurité : blocage de force brute sudo, assainissement des erreurs d'outils, et plus encore

Trois améliorations de sécurité significatives :

1. **Blocage de force brute sudo** — la porte d'approbation bloque désormais les tentatives de force brute `sudo -S` et classe les invocations sudo alimentées par stdin/sans askpass comme DANGEREUSES ([#23736](https://github.com/NousResearch/hermes-agent/pull/23736))
2. **Trois contournements de commandes dangereuses fermés** — inspirés par le travail de détection de commandes de Claude Code ([#26829](https://github.com/NousResearch/hermes-agent/pull/26829))
3. **Assainissement des erreurs d'outils** — les chaînes d'erreur sont assainies avant d'être réinjectées dans le contexte du modèle, empêchant les fichiers malveillants ou les services distants de faire passer des instructions via la sortie d'erreur ([#26823](https://github.com/NousResearch/hermes-agent/pull/26823))

---

## 📊 Résumé de la croissance (7 mai → 18 mai)

| Métrique | 7 mai (v0.13.0) | 18 mai (v0.14.0) | Changement |
|--------|-----------------|------------------|--------|
| **Étoiles GitHub** | ~138 000 | **155 609** | **+17 609** |
| **Forks** | ~22 000 | **24 980** | **+2 980** |
| **Tickets fermés** | — | **545** (12 P0, 50 P1) | — |
| **PRs fusionnées** | — | **633** | — |
| **Contributeurs** | — | **215** | — |
| **Plateformes de messagerie** | 19 | **22** | +3 |
| **Fournisseurs d'inférence** | ~20 | **~25** | +NovitaAI, Grok OAuth |

---

## 🔭 Et ensuite ?

Le nom de Foundation Release est approprié : la v0.14.0 construit l'infrastructure sur laquelle la prochaine vague de fonctionnalités reposera. Avec le packaging PyPI, un proxy local compatible OpenAI, le support natif de Windows et 22 plateformes de messagerie, Hermes Agent possède **la plus large surface d'exposition de tous les runtimes d'agents open source**.

Domaines à surveiller pour la v0.15.0 :

1. **Runtime Frontdesk** — l'architecture de worker en arrière-plan toujours disponible (toujours en PR)
2. **Maturité Kanban** — primitives de suspension/reprise pour le cycle de vie des tâches de longue durée
3. **Expansion de Cron** — raisonnement par tâche, recherche par nom, portes conditionnelles
4. **Plus de fournisseurs** — l'ajout de NovitaAI suggère une croissance de la longue traîne du support des fournisseurs
5. **160K étoiles** — à la croissance actuelle (~1 700/jour), ce jalon sera atteint en quelques jours

Pour les développeurs qui construisent des systèmes agentiques : la Foundation Release est la version que vous attendiez pour intégrer Hermes Agent dans votre pile — elle s'installe proprement, se connecte partout et fonctionne sur tous les principaux systèmes d'exploitation.

---

*Couverture basée sur la version Hermes Agent v0.14.0 (v2026.5.16). Comptage des étoiles au 18 mai 2026 à 09:00 UTC. Journal des modifications complet : [v2026.5.7...v2026.5.16](https://github.com/NousResearch/hermes-agent/compare/v2026.5.7...v2026.5.16)*