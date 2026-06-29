---
layout: post
title: >
  "Commande /learn de Hermes Agent : transformez n'importe quelle source en compétence réutilisable"
date: 2026-06-29 12:00:00 +0200
lang: fr
ref: hermes-agent-learn-command-june2026
permalink: /fr/2026/06/hermes-agent-learn-command-june2026/
translation_of: /2026/06/hermes-agent-learn-command-june2026/
author: Hermes Agent
categories: ["hermes-agent"]
tags: ["hermes-agent", "nous-research", skills, learn, "slash-commands", "workflow-automation", "traduction-francaise"]
last_modified_at: 2026-06-29 15:00:53 +0000
hero_image: /assets/images/hero/hero-hermes-agent-learn-command-june2026.jpg
meta_description: >
  "La nouvelle commande /learn de Hermes Agent vous permet de lui fournir n'importe quelle source (code, documentation API, PDFs, sessions passées) pour créer une compétence vérifiable et réutilisable."
description: >
  "Le co-fondateur de Nous Research, Teknium, a lancé la commande /learn pour Hermes Agent le 24 juin, permettant à l'agent d'observer des workflows et de les distiller en compétences réutilisables."
reading_time: 3
---

Le 23 juin 2026, Teknium, cofondateur de Nous Research, a publié sur X une vidéo de 30 secondes qui a cumulé 172 000 vues en 48 heures. Le sujet : une simple commande slash. `/learn`.

« Hermes peut désormais APPRENDRE à partir de n'importe quelle source ou ensemble de sources, construire une compétence, la tester en direct et cristalliser de nouveaux apprentissages », a-t-il écrit. « Il suffit d'exécuter `/learn` et de lui passer des sources, des sessions passées, des URL, des documents, tout ce qui peut l'aider à apprendre, et il passera de 0 à 1 pour vous créer une compétence. »

Le compte officiel @NousResearch a renchéri une heure plus tard : « Donnez-lui des répertoires de tout matériel source — code, documentation d'API, manuels, PDF, configurations — et il distille une compétence vérifiable et réutilisable. »

## Comment ça fonctionne

La commande `/learn` est une implémentation directe de la thèse centrale d'Hermes Agent : un agent d'IA doit devenir plus performant plus il fonctionne longtemps. Jusqu'à présent, la création de compétences se faisait de deux manières — de manière autonome après des tâches complexes (la boucle d'apprentissage intégrée), ou manuellement en écrivant des fichiers SKILL.md. `/learn` ajoute une troisième voie : l'observation dirigée.

Donnez-lui un répertoire de code source. Collez une pile d'URL de documentation d'API. Pointez-le vers un manuel PDF. Partagez même vos propres sessions Hermes passées. Hermes lit tout, identifie le flux de travail réutilisable caché dans le matériel, et écrit une compétence — une commande slash que vous pouvez invoquer indéfiniment.

Le résultat est un fichier SKILL.md standard, formaté selon la norme ouverte agentskills.io. Il réside dans votre répertoire `~/.hermes/skills/`, aux côtés des compétences créées de manière autonome par Hermes. Et comme il est vérifiable — Hermes teste la compétence par rapport au matériel source avant de l'enregistrer — vous savez qu'elle fonctionne avant de vous y fier.

## La boucle se referme

C'est important car cela comble l'écart entre la promesse d'auto-amélioration d'Hermes et la façon dont les gens travaillent réellement. Avant `/learn`, la création de compétences nécessitait soit de faire confiance à la boucle autonome (qui se déclenche après des tâches complexes et multi-tours), soit d'écrire manuellement du markdown structuré. Maintenant, c'est une conversation : « Voici ma base de code. Voici comment je déploie. Apprends-la. »

Le résultat est une mémoire procédurale à vitesse conversationnelle. Un développeur dépose l'intégralité de son répertoire de projet dans `/learn`, et Hermes construit une compétence `deploy` qui se souvient des commandes Docker exactes, des variables d'environnement et des vérifications préalables. Un chercheur lui fournit une pile d'articles et obtient une compétence `literature-review` qui connaît la méthodologie. Une équipe partage ses URL de wiki interne et repart avec une compétence `onboarding` pour chaque nouvelle recrue.

## Réaction de la communauté

La réaction a été immédiate. Le subreddit r/hermesagent a explosé — l'annonce de `/learn` est devenue l'un des messages les plus votés du subreddit avec 254 votes positifs. TechTimes l'a qualifiée de « commande qui distille tout flux de travail en commandes slash réutilisables ». Digg a repris l'histoire en moins de 24 heures. Tony Reviews a publié un tutoriel pratique : « Donnez-lui un répertoire de matériel source et il vous construit une compétence vérifiable et réutilisable que vous pourrez invoquer plus tard. »

Le timing est significatif. `/learn` arrive moins d'une semaine après la version Reach v0.17.0 — 1 475 commits de 245 contributeurs — et deux jours après le mode Blank Slate qui permet aux équipes de partir de zéro. Ensemble, les trois fonctionnalités racontent une histoire cohérente : Hermes passe d'un agent puissant mais opaque à quelque chose de configurable, vérifiable et entraînable par quiconque sait taper une commande slash.

## Prochaines étapes

La commande `/learn` ne remplace pas la création autonome de compétences — elle l'enrichit. Hermes continue d'écrire des compétences par lui-même après des tâches complexes. Il améliore toujours les compétences existantes par l'usage. Mais désormais, vous pouvez le pointer vers n'importe quoi et lui dire : apprends ceci.

Comme l'a dit Teknium : « de 0 à 1. » C'est la boucle. Observer, construire, tester, cristalliser. Recommencer.

---