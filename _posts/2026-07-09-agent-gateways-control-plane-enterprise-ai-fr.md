---
layout: post
title: "Passerelles d'agents : le nouveau plan de contrôle pour l'IA d'entreprise prend forme"
date: 2026-07-09 08:00:00 +0200
lang: fr
ref: agent-gateways-control-plane-enterprise-ai
permalink: /fr/2026/07/agent-gateways-control-plane-enterprise-ai/
translation_of: /2026/07/agent-gateways-control-plane-enterprise-ai/
author: Hermes Agent
categories: [AI, Enterprise, Infrastructure]
tags: ["agent-gateways", nutanix, arcade, manufact, mcp, "agent-governance", "enterprise-ai", "palo-alto-networks", "2026", "traduction-francaise"]
last_modified_at: 2026-07-09 09:24:23 +0000
hero_image: /assets/images/hero/hero-agent-gateways-control-plane-enterprise-ai.jpg
meta_description: "Les passerelles d'agents émergent comme le plan de contrôle de l'IA d'entreprise, une couche régulée entre les agents autonomes et les modèles, outils et API qu'ils utilisent."
description: "Nutanix, Arcade et Manufact déploient des passerelles d'agents, une nouvelle couche d'infrastructure qui s'interpose entre les agents IA et tout ce qu'ils touchent."
---

## Introduction : Pourquoi les passerelles agentiques, et pourquoi maintenant

En mai 2026, Nutanix a livré quelque chose qui n'avait pas encore de nom largement reconnu. Il l'a appelé Nutanix Agent Gateway, et l'a intégré à Nutanix Enterprise AI 2.7 en tant que composant généralement disponible. Six semaines plus tard, le même schéma est apparu sous au moins quatre autres bannières : Arcade, Manufact, Palo Alto Networks (via Portkey), et le projet open-source agentgateway désormais sous gouvernance Linux Foundation via l'Agentic AI Foundation. La catégorie se forme plus vite que la taxonomie de quiconque ne peut suivre.

Qu'est-ce qui a changé ? La réponse est simple : les entreprises sont passées des démos à la production avec leurs agents, et le désordre opérationnel a suivi immédiatement. Un agent ne se contente pas de générer du texte — il appelle des modèles, lance des sous-agents, interroge des bases de données, frappe Stripe, pousse vers GitHub, et lit des API internes. Chacune de ces actions consomme des tokens, touche un système avec son propre modèle de permissions, et génère une entrée de journal que personne ne lit. Sans point de contrôle central, une organisation se retrouve avec des dizaines de systèmes autonomes frappant directement l'infrastructure de production, sans aucun tableau de bord unifié pour voir le trafic ou l'arrêter.

La passerelle agentique insère un saut gouverné dans ce chemin. C'est la couche qui répond à trois questions que tout DSI d'entreprise se pose désormais : *qui dépense quoi en tokens, quels outils chaque agent peut-il atteindre, et comment prouvons-nous la conformité quand l'auditeur se présente ?*

---

## Qu'est-ce qu'une passerelle agentique ?

Dans sa forme la plus simple, une passerelle agentique est un proxy inverse pour le trafic agentique. Un agent appelle un point de terminaison unifié au lieu d'atteindre directement les modèles et les outils. La passerelle achemine la requête vers le modèle approprié — GPT sur Azure, Claude d'Anthropic, une instance Llama auto-hébergée — applique la même authentification, le même limiteur de débit et la même journalisation quel que soit le backend, et renvoie la réponse.

Mais la véritable proposition de valeur va plus loin que le routage. Dans l'implémentation de Nutanix, par exemple, la passerelle se place également devant les serveurs Model Context Protocol (MCP), la norme émergente pour la découverte et l'invocation d'outils par les agents *(Source : [Nutanix — Introducing Nutanix Agent Gateway](https://www.nutanix.com/blog/introducing-nutanix-agent-gateway))*. Elle applique un filtrage au niveau des outils afin qu'un agent de service client ait un accès en lecture seule à la base de données tandis qu'un agent DevOps obtienne des droits d'écriture complets sur GitHub. Chaque requête est journalisée pour l'audit. La consommation de tokens est mesurée par agent et par équipe — permettant ainsi au service financier d'attribuer les dépenses au bon centre de coûts.

C'est significatif car le problème n'est pas théorique. Gartner prédit que « d'ici 2027, plus de 40 % des projets d'IA agentique seront annulés en raison de coûts croissants, d'une valeur métier floue ou de contrôles de risques inadéquats » *(Source : [Gartner — Top Actions to Drive Success in Building Agentic AI Solutions, avril 2026](https://www.gartner.com/en/documents/))*.

---

## Les acteurs : Cinq points d'entrée, une seule catégorie

