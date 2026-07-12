---
layout: post
title: >
  "Hermes Agent v0.15.0 'Velocity' + v0.15.1 Hotfix : run_agent.py -76%, Kanban comme plateforme, et 172K étoiles"
date: 2026-05-29 18:00:00 +0200
lang: fr
ref: hermes-agent-v0150-velocity-release-may28
permalink: /fr/2026/05/hermes-agent-v0150-velocity-release-may28/
translation_of: /2026/05/hermes-agent-v0150-velocity-release-may28/
author: The Agent Report
categories: ["hermes-agent"]
tags: ["hermes-agent", "nous-research", "open-source", v0.15.0, "velocity-release", "run-agent-refactor", "kanban-platform", "session-search", "promptware-defense", "bitwarden-secrets", "traduction-francaise"]
last_modified_at: 2026-07-12 15:01:21 +0000
hero_image: /assets/images/hero/hero-hermes-agent-v0150-velocity-release-may28.jpg
meta_description: >
  "Hermes Agent v0.15.0 'Velocity Release' apporte la plus grande refonte jamais vue (run_agent.py de 16K à 3,8K lignes), Kanban comme plateforme multi-agent, session_search 4 500× plus rapide, défense par promptware, Bitwarden Secrets Manager, et un correctif v0.15.1 le jour même."
description: >
  "Hermes Agent v0.15.0 'Velocity Release' livre la plus grande refonte jamais vue (run_agent.py de 16K à 3,8K lignes), Kanban comme plateforme multi-agent, session_search 4 500× plus rapide"
reading_time: 8
---

## 🔧 La grande refonte : `run_agent.py` passe de 16 000 à 3 800 lignes

L'exploit technique phare de v0.15.0 est le démantèlement chirurgical du fichier monolithique `run_agent.py` — le cœur de la boucle de conversation de l'agent Hermes. Il est passé de **16 083 lignes à 3 821 lignes (-76 %)**, la logique extraite étant redistribuée dans **14 modules cohérents** sous `agent/`.

Chaque extraction conserve un adaptateur léger pour la rétrocompatibilité, donc le comportement reste inchangé — mais la base de code est désormais nettement plus facile à naviguer, à tester et à enrichir. C'est le genre de remboursement de dette d'infrastructure qui génère des intérêts composés pour chaque version future.

> *Un fichier de 16 000 lignes, c'est un prototype de recherche. Une arborescence de modules de 3 800 lignes, c'est une plateforme de production.*

## 🧩 Kanban : d'une fonctionnalité à une plateforme multi-agents

Le système Kanban — introduit pour la première fois dans v0.13.0 « Tenacity » — a évolué d'un simple tableau de tâches vers une véritable **plateforme d'orchestration multi-agents**, fruit de **104 pull requests fusionnées**. Les nouvelles capacités incluent :

- **Décomposition automatique par l'orchestrateur** — le maître Kanban divise les objectifs complexes en sous-tâches automatiquement
- **Topologie en essaim** — les travailleurs s'organisent en graphes d'exécution tenant compte des dépendances
- **Tâches planifiées** — emplacements de tableau intégrés à cron qui se déclenchent sur une minuterie
- **Répertoire de travail par tâche** — chaque tâche dispose d'un dossier de travail isolé pour éviter les contaminations croisées
- **Surcharge de modèle par tâche** — assigner différents LLM à différents emplacements du tableau

Cela positionne Kanban comme un véritable concurrent des frameworks multi-agents dédiés comme AutoGen et CrewAI — mais fonctionnant au sein d'une seule installation `hermes`, sans infrastructure supplémentaire.

## ⚡ Performances au démarrage à froid : une seconde de gagnée

La vague d'amélioration des performances au démarrage à froid, initiée avec Foundation, se poursuit. v0.15.0 apporte :

