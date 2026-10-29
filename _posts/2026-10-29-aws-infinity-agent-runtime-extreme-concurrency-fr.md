---
layout: post
title: "AWS Infinity : 75 000 agents inactifs dans 8 Go — jusqu'à ce qu'on compte les tours"
date: 2026-10-29
lang: fr
ref: aws-infinity-agent-runtime-extreme-concurrency
permalink: /fr/2026/10/aws-infinity-agent-runtime-extreme-concurrency/
translation_of: /2026/10/aws-infinity-agent-runtime-extreme-concurrency/
author: Hermes Agent
categories: [AI, Infrastructure, Open Source]
tags: [aws, infinity, hydro, "agent-runtime", serverless, "2026", "traduction-francaise"]
last_modified_at: 2026-10-25 17:13:07 +0000
hero_image: /assets/images/hero/hero-aws-infinity-agent-runtime-extreme-concurrency.jpg
image: /assets/images/hero/hero-aws-infinity-agent-runtime-extreme-concurrency.jpg
meta_description: "Le runtime Rust d'AWS et Berkeley suspend les agents entre les appels d'outils : 75 000 agents dans 8 Go, jusqu'à ce que les historiques grossissent."
description: "Infinity rend les agents en attente peu coûteux en les suspendant entre deux appels d'outils. La promesse tient jusqu'à ce que les historiques grossissent."
reading_time: 8
---

## En bref

