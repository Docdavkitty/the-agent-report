---
layout: post
title: >
  "[FR] Elsevier Sues Meta Over Llama Training Data — First Science Publisher Joins the Copyright Fight"
date: 2026-05-12 14:00:00 +0200
lang: fr
ref: elsevier-meta-llama-copyright-lawsuit
permalink: /fr/2026/05/elsevier-meta-llama-copyright-lawsuit/
translation_of: /2026/05/elsevier-meta-llama-copyright-lawsuit/
author: The Agent Report
categories: [research]
tags: [meta, llama, "open-source", "copyright-lawsuit", elsevier, "academic-publishing", "traduction-francaise"]
last_modified_at: 2026-08-09 15:12:33 +0000
hero_image: /assets/images/hero/hero-elsevier-meta-llama-copyright-lawsuit.jpg
reading_time: 6
description: "La guerre des droits d'auteur contre les modèles Llama de Meta vient de s'étendre au front académique."
meta_description: "La guerre des droits d'auteur contre les modèles Llama de Meta vient de s'étendre au front académique."
---

**La guerre des droits d'auteur contre les modèles Llama de Meta vient de s'étendre au front académique.** Elsevier — le plus grand éditeur scientifique au monde, avec plus de 2 900 revues, dont *The Lancet* et *Cell* — a rejoint le recours collectif contre Meta, alléguant que des millions d'articles de recherche protégés par le droit d'auteur ont été aspirés et utilisés sans autorisation pour entraîner la famille de modèles Llama.

C'est la **première fois qu'un grand éditeur scientifique** entre dans la bataille juridique autour de l'IA et des droits d'auteur, ce qui modifie considérablement le calcul juridique. Voici ce qui s'est passé, pourquoi c'est important et ce que cela signifie pour l'avenir des [données d'entraînement de l'IA open source]({% post_url 2026-05-27-ultimate-guide-open-source-ai-agent-frameworks %}).

## Ce qu'allègue Elsevier

La plainte, déposée initialement le 5 mai par cinq grandes maisons d'édition (Elsevier, Cengage, Hachette, Macmillan et McGraw Hill) auxquelles s'est joint l'auteur Scott Turow, cible spécifiquement l'utilisation d'œuvres protégées par Meta pour entraîner Llama. Elsevier apporte une revendication unique : en tant qu'éditeur scientifique, l'intégralité de son catalogue d'articles de recherche en accès payant — représentant des milliards de dollars de revenus d'abonnements institutionnels — aurait été reproduite dans les jeux de données d'entraînement de Meta.

Les principales allégations :

| Allégation | Détail |
|---|---|
| **Scraping de Common Crawl** | Meta a utilisé Common Crawl, un ensemble de données de milliards de pages web, qui, selon les plaignants, contenait des copies non autorisées de résumés scientifiques protégés et d'articles en accès payant |
| **Torrenting depuis LibGen** | Meta aurait téléchargé et partagé via torrent des œuvres depuis **LibGen** — une bibliothèque clandestine controversée de livres, d'articles de recherche et de manuels, largement considérée comme du piratage par l'industrie de l'édition |
| **Échelle globale** | « Des millions d'œuvres protégées » ont été reproduites, couvrant l'ensemble du catalogue de revues d'Elsevier, représentant des décennies de recherche universitaire |
| **Violation délibérée** | La plainte soutient que Meta savait exactement ce qu'elle faisait — entraîner des modèles d'IA sur de la littérature scientifique en accès payant sans accords de licence ni compensation pour les auteurs |

L'Association of American Publishers a publié une déclaration marquante : *« Cette affaire est la première action en matière d'IA intentée par de grandes maisons d'édition, qui ont leur propre histoire à raconter sur la violation flagrante de leurs droits par Meta. »*

## Pourquoi cette affaire est différente des précédents procès

Meta est déjà confrontée à une vague de litiges sur les droits d'auteur — des auteurs, des artistes visuels, des éditeurs de presse et même des labels de musique ont poursuivi l'entreprise au sujet des données d'entraînement. Mais l'angle d'Elsevier est **structurellement différent** pour plusieurs raisons :

### 1. Les articles scientifiques ne sont pas des romans

Contrairement aux romans d'Hachette ou de Macmillan, les articles scientifiques existent dans une **zone grise paratextuelle**. De nombreux articles ont des prépublications librement accessibles sur arXiv ou bioRxiv. Les auteurs conservent souvent leurs droits ou signent des licences non exclusives. Le statut juridique du scraping de résumés scientifiques est véritablement incertain — et la poursuite agressive d'Elsevier pourrait se retourner contre elle en poussant les tribunaux à définir ce que signifie réellement l'« usage loyal » (*fair use*) pour la littérature universitaire.

### 2. La connexion LibGen est explosive

LibGen n'est pas une archive en zone grise — c'est une bibliothèque pirate qui a été poursuivie, bloquée et ciblée pénalement dans plusieurs juridictions. S'il peut être démontré que Meta a sciemment téléchargé via torrent depuis LibGen — un site dont la *raison d'être* tout entière est la violation du droit d'auteur — cela affaiblit considérablement la défense d'« usage loyal ». Les éditeurs ont poursuivi avec succès LibGen pour 15 millions de dollars en 2017. Si Meta l'a utilisé, l'argument de l'« entraînement innocent » s'effondre.

### 3. La communauté scientifique observe de près

