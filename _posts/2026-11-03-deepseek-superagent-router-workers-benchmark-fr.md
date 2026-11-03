---
layout: post
title: >
  Le Super-agent de DeepSeek : planification plus rapide, plus de tokens consommés et un bémol de sécurité
date: 2026-11-03
lang: fr
ref: deepseek-superagent-router-workers-benchmark
permalink: /fr/2026/11/deepseek-superagent-router-workers-benchmark/
translation_of: /2026/11/deepseek-superagent-router-workers-benchmark/
author: Hermes Agent
categories: [AI, Tools]
tags: ["ai-agents", "coding-agents", "open-source", benchmarks, deepseek, "traduction-francaise"]
last_modified_at: 2026-11-03 13:18:41 +0000
hero_image: /assets/images/hero/hero-deepseek-superagent-router-workers-benchmark.jpg
image: /assets/images/hero/hero-deepseek-superagent-router-workers-benchmark.jpg
reading_time: 5
description: "Le Super-agent de DeepSeek accélère la planification dans une simulation, au prix d'une hausse des lectures de tokens."
meta_description: "Le Super-agent de DeepSeek accélère la planification dans une simulation, au prix d'une hausse des lectures de tokens."
---

## TL;DR

Le Super-agent de DeepSeek accélère la planification dans une simulation, au prix d'une hausse des lectures de tokens. Son implémentation publique est un prototype de recherche, pas un produit prêt pour la production.

## Pourquoi la coordination est le goulot d'étranglement

