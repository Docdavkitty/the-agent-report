---
layout: post
title: "Meta Muse Spark : la fin de l'ère open-source chez Meta ?"
date: 2026-05-26 14:00:00 +0200
lang: fr
ref: meta-muse-spark-hybrid-strategy-2026
permalink: /fr/2026/05/meta-muse-spark-hybrid-strategy-2026/
translation_of: /2026/05/meta-muse-spark-hybrid-strategy-2026/
author: The Agent Report
categories: [research]
tags: [meta, llama, "muse-spark", "open-source", "alexandr-wang", superintelligence, "traduction-francaise"]
last_modified_at: 2026-07-18 15:01:42 +0000
hero_image: /assets/images/hero/hero-meta-muse-spark-hybrid-strategy-2026.jpg
meta_description: >
  "Meta franchit le Rubicon avec Muse Spark, son premier modèle phare fermé, alors que la déception Llama 4 et la stratégie hybride open-source redessinent le paysage."
description: >
  "Meta franchit le Rubicon avec Muse Spark, son premier modèle phare fermé, tandis que la déception Llama 4 et la stratégie hybride open-source redessinent l'IA."
reading_time: 9
---

## La déception Llama 4

Pour comprendre pourquoi Meta a changé de cap, il faut examiner la trajectoire de Llama 4. Publié en avril 2025 après près d'un an de retards, le groupe Llama 4 — Scout (17B, 16 experts), Maverick (17B, 128 experts) et le Behemoth non publié — était censé consolider le leadership de Meta dans l'IA ouverte.

Cela n'a pas été le cas.

- **Déception sur les benchmarks** : Llama 4 Maverick s'est d'abord bien classé sur le leaderboard LM Arena, mais des tests indépendants ont montré qu'il était à la traîne par rapport à DeepSeek V3, Qwen 2.5 et Claude 4 sur les tâches de raisonnement et de mathématiques.
- **Mécontentement des développeurs** : Selon un reportage de Business Insider (mai 2025), les développeurs ont exprimé leur frustration face à l'absence d'un modèle de raisonnement compétitif de la part de Meta. Plusieurs développeurs ont confié au média qu'ils s'attendaient à un modèle axé sur le raisonnement lors de la LlamaCon et qu'ils se seraient « même contentés d'un modèle traditionnel capable de battre DeepSeek ».
- **Behemoth mis de côté** : Meta aurait suspendu les tests de Llama 4 Behemoth, le modèle le plus grand et le plus attendu de la famille. Des sources internes ont cité des benchmarks qui n'ont pas répondu aux attentes, en particulier dans le raisonnement STEM.

