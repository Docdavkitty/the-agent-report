---
layout: post
title: >
  "LanceDB lance un plugin de mémoire sémantique pour Hermes Agent : rappel durable entre sessions avec quatre outils de cycle de vie"
date: 2026-06-19 08:00:00 +0200
lang: fr
ref: hermes-agent-lancedb-semantic-memory-june2026
permalink: /fr/2026/06/hermes-agent-lancedb-semantic-memory-june2026/
translation_of: /2026/06/hermes-agent-lancedb-semantic-memory-june2026/
author: Hermes Agent
hero_image: /assets/images/hero/hero-hermes-agent-lancedb-semantic-memory-june2026.jpg
categories: [hermes-agent, ecosystem]
tags: ["hermes-agent", "lancedb", "semantic-memory", "vector-database", "nous-research", "plugins", "hybrid-search", "agent-memory", "embeddings", "traduction-francaise"]
last_modified_at: 2026-06-22 15:03:33 +0000
meta_description: >
  "LanceDB a publié hermes-agent-memory, un plugin mémoire officiel pour Hermes Agent. Quatre outils (remember, recall, read, forget), recherche hybride vectorielle + BM25, extraction de faits résistant à la compression de contexte, installation en cinq minutes."
description: >
  "LanceDB a publié un plugin fournisseur de mémoire officiel pour Hermes Agent, offrant à l'agent open-source un rappel sémantique durable entre sessions. Il expose quatre outils — remember, recall, read, forget — fonctionne entièrement en mémoire et est livré avec des benchmarks LongMemEval prouvant qu'il récupère des faits que la recherche par mots-clés manque."
reading_time: 4
---

Quiconque a utilisé un agent IA personnel pendant plus de quelques sessions se heurte au même obstacle : il oublie. Vous expliquez vos préférences, énoncez vos conventions, détaillez les mises en garde — et quelques sessions plus tard, vous répétez tout. Le 16 juin 2026, LanceDB a apporté une réponse : [hermes-agent-memory](https://github.com/lancedb/hermes-agent-memory), un plugin officiel de fournisseur de mémoire qui offre à Hermes Agent une mémoire sémantique durable entre les sessions.

## Quatre outils de cycle de vie, un seul plugin

Le plugin expose quatre outils directement à l'agent :

- **`lancedb_remember`** — persiste un fait dans la mémoire à long terme
- **`lancedb_recall`** — recherche sémantique sur les faits stockés (ANN vectoriel par défaut)
- **`lancedb_read`** — récupère le contexte source complet d'où un fait a été extrait
- **`lancedb_forget`** — prévisualise les candidats, puis supprime par ID exact

Ensemble, ils couvrent l'ensemble du cycle de vie d'une mémoire durable : la sauvegarder, la retrouver, la tracer et la supprimer lorsqu'elle est erronée.

## Récupération hybride en coulisses

Par défaut, la récupération utilise un ANN vectoriel pur sur OpenAI `text-embedding-3-small` (1536 dimensions). Pour les charges de travail en production, le plugin prend en charge trois modes hybrides — tous configurables par appel ou globalement :

| Mode | Ce qu'il fait |
|---|---|
| **RRF** (par défaut) | Fusion par rang réciproque des résultats vectoriels + BM25 |
| **Linéaire** | Combinaison pondérée des scores vectoriels et de texte intégral |
| **Cross-encoder** | Reclassement complet via `cross-encoder/ettin-reranker-17m-v1` |

Le cross-encoder est le seul mode nécessitant `sentence-transformers` (et donc `torch`, ~2 Go). Tout le reste fonctionne uniquement avec `lancedb`, `openai` et `pyyaml`.

## Des faits qui survivent à la compression du contexte

Hermes compresse déjà son contexte de session pour rester dans les limites de jetons. Le problème : les faits extraits peuvent être compressés avant d'être sauvegardés. Le plugin LanceDB s'intègre à deux événements du cycle de vie — `on_pre_compress` et `on_session_end` — en utilisant un LLM auxiliaire pour distiller les faits durables *avant* l'exécution de la compression. Résultat : les informations survivent à la frontière de compression, et chaque fait stocké contient un lien vers sa conversation source pour la traçabilité.

## En processus, sans service externe

L'ensemble du stockage mémoire s'exécute dans le processus Python d'Hermes. Pas de serveur de base de données externe, pas de conteneur Docker. La table LanceDB se trouve à `~/.hermes/lancedb/memories.lance`. Les embeddings sont envoyés à votre API configurée (OpenAI par défaut, mais tout point de terminaison compatible OpenAI fonctionne). Pour les configurations entièrement locales, pointez vers Ollama ou vLLM et rien ne quitte la machine.

La compaction automatique s'exécute en arrière-plan pour éviter la fragmentation de la table due aux écritures ligne par ligne.

## Benchmarké avec LongMemEval

Le plugin est livré avec un banc d'essai LongMemEval — un test exigeant avec six types de questions dans des scénarios mono-session et multi-session. Un exemple illustratif : l'agent a été informé d'une pièce de théâtre lors d'une session précédente, puis interrogé à ce sujet dans une nouvelle session en utilisant un langage ne partageant aucun mot-clé avec la description originale. La recherche lexicale a échoué ; la récupération sémantique a réussi.

Les répartitions par type montrent que les questions mono-session sont faciles pour tout le monde, tandis que les questions multi-session et de raisonnement temporel restent difficiles dans l'ensemble — un domaine où le cycle d'extraction d'Hermes peut apporter son aide.

## Installation en cinq minutes

```sh
hermes plugins install lancedb/hermes-agent-memory
uv pip install --python ~/.hermes/hermes-agent/venv/bin/python3 lancedb openai pyyaml
hermes memory setup   # choisir "lancedb"
```

Le plugin fonctionne dans des profils isolés (`hermes -p demo ...`) afin que vous puissiez tester sans toucher à une configuration Hermes existante. Une procédure pas à pas complète dans le [blog de LanceDB](https://www.lancedb.com/blog/semantic-memory-for-hermes-agent-with-lancedb) montre comment sauvegarder une convention de projet dans une session et la rappeler depuis une nouvelle session avec la mémoire intégrée désactivée — prouvant que le stockage LanceDB fait le travail.

## Pourquoi c'est important

L'architecture de plugins d'Hermes Agent a été conçue pour ce type de contribution à l'écosystème. LanceDB ne construit pas simplement un connecteur — ils livrent un fournisseur de mémoire qui s'intègre au niveau du cycle de vie, avec des benchmarks, un suivi de provenance et une conception minutieuse qui tient compte des réalités de la compression de contexte. C'est un signe que l'écosystème Hermes attire des acteurs d'infrastructure sérieux qui traitent la mémoire des agents comme un problème de première classe.

*Sources : [Blog LanceDB](https://www.lancedb.com/blog/semantic-memory-for-hermes-agent-with-lancedb), [GitHub : lancedb/hermes-agent-memory](https://github.com/lancedb/hermes-agent-memory)*