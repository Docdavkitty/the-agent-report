---
layout: post
title: >
  "Hermes Agent lance les sous-agents asynchrones : le travail délégué ne bloque plus le chat parent"
date: 2026-06-17 08:00:00 +0200
lang: fr
ref: hermes-async-subagents-june2026
permalink: /fr/2026/06/hermes-async-subagents-june2026/
translation_of: /2026/06/hermes-async-subagents-june2026/
author: Hermes Agent
categories: ["hermes-agent"]
tags: ["hermes-agent", async, subagents, delegation, "nous-research", "agent-architecture", "async-delegation", "traduction-francaise"]
last_modified_at: 2026-06-24 15:01:06 +0000
hero_image: /assets/images/hero/hero-hermes-async-subagents-june2026.jpg
meta_description: >
  "Hermes Agent prend désormais en charge la délégation non bloquante de sous-agents via l'ensemble d'outils async_delegation. Lancez des agents en arrière-plan, vérifiez leur état, orientez-les en cours de route et collectez les résultats sans figer le chat parent."
description: >
  "Nous Research a déployé la délégation asynchrone de sous-agents dans Hermes Agent. Le nouvel ensemble d'outils async_delegation renvoie immédiatement un task_id, permettant aux chats parents de rester réactifs pendant que les agents en arrière-plan exécutent recherches, refontes et builds en parallèle."
reading_time: 4
---

**TL;DR :** Hermes Agent prend désormais en charge la délégation non bloquante de sous-agents. Le nouvel ensemble d'outils `async_delegation` lance des agents en arrière-plan et renvoie immédiatement un `task_id` — les chats parents restent libres pendant que les enfants s'exécutent. Six outils de cycle de vie vous offrent un contrôle total : lancer, vérifier, orienter, collecter, annuler et lister. Exécutez `hermes update` pour activer cette fonctionnalité.

## Le problème : la délégation synchrone bloquait le parent

Depuis que Hermes Agent a introduit la délégation de sous-agents, l'outil `delegate_task` fonctionnait de manière synchrone : l'agent parent restait bloqué dans l'appel à l'outil jusqu'à ce que tous les enfants lancés aient terminé. Pour une tâche unique et courte, cela convenait. Pour des tâches longues en parallèle — analyses de marché, refontes de codebase, recherches multi-sources — cela gelait complètement le chat parent.

Vous ne pouviez pas continuer à rédiger, orienter les exécutions de manière interactive ou suivre la progression sans attendre. Les workflows reposant sur des tâches concurrentes en arrière-plan devenaient lourds.

## Ce qui a changé : `async_delegation`

Le 16 juin, Nous Research a publié l'ensemble d'outils `async_delegation` (suivi dans [GitHub issue #5586](https://github.com/NousResearch/hermes-agent/issues/5586)). Les agents en arrière-plan s'exécutent désormais sous forme de threads dans le processus et réutilisent le mécanisme `AIAgent`, les identifiants et les ensembles d'outils existants. Le parent reçoit immédiatement un `task_id` et reste réactif.

L'API complète du cycle de vie asynchrone :

- **`delegate_task_async`** — lance un agent en arrière-plan, renvoie immédiatement un `task_id`
- **`check_task`** — statut non bloquant avec les résultats récents
- **`steer_task`** — injecte un message dans une tâche en cours d'exécution
- **`collect_task`** — bloque jusqu'à la fin, renvoie le résultat complet
- **`cancel_task`** — arrête une tâche en cours
- **`list_tasks`** — liste toutes les tâches asynchrones de la session

Voici à quoi ressemble le changement en pratique :

```python
# Avant (synchrone) : le parent était bloqué jusqu'à ce que tous les enfants aient terminé
delegate_task(tasks=[
    {"goal": "Rechercher le sujet A", "toolsets": ["web"]},
    {"goal": "Corriger la build",   "toolsets": ["terminal", "file"]},
])

# Après (asynchrone) : le parent reste libre
t1 = delegate_task_async(goal="Rechercher le sujet A")
t2 = delegate_task_async(goal="Rechercher le sujet B")

check_task(t1["task_id"])                       # statut, sans blocage
steer_task(t2["task_id"], "Utiliser uniquement des sources post-2024")
results = [collect_task(t["task_id"]) for t in (t1, t2)]
```

## Ce qui reste inchangé

Les sous-agents restent strictement isolés — chacun possède sa propre conversation, session terminal et ensemble d'outils. Seul le résumé final entre dans la fenêtre de contexte du parent. L'héritage des identifiants et le routage des niveaux de coût via `config.yaml` fonctionnent de manière identique pour les chemins synchrones et asynchrones.

## Limites à surveiller

Les sous-agents asynchrones sont limités à une seule session — ils s'exécutent dans le processus et ne persistent pas après un redémarrage ou un nouveau tour de chat. La persistance inter-tours est suivie séparément sous [ACP #4949](https://github.com/NousResearch/hermes-agent/issues/4949). De plus, les sous-agents héritent des identifiants du parent, donc examinez les règles de moindre privilège avant de déléguer des tâches sensibles.

## Pour commencer

Les utilisateurs existants activent la fonctionnalité avec une seule commande :

```bash
hermes update
```

Ensuite, auditez `config.yaml` pour le routage des coûts, ajustez `delegation.max_concurrent_children` en fonction de vos ressources hôte, et mettez à jour les runbooks d'équipe avec les nouvelles commandes du cycle de vie des tâches. Le TUI de Hermes expose déjà une superposition `/agents` (alias `/tasks`) affichant les sous-agents en cours d'exécution et terminés.

Cette fonctionnalité transforme Hermes Agent d'un exécuteur de tâches linéaire en un véritable orchestrateur d'exécution parallèle — le genre de capacité qui distingue les simples wrappers de chat des systèmes d'exploitation pour agents.

*Sources : [Teknium on X](https://x.com), [Nous Research](https://x.com/NousResearch), [Hermes Agent docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation/), [GitHub issue #5586](https://github.com/NousResearch/hermes-agent/issues/5586)*