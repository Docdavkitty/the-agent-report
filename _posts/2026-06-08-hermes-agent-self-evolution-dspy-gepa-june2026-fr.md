---
layout: post
title: >
  "Auto-évolution de l'agent Hermes : Nous Research déploie l'optimisation génétique des prompts avec DSPy + GEPA"
date: 2026-06-08 10:00:00 +0200
lang: fr
ref: hermes-agent-self-evolution-dspy-gepa-june2026
permalink: /fr/2026/06/hermes-agent-self-evolution-dspy-gepa-june2026/
translation_of: /2026/06/hermes-agent-self-evolution-dspy-gepa-june2026/
author: The Agent Report
categories: ["hermes-agent"]
tags: ["hermes-agent", "nous-research", "open-source", "self-evolution", dspy, gepa, "genetic-algorithms", "prompt-optimization", "autonomous-agents", "traduction-francaise"]
last_modified_at: 2026-07-02 15:01:52 +0000
hero_image: /assets/images/hero/hero-hermes-agent-self-evolution-dspy-gepa-june2026.jpg
meta_description: >
  "Nous Research a open-sourcé hermes-agent-self-evolution, un framework utilisant DSPy + GEPA pour optimiser automatiquement les compétences, prompts et descriptions d'outils de l'agent Hermes via une recherche évolutive réflexive, sans GPU requis."
description: >
  "Le nouveau dépôt hermes-agent-self-evolution de Nous Research utilise DSPy et des algorithmes génétiques pour faire évoluer automatiquement les compétences, prompts et codes d'outils des agents. Voici son fonctionnement et son importance."
reading_time: 6
---

