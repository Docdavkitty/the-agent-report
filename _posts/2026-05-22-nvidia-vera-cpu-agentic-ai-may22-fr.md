---
layout: post
title: "NVIDIA Vera est là — le premier CPU conçu de zéro pour l'IA agentique"
date: 2026-05-22 10:00:00 +0200
lang: fr
ref: nvidia-vera-cpu-agentic-ai-may22
permalink: /fr/2026/05/nvidia-vera-cpu-agentic-ai-may22/
translation_of: /2026/05/nvidia-vera-cpu-agentic-ai-may22/
author: The Agent Report
categories: research
tags: [nvidia, "vera-cpu", "agentic-ai", hardware, infrastructure, "ai-labs", "traduction-francaise"]
last_modified_at: 2026-07-23 15:01:47 +0000
hero_image: /assets/images/hero/hero-nvidia-vera-cpu-agentic-ai-may22.jpg
meta_description: >
  "NVIDIA livre les CPU Vera à Anthropic, OpenAI, SpaceXAI et Oracle : 88 cœurs Olympus, 1,2 To/s de bande passante, 2x d'efficacité, premier silicium dédié à l'orchestration d'agents."
description: >
  "NVIDIA livre les CPU Vera à Anthropic, OpenAI, SpaceXAI et Oracle : 88 cœurs Olympus, 1,2 To/s de bande passante, 2x d'efficacité, premier silicium dédié à l'orchestration d'agents."
reading_time: 8
---

## Qu'est-ce qui rend Vera différent ?

Jusqu'à présent, l'histoire matérielle de l'industrie de l'IA était presque entièrement centrée sur les GPU — des processeurs parallèles massifs optimisés pour l'entraînement et l'inférence. Mais l'IA agentique introduit un profil de charge de travail fondamentalement différent :

| Exigence | IA traditionnelle | IA agentique |
|------------|---------------|------------|
| **Tâche principale** | Multiplications matricielles | Orchestration, appel d'outils, exécution de code |
| **Schéma mémoire** | Lots volumineux et prévisibles | Sporadique, ramifié, multi-étapes |
| **Sensibilité à la latence** | Modérée | Élevée (agents attendant des réponses) |
| **Gestion du contexte** | Fenêtres de prompt fixes | État long et évolutif entre les appels d'outils |
| **Apprentissage par renforcement** | Entraînement hors ligne | Boucles de rétroaction en ligne et continues |

Vera relève ces défis de front. Ses **88 cœurs NVIDIA Olympus personnalisés** offrent des performances par cœur 50 % supérieures en charge complète par rapport aux CPU serveurs traditionnels, tout en consommant nettement moins d'énergie. La **bande passante mémoire de 1,2 To/s** — plus de 3 fois ce qu'offrent les CPU serveurs typiques — permet aux agents de transférer d'immenses fenêtres de contexte entre la mémoire et le calcul sans goulots d'étranglement.

> *« Vera est conçu pour maintenir ce travail en mouvement à grande échelle »* — Ian Buck, NVIDIA

## Le silicium derrière la révolution des agents

Vera n'est pas seulement un CPU autonome — c'est le processeur hôte du futur système **Vera Rubin NVL72**, où il s'associe aux GPU Rubin de nouvelle génération de NVIDIA via l'interconnexion NVLink-C2C. Cette architecture mémoire unifiée signifie que le CPU et le GPU partagent un espace mémoire cohérent, éliminant les surcoûts de transfert de données qui entravent les configurations CPU+GPU traditionnelles.

L'impact pratique est immédiat pour les charges de travail agentiques :

- **Boucles d'orchestration** — Les agents qui planifient, exécutent, observent et replanifient bénéficient de la capacité de Vera à maintenir des milliers de threads de décision parallèles simultanément actifs
- **Appel d'outils** — Générer et exécuter du code Python, effectuer des appels API et analyser des réponses JSON sont des opérations liées au CPU que Vera accélère considérablement
- **Apprentissage par renforcement** — SpaceXAI évalue déjà Vera pour les pipelines d'entraînement d'agents basés sur le RL, où le CPU gère les simulations et le calcul des récompenses tandis que les GPU gèrent l'inférence des modèles
- **Gestion d'état à long contexte** — Les agents maintenant des conversations de plusieurs heures ou itérant sur de grandes bases de code peuvent conserver l'intégralité du contexte dans le chemin mémoire de 1,2 To/s

## La remise qui a fait les gros titres