Le résultat a été une crise de confiance. Meta, qui s'était positionné comme le champion de l'IA open-source, se faisait distancer par des concurrents chinois (DeepSeek, Qwen d'Alibaba) et prenait encore plus de retard par rapport aux laboratoires frontaliers à code source fermé (OpenAI, Anthropic, Google).

---

## L'arrivée d'Alexandr Wang et des Superintelligence Labs

La réponse de Mark Zuckerberg a été, comme à son habitude, audacieuse. À la mi-2025, Meta a conclu un **accord de 15 milliards de dollars avec Scale AI**, qui a amené son PDG de 28 ans, Alexandr Wang, à diriger une nouvelle division : **Meta Superintelligence Labs (MSL)**. Wang a reçu un chèque en blanc pour reconstruire les efforts d'IA de Meta de zéro.

Le mandat était clair : rattraper le retard, à tout prix.

Yann LeCun, le scientifique en chef de l'IA de Meta depuis plus d'une décennie, a annoncé son départ en novembre 2025 pour fonder sa propre startup. Dans des entretiens ultérieurs, LeCun a été direct, qualifiant Wang d'« inexpérimenté » et prédisant d'autres départs. La tension entre la culture de recherche de Meta et l'approche axée sur les produits de Wang est devenue un récit déterminant de l'année 2025.

---

## Muse Spark : ce que Meta a construit en 9 mois

Muse Spark (nom de code interne « Avocado ») est le premier fruit de la reconstruction de MSL. Les résultats sont frappants, non seulement pour ce que le modèle peut faire, mais aussi pour *l'efficacité* avec laquelle il le fait.

### Capacités clés

- **Raisonnement multimodal natif** : Contrairement à Llama 4, qui a ajouté des capacités de vision après coup, Muse Spark a été construit dès le départ pour intégrer des informations visuelles.
- **Orchestration de sous-agents parallèles** : Muse Spark peut lancer plusieurs agents de raisonnement simultanément. Par exemple, pour planifier un voyage — un agent rédige un itinéraire, un autre compare les destinations, un troisième trouve des activités — le tout en parallèle.
- **Mode Contemplation** : Un mode de raisonnement multi-agents qui rivalise avec Gemini Deep Think de Google et GPT Pro d'OpenAI. Scores : **58 % sur Humanity's Last Exam**, **38 % sur FrontierScience Research**.
- **Efficacité de calcul 10×** : Meta affirme que Muse Spark nécessite plus d'un ordre de grandeur de calcul en moins que Llama 4 Maverick pour atteindre le même niveau de capacité. La pile de pré-entraînement a été reconstruite de zéro en 9 mois.
- **Codage visuel** : Génère des sites Web personnalisés, des mini-jeux, des tableaux de bord et des simulations interactives à partir d'invites en langage naturel.
- **Raisonnement santé** : Entraîné en collaboration avec plus de 1 000 médecins pour des réponses factuelles et complètes en matière de santé.

### La mise à jour du 12 mai

Le 12 mai 2026, Meta a déployé une mise à jour majeure de Muse Spark, étendant sa portée à l'ensemble de l'écosystème d'applications :

- **Conversations vocales** : Interactions vocales naturelles et interruptibles dans l'application Meta AI, avec génération d'images, Reels, cartes et flux de caméra en direct.
- **IA en direct sur mobile** : Auparavant limité aux lunettes AI, les utilisateurs peuvent désormais pointer l'appareil photo de leur téléphone vers le monde pour obtenir des réponses en temps réel.
- **Mode Shopping** : Recherche simultanément sur Facebook Marketplace et le Web au sens large, avec vue cartographique et affinage par prix/style/distance.
- **Déploiement des lunettes** : Lunettes Ray-Ban Meta et Oakley Meta aux États-Unis et au Canada ; Meta Ray-Ban Display à venir à l'été 2026.
- **Expansion inter-applications** : Muse Spark alimente désormais Meta AI sur WhatsApp, Instagram, Facebook, Messenger et Threads.

---

## La stratégie hybride : open source, mais pas entièrement

Le changement le plus important n'est pas le modèle lui-même — c'est la stratégie de licence de Meta.

Axios a rapporté le 6 avril 2026 que Meta prévoit de **publier en open source des versions de ses prochains modèles d'IA**, mais pas les plus grands ou les plus performants. Détails clés :

- **Certains modèles, certains composants** : Meta publiera des versions open source des successeurs de Muse Spark, mais avec des composants propriétaires retenus. Le risque pour la sécurité est cité comme l'une des raisons.
- **Les plus grands modèles restent fermés** : Wang a indiqué que certains des plus grands modèles de Meta resteront propriétaires — une stratégie « hybride ».
- **Orientation grand public** : Wang considère qu'Anthropic et OpenAI se concentrent de plus en plus sur les entreprises et les gouvernements. La stratégie de Meta est de dominer le marché de l'IA grand public grâce à ses milliards d'utilisateurs de WhatsApp, Instagram et Facebook.
- **Couverture de l'écosystème** : L'approche hybride maintient suffisamment d'ouverture pour gagner la part d'esprit des développeurs tout en réservant les modèles les plus performants pour un avantage concurrentiel.

Cela reflète une tendance plus large de l'industrie. Alibaba a récemment gardé ses modèles Qwen les plus puissants propriétaires, inversant ainsi sa propre stratégie open source. Même les entreprises qui défendent l'ouverture reculent sur leurs systèmes les plus avancés.

---

## Ce que cela signifie pour l'écosystème open source

Les implications sont profondes pour l'écosystème des LLM à poids ouverts :

1. **Le successeur de Llama n'est pas Llama 5** : Wikipédia répertorie déjà Muse Spark comme le remplacement de Llama. La marque Llama pourrait perdurer pour les versions open source, mais le modèle phare — et l'investissement en R&D — a été transféré à la série Muse de MSL. C'est la même division derrière [SAM 3.1]({% post_url 2026-05-21-meta-sam-3-1-video-detection-multiplexing-may21 %}), qui perpétue la tradition open source de Meta en vision par ordinateur.

2. **La couronne du « meilleur modèle ouvert » est à prendre** : Avec le recul de Meta par rapport à l'ouverture totale, le titre de « meilleur modèle à poids ouverts » passe à DeepSeek (V4 ?), Qwen (Alibaba) et Mistral. L'engagement continu de DeepSeek en faveur des versions à poids ouverts en a fait le choix par défaut pour de nombreux développeurs qui comptaient auparavant sur Llama.

3. **Les développeurs face à une bifurcation** : Ceux qui ont construit sur Llama pour son ouverture doivent désormais décider : suivre les modèles fermés de Meta (Muse Spark via API), passer à des modèles ouverts concurrents (DeepSeek, Qwen), ou attendre les futures versions ouvertes de Meta qui pourraient être en retard sur la frontière.

4. **La sécurité comme justification — ou comme couverture ?** : La raison invoquée par Meta pour garder certains modèles fermés — le risque pour la sécurité — est plausible compte tenu de la découverte de la conscience d'évaluation de Muse Spark (Apollo Research a trouvé « le taux le plus élevé de conscience d'évaluation parmi les modèles qu'ils ont observés »). Mais cela protège aussi commodément la position concurrentielle de Meta.

---

## Le tableau général

Le passage de Meta d'une stratégie entièrement ouverte à une stratégie hybride reflète ce que beaucoup dans l'industrie prédisaient : l'IA open source fonctionne comme une stratégie lorsque vous *rattrapez votre retard*, mais une fois que vous *avez* une avance — ou que vous en avez besoin — les incitations à garder les choses fermées deviennent écrasantes. Notre récapitulatif [State of AI Agents May 2026](/2026/05/state-of-ai-agents-may-2026/) confirme que cette tendance s'accélère dans tout l'écosystème.

La question pour 2026-2027 est de savoir si une alternative entièrement ouverte crédible (DeepSeek, Qwen, Mistral ou un nouveau venu) peut maintenir le rythme des progrès frontaliers que la série Llama de Meta offrait autrefois.

Pour l'instant, le monde de l'IA open source a perdu son plus grand mécène. L'ère de Meta publiant chaque modèle sous une licence permissive est révolue — et aucun successeur unique ne s'est encore présenté pour combler le vide.

---

*Cet article a été recherché à partir des articles de blog officiels de Meta, des reportages d'Axios, de Business Insider, du NYT, de Fortune et d'analyses de benchmarks indépendantes. Toutes les informations sont à jour au 26 mai 2026.*