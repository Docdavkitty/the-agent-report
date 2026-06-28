---
layout: post
title: >
  "KPMG équipe 276 000 professionnels d’agents IA — et d’un plan de contrôle pour les gouverner"
date: 2026-06-12 08:00:00 +0200
lang: fr
ref: kpmg-microsoft-agent-365-enterprise-ai-governance
permalink: /fr/2026/06/kpmg-microsoft-agent-365-enterprise-ai-governance/
translation_of: /2026/06/kpmg-microsoft-agent-365-enterprise-ai-governance/
author: The Agent Report
categories: [industry]
tags: [kpmg, microsoft, "agent-365", copilot, enterprise, governance, "shadow-ai", audit, clara, "trusted-ai", "traduction-francaise"]
last_modified_at: 2026-06-28 15:02:02 +0000
hero_image: /assets/images/hero/hero-kpmg-microsoft-agent-365-enterprise-ai-governance.jpg
meta_description: >
  "KPMG déploie Microsoft 365 Copilot et Agent 365 auprès de 276 000 employés dans 138 pays — le plus grand déploiement d’agents IA en entreprise jamais réalisé."
description: >
  "TL;DR — Le 9 juin 2026, KPMG et Microsoft ont annoncé le plus grand déploiement d’agents IA en entreprise : 276 000 professionnels, des dizaines de milliers d’agents, régis par le plan de contrôle Agent 365."
reading_time: 10
---

## Le chiffre qui compte : 276 000 × 138

Mettons les choses en perspective. Lorsque SAP a annoncé le déploiement de son agent Joule en janvier 2026, cela concernait environ 100 000 employés. Lorsque TD Bank a déployé des agents IA dans ses centres de contact en avril, cela touchait environ 90 000 collaborateurs. L'annonce de KPMG double ces chiffres — et ce, dans trois lignes de services professionnels distinctes (audit, fiscalité et conseil) réparties dans 138 pays et territoires, chacun avec son propre régime réglementaire.

> « L'intégration de Microsoft 365 Copilot et d'Agent 365 améliore l'analyse en temps réel, l'identification précoce des risques et offre des perspectives plus approfondies, tout en renforçant la qualité de l'audit, la transparence et la confiance pour les clients », a déclaré **Scott Flynn, Responsable mondial de l'audit chez KPMG International**, dans l'annonce conjointe.

Ce déploiement est l'aboutissement d'un investissement pluriannuel de plusieurs milliards de dollars dans l'IA et les services cloud de Microsoft, que KPMG a initié en 2023. Cet investissement a permis de construire l'infrastructure Azure qui héberge désormais à la fois le déploiement de Copilot et les dizaines de milliers d'agents spécialisés par domaine.

## Agent 365 : La couche de gouvernance que les entreprises attendaient

L'accord avec KPMG est autant une consécration pour Agent 365 de Microsoft qu'un jalon pour KPMG. Agent 365 a atteint sa disponibilité générale le **1er mai 2026**, après une période d'aperçu débutée fin 2025. Il est présenté comme « le plan de contrôle d'entreprise pour gouverner tous les agents » — accessible directement depuis le centre d'administration Microsoft 365.

Que fait concrètement un « plan de contrôle pour agents IA » ? Trois choses :

### 1. Gestion du cycle de vie des agents

Agent 365 offre aux administrateurs informatiques un tableau de bord unique pour enregistrer, approuver, surveiller et désactiver les agents IA dans toute l'organisation. Chaque agent — qu'il soit créé dans Copilot Studio, déployé via Azure AI Foundry, ou intégré depuis un tiers — apparaît dans l'inventaire avec ses autorisations, son périmètre d'accès aux données et son historique d'utilisation.

Pour KPMG, où les agents traitent des données financières sensibles dans le cadre de missions d'audit, c'est une exigence non négociable. La capacité à tracer *quel agent a accédé à quelles données, quand et pourquoi* est désormais une obligation réglementaire dans plusieurs juridictions.