La livraison elle-même est devenue une petite légende de la Silicon Valley. Chez **Anthropic**, James Bradbury (Responsable du calcul) a reçu le système et a immédiatement commencé à discuter de la manière dont l'architecture de Vera s'aligne sur les charges de travail agentiques de Claude. La visite de Buck avec la carte mère nue comprenait une présentation détaillée de la hiérarchie du cache, des contrôleurs mémoire et du tissu d'E/S.

Chez **OpenAI**, Buck a rencontré Sachin Katti (Responsable de l'infrastructure de calcul) sur un balcon à ciel ouvert. L'équipe de Katti s'est plongée dans les détails internes du système — à un moment donné, Buck aurait sorti un tournevis pour une démonstration en direct.

**Elon Musk** chez SpaceXAI a posé des questions détaillées sur le nombre de cœurs, la disposition mémoire et les solutions de refroidissement. SpaceXAI exécute d'immenses pipelines de simulation basés sur des agents pour les systèmes autonomes, et la combinaison du débit CPU et de l'efficacité énergétique de Vera correspond parfaitement à leurs besoins.

> *« Augmenter la puissance de calcul est un accélérateur important pour la croissance des modèles. Nous sommes ravis de voir Vera émerger comme une pièce prometteuse de l'écosystème pour résoudre les charges de travail agentiques. »* — James Bradbury, Anthropic

## Oracle Cloud : Le premier foyer hyperscale pour Vera

La livraison la plus conséquente a peut-être été la dernière. **Oracle Cloud Infrastructure** a annoncé son intention de déployer **des centaines de milliers de CPU NVIDIA Vera** à partir de 2026, faisant d'OCI le premier fournisseur de cloud hyperscale à proposer une infrastructure IA agentique basée sur Vera.

Karan Batta, Responsable de la gestion des produits chez OCI, a expliqué : *« L'IA agentique exige des performances soutenues à grande échelle. Vera nous offre l'architecture CPU pour y parvenir. »*

Pour les clients entreprises, cela signifie qu'une infrastructure IA agentique de qualité production devient disponible en tant que service cloud — sans avoir à construire et gérer des clusters matériels personnalisés.

## Pourquoi cela compte pour l'écosystème des agents

L'arrivée de Vera signale quelque chose de plus profond qu'un simple lancement de produit. C'est la reconnaissance que l'ère de l'IA agentique a des **exigences d'infrastructure fondamentalement différentes** de ce qui existait auparavant. Comme notre [Guide complet des agents IA]({% post_url 2026-05-26-complete-guide-to-ai-agents-2026 %}) le détaille, le passage de l'inférence sans état à l'orchestration avec état stimule l'innovation matérielle à chaque niveau de la pile.

Lorsque les modèles d'IA se contentaient de répondre à des questions, les exigences matérielles étaient simples : l'inférence nécessitait des GPU, l'entraînement nécessitait des clusters. Mais les agents sont différents. Ils planifient, exécutent du code, appellent des API, gèrent l'état, traitent les erreurs et itèrent. Ce sont des tâches d'orchestration intensives pour le CPU que les GPU n'ont jamais été conçus pour gérer.

La thèse de NVIDIA avec Vera est que le **CPU est le nouveau goulot d'étranglement** dans l'IA agentique — et ils ont construit une solution spécialement conçue.

## La route à venir

Vera est actuellement évalué dans les meilleurs laboratoires d'IA du monde. Les premiers benchmarks sont attendus dans les semaines à venir. Pendant ce temps, les plans de déploiement d'OCI suggèrent que d'ici fin 2026, les développeurs d'entreprise construisant des applications agentiques pourraient avoir accès à une infrastructure alimentée par Vera aussi facilement que de lancer une machine virtuelle aujourd'hui.

Pour l'écosystème IA dans son ensemble, Vera représente un pari que les agents ne sont pas une tendance passagère mais le paradigme dominant du déploiement de l'IA. Si NVIDIA a raison — et la réponse de l'industrie suggère que c'est possible — nous assistons à la naissance d'une nouvelle catégorie d'infrastructure de calcul. Cette évolution matérielle fait écho à ce que la [plateforme d'agents gérés d'Anthropic]({% post_url 2026-05-25-anthropic-managed-agents-platform-dreaming-orchestration-may25 %}) fait au niveau logiciel — construire une infrastructure sur mesure pour des charges de travail autonomes soutenues.

L'ère de l'IA agentique a un CPU conçu sur mesure. Son nom est Vera.

---

*Sources : [Blog NVIDIA](https://blogs.nvidia.com/blog/vera-cpu-delivery), [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/), [NVIDIA Vera CPU](https://www.nvidia.com/en-us/data-center/vera-cpu/)*