Ce procès crée un **conflit d'intérêts direct** pour la communauté scientifique. D'un côté, les chercheurs bénéficient énormément des grands modèles de langage qui comprennent la littérature scientifique — les modèles de type PubMedGPT, les agents de recherche documentaire et la révision par les pairs automatisée dépendent tous d'un entraînement sur des textes scientifiques. De l'autre, le modèle d'abonnement d'Elsevier signifie que ces mêmes articles sont verrouillés derrière des paywalls que les chercheurs contournent régulièrement.

Comme l'a écrit un commentaire de Nature sur le sujet : *« Votre article a-t-il été utilisé pour entraîner un modèle d'IA ? Presque certainement. »* La question est de savoir si cette utilisation constitue un vol — ou l'évolution naturelle de la diffusion du savoir.

## À quoi ressemblera la défense de Meta

Meta a déjà fait connaître sa position : **l'usage loyal**. Un porte-parole de l'entreprise a déclaré :

> « L'IA alimente des innovations transformatrices, la productivité et la créativité pour les particuliers et les entreprises, et les tribunaux ont estimé à juste titre que l'entraînement de l'IA sur du matériel protégé par le droit d'auteur peut relever du “fair use”. »

Cette défense repose sur quatre piliers :

- **Usage transformatif** : entraîner un modèle d'IA n'équivaut pas à reproduire un article pour des lecteurs
- **Absence de préjudice pour le marché** : les grands modèles de langage ne se substituent pas aux abonnements à des revues (on ne peut pas lire un article par le biais d'un LLM)
- **Intérêt public** : la compréhension scientifique par l'IA est un résultat bénéfique pour la société
- **Précédent sectoriel** : Google Books (Authors Guild v. Google, 2015) a établi que la numérisation de masse à des fins non expressives peut relever de l'usage loyal

Mais il y a un hic : Google Books a numérisé des textes pour qu'ils puissent être *consultés*, et non pour générer de nouveaux textes. Un grand modèle de langage qui reproduit des données d'entraînement (comme Llama l'a fait avec des passages d'Harry Potter, ainsi que cela a été montré) est plus difficile à défendre comme « transformatif ».

## Le contexte plus large : la course aux armements des données d'entraînement

Ce procès ne se déroule pas en vase clos. L'industrie de l'IA est confrontée à une **remise en question des données d'entraînement** :

| Développement récent | Impact |
|---|---|
| **Règlement de 1,5 milliard de dollars d'Anthropic** (2025) | A établi une référence pour les coûts de licence des données d'entraînement |
| **NYT v. OpenAI** (en cours) | Pourrait déterminer si le web scraping constitue une violation du droit d'auteur |
| **Recours collectifs d'artistes** (Stability AI, Midjourney) | Testent si l'entraînement sur de l'art visuel nécessite le consentement des artistes |
| **Mise en œuvre de l'EU AI Act** | Exige la transparence des données d'entraînement — difficile à respecter si l'on cache ses sources |
| **Elsevier contre Meta** (mai 2026) | Premier test majeur pour déterminer si l'édition scientifique bénéficie d'un statut particulier |

L'affaire Meta est particulièrement significative parce qu'elle touche au **cœur de l'IA open source**. Llama a été célébré comme « l'IA du peuple » — des poids ouverts que tout le monde peut télécharger, affiner et déployer. Mais si les données d'entraînement s'avèrent systématiquement contrefaites, chaque dérivé de Llama — des milliers de modèles affinés, de fusions et d'applications — hérite de ce risque juridique.

## Ce qu'il faut surveiller

1. **Les preuves concernant LibGen** — si la communication de pièces révèle un téléchargement systématique depuis des bibliothèques pirates, la défense d'usage loyal de Meta s'affaiblit considérablement
2. **L'exclusion de Common Crawl** — les éditeurs scientifiques pourraient exiger que Common Crawl filtre le contenu payant, réduisant la qualité des données d'entraînement des LLM dans tout le secteur
3. **Les expériences de licence** — nous pourrions voir l'émergence de licences d'entraînement pour l'IA dans l'édition scientifique, où les éditeurs facturent l'accès aux modèles par token
4. **La responsabilité des modèles open-weight** — les créateurs de modèles dérivés de Llama seront-ils également exposés à des revendications de droits d'auteur ?

## En résumé

L'entrée d'Elsevier dans le litige sur les droits d'auteur contre Meta marque une **nouvelle phase** dans la guerre des données d'entraînement de l'IA. L'édition scientifique a son propre paysage juridique complexe — mêlant droits d'auteur, licences d'éditeurs, normes de prépublication et mandats d'accès public. Une décision de justice dans ce domaine pourrait redéfinir les données d'entraînement disponibles pour les modèles d'IA open source, creusant potentiellement l'écart entre les modèles propriétaires bien financés (qui peuvent se permettre des licences) et les alternatives open-weight (qui dépendent de données récupérées sur le web).

Pour la communauté de l'IA open source, le message est clair : **l'ère de l'entraînement sur tout ce qui est disponible sur le web touche à sa fin.** Que ce soit par le biais de litiges, de législations ou de licences, les données d'entraînement deviennent une ressource réglementée — et les modèles de demain devront prouver d'où proviennent leurs connaissances.

Le feuilleton des droits d'auteur de Llama continue, et Elsevier vient de le rendre personnel pour chaque chercheur dont les articles ont pu être utilisés à son insu.