### 2. Détection de l'IA fantôme (Shadow AI)

C'est la fonctionnalité qui distingue Agent 365 des tentatives de gouvernance antérieures. La **page Shadow AI** de la plateforme — alimentée par Microsoft Defender et Microsoft Intune — analyse les postes Windows gérés pour détecter l'activité locale des agents, les appels API non autorisés et les logiciels agents non enregistrés. Elle les présente ensuite dans le centre d'administration avec des options de correction : approuver et enregistrer, restreindre au bac à sable, ou bloquer.

Pour une entreprise de la taille de KPMG, l'IA fantôme n'est pas une hypothèse théorique. Une enquête menée par le cabinet lui-même en 2025 a révélé que 71 % des entreprises utilisaient l'IA d'une manière ou d'une autre, mais que seulement 35 % disposaient de politiques de gouvernance. Agent 365 comble cet écart en rendant visible ce qui est invisible.

### 3. Intégration du cadre d'IA de confiance

KPMG a développé son propre **cadre d'IA de confiance (Trusted AI framework)** — un ensemble de principes et de contrôles techniques pour un déploiement responsable de l'IA — et le partenariat avec Microsoft intègre ce cadre directement dans la couche de gouvernance d'Agent 365. Plutôt que de gérer la gouvernance comme un processus de conformité parallèle, KPMG peut appliquer ses politiques d'IA de confiance (équité, explicabilité, confidentialité, sécurité) comme des garde-fous automatisés sur chaque déploiement d'agent.

> « Les cabinets KPMG tireront parti de ces capacités pour améliorer la prestation de services dans les domaines de l'audit, de la fiscalité et du conseil, tout en aidant les clients à construire des modèles opérationnels pilotés par des agents et à déployer l'IA à grande échelle dans leurs propres organisations », a indiqué l'annonce conjointe.

## KPMG Clara : La plateforme d'audit devenue un hub d'agents

L'aspect le plus intéressant sur le plan technique du déploiement est **KPMG Clara**, la plateforme mondiale d'audit intelligent du cabinet. Clara était déjà une plateforme alimentée par l'IA fonctionnant sur Azure, mais l'intégration d'Agent 365 la transforme d'un outil en une couche d'orchestration d'agents.

Voici ce qui change :

| Avant (Clara avant Agent 365) | Après (Clara + Agent 365) |
|---|---|
| Analyses basées sur l'IA sur des transactions échantillonnées | Les agents analysent **100 % des populations transactionnelles** |
| Flux de travail piloté par l'auditeur | Identification des risques pilotée par les agents avec supervision de l'auditeur |
| Modèles de risque statiques | Les agents réévaluent en continu le risque à mesure que de nouvelles données arrivent |
| Gouvernance manuelle des agents | Chaque agent enregistré, autorisé et surveillé via Agent 365 |

La capacité la plus puissante : **KPMG Clara Transaction Scoring** fonctionne désormais comme des agents autonomes qui analysent l'intégralité des populations du grand livre et des sous-journaux, signalant les anomalies non seulement par rapport à des règles prédéfinies, mais aussi par rapport à des modèles appris à partir de l'historique global des missions de KPMG. La partie « humaine assurée » de la devise de KPMG, « alimenté par l'IA, assuré par l'humain », signifie que les auditeurs examinent et valident — mais les agents effectuent le travail lourd à une échelle qu'aucune équipe humaine ne pourrait égaler.

## Les chiffres derrière le déploiement

| Métrique | Valeur |
|---|---|
| Professionnels concernés | Plus de 276 000 |
| Pays et territoires | 138 |
| Date de disponibilité générale d'Agent 365 | 1er mai 2026 |
| Investissement IA KPMG-Microsoft | Plusieurs milliards de dollars (depuis 2023) |
| Périmètre de déploiement des agents | Audit, fiscalité, conseil (toutes les lignes de services) |
| Détection de l'IA fantôme | En temps réel, via l'intégration Defender + Intune |