- **Environ 1 seconde de moins au lancement de `hermes`** — le temps entre le boot et l'invite de commande est désormais nettement réduit
- **47 % d'appels de fonction en moins par conversation** — l'agent passe moins de temps sur le code standard et plus de temps à travailler
- **Victoire au benchmark `hermes --version`** — Hermes Agent bat désormais Codex CLI en tête-à-tête dans les benchmarks de démarrage à froid

Pour un runtime d'agent que les utilisateurs invoquent des dizaines de fois par jour, chaque seconde se traduit par un gain de productivité réel.

## 🔍 `session_search` : 4 500 fois plus rapide et gratuit

La compétence `session_search` — qui permet à Hermes de rechercher dans toutes vos conversations passées — a été reconstruite. Résultat : **des recherches 4 500 fois plus rapides** sans coût supplémentaire. Aucune base de données vectorielle, aucune API externe, aucun service d'embedding requis. Il s'agit d'une optimisation algorithmique pure sur le stockage local des conversations.

## 🛡️ Défense contre les promptwares : protection contre les attaques de type Brainworm

v0.15.0 intègre une **défense contre les promptwares** — une couche de sécurité conçue spécifiquement pour détecter et neutraliser les **attaques par injection de prompt de classe Brainworm**. À une époque où la lecture de contenu web non fiable par les agents est monnaie courante, il s'agit d'un ajout critique. Cette couche de défense :

- Analyse le contenu entrant à la recherche de motifs d'injection connus
- Isole le contenu suspect avant qu'il n'atteigne la boucle de l'agent
- Signale les tentatives d'attaque sans perturber le travail légitime

## 🔐 Gestionnaire de secrets Bitwarden : un seul jeton pour les gouverner tous

L'une des améliorations pratiques les plus notables : l'intégration du **gestionnaire de secrets Bitwarden**. Au lieu de gérer N clés API différentes pour N fournisseurs différents (Claude, Grok, OpenAI, etc.), vous configurez désormais un **unique jeton d'amorçage Bitwarden**, et Hermes récupère automatiquement les autres au moment de l'exécution. C'est un gain considérable pour :

- **La sécurité** — moins de jetons dans des fichiers de configuration en clair
- **La portabilité** — déplacer votre installation Hermes sans migrer les clés
- **Les déploiements en équipe** — partager les secrets via Bitwarden sans partager de fichiers

## 🎨 Ink TUI : orchestrateur multi-sessions

L'interface utilisateur terminal se dote de son propre **orchestrateur multi-sessions**, vous permettant de gérer plusieurs sessions Hermes depuis un seul tableau de bord TUI. Basculez entre les conversations, inspectez les tableaux Kanban et surveillez les tâches en arrière-plan — le tout sans quitter le terminal.

## 📦 Lots de compétences : une commande slash, un workflow

Un nouveau système de **lots de compétences** vous permet de regrouper plusieurs compétences derrière une seule commande slash. Au lieu de charger les compétences une par une, vous définissez un lot — `@deploy` pourrait charger `k8s-skills`, `docker-skills`, `monitoring-skills` et `rollback-skills` en une seule fois.

## 🌐 Extension de la plateforme

v0.15.0 étend la portée déjà impressionnante de la plateforme Hermes :

- **ntfy** devient la **23e plateforme de messagerie** — notifications push vers n'importe quel appareil via ntfy.sh
- **Deux nouveaux fournisseurs `image_gen`** : Krea 2 (Medium + Large) et un portage du plugin FAL
- **Catalogue MCP approuvé par Nous** avec un sélecteur interactif — découvrez et installez des serveurs MCP depuis Hermes
- **Compétence d'orchestration OpenHands** — exécutez des workflows OpenHands comme des compétences Hermes
- **Intégration approfondie avec xAI** — plugin de recherche Web via Grok, proxy amont `xai-oauth`, détection des modèles retirés le 15 mai avec `hermes migrate xai`, pauses naturelles de balises de parole TTS, garde-fou `base_url` leak, et guide d'exécution de style OpenAI pour Grok

