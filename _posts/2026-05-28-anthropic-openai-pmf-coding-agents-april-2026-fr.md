---
layout: post
title: "Anthropic et OpenAI trouvent enfin leur marché — grâce aux agents de codage"
date: 2026-05-28 09:00:00 +0200
lang: fr
ref: anthropic-openai-pmf-coding-agents-april-2026
permalink: /fr/2026/05/anthropic-openai-pmf-coding-agents-april-2026/
translation_of: /2026/05/anthropic-openai-pmf-coding-agents-april-2026/
author: The Agent Report
categories: [industry]
tags: [anthropic, openai, "product-market-fit", "coding-agents", "claude-code", codex, "ai-economics", "enterprise-ai", "traduction-francaise"]
last_modified_at: 2026-07-14 15:02:45 +0000
hero_image: /assets/images/hero/hero-anthropic-openai-pmf-coding-agents-april-2026.jpg
meta_description: >
  "Simon Willison estime qu'Anthropic et OpenAI ont trouvé un véritable marché grâce aux agents de codage comme Claude Code et Codex, alors que les prix entreprise évoluent vers les tarifs API."
description: >
  "Simon Willison estime qu'Anthropic et OpenAI ont trouvé un véritable marché grâce aux agents de codage comme Claude Code et Codex, alors que les prix évoluent."
reading_time: 9
---

# Anthropic et OpenAI ont enfin trouvé leur marché — et tout tourne autour des agents de codage

**28 mai 2026** — Les investissements massifs dans les infrastructures de l'IA commencent-ils enfin à porter leurs fruits ? Selon une [analyse approfondie](https://simonwillison.net/2026/May/27/product-market-fit/) de Simon Willison, la réponse est un **oui** retentissant — et le moteur n'est ni les chatbots, ni les générateurs d'images, mais les **agents de codage**.

L'article de Willison, qui a rapidement grimpé en tête de Hacker News avec plus de 830 points et 950 commentaires, soutient qu'avril 2026 marque un véritable point d'inflexion pour les laboratoires d'IA de pointe. « Je pense qu'ils ont enfin trouvé leur marché, avec les produits agents de codage/usage général incarnés par Claude Code/Cowork et Codex », écrit-il.

## Les clients entreprises paient désormais les prix de l'API

Le pilier de l'argumentation de Willison repose sur un changement sismique dans la façon dont Anthropic et OpenAI facturent leurs clients entreprises. À un moment donné au cours des six derniers mois, Anthropic est passé à une formule Entreprise à **20 $/siège/mois plus les prix de l'API selon l'utilisation**. OpenAI a suivi le mouvement en avril 2026, alignant la tarification de Codex sur les coûts des tokens d'API.

Il s'agit d'une rupture radicale avec les contrats d'entreprise à tarif forfaitaire qui caractérisaient l'ère 2024-2025. Désormais, les entreprises signant des contrats d'un an sont verrouillées sur les prix complets de l'API — **fini les remises importantes**.

> « Je suis actuellement abonné au plan Max à 100 $/mois d'Anthropic et au plan Pro à 100 $/mois d'OpenAI », note Willison. « Je viens d'exécuter l'outil ccusage sur mon ordinateur portable pour estimer ce que j'aurais dépensé si j'avais payé les tokens d'API au cours des 30 derniers jours, et j'obtiens 1 199,79 $ pour Anthropic Claude Code et 980,37 $ pour OpenAI Codex. »

Cela représente **2 180,16 $ de tokens pour 200 $** — et Willison se décrit comme un « utilisateur modérément intensif », pas quelqu'un qui fait tourner des agents 24 heures sur 24.

La tarification devient encore plus frappante si l'on considère les dernières versions de modèles. **GPT-5.5** (sorti le 23 avril) coûte 2× le prix de l'API de GPT-5.4. **Opus 4.7** (16 avril) tourne autour de 1,4× le prix d'Opus 4.6 en tenant compte d'un nouveau tokenizer. Les clients entreprises subissent un double effet : des prix de modèles plus élevés et la suppression des remises de volume.

## Pourquoi c'est une adéquation produit-marché

Willison établit une distinction cruciale entre popularité et rentabilité. ChatGPT compte plus de **900 millions d'utilisateurs actifs hebdomadaires**, mais seulement **50 millions** — soit 5,6 % — sont des abonnés payants.

« Facturer 10 à 20 $/mois par utilisateur est une activité correcte, mais il faudrait 1 à 2 milliards d'abonnés restant quatre ans pour couvrir 1 billion de dollars d'infrastructures », calcule-t-il.

Les agents de codage changent complètement cette équation. Ces outils consomment beaucoup plus de tokens que les interfaces de chat, mais ils deviennent rapidement **des outils quotidiens pour des professionnels extrêmement bien rémunérés**. Les entreprises dépensant **200 $/mois et plus par utilisateur** — ou dans le cas de Willison, utilisateur intensif, **~1 000 $/mois par fournisseur** — génèrent des revenus à une échelle qui peut compenser significativement les coûts d'infrastructure.

> « Les agents de codage ont vraiment tout changé. Ce sont des outils qui consomment beaucoup plus de tokens, mais qui deviennent aussi rapidement des outils quotidiens pour le travail de professionnels extrêmement bien rémunérés. »

Les modèles sortis en **novembre 2025** — GPT-5.1 et Opus 4.5 combinés à leurs environnements d'agents de codage respectifs — ont élevé les agents à un niveau d'utilité réelle. Nous avons maintenant six mois de recul pour que les organisations intègrent ces outils dans leurs flux de travail, et les dépenses suivent.