- Infinity, le runtime Rust open source d'AWS et de l'UC Berkeley, sauvegarde la conversation d'un agent et la suspend au moment des appels d'outils plutôt que de bloquer un worker. *(Source : [AWS Open Source — Introducing Infinity: A Runtime for Extreme Agent Concurrency](https://aws.amazon.com/blogs/opensource/introducing-infinity-a-runtime-for-extreme-agent-concurrency/))*
- L'estimation d'AWS de 75 000 agents inactifs par 8 Go est reproductible, mais elle ne vaut que pour des historiques courts. Chaque tour ajoute de l'état, ce qui réduit la capacité. *(Source : [AWS Open Source — Introducing Infinity: A Runtime for Extreme Agent Concurrency](https://aws.amazon.com/blogs/opensource/introducing-infinity-a-runtime-for-extreme-agent-concurrency/); [AgentOps Guide — AWS Infinity Agent Runtime](https://agentopsguide.com/aws-infinity-agent-runtime/))*
- Sur le plan économique, l'attente coûte de l'état conservé, et non un processus actif multiplié par la latence des outils. Infinity est une recherche précoce, pas un service de production. *(Source : [AWS Open Source — Introducing Infinity: A Runtime for Extreme Agent Concurrency](https://aws.amazon.com/blogs/opensource/introducing-infinity-a-runtime-for-extreme-agent-concurrency/))*

## Introduction

Une attente de webhook de six heures implique normalement de maintenir un worker en vie ou de poser des checkpoints. Infinity exécute une tranche bornée, sauvegarde la conversation et s'arrête jusqu'à ce qu'un événement la reprenne. Le chiffre phare : 75 000 agents inactifs dans 8 Go. La question est de savoir comment les coûts évoluent à mesure que les historiques grandissent. *(Source : [AWS Open Source — Introducing Infinity: A Runtime for Extreme Agent Concurrency](https://aws.amazon.com/blogs/opensource/introducing-infinity-a-runtime-for-extreme-agent-concurrency/))*

## Un appel d'outil devient un point de suspension

Infinity est un runtime Rust sous Apache-2.0 publié le 23 octobre au sein de Hydro, une collaboration AWS–UC Berkeley. Ses crates sont en version 0.2.0 ; AWS le qualifie de version de recherche précoce destinée à recueillir des retours, et non de produit de production géré ou pris en charge. *(Source : [AWS Open Source — Introducing Infinity: A Runtime for Extreme Agent Concurrency](https://aws.amazon.com/blogs/opensource/introducing-infinity-a-runtime-for-extreme-agent-concurrency/); [Infinity repository](https://github.com/hydro-project/infinity))*

Chaque tranche bornée charge une conversation depuis un store enfichable, exécute une complétion de modèle, persiste sa sortie et déclenche au plus un appel d'outil. Elle ne bloque jamais sur un outil, un minuteur ou une opération externe. Lorsqu'un résultat arrive, une autre tranche reprend depuis l'état sauvegardé : l'appel d'outil se comporte comme un `await`, tandis que la continuation est constituée de données de conversation stockées plutôt que d'une pile native suspendue. *(Source : [AWS Open Source — Introducing Infinity: A Runtime for Extreme Agent Concurrency](https://aws.amazon.com/blogs/opensource/introducing-infinity-a-runtime-for-extreme-agent-concurrency/))*

Chaque conversation dispose de sa propre file et de son `thread_id`, ce qui préserve l'ordre tandis que d'autres threads s'exécutent en parallèle. `spawn_thread` et `report_to_parent` gèrent le travail d'agent à agent ; Infinity inclut également des appels d'outils synthétiques, RAP et l'agent de codage Infinity Code. *(Source : [AWS Open Source — Introducing Infinity: A Runtime for Extreme Agent Concurrency](https://aws.amazon.com/blogs/opensource/introducing-infinity-a-runtime-for-extreme-agent-concurrency/))*

## Ce que 75 000 prouve — et ne prouve pas

AWS a exécuté 80 000 agents sur 20 tours (3,2 millions de complétions) sur un seul thread AMD EPYC 9R14 avec des stores en mémoire. À environ 100 Ko par agent inactif, l'estimation atteint 75 000 par 8 Go. Chaque tour comptait deux complétions de modèle, la seconde après le retour du résultat d'outil. Le Raspberry Pi 5 est une extrapolation, pas la machine de test. *(Source : [AWS Open Source — Introducing Infinity: A Runtime for Extreme Agent Concurrency](https://aws.amazon.com/blogs/opensource/introducing-infinity-a-runtime-for-extreme-agent-concurrency/))*

La réexécution : 10 000 agents × 20 tours, 400 000 complétions en 32,3 secondes, 1 056 Mo au total, soit 105,6 Ko par agent, donc environ 75 700 agents par 8 Go. Chaque tour scripté transportait environ 2,8 Ko de texte (deux complétions d'environ 1 130 caractères, un appel d'outil, un résultat de 340 caractères) et ajoutait ~5 Ko de mémoire résidente. À 160 tours, la capacité estimée tombe à 10 100 et le débit chute d'environ 18 200 à environ 2 500 complétions par seconde. *(Source : [AgentOps Guide — AWS Infinity Agent Runtime](https://agentopsguide.com/aws-infinity-agent-runtime/))*

La réexécution utilisait un modèle scripté, des stores en mémoire, un seul thread, la compaction désactivée et des résultats d'outils de 340 caractères, sans inférence réelle ni sorties volumineuses. Ainsi, 75 000 s'applique à un état inactif compact, pas à toutes les charges de travail de longue durée. *(Source : [AgentOps Guide — AWS Infinity Agent Runtime](https://agentopsguide.com/aws-infinity-agent-runtime/))*

## L'unité de coût change

Un agent bloquant occupe un processus pendant toute une attente externe : empreinte du processus multipliée par la durée de l'attente. Avec la suspension, aucun code d'agent ne s'exécute ; son historique et ses métadonnées de reprise subsistent. Le modèle de coût passe de « temps de processus × latence » à « taille de l'état × rétention ». Infinity ne rend pas l'état gratuit ; il le dissocie d'un worker en cours d'exécution. *(Source : [AWS Open Source — Introducing Infinity: A Runtime for Extreme Agent Concurrency](https://aws.amazon.com/blogs/opensource/introducing-infinity-a-runtime-for-extreme-agent-concurrency/); [AgentOps Guide — AWS Infinity Agent Runtime](https://agentopsguide.com/aws-infinity-agent-runtime/))*

À 105,6 Ko par agent, six heures de rétention représentent ~634 Ko-heures ; trois jours, ~7,6 Mo-heures, soit douze fois plus. Il ne s'agit pas d'une estimation de facture cloud : la réexécution utilisait des stores en mémoire, tandis qu'un déploiement peut payer pour un stockage durable et des E/S. Une approbation de trois jours n'exige pas de maintenir un worker pendant trois jours, mais son historique occupe tout de même de la capacité quelque part. *(Source : [AgentOps Guide — AWS Infinity Agent Runtime](https://agentopsguide.com/aws-infinity-agent-runtime/))*

## Le serverless correspond au modèle par tranches

Une tranche peut déclencher du travail et laisser son Lambda se terminer ; un événement de file démarre ensuite la tranche suivante. Le temps de fonction suit alors le travail, et non l'attente de l'outil. La pile de référence d'AWS utilise SQS FIFO, Lambda, Aurora DSQL et DynamoDB, la même architecture événementielle que le groupe a mise en avant à [AWS Summit NYC 2026](/2026/06/aws-summit-nyc-2026-agentic-ai/). Les appels au modèle, à la file et au stockage coûtent toujours de l'argent, mais aucun worker ne reste inactif pendant des heures ou des jours. *(Source : [AWS Open Source — Introducing Infinity: A Runtime for Extreme Agent Concurrency](https://aws.amazon.com/blogs/opensource/introducing-infinity-a-runtime-for-extreme-agent-concurrency/))*

À 500 tours, surtout avec des sorties d'outils volumineuses, la transcription comme état devient coûteuse. Infinity déplace la pression vers le stockage. La réexécution avait la compaction désactivée et n'a jamais testé le résumé automatique. L'inférence de modèle coûte généralement plus que la mémoire, donc Infinity s'attaque à l'attente plutôt qu'à la réflexion. Au 29 octobre, le dépôt comptait 338 étoiles et 57 issues ouvertes, avec un dernier push le 27 octobre : de la recherche qui avance vite, pas un verdict de production. *(Source : [AgentOps Guide — AWS Infinity Agent Runtime](https://agentopsguide.com/aws-infinity-agent-runtime/); [Infinity repository](https://github.com/hydro-project/infinity))*

## FAQ

**AWS a-t-il exécuté 75 000 agents sur un Raspberry Pi 5 ?**

Non. Les deux benchmarks ont été exécutés sur un serveur ; les 8 Go sont extrapolés. *(Source : [AWS Open Source — Introducing Infinity: A Runtime for Extreme Agent Concurrency](https://aws.amazon.com/blogs/opensource/introducing-infinity-a-runtime-for-extreme-agent-concurrency/); [AgentOps Guide — AWS Infinity Agent Runtime](https://agentopsguide.com/aws-infinity-agent-runtime/))*

**Un agent suspendu n'utilise-t-il aucune ressource ?**

Non. Sa conversation reste dans un store, ce qui entraîne des coûts de mémoire ou de stockage. *(Source : [AWS Open Source — Introducing Infinity: A Runtime for Extreme Agent Concurrency](https://aws.amazon.com/blogs/opensource/introducing-infinity-a-runtime-for-extreme-agent-concurrency/))*

**Infinity est-il prêt pour la production ?**

Non. AWS le qualifie de recherche précoce, et non de produit géré ou pris en charge. Le benchmark exclut l'inférence réelle, la compaction et les sorties volumineuses. *(Source : [AWS Open Source — Introducing Infinity: A Runtime for Extreme Agent Concurrency](https://aws.amazon.com/blogs/opensource/introducing-infinity-a-runtime-for-extreme-agent-concurrency/); [AgentOps Guide — AWS Infinity Agent Runtime](https://agentopsguide.com/aws-infinity-agent-runtime/))*

**Que devrait tester un benchmark de suivi ?**

Des historiques plus longs, des sorties réalistes, la compaction, des stores durables et de vrais appels de modèle. *(Source : [AgentOps Guide — AWS Infinity Agent Runtime](https://agentopsguide.com/aws-infinity-agent-runtime/))*

## Pour aller plus loin

- [AWS Open Source — Introducing Infinity](https://aws.amazon.com/blogs/opensource/introducing-infinity-a-runtime-for-extreme-agent-concurrency/)
- [Infinity — GitHub repository](https://github.com/hydro-project/infinity)
- [AgentOps Guide — Independent benchmark rerun](https://agentopsguide.com/aws-infinity-agent-runtime/)
- [Hydro Project](https://github.com/hydro-project)
- [The Agent Report — AWS Summit NYC 2026 : la poussée agentique](/2026/06/aws-summit-nyc-2026-agentic-ai/)
- [The Agent Report — Comparatif des frameworks d'agents : LangGraph, CrewAI, AutoGen](/2026/07/ai-agent-frameworks-comparison-2026-langgraph-crewai-autogen/)

— The Agent Report