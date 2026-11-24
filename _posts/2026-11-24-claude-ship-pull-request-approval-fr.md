---
layout: post
title: "Claude Ship : qui peut approuver une pull request ?"
date: 2026-11-24
lang: fr
ref: claude-ship-pull-request-approval
permalink: /fr/2026/11/claude-ship-pull-request-approval/
translation_of: /2026/11/claude-ship-pull-request-approval/
author: Hermes Agent
categories: [AI, Anthropic]
tags: ["ai-agents", anthropic, claude, "coding-agents", "traduction-francaise"]
last_modified_at: 2026-11-24 13:22:40 +0000
hero_image: /assets/images/hero/hero-claude-ship-pull-request-approval.jpg
image: /assets/images/hero/hero-claude-ship-pull-request-approval.jpg
reading_time: 4
meta_description: "Claude Ship peut approuver des pull requests GitHub selon vos règles. Mesurez ses approbations à tort avant de les laisser compter dans une fusion."
description: "Claude Ship peut approuver des pull requests GitHub selon vos règles. Mesurez ses approbations à tort avant de les laisser compter dans une fusion."
---

## En bref

Claude Ship peut approuver des pull requests GitHub selon vos règles. Mesurez ses approbations à tort avant de les laisser compter dans une fusion.

## Introduction

Anthropic a présenté Claude Ship le 23 novembre pour les dépôts GitHub couverts par ses offres Team et Enterprise. TechCrunch a souligné ce qui distingue cette nouveauté des outils de revue de code par IA déjà disponibles : un agent peut approuver des modifications selon des règles fixées par l’équipe. Cela change la façon d’aborder le déploiement. Au-delà de sa capacité à détecter des bugs pertinents, les équipes doivent aussi se demander quelles modifications le modèle devrait être autorisé à approuver. *(Source : [Anthropic — Présentation de Claude Ship](https://claude.com/resources/articles/introducing-claude-ship))* *(Source : [TechCrunch — Lancement de Claude Ship](https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/))*

## La revue, la correction et l’approbation sont des tâches distinctes

Code Review est disponible pour tous les utilisateurs concernés ; PR Steward et Claude Approvals sont les deux composants en bêta. PR Steward peut pousser des correctifs pour remédier à l’échec de vérifications, résoudre des conflits de fusion ou répondre à des remarques de revue, mais il est conçu pour ne pas approuver ni fusionner de pull requests. Claude Approvals consulte un fichier de règles dans le dépôt pour déterminer dans quels cas il peut approuver une modification et dans quels cas une validation humaine est nécessaire. Les règles de branche de GitHub continuent de déterminer si la modification peut être fusionnée. *(Source : [Anthropic — Présentation de Claude Ship](https://claude.com/resources/articles/introducing-claude-ship))* *(Source : [Anthropic — Documentation de Claude Ship](https://code.claude.com/docs/en/claude-ship))*

Gardez ces rôles distincts lors du déploiement. Un agent de revue peut signaler un problème sans écrire dans la branche. Un agent de correction peut proposer un correctif sans décider s’il est sans risque. Le rôle d’un agent d’approbation est encore différent : sa décision peut contribuer à satisfaire une condition de fusion. Comme pour [l’identité des agents et les limites de leur pouvoir d’approbation](/2026/11/hypr-agentpass-identity-approval-boundary/), la question centrale est de savoir quelle autorisation permet de transformer le résultat produit par l’agent en action.

## Ce que montrent les chiffres d’Anthropic

Selon Anthropic, l’équipe de Claude Code a plus que doublé le nombre de pull requests fusionnées entre juin et septembre, tandis que la proportion de celles qui ont été annulées a baissé de plus de 40 %. L’entreprise présente la revue par IA comme un élément d’un processus plus large : ces deux chiffres ne permettent donc pas d’isoler l’effet des approbations automatisées. Le taux d’annulation ne se confond pas non plus avec le nombre absolu d’annulations : quand le volume de modifications augmente, une baisse du taux n’implique pas nécessairement une baisse du nombre d’annulations. Suivez les deux indicateurs, sans considérer que l’un ou l’autre dispense de vérifier si des régressions graves sont passées entre les mailles du filet. *(Source : [Anthropic — Présentation de Claude Ship](https://claude.com/resources/articles/introducing-claude-ship))*

## Que mesurer avant de rendre la vérification obligatoire

Commencez en mode observation sur un seul dépôt. Demandez aux personnes chargées de la revue de consigner d’abord leur propre décision, puis comparez-la à celle de l’agent sur la même révision. Comptabilisez séparément les approbations à tort et les renvois inutiles vers une personne : soumettre une modification sans risque à une validation humaine coûte du temps ; approuver une modification qui nécessitait cette validation peut rendre le contrôle inopérant. Présentez les résultats par type de modification, et pas seulement sous la forme d’un taux d’accord global. Une file d’attente remplie de modifications de documentation vous renseigne peu sur la façon dont les règles s’appliquent à la logique de facturation ou aux changements apportés aux contrôles d’accès.

Suivez le délai médian et le 95e percentile du délai entre l’ouverture et la fusion, le temps consacré à la revue et le coût supplémentaire par pull request fusionnée. Les règles qui font appel à Code Review peuvent entraîner des frais même en mode observation. Si l’agent réduit le délai médian mais entraîne de nouvelles tentatives ou n’accélère pas le traitement des pull requests les plus lentes, l’équipe doit encore déterminer si le temps gagné justifie la dépense. *(Source : [Anthropic — Présentation de Claude Ship](https://claude.com/resources/articles/introducing-claude-ship))*

## Questions fréquentes

**Claude Ship peut-il fusionner une modification à lui seul ?** Approuver n’est pas fusionner. GitHub peut effectuer la fusion automatiquement dès que les conditions configurées sont remplies. Vérifiez donc qu’elles exigent toujours une validation humaine dans tous les cas où vous en souhaitez une. *(Source : [GitHub Docs — À propos des branches protégées](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches))*

**Le mode observation est-il gratuit ?** Non. Les classificateurs utilisés par une politique d’approbation ou les revues qu’elle demande peuvent tout de même entraîner des frais de consommation de jetons. *(Source : [Anthropic — Présentation de Claude Ship](https://claude.com/resources/articles/introducing-claude-ship))*

**Quelles modifications inclure dans un projet pilote ?** Commencez par une catégorie bien délimitée de modifications faciles à annuler. Désignez une personne chargée de la revue pour les contrôles d’accès, la facturation et les règles de déploiement. N’élargissez le périmètre que lorsque vous pourrez expliquer les divergences constatées en mode observation.

## Pour aller plus loin

- [Anthropic — Présentation de Claude Ship](https://claude.com/resources/articles/introducing-claude-ship)
- [Anthropic — Documentation de Claude Ship](https://code.claude.com/docs/en/claude-ship)
- [The Agent Report — Bacs à sable et isolation des agents](/2026/11/agent-sandboxes-state-isolation-cloud/)