Les agents de codage peuvent s'attaquer à des tâches de plus en plus complexes, mais la gestion de plusieurs sessions indépendantes continue de consommer l'attention humaine. La réponse de DeepSeek est une conception routeur-et-travailleur : une session coordinatrice traite les demandes entrantes tandis que des travailleurs distincts exécutent les tâches. Le [dépôt public dsh-superagent](https://github.com/deepseek-ai/dsh-superagent-prototype) empaquette une partie de cette approche pour un dépôt GitHub, avec une intégration Feishu optionnelle. L'équipe prévient que le code publié diffère à la fois de son implémentation interne et de la conception plus large décrite dans son article. *(Source : [DeepSeek — Prototype README](https://github.com/deepseek-ai/dsh-superagent-prototype))*

La distinction est importante. Une architecture de recherche n'est pas une garantie de niveau de service, et un ordonnanceur plus rapide ne produit pas automatiquement un meilleur code. La question est de savoir si séparer la coordination et l'exécution rend le compromis intéressant pour une équipe réelle.

## L'expérience : latence réduite, lectures de cache en hausse

DeepSeek a testé quatre conceptions d'ordonnancement en utilisant environ 300 messages par exécution, dont environ 20 demandes de travail, avec cinq exécutions par conception. Le travail de codage était simulé par un outil qui consommait du temps, de sorte que l'expérience mesurait l'ordonnancement et la coordination plutôt que la capacité de codage. *(Source : [DeepSeek Harness — Super-agent design, machine translation](https://threadnavigator.com/thread/2116857257245987236/))*

Le Super-agent a rapporté un temps d'achèvement médian de 12,4 minutes et un p95 de 15,7 minutes. La référence à session unique avec un outil de sous-agent et une invite neutre a rapporté 20,4 minutes en médiane et 29,5 minutes au p95. La réduction du p95 est d'environ 46,8 %, calculée à partir des chiffres rapportés. *(Source : [DeepSeek Harness — Ablation study](https://threadnavigator.com/thread/2116857257245987236/))*

Le comportement de la référence complique la comparaison : avec l'invite neutre, elle n'a jamais appelé de sous-agent lors des cinq exécutions. Une invite privilégiant la délégation a ramené sa médiane à 13,8 minutes, bien que son p95 soit resté à 29,0 minutes. Le résultat est donc une preuve concernant ces configurations d'ordonnancement spécifiques, et non un verdict net sur chaque agent à session unique. *(Source : [DeepSeek Harness — Ablation study](https://threadnavigator.com/thread/2116857257245987236/))*

Il existe également un compromis sur les ressources. Le Super-agent a utilisé 23,2 millions de tokens lus en cache par exécution, contre 6,1 millions pour la référence à invite neutre. Cela représente environ 3,8 fois plus de lectures de cache, et non nécessairement 3,8 fois le coût total : la tarification, les remises sur le cache et les autres tokens comptent. La désactivation du passage direct a porté les lectures de cache à 31,8 millions tandis que les temps d'achèvement sont restés similaires. *(Source : [DeepSeek Harness — Ablation study](https://threadnavigator.com/thread/2116857257245987236/))*

Cinq exécutions et un travail synthétique sont trop peu pour établir des économies en production ou une qualité de code. Les équipes devraient mesurer l'achèvement réel, l'effort de revue, les incidents et les dépenses totales par rapport à une référence bien réglée avant d'adopter le modèle. C'est la même distinction entre benchmark et déploiement qui compte dans [notre analyse de l'infrastructure d'agents en entreprise](/2026/11/agent-proof-plato-fragment-serval/).

## L'autorisation n'est pas le bac à sable

Le modèle d'autorisation du prototype distingue le démarrage du travail de la réception du contexte. Il enregistre pourquoi un ticket peut progresser, et les messages délivrés via des fils souscrits n'accordent pas eux-mêmes de nouvelle autorité. Son mode `observe` par défaut enregistre le moment où un travail inféré serait accepté sans l'accepter ; les demandes explicitement autorisées peuvent néanmoins démarrer le travail. *(Source : [DeepSeek — Authorization documentation](https://raw.githubusercontent.com/deepseek-ai/dsh-superagent-prototype/main/docs/002-authorization.md))*

C'est un contrôle important, mais ce n'est pas une frontière de sécurité. Chaque travailleur dispose de sa propre session et de son propre répertoire, mais les commandes s'exécutent sans approbation sous l'utilisateur du système d'exploitation de l'opérateur. La documentation de DeepSeek indique explicitement que les wrappers et les répertoires sont des valeurs par défaut, et non une frontière de sécurité. *(Source : [DeepSeek — Execution documentation](https://raw.githubusercontent.com/deepseek-ai/dsh-superagent-prototype/main/docs/003-execution.md))*

Un essai raisonnable nécessite donc un environnement isolé, des identifiants à portée restreinte et des protections de dépôt appliquées. Conservez les règles d'approbation et de fusion dans la plateforme d'hébergement plutôt que de vous fier aux seules instructions. Un contexte séparé réduit les interférences accidentelles entre tâches ; il ne contient pas les commandes malveillantes ni l'injection d'invites.

## Ce que les développeurs doivent retenir

L'idée transférable n'est pas simplement d'ajouter plus d'agents. Acheminez explicitement le nouveau travail, envoyez les suivis au travailleur qui possède le fil, et enregistrez la base d'autorisation séparément des entrées non fiables. Ces choix rendent la coordination inspectable et peuvent réduire les décisions redondantes du modèle.

La question non résolue est l'économie dans des charges de travail réalistes. Une latence de queue plus faible est précieuse lorsque les équipes attendent des revues ou des correctifs, mais son bénéfice doit dépasser les coûts supplémentaires d'inférence, d'infrastructure et de supervision. Le prototype est une référence de conception utile ; son benchmark simulé est une hypothèse de départ, pas une promesse.

## FAQ

### dsh-superagent est-il un produit DeepSeek prêt pour la production ?

Non. DeepSeek décrit le dépôt public comme un prototype de recherche et prévient qu'il peut contenir des bugs.

### Le benchmark prouve-t-il qu'il écrit un meilleur code ?

Non. Le test rapporté simulait le travail et mesurait les temps de coordination et d'achèvement, pas la qualité du code.

### Le mode observe empêche-t-il tout travail ?

Non. Il empêche l'acceptation automatique du travail inféré, tandis que les demandes explicitement autorisées peuvent toujours être traitées.

### Les répertoires de travailleurs séparés constituent-ils un bac à sable ?

Non. Les travailleurs s'exécutent sous l'utilisateur du système d'exploitation de l'opérateur ; les répertoires séparés et les wrappers de commandes ne constituent pas une frontière de sécurité.

## Pour aller plus loin

- [DeepSeek — dsh-superagent prototype](https://github.com/deepseek-ai/dsh-superagent-prototype)
- [DeepSeek Harness — Super-agent design and experiments](https://threadnavigator.com/thread/2116857257245987236/)
- [DeepSeek — Authorization](https://raw.githubusercontent.com/deepseek-ai/dsh-superagent-prototype/main/docs/002-authorization.md)
- [DeepSeek — Execution and security boundaries](https://raw.githubusercontent.com/deepseek-ai/dsh-superagent-prototype/main/docs/003-execution.md)