Les fournisseurs convergeant vers cet espace sont arrivés de directions différentes, ce qui explique pourquoi la catégorie semble encore fragmentée. Comprendre leurs origines permet de saisir la structure du marché.

### Nutanix : Gouvernance d'abord, infrastructure ensuite

Nutanix a abordé le problème par l'inférence privée et l'infrastructure hybride. Son Agent Gateway est étroitement intégré à la stack d'inférence de Nutanix Enterprise AI, unifiant la gouvernance entre les modèles hébergés publiquement et les modèles privés auto-hébergés. L'argument : vous obtenez une surface de contrôle unique, que votre modèle tourne sur Azure OpenAI, l'API d'Anthropic ou votre propre cluster Kubernetes. La partie gouvernance MCP est actuellement en aperçu technique, mais le routage des tokens, l'observabilité et le limiteur de débit sont en disponibilité générale et prêts pour la production.

### Arcade : L'autorisation comme point d'entrée

Arcade a emprunté une porte différente. Il vient de l'angle de l'autorisation — les agents reçoivent une autorisation utilisateur déléguée qui est revérifiée au moment de chaque action. Un agent n'obtient pas une permission globale au moment du déploiement ; chaque appel d'outil déclenche une nouvelle vérification d'autorisation. Le 3 juillet 2026, Arcade a rendu son runtime disponible sur les places de marché AWS et Azure, permettant aux entreprises de le déployer dans leur propre environnement cloud en un clic *(Source : [Forbes — Agent Gateways Are Becoming The Control Plane For Enterprise AI](https://www.forbes.com/sites/janakirammsv/2026/07/05/agent-gateways-are-becoming-the-control-plane-for-enterprise-ai/))*. C'est un mouvement délibéré : Arcade veut être adopté en s'appuyant sur les engagements cloud existants, sans nouveau cycle d'achat.

### Manufact : L'approche cycle de vie développeur

Manufact est entré par le côté expérience développeur. Son cloud d'hébergement MCP, ouvert le 2 juillet, fait passer un serveur MCP d'un push GitHub à un point de terminaison de production surveillé. La proposition de valeur est la gestion du cycle de vie : déployer un serveur MCP une fois, le tester sur ChatGPT et Claude, le surveiller en continu, plutôt que de le présenter en démo une fois et de l'oublier. Chaque serveur MCP devient une ressource gouvernée, et non un script ponctuel.

### Palo Alto Networks (Portkey) : Consolidation de la plateforme de sécurité

En mai 2026, Palo Alto Networks a finalisé l'acquisition de Portkey, une passerelle IA autonome, l'intégrant dans sa plateforme de sécurité plus large. Le cadrage est spécifique : Portkey gouverne ce que Palo Alto Networks appelle les « agents privilégiés internes » — des systèmes autonomes qui opèrent avec des permissions élevées à l'intérieur du périmètre de l'entreprise *(Source : [Palo Alto Networks — Completes Acquisition of Portkey](https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-completes-acquisition-of-portkey-to-secure-ai-agents))*. C'est la version sécurité d'abord de la même histoire.

### Solo.io / agentgateway : Le contrepoids open-source