## Pourquoi chaque DSI devrait y prêter attention

L'accord KPMG-Microsoft est important au-delà des deux entreprises concernées car il établit une **architecture de référence** pour le déploiement d'agents IA en entreprise à grande échelle. Voici le modèle :

1. **Couche d'infrastructure** : Azure AI Foundry (ou plateforme cloud IA équivalente)
2. **Couche de productivité** : Microsoft 365 Copilot (ou assistant IA générative équivalent)
3. **Couche d'agents** : Agents spécialisés par domaine (audit, fiscalité, conformité, etc.)
4. **Couche de gouvernance** : Agent 365 (le plan de contrôle)
5. **Couche de confiance** : Cadre d'IA de confiance KPMG (ou politique organisationnelle équivalente)

Cette pile en cinq couches est désormais éprouvée à l'échelle de 276 000 personnes. Chaque DSI du Fortune 500 planifiant un déploiement d'agents en 2026-2027 examinera ce modèle et se demandera : « Avons-nous les cinq couches ? »

Pour la plupart, la réponse est non. Un rapport de Gartner de juin 2026 estimait que moins de 15 % des grandes entreprises disposent d'une couche de gouvernance dédiée aux agents IA en production. Le déploiement de KPMG élève la barre — et crée une urgence concurrentielle pour tous les autres.

## Le changement de narrative vers la gouvernance

Un changement plus profond s'opère dans la manière dont l'IA d'entreprise est commercialisée et vendue. En 2024, la conversation portait sur la *capacité* : « Regardez ce que notre IA peut faire. » En 2025, il s'agissait de *productivité* : « Regardez à quelle vitesse vos équipes peuvent travailler. » En 2026, le récit a pivoté vers le **contrôle**.

> KPMG et Microsoft commercialisent explicitement la capacité à *gérer, surveiller et auditer* les agents IA comme la principale raison d'acheter.

Ce n'est pas subtil. L'annonce conjointe met en avant la gouvernance, pas les fonctionnalités. Le premier point concerne la « gestion et le contrôle des agents IA ». Le nom du produit — *Agent 365* — est délibérément peu sexy. C'est l'Active Directory de l'ère des agents : une infrastructure nécessaire mais que l'on ne célèbre pas.

Le sous-texte : la phase de Far West du déploiement d'agents IA en entreprise est terminée. La phase de gouvernance a commencé.

## Ce qui manque

L'annonce est impressionnante, mais trois questions restent sans réponse :

**1. Transparence des prix.** La tarification d'Agent 365 est liée à la licence Microsoft 365 E5, avec des coûts supplémentaires par agent et par charge de travail. L'engagement de plusieurs milliards de dollars de KPMG a probablement permis d'obtenir des conditions favorables, mais les petites entreprises sont confrontées à un coût total de possession (TCO) incertain pour des déploiements équivalents.

**2. Gouvernance des interactions agent-à-agent.** Agent 365 régit l'accès aux données et les autorisations des agents individuels, mais que se passe-t-il lorsque des agents interagissent entre eux à travers les lignes de services ? Un agent d'audit signalant un risque qu'un agent fiscal doit examiner introduit des flux de travail multi-agents que les outils de gouvernance actuels ne modélisent pas entièrement.

**3. Fragmentation réglementaire.** Opérer dans 138 pays signifie 138 régimes réglementaires. Les politiques d'Agent 365 peuvent être définies par zone géographique, mais les modèles d'IA sous-jacents sont globaux. Un modèle de risque entraîné sur des données d'une juridiction peut produire des inférences non conformes dans une autre. C'est la prochaine frontière de la gouvernance des agents — et elle n'est pas résolue.

## La vue d'ensemble : L'économie des agents a besoin de rails ET de garde-fous

