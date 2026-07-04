---
layout: post
title: >
  "Workday lance Agent Passport — une vérification de sécurité indépendante pour les agents IA d'entreprise"
date: 2026-06-04 08:00:00 +0200
lang: fr
ref: workday-agent-passport-devcon-2026
permalink: /fr/2026/06/workday-agent-passport-devcon-2026/
translation_of: /2026/06/workday-agent-passport-devcon-2026/
author: The Agent Report
categories: [industry]
tags: [workday, "enterprise-ai", "ai-agents", "ai-safety", "agent-passport", "nist-ai-rmf", "traduction-francaise"]
last_modified_at: 2026-07-04 15:01:05 +0000
hero_image: /assets/images/hero/hero-workday-agent-passport.jpg
meta_description: >
  "Workday dévoile Agent Passport à DevCon 2026 : un système de vérification indépendant testant les agents IA selon les normes OWASP, NIST et MITRE ATLAS."
description: >
  "Les agents IA d'entreprise prolifèrent rapidement, mais une question fondamentale demeure : comment savoir si un agent est sûr pour vos ressources RH..."
reading_time: 4
---

## Le fossé de confiance dans les agents IA d'entreprise

Les agents IA d'entreprise prolifèrent rapidement, mais une question fondamentale reste sans réponse : **comment savoir si un agent peut être déployé en toute sécurité sur vos données RH et financières ?**

Un seul agent mal configuré, positionné sur les données de paie, d'avantages sociaux ou d'organigramme, suffit pour provoquer un salaire manqué, un dossier employé exposé ou un appel d'un régulateur. La sécurité API traditionnelle ne s'applique pas — les agents autonomes prennent des décisions indépendantes, exécutent des workflows multi-étapes et interagissent avec les systèmes de manière imprévisible.

Lors du DevCon 2026, le 2 juin, Workday a dévoilé ce qui pourrait être la réponse la plus directe à ce jour : **Agent Passport**, un système de vérification indépendant par un tiers pour chaque agent IA opérant dans l'entreprise.

## Agent Passport : Comment ça fonctionne

Agent Passport teste et vérifie chaque agent IA — qu'il soit développé par Workday, le client ou un tiers — avant sa mise en production, et assure une surveillance continue après son déploiement.

Chaque agent reçoit un **passeport numérique** contenant :

- **Quels tests de sécurité et de conformité** l'agent a réussis
- **Qui a effectué** la vérification (un partenaire d'attestation indépendant)
- **Quelles normes publiques** ont été utilisées comme cadre de test

La vérification est directement liée aux normes industrielles établies : **OWASP LLM Top 10**, **NIST AI Risk Management Framework** et **MITRE ATLAS**. Chaque attestation est signée et vérifiable, offrant ainsi aux équipes de sécurité un enregistrement clair et comparable entre les agents, quel que soit le fournisseur.

> « Les agents seront omniprésents dans l'entreprise, et cela ne fonctionne que si les équipes de sécurité disposent d'un enregistrement clair et signé de ce pour quoi chacun a été testé. »
> — **Workday**, annonce d'Agent Passport

## Cisco comme partenaire de lancement

Cisco est le premier partenaire d'attestation pour Agent Passport. Cisco AI Defense teste indépendamment les agents IA selon les principales normes de sécurité avant le déploiement, et assure une protection continue en runtime contre :

- Les attaques par injection de prompt
- Les fuites de données
- Les tentatives de jailbreak
- Les actions autonomes non sécurisées

Ce partenariat est stratégique — les relations existantes de Cisco avec les entreprises en matière de sécurité confèrent à Agent Passport une crédibilité immédiate auprès des équipes de sécurité du Fortune 500, qui constituent la clientèle principale de Workday.

## Plus qu'une simple vérification

Workday a également lancé deux outils complémentaires lors du DevCon :

**Developer Agent** — permet aux développeurs de créer des applications et agents IA en langage naturel à partir des outils agentiques qu'ils utilisent déjà : Claude Code, Cline, Codex, Cursor et Google Antigravity. Un développeur peut taper « Crée un agent qui alerte la finance lorsqu'un département est en voie de dépasser son budget ce trimestre », et Developer Agent s'occupe du reste — sélection des bons outils, connexion des sources de données et extraction de la documentation.

**Agent-Ready Tools** — une nouvelle catégorie de connecteurs d'entreprise conçus spécifiquement pour les agents autonomes, utilisant des normes ouvertes comme le Model Context Protocol (MCP). Des centaines de ces outils couvrent les domaines RH, finance et IT, chacun héritant automatiquement du modèle de sécurité, des contrôles de délégation et de la piste d'audit de Workday.

> « Les plateformes gagnent lorsqu'elles font disparaître la difficulté pour le développeur », a déclaré **Gabe Monroy**, CTO de Workday. « N'importe qui peut donner de la vitesse à un agent — la partie difficile est de le laisser agir sur l'organigramme ou le grand livre tout en faisant confiance à chaque étape. »

## Implications pour l'industrie

Agent Passport répond à ce qu'on appelle le **« mur d'autorisation »** — le constat que la capacité technique des agents IA a largement dépassé l'infrastructure de confiance des entreprises. Les entreprises peuvent construire des agents capables de choses remarquables, mais les déployer sur des données RH et financières sensibles nécessite un niveau de confiance que la plupart des équipes de sécurité IT ne possèdent pas encore.

L'approche de Workday est remarquable car elle ne tente pas de résoudre seule le problème de vérification. En faisant appel à des partenaires d'attestation tiers, en s'alignant sur des normes publiques et en rendant les résultats vérifiables, Agent Passport crée un **écosystème de vérification** plutôt qu'un verrouillage propriétaire.

Pour le marché plus large des agents IA d'entreprise, cela établit un précédent. Si l'approche de Workday gagne du terrain, attendez-vous à ce que des concurrents ERP et HCM comme SAP, Oracle et UKG suivent avec leurs propres cadres de vérification — et à ce que des fournisseurs de sécurité comme CrowdStrike, Palo Alto Networks et Zscaler rivalisent avec Cisco pour les partenariats d'attestation.

## Disponibilité

| Fonctionnalité | Accès anticipé | Disponibilité générale |
|---------|-------------|---------------------|
| Developer Agent | Maintenant (Workday Extend Professional) | S2 2026 |
| Agent-Ready Tools | Maintenant (Workday Extend Professional) | S2 2026 |
| Agent Passport | S2 2026 | Avant fin 2026 |