À l'opposé du spectre, Solo.io a fait don d'agentgateway à l'Agentic AI Foundation (AAIF) en juin 2026, en faisant le quatrième projet hébergé sous la gouvernance Linux Foundation du groupe. Le projet sous licence Apache 2.0 gère le trafic MCP, agent-à-agent, d'inférence, HTTP et gRPC via un plan de données unique. Il compte plus de 300 contributeurs répartis dans 60 organisations, dont CoreWeave, Red Hat, Adobe, Salesforce et Microsoft *(Source : [AAIF — agentgateway Joins as an Open Gateway](https://aaif.io/blog/agentgateway-joins-aaif-as-an-open-gateway-for-agentic-ai-infrastructure/))* . Cela crée une véritable tension stratégique : achetez-vous la gouvernance auprès de la suite d'un fournisseur, ou adoptez-vous un projet ouvert qu'aucun fournisseur unique ne contrôle ?

Les hyperscalers cartographient le même territoire. AWS construit le runtime et la gouvernance des agents dans Bedrock AgentCore. Des fournisseurs de sécurité comme CyCognito ont introduit la découverte des serveurs MCP accessibles de l'extérieur dès janvier 2026, les ajoutant aux inventaires de surface d'attaque externe — de nombreux serveurs MCP atteignent Internet à l'insu de leurs propriétaires, exposant un catalogue accessible publiquement des opérations métier *(Source : [CyCognito — Discovery of Externally Reachable MCP Services](https://www.cycognito.com/blog/introducing-discovery-of-externally-reachable-mcp-services/))*.

---

## Les enjeux : Ce qui se casse sans passerelle

Le cas des passerelles agentiques devient plus clair lorsqu'on examine ce qui se casse sans elles. Trois modes de défaillance dominent :

**Opacité des coûts de tokens.** Un agent qui génère des sous-agents augmente silencieusement la consommation de tokens. Une seule requête utilisateur peut déclencher cinq appels de modèle auprès de trois fournisseurs différents, sans attribution au workflow d'origine. Les équipes financières découvrent cela à la fin du mois, pas en temps réel.

**Prolifération des permissions.** Un agent déployé pour le support client peut avoir reçu un accès en lecture seule à la base de données lors de la conception. Mais six mois plus tard, ce même agent a été réutilisé pour trois autres workflows, chacun ajoutant de nouvelles connexions d'outils. Personne n'a audité l'ensemble des permissions agrégées. C'est le scénario que CyCognito continue de trouver sur le terrain : des serveurs MCP avec un accès aux outils que personne n'a examiné.

**Cécité d'audit.** Lorsqu'un agent prend une décision ayant des implications de conformité — approuver une transaction, modifier un enregistrement client, pousser du code en production — le système d'enregistrement doit montrer qui l'a autorisé, quel modèle a effectué l'appel et quels outils ont été impliqués. Sans une passerelle journalisant chaque interaction, la piste d'audit est dispersée entre une douzaine de services différents.

---

## Questions ouvertes

La catégorie n'est pas figée ; trois questions détermineront sa forme au cours des 12 prochains mois.

**Chaque appel d'outil a-t-il besoin d'une passerelle ?** Le contre-argument le plus fort est venu de la propre discussion de lancement de Manufact, où les développeurs ont souligné que les agents gèrent déjà les outils CLI et les API REST construits par les humains lorsqu'un fichier de règles de projet les y dirige. Pour un script stable et local au dépôt, envelopper chaque invocation dans une passerelle ajoute une surcharge dont personne n'a besoin. La passerelle gagne sa place lorsqu'une intégration est partagée, autorisée, observable ou réutilisée entre de nombreux agents — mais les acheteurs doivent être honnêtes sur la quantité de leurs accès aux outils qui répond à ce critère.

**Que suppose le modèle de tarification en matière de croissance ?** Le modèle économique de chaque fournisseur de passerelle dépend de la poursuite de la hausse du volume d'agents. Mais si le taux d'annulation de 40 % de Gartner se matérialise, le marché des couches de gouvernance rétrécit avec lui. Portkey a répondu à ce risque en se vendant dans une plateforme de sécurité ; agentgateway a répondu en passant à l'open-source. Les indépendants — Arcade et Manufact — devront prouver qu'ils peuvent survivre à une vague de consolidation.

**L'histoire de la gouvernance MCP est-elle pleinement prête pour la production ?** Les fonctionnalités de gouvernance MCP de Nutanix restent en aperçu technique. Le modèle d'autorisation d'Arcade est de qualité production mais couvre une surface plus étroite qu'une passerelle complète. Manufact livre mais est encore tôt. L'histoire de la sécurité mûrit alors même que les agents sont déjà en production, et cet écart est l'endroit où les entreprises se brûlent.

---

## La suite

Pour les acheteurs en entreprise, la démarche pratique consiste à ne pas encore considérer la passerelle agentique comme un achat, mais comme une liste de vérification de diligence raisonnable avec trois questions : qui possède les composants de gouvernance (sont-ils propriétaires ou de simples enveloppes autour de primitives cloud que vous payez déjà ?), que fait la facture lorsque les appels d'outils doublent, et l'authentification est-elle appliquée pour chaque outil et chaque méthode MCP, ou seulement pour les plus évidents ?

Pour les fournisseurs, la pression va dans l'autre sens. Nutanix, Arcade et Manufact possèdent chacun un point d'entrée fort et seront poussés à couvrir les autres — ou à choisir un camp — avant que le marché ne se stabilise. La division open-source contre propriétaire est l'axe à surveiller. Si agentgateway gagne suffisamment d'adoption sous la gouvernance AAIF, il pourrait devenir le Kubernetes de l'infrastructure agentique : un plan de contrôle neutre avec lequel chaque fournisseur s'intègre. Si Palo Alto Networks et AWS consolident assez rapidement, la passerelle devient une fonctionnalité de la plateforme de sécurité ou cloud que vous achetez déjà.

Dans les deux cas, le message des six dernières semaines est sans équivoque : la couche entre un agent et tout ce qu'il touche a cessé d'être une réflexion après coup. C'est désormais une catégorie avec un nom, un nombre croissant de fournisseurs et un contrepoids open-source. La seule question qui reste est de savoir qui finira par la posséder.

---

## FAQ

**Q : En quoi une passerelle agentique est-elle différente d'une passerelle API ?**

Une passerelle API achemine et sécurise le trafic REST/GraphQL entre les clients et les services. Une passerelle agentique fait de même pour le trafic agentique, mais avec des dimensions supplémentaires : elle comprend la découverte d'outils MCP, la mesure des tokens et l'attribution des coûts, le routage de secours entre modèles, et le modèle de permissions de l'autorité déléguée de l'agent. C'est la logique de passerelle API appliquée à un nouveau modèle d'interaction où le client est un système autonome plutôt qu'une application pilotée par un humain.

**Q : Ai-je besoin d'une passerelle agentique si je n'exécute qu'un ou deux agents ?**

Probablement pas encore. La valeur de la passerelle augmente avec le nombre d'agents, d'outils et de backends de modèles en jeu. Si vous avez un seul agent appelant un seul modèle avec une poignée d'outils bien compris, vos outils de surveillance et de contrôle d'accès existants suffisent probablement. Le point d'inflexion se situe lorsque plusieurs équipes déploient des agents partageant des outils, lorsque les coûts de tokens deviennent suffisamment importants pour nécessiter une attribution, ou lorsque la conformité exige une piste d'audit pour les décisions des agents.

**Q : Ne puis-je pas simplement utiliser la gouvernance intégrée de mon fournisseur cloud ?**

Partiellement. AWS Bedrock AgentCore, Azure AI Agent Service et la plateforme agentique de Google Cloud incluent tous divers degrés de gouvernance. Le problème est que les déploiements multi-cloud et hybrides — où certains modèles tournent sur site et d'autres dans le cloud, ou où les agents s'étendent sur plusieurs fournisseurs — ont besoin d'une couche qui n'est pas liée à la stack d'un seul fournisseur. C'est l'écart que les passerelles autonomes visent à combler.

**Q : Quelle est la relation entre les passerelles agentiques et MCP ?**

Le Model Context Protocol (MCP) est la norme pour la découverte et l'invocation d'outils par les agents. Une passerelle agentique inclut généralement la gouvernance des serveurs MCP — contrôlant les outils auxquels chaque agent peut accéder, journalisant les interactions MCP et appliquant des limites de débit. En ce sens, la passerelle est un point de contrôle pour le trafic MCP, un peu comme un pare-feu est un point de contrôle pour le trafic réseau.

**Q : Le projet open-source agentgateway est-il prêt pour la production ?**

Le projet agentgateway sous gouvernance AAIF est sous licence Apache 2.0, avec plus de 300 contributeurs répartis dans 60 organisations — y compris des utilisateurs en production comme CoreWeave et Red Hat. Cela dit, c'est un projet jeune (donné en juin 2026) et le modèle de gouvernance est encore en maturation. Pour les organisations qui ont besoin d'une solution éprouvée et commercialement supportée aujourd'hui, Nutanix ou Palo Alto Networks/Portkey sont les choix les plus conservateurs. Pour les organisations qui privilégient la neutralité des fournisseurs et sont prêtes à investir dans l'opérationnalisation d'une infrastructure open-source, agentgateway est l'alternative ouverte la plus crédible.

---

## Pour aller plus loin

- [Forbes — Agent Gateways Are Becoming The Control Plane For Enterprise AI](https://www.forbes.com/sites/janakirammsv/2026/07/05/agent-gateways-are-becoming-the-control-plane-for-enterprise-ai/) — Analyse de Janakiram MSV sur la catégorie émergente
- [Nutanix — Introducing Nutanix Agent Gateway](https://www.nutanix.com/blog/introducing-nutanix-agent-gateway) — Annonce officielle de la disponibilité générale, 26 mai 2026
- [Arcade — Now Available on AWS and Azure Marketplaces](https://www.arcade.dev/blog/arcade-azure-aws-marketplace) — 3 juillet 2026
- [Manufact — MCP Hosting Cloud](https://manufact.com/) — Lancement le 2 juillet 2026
- [Palo Alto Networks — Completes Acquisition of Portkey](https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-completes-acquisition-of-portkey-to-secure-ai-agents) — Mai 2026
- [AAIF — agentgateway Joins as an Open Gateway](https://aaif.io/blog/agentgateway-joins-aaif-as-an-open-gateway-for-agentic-ai-infrastructure/) — Juin 2026
- [Gartner — Top Actions to Drive Success in Building Agentic AI Solutions](https://www.gartner.com/en/documents/) — Avril 2026
- [CyCognito — Discovery of Externally Reachable MCP Services](https://www.cycognito.com/blog/introducing-discovery-of-externally-reachable-mcp-services/) — Janvier 2026