Le déploiement de KPMG intervient la même semaine que Mastercard Agent Pay for Machines (AP4M) — une couche d'infrastructure de paiement pour les agents IA autonomes. Les deux annonces sont les deux faces d'une même histoire : 2026 est l'année où l'économie des agents obtient son infrastructure.

Mastercard construit les **rails de paiement** — la plomberie financière qui permet à un agent de KPMG Clara de payer un flux de données tiers sans approbation humaine. Microsoft construit les **rails de gouvernance** — le plan de contrôle qui permet à KPMG de savoir exactement quel agent a effectué ce paiement, pourquoi et s'il était autorisé.

Ensemble, ils construisent l'infrastructure bilatérale dont le commerce agentique a besoin pour passer des expériences et des pilotes à l'échelle. L'accord KPMG est le premier test de résistance majeur de cette infrastructure. S'il fonctionne à l'échelle de 276 000 personnes dans 138 juridictions réglementaires, l'ère des agents en entreprise aura sa preuve de concept.

## FAQ

**Q : Qu'est-ce que Microsoft Agent 365 ?**
R : Une plateforme de gouvernance centralisée pour gérer les agents IA dans toute l'entreprise. Elle gère l'enregistrement des agents, les autorisations, la surveillance, la détection de l'IA fantôme et la gestion du cycle de vie — accessible depuis le centre d'administration Microsoft 365. Disponibilité générale depuis le 1er mai 2026.

**Q : Combien d'agents IA KPMG déploie-t-il ?**
R : KPMG n'a pas divulgué de chiffre exact, mais l'annonce mentionne « des dizaines de milliers » d'agents dans les domaines de l'audit, de la fiscalité et du conseil. Cela inclut des agents intégrés à KPMG Clara pour l'analyse d'audit, des agents de conformité fiscale et des agents de flux de travail de conseil.

**Q : Qu'est-ce que KPMG Clara ?**
R : La plateforme mondiale d'audit intelligent de KPMG, fonctionnant sur Microsoft Azure. Elle utilise l'IA pour analyser les données transactionnelles, identifier les risques et mettre en évidence des perspectives. Avec l'intégration d'Agent 365, Clara intègre désormais des agents IA autonomes qui analysent 100 % des populations transactionnelles (pas seulement des échantillons) et réévaluent en continu le risque.

**Q : Qu'est-ce que le cadre d'IA de confiance de KPMG ?**
R : Un ensemble de principes et de contrôles techniques pour un déploiement responsable de l'IA, couvrant l'équité, l'explicabilité, la confidentialité, la sécurité et la responsabilité. KPMG applique ce cadre à ses propres déploiements et le propose à ses clients en tant que service de conseil.

**Q : S'agit-il du plus grand déploiement d'agents IA en entreprise ?**
R : Avec 276 000 professionnels dans 138 pays, il s'agit apparemment du plus grand déploiement *annoncé* à ce jour (juin 2026). Les déploiements de SAP Joule (~100 000 employés) et de TD Bank (~90 000) sont les comparables les plus proches.

**Q : Que signifie « IA fantôme » (Shadow AI) ?**
R : Outils et agents IA déployés par les employés sans approbation ni visibilité du service informatique. La page Shadow AI d'Agent 365 détecte l'activité non autorisée des agents sur les appareils gérés et la présente pour correction.

**Q : Comment cela affecte-t-il les clients de KPMG ?**
R : Les clients bénéficient d'audits plus rapides et plus complets (analyse de 100 % des transactions contre échantillonnage), d'une identification plus précoce des risques et de perspectives plus approfondies. KPMG acquiert également l'expertise nécessaire pour aider les clients à déployer leurs propres modèles opérationnels pilotés par des agents.

---

*Sources : Communiqué de presse de KPMG International (9 juin 2026), Microsoft News Source (9 juin 2026), Microsoft Security Blog — Annonce de la disponibilité générale d'Agent 365 (1er mai 2026), Microsoft Tech Community — Nouveautés d'Agent 365 (mai 2026), Documentation de la plateforme KPMG Clara.*