La boucle d'auto-amélioration de l'agent Hermes vient de gagner une nouvelle dimension. Le **6 juin 2026**, Nous Research a discrètement open-sourcé [`hermes-agent-self-evolution`](https://github.com/NousResearch/hermes-agent-self-evolution) — un dépôt séparé qui applique des **algorithmes génétiques** aux propres compétences, invites et descriptions d'outils de l'agent. Construit sur **DSPy** (le framework déclaratif de programmation LLM de Stanford) et **GEPA** (Genetic-Pareto Prompt Evolution, un article Oral de l'ICLR 2026), il lit les traces d'exécution pour comprendre *pourquoi* les échecs se produisent et propose des correctifs ciblés — pas de simples mutations aléatoires.

> Le Curateur existant élague les compétences inutilisées. L'auto-évolution *améliore* celles que vous conservez.

## Comment ça fonctionne : Lire, Muter, Évaluer, Sélectionner

Le pipeline d'optimisation suit un cycle en quatre étapes :

1. **Lire** la compétence, l'invite ou la description d'outil actuelle depuis le dépôt Hermes Agent
2. **Muter** celle-ci en variantes candidates en utilisant la recherche évolutive réflexive de GEPA — le moteur lit les traces d'exécution et propose des modifications chirurgicales, pas des réécritures aléatoires
3. **Évaluer** chaque candidate par rapport à une suite de tests, des contraintes de taille (compétences ≤15 Ko, descriptions d'outils ≤500 caractères) et des vérifications de dérive sémantique
4. **Sélectionner** la variante la plus performante et ouvrir une PR (Pull Request) contre `hermes-agent`

```text
Lire la compétence/invite/outil actuel ──► Optimiseur GEPA ◄── Traces d'exécution
                                               │
                                          Variantes candidates ──► Évaluation
                                               │
                                       Passerelles de contraintes (tests, taille, sémantique)
                                               │
                                       Meilleure variante ──► PR contre hermes-agent
```

L'ensemble du pipeline coûte **2 à 10 $ par cycle d'optimisation** et ne nécessite **aucun entraînement GPU** — il fonctionne entièrement via des appels API à un LLM qui évalue et mute le texte.

## Cinq phases d'évolution

Nous Research a défini une feuille de route en cinq phases dans [`PLAN.md`](https://github.com/NousResearch/hermes-agent-self-evolution/blob/main/PLAN.md) :

| Phase | Cible | Moteur | Statut |
|-------|-------|--------|--------|
| **Phase 1** | Fichiers de compétences (`SKILL.md`) | DSPy + GEPA | ✅ Implémentée |
| **Phase 2** | Descriptions d'outils | DSPy + GEPA | 🔲 Planifiée |
| **Phase 3** | Sections d'invite système | DSPy + GEPA | 🔲 Planifiée |
| **Phase 4** | Code d'implémentation des outils | Évoluteur Darwinien | 🔲 Planifiée |
| **Phase 5** | Boucle d'amélioration continue | Pipeline automatisé | 🔲 Planifiée |

La Phase 4 est particulièrement ambitieuse : l'[Évoluteur Darwinien](https://github.com/imbue-ai/darwinian_evolver) (AGPL v3, CLI externe) traite le code comme des "organismes basés sur Git", appliquant une pression évolutive aux implémentations d'outils elles-mêmes. Cela bouclerait la boucle de "l'agent écrit une compétence" à "l'agent fait évoluer le code derrière ses propres outils".

## Garde-fous : Pourquoi ce n'est pas un chaos non supervisé

Chaque variante évoluée doit passer cinq vérifications avant d'être acceptée :

1. **Suite de tests complète** — `pytest tests/ -q` doit réussir à 100 %
2. **Limites de taille** — compétences ≤15 Ko, descriptions d'outils ≤500 caractères
3. **Compatibilité du cache** — aucun changement en cours de conversation qui casserait la mise en cache
4. **Préservation sémantique** — ne doit pas dériver du but original
5. **Révision humaine via PR** — toutes les modifications sont proposées via pull request, **jamais** commitées directement

Le dépôt est explicite : *"Tous les changements évolués passent par une révision humaine et ne sont jamais appliqués directement."* C'est une optimisation évolutive avec un filet de sécurité — pas une boucle de rétroaction incontrôlée.

## Comment l'exécuter

Pointez l'outil d'évolution vers votre dépôt local Hermes Agent et choisissez votre source de données d'évaluation :

```bash
git clone https://github.com/NousResearch/hermes-agent-self-evolution.git
cd hermes-agent-self-evolution
pip install -e ".[dev]"
export HERMES_AGENT_REPO=~/.hermes/hermes-agent

# Faire évoluer une compétence avec des données d'évaluation synthétiques
python -m evolution.skills.evolve_skill \
    --skill github-code-review \
    --iterations 10 \
    --eval-source synthetic

# Ou utiliser l'historique de session réel de Claude Code, Copilot et Hermes
python -m evolution.skills.evolve_skill \
    --skill github-code-review \
    --iterations 10 \
    --eval-source sessiondb
```

La source `sessiondb` puise dans les traces d'exécution réelles de plusieurs agents de codage, fournissant à GEPA des données d'échec riches pour apprendre.

## Ce que cela signifie pour l'écosystème des agents

Le dépôt d'auto-évolution représente une **nouvelle couche dans la pile d'autonomie d'Hermes Agent** :

- **Création de compétences** — l'agent écrit des compétences à partir de l'expérience (intégré depuis la v0.2)
- **Le Curateur** — l'agent élague et note sa bibliothèque de compétences (depuis la v0.12, avril 2026)
- **Auto-évolution** — l'agent *améliore* ses compétences et ses invites grâce à l'optimisation génétique (nouveau)

Ensemble, ces trois couches forment un cycle de vie complet : **créer → maintenir → faire évoluer**. C'est la chose la plus proche que nous ayons vue d'un agent qui s'améliore véritablement plus il fonctionne longtemps — non pas simplement en accumulant plus de compétences, mais en affinant celles qu'il possède par rapport à des benchmarks mesurables.

Avec **3,9k étoiles** en quelques jours après sa sortie, la communauté est clairement attentive. Le dépôt est jeune — seulement 7 commits sur `main` — mais l'architecture est ambitieuse, les garde-fous sont solides, et la base DSPy + GEPA est soutenue par une recherche évaluée par les pairs.

> L'agent qui apprend de l'expérience peut désormais apprendre de ses propres erreurs — et les corriger automatiquement.