## 🪲 Correctif v0.15.1 (29 mai) — Résolution du rechargement infini du tableau de bord

Publié quelques heures seulement après v0.15.0, **v0.15.1** est un **correctif** livré le jour même avec **28 commits, 21 PR fusionnées et 9 contributeurs**. Le correctif principal :

- **Boucle de rechargement 401 du tableau de bord corrigée** — En mode boucle locale (Docker, Hermes hébergé, nouvelles installations), la sonde d'identité du tableau de bord (`/api/auth/me`) renvoie 401 par conception, mais le garde-fou de rechargement des jetons obsolètes de v0.15.0 traitait chaque 401 comme une session tournée et déclenchait un rechargement complet de la page. Cela provoquait une boucle infinie — signalée dans les tickets [#34206](https://github.com/NousResearch/hermes-agent/issues/34206) et [#34202](https://github.com/NousResearch/hermes-agent/issues/34202), corrigée dans la PR [#30698](https://github.com/NousResearch/hermes-agent/pull/30698) par @austinpickett.

Correctifs supplémentaires dans v0.15.1 :

- **`--insecure` dans Docker comme option d'environnement explicite** — n'est plus dérivé de l'hôte de liaison
- Gestion améliorée du signal SIGTERM pour les travailleurs Kanban
- Unification du sélecteur `/model` entre l'interface utilisateur et la CLI
- Contournement de session `/yolo` pour les utilisateurs avancés
- Le catalogue complet de **19 932 entrées `skills.sh`** se charge désormais correctement
- Restauration de la livraison des médias `.md` dans les conversations
- **Sécurité de descente progressive des sondes** de la passerelle — dégradation gracieuse en cas d'échec en amont
- **Transmission de la censure des URL web** corrigée pour le mode de navigation privée
- Les travailleurs Kanban peuvent désormais voir les images jointes
- Observation rétrospective définie comme mode comportemental par défaut
- Résolution du **chemin des commandes nues** du serveur MCP sur les systèmes avec des chemins personnalisés
- **Corrections du cache de construction PR arm64** pour les contributeurs Apple Silicon et ARM Linux

## 📊 La trajectoire de croissance

<div class="highlight-box">
<p><strong>172 224 étoiles GitHub · 28 932 forks · 14 855 tickets ouverts</strong></p>
<p>Depuis la version Foundation (16 mai) : +17K étoiles (+11 %) en 13 jours. Le projet est désormais le runtime d'agent IA le plus étoilé sur GitHub, avec une large avance, et la vélocité des contributions ne montre aucun signe de ralentissement.</p>
</div>

## En résumé

Hermes Agent v0.15.0 « Velocity » n'est pas une simple version de fonctionnalités — c'est un **investissement fondamental dans la rapidité et la maintenabilité**. La seule refonte de `run_agent.py` portera ses fruits pour chaque version à venir. La maturation de la plateforme Kanban, la réécriture de `session_search`, la couche de défense contre les promptwares et l'intégration de Bitwarden créent ensemble un runtime plus rapide, plus sûr et plus pratique pour une utilisation quotidienne en production.

Le correctif v0.15.1 livré le jour même démontre la maturité opérationnelle du projet — corriger un bug critique en quelques heures après une version majeure, avec une communication claire et des journaux de modifications détaillés. C'est la marque d'un projet qui prend ses utilisateurs au sérieux.

Avec **172K étoiles**, **28,9K forks** et un **cycle de version impliquant 321 contributeurs**, Hermes Agent n'est pas seulement le runtime d'agent open source à la croissance la plus rapide — il devient le choix par défaut pour les développeurs qui veulent un agent capable de livrer du travail concret, à une vitesse réelle.

*Restez à l'écoute pour notre prochaine analyse approfondie — la version Velocity a déjà généré plus de 200 nouveaux tickets ouverts, et le sprint communautaire ne montre aucun signe d'essoufflement.*