## La montée en puissance : les équipes commerciales entreprises recrutent massivement

Comme preuve supplémentaire, Willison pointe les offres d'emploi ouvertes chez les deux entreprises :

- **OpenAI** : 703 postes ouverts, dont **229 (32,6 %)** liés aux ventes et au support entreprises — responsables de comptes, rôles « Go To Market » et ingénieurs déployés sur le terrain.
- **Anthropic** : 390 postes ouverts, dont **105 (26,9 %)** dans des rôles orientés entreprises.

« Il est plaisamment ironique que ces laboratoires d'IA aient choisi un modèle économique avec une demande aussi forte en main-d'œuvre humaine — les contrats de vente aux entreprises ne se concluent pas sans une bonne dose d'humains dans l'équation ! », observe Willison.

Notons qu'il a réalisé cette analyse **en utilisant Claude Code lui-même** — en extrayant des sites d'emploi, en important les données dans Datasette Cloud et en analysant avec Datasette Agent. Du dogfooding à 100 %.

## Les histoires d'« échec de l'IA » sont en réalité des preuves de l'adéquation produit-marché

Le récit autour des entreprises « choquées » par leurs factures d'IA — notamment Uber qui aurait épuisé son budget IA annuel dès les premiers mois de 2026 — est en réalité **une preuve de la thèse de l'adéquation produit-marché**, pas l'inverse.

> « Le meilleur conseil que j'aie jamais entendu sur la tarification d'un produit est que votre client devrait aspirer l'air entre ses dents puis dire oui. Le dépassement de budget d'Uber et les annulations de licences de Microsoft ressemblent à cet effet en pratique. »

La décision de Microsoft d'annuler les licences Claude Code — officiellement pour encourager le dogfooding de Copilot CLI — aurait également été une décision financière déclenchée par la fin de l'exercice fiscal de Microsoft le 30 juin. Quand vos clients prennent des décisions d'allocation budgétaire d'un milliard de dollars concernant votre produit, vous avez trouvé l'adéquation produit-marché.

## L'accord Colossus change tout

Le point de données le plus stupéfiant vient peut-être d'une source inattendue : le **récent dépôt S-1 de SpaceX** a révélé qu'Anthropic a signé un accord pour des services cloud d'une valeur de **1,25 milliard de dollars par mois jusqu'en mai 2029** pour accéder à la capacité de calcul des clusters Colossus et Colossus II.

L'annonce d'Anthropic indiquait que cet accord leur permettrait « d'augmenter nos limites d'utilisation pour Claude Code et l'API Claude », suggérant fortement que Colossus est utilisé pour l'inférence, pas l'entraînement. Étant donné qu'Anthropic dispose déjà d'une vaste capacité de calcul auprès d'autres fournisseurs, la volonté de dépenser 1,25 milliard de dollars/mois auprès d'un seul fournisseur laisse entrevoir l'échelle énorme des budgets d'inférence aujourd'hui.

## Une histoire à deux points d'inflexion

Willison identifie deux points d'inflexion critiques :

1. **Novembre 2025** — Le point d'inflexion des *capacités*, lorsque GPT-5.1 et Opus 4.5, combinés à leurs environnements d'agents de codage, sont devenus véritablement utiles pour le travail réel.

2. **Avril 2026** — Le point d'inflexion des *revenus*, lorsque le changement de tarification entreprises et les impacts budgétaires qui en ont résulté ont clairement montré qu'il s'agit de véritables entreprises, pas seulement de projets de recherche.

> « Nous saurons avec certitude à quel point ce moment est réel lorsque les documents S-1 des prochaines introductions en bourse d'Anthropic et d'OpenAI nous donneront des chiffres réels et audités à analyser. »

## Ce que cela signifie pour l'écosystème des agents

Pour l'écosystème plus large des agents d'IA, les implications sont profondes :

- **Cursor et Copilot font face à une concurrence directe** des produits agents d'Anthropic et d'OpenAI. Pas étonnant que Cursor investisse dans ses propres modèles.
- **La tarification entreprises aux taux de l'API** signifie que le coût d'exécution des agents d'IA à grande échelle est désormais transparent et prévisible — mais coûteux.
- **L'écrasement des intermédiaires** est réel : Claude Code d'Anthropic concurrence directement les outils qui étaient auparavant les plus gros clients API d'Anthropic (Cursor et GitHub Copilot étaient apparemment responsables de 1,2 milliard de dollars des 4 milliards de dollars de revenus d'Anthropic en 2025).
- **Les fournisseurs d'infrastructure** (CoreWeave, Lambda, et maintenant SpaceX) deviennent critiques — et leurs propres introductions en bourse fourniront une visibilité sur l'échelle réelle de l'industrie de l'IA.

Pour les développeurs et les entreprises qui construisent sur des agents d'IA, le message est clair : l'ère de l'automatisation agentique bon marché et à tarif forfaitaire est révolue. Mais la valeur que ces outils apportent est désormais suffisamment prouvée pour que les organisations soient prêtes à payer le prix fort. Ce n'est pas un défaut — c'est l'adéquation produit-marché.

<p><em>Lire l'analyse originale complète : <a href="https://simonwillison.net/2026/May/27/product-market-fit/">« I think Anthropic and OpenAI have found product-market fit » par Simon Willison</a></em></p>