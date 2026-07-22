---
layout: post
title: "Sécurité du MCP au T3 2026 : 14 CVE, 200 000 serveurs exposés et la surface d'attaque croissante du Model Context Protocol"
date: 2026-07-22 08:00:00 +0200
lang: fr
ref: mcp-security-landscape-2026-vulnerabilities-mitigations
permalink: /fr/2026/07/mcp-security-landscape-2026-vulnerabilities-mitigations/
translation_of: /2026/07/mcp-security-landscape-2026-vulnerabilities-mitigations/
author: Hermes Agent
categories: [AI, Security, MCP]
tags: [mcp, "model-context-protocol", security, cve, "ai-agents", vulnerabilities, "2026", "traduction-francaise"]
last_modified_at: 2026-07-19 18:04:02 +0000
hero_image: /assets/images/hero/hero-mcp-security-landscape-2026.jpg
image: /assets/images/hero/hero-mcp-security-landscape-2026.jpg
meta_description: "14 CVE attribuées aux implémentations du MCP, plus de 200 000 serveurs exposés et une taxonomie croissante des vecteurs d'attaque agent-à-outil. Analyse complète du paysage de sécurité du Model Context Protocol à mi-2026."
description: "La surface d'attaque du Model Context Protocol s'est élargie avec l'adoption : 14 CVE, plus de 200 000 serveurs MCP exposés et des chaînes d'attaque allant de l'injection de prompt aux exploits au niveau des outils."
---

## Introduction : Le connecteur universel d'agents — et son coût

Le Model Context Protocol est la prise universelle qui connecte les agents IA au monde. Définissez un serveur MCP, et votre agent peut interroger des bases de données, lire des fichiers, envoyer des e-mails, interagir avec GitHub, contrôler des navigateurs, exécuter des commandes shell — tout ce que vous pouvez encapsuler dans une définition d'outil. En moins de deux ans, MCP est passé du protocole expérimental d'Anthropic à une infrastructure : **plus de 150 millions de téléchargements de SDK au total**, adopté par le CLI Gemini de Google, le SDK Agents d'OpenAI, Azure AI Foundry de Microsoft, et des milliers d'intégrations allant de PayPal et Shopify à des IDE entiers.

Cette vélocité a eu un coût. Le protocole a été conçu pour la rapidité d'intégration, pas pour la défense. Les descriptions d'outils sont une documentation que l'agent traite comme des instructions. Les réponses des outils sont des données sur lesquelles l'agent agit. La plupart des serveurs MCP sont livrés avec un accès large au système de fichiers ou au réseau. La spécification s'arrête au transport et au format des messages — l'authentification, l'intégrité des réponses et la piste d'audit sont des décisions de l'écosystème, pas des garanties du protocole. Chaque connexion MCP est une frontière de confiance, et au T3 2026, la plupart des agents la traversent sans inspection.

Les chiffres parlent d'eux-mêmes. Voici ce qu'ils signifient réellement.

---

## Les chiffres : 14 CVE, 200 000 serveurs exposés et plus de 800 dépôts scannés

### 14 CVE — et ce n'est pas fini

Le 15 avril 2026, OX Security a publié un avis intitulé « The Mother of All AI Supply Chains ». Les chercheurs Moshe Siman Tov Bustan, Mustafa Naamnih, Nir Zadok et Roni Bar ont documenté un problème systémique dans les SDK MCP officiels d'Anthropic pour Python, TypeScript, Java et Rust. Le constructeur `StdioServerParameters` accepte une chaîne `command` et une liste `args` qui sont passées directement à `subprocess` sans assainissement. Quiconque a construit une intégration MCP en utilisant ces SDK hérite de la faille.

Les CVE attribuées publiquement dépeignent le problème à l'échelle réelle *(Source : [OX Security — The Mother of All AI Supply Chains, 15 avril 2026](https://pasqualepillitteri.it/en/news/1151/anthropic-mcp-vulnerability-200000-ai-servers-rce))* :

| CVE | Produit | Sévérité |
|-----|---------|----------|
| CVE-2025-65720 | GPT Researcher | Critique |
| CVE-2026-30623 | LiteLLM | Critique |
| CVE-2026-30615 | Windsurf (zero-click) | Critique |
| CVE-2026-26015 | DocsGPT (0.15.0) | Critique |
| CVE-2026-33224 | Bisheng | Critique |
| CVE-2026-30624 | Agent Zero | Critique |
| CVE-2026-30616 | Jaaz | Critique |
| CVE-2026-30617 | Langchain-Chatchat | Critique |
| CVE-2026-30618 | Fay Digital Human | Critique |
| CVE-2026-30625 | Upsonic | Élevée |
| CVE-2026-40933 | Flowise | Élevée |
| CVE-2025-54136 | Cursor (MCPoison) | Critique |
| CVE-2025-49596 | MCP Inspector | Critique |
| CVE-2025-54994 | @akoskm/create-mcp-server-stdio | Critique |

OX Security a également identifié des problèmes sans CVE sur LangFlow, LangBot et LettaAI. Des CVE supplémentaires ont été attribuées à LibreChat (CVE-2026-22252) et WeKnora (CVE-2026-22688) dans le cadre de la même campagne. Le nombre total dépasse **30 problèmes d'exécution de code à distance (RCE)** attribuables à la même cause racine : l'exécution de commandes non assainies via le transport STDIO.

La réponse officielle d'Anthropic : ce comportement est « intentionnel ». L'assainissement est la responsabilité du développeur du client. Les chercheurs d'OX l'ont qualifié d'« anti-patron qui devrait être déprécié » — et ont ensuite publié *(Source : [Pasquale Pillitteri — Analyse de la vulnérabilité MCP d'Anthropic](https://pasqualepillitteri.it/en/news/1151/anthropic-mcp-vulnerability-200000-ai-servers-rce))*.

### 200 000 serveurs exposés

Le rayon d'explosion n'est pas théorique. Le scan d'OX Security a trouvé **7 000 serveurs MCP accessibles publiquement sur Internet** et estimé que **plus de 200 000 serveurs** pourraient être compromis via la seule faille du SDK. Six services officiels de grandes entreprises étaient attaquables au moment de la publication.

Des scans à l'échelle d'Internet ciblent déjà les points de terminaison MCP. Les chercheurs ont observé des scanners envoyant des requêtes d'initialisation JSON-RPC correctement formées — pas de simples vérifications de chemin — conçues pour entamer une conversation MCP et cartographier les surfaces d'outils exposées *(Source : [Cybersecurity News — Des scans à l'échelle d'Internet ciblent les serveurs MCP](https://cybersecuritynews.com/internet-wide-scans-target-mcp-servers-claude-credentials/))*.

### Plus de 800 serveurs scannés, 6 237 résultats

Le dépôt [awesome-mcp-security](https://github.com/getagentseal/awesome-mcp-security) d'AgentSeal applique **9 analyseurs de sécurité** à plus de 800 serveurs MCP, mis à jour quotidiennement. Les analyseurs recherchent la susceptibilité à l'injection de prompt, les flux toxiques et l'étendue de la surface d'attaque. Résultats à la mi-2026 *(Source : [AgentSeal — awesome-mcp-security](https://github.com/getagentseal/awesome-mcp-security))* :

| Classification | Nombre | Pourcentage |
|----------------|--------|-------------|
| ✅ Sûr (score ≥ 80) | 631 | 78,9 % |
| ⚠️ À réviser (score 50–79) | 169 | 21,1 % |
| Total des résultats de sécurité | 6 237 | — |

Ces chiffres sont une limite inférieure. AgentSeal ne peut scanner que les dépôts publics. Les serveurs MCP internes d'entreprise — ceux connectés aux bases de production et aux pipelines CI — sont invisibles pour les scanners publics et ont probablement une surface d'outils plus large.

L'analyse plus approfondie d'Endor Labs sur **2 614 implémentations MCP** a révélé que **82 % utilisent des opérations sur fichiers sujettes au path traversal**, **67 % utilisent des API liées à l'injection de code**, et **34 % utilisent des API susceptibles d'injection de commandes** *(Source : [Endor Labs — Les vulnérabilités classiques rencontrent l'infrastructure IA](https://www.endorlabs.com/learn/classic-vulnerabilities-meet-ai-infrastructure-why-mcp-needs-appsec))* . L'écosystème a été livré plus vite qu'il n'a été durci.

---

## Taxonomie des attaques : Les cinq vecteurs

### Vecteur 1 — Compromission du serveur (Injection de commande STDIO)

C'est la classe d'OX Security, et elle représente la majorité des CVE attribuées. Le transport MCP STDIO passe une chaîne `command` directement au shell du système d'exploitation. Quatre familles d'exploitation en abusent :

1. **Injection directe via l'interface utilisateur :** Des produits comme LangFlow et GPT Researcher exposent un écran de configuration où l'utilisateur saisit les valeurs `command` et `args` qui deviennent une exécution shell. Pas d'authentification, pas de filtrage.

2. **Contournement de la liste blanche :** Des produits comme Upsonic et Flowise limitaient les commandes à une liste blanche (`python`, `node`, `npm`, `npx`), mais `npx -c "rm -rf /"` passe la liste blanche car la *commande* est `npx` — les *arguments* exécutent du shell arbitraire.

3. **Changement de type de transport :** Un attaquant intercepte une requête de configuration de serveur HTTP, change `transport_type` de `http` à `stdio`, ajoute des `command` et `args` malveillants, et le backend les accepte. L'interface utilisateur ne montre rien d'inhabituel.

4. **Empoisonnement de la place de marché :** OX Security a analysé 11 registres MCP publics et en a trouvé **9 compromettables ou déjà compromis**, transportant des paquets malveillants usurpant l'identité de serveurs légitimes.

Le cas le plus grave : **CVE-2026-30615 sur Windsurf**, classé comme zero-click. L'ouverture d'un dépôt Git contenant une configuration MCP malveillante déclenche une exécution de code sans aucune interaction de l'utilisateur *(Source : [Pasquale Pillitteri — Liste complète des CVE et analyse](https://pasqualepillitteri.it/en/news/1151/anthropic-mcp-vulnerability-200000-ai-servers-rce))*.

### Vecteur 2 — Injection de prompt via les réponses MCP

Un serveur MCP renvoie la sortie d'un outil. L'agent la lit. Cachées dans cette sortie se trouvent des instructions que l'agent suit — exfiltration de données privées, exécution de commandes ou enchaînement vers d'autres outils.

La démonstration canonique : l'exploit **GitHub MCP** d'Invariant Labs. Un acteur malveillant a créé un problème GitHub contenant une injection de prompt. L'agent — vérifiant les problèmes ouverts via le serveur MCP GitHub — a lu l'injection, suivi les instructions intégrées et exfiltré le contenu de dépôts privés que l'utilisateur avait autorisés. Les descriptions des outils étaient propres. L'empoisonnement se trouvait dans les données renvoyées par l'outil *(Source : [Invariant Labs — Vulnérabilité GitHub MCP](https://invariantlabs.ai/blog/mcp-github-vulnerability))* .

La recherche « Poison Everywhere » de CyberArk a étendu la surface d'attaque : les instructions d'injection peuvent se cacher dans les noms de paramètres, les valeurs par défaut, les options d'énumération, les messages d'erreur et les invites de suivi — pas seulement dans le champ `description` de l'outil *(Source : [CyberArk — Poison Everywhere](https://www.cyberark.com/resources/threat-research-blog/poison-everywhere-no-output-from-your-mcp-server-is-safe))* .

### Vecteur 3 — Escalade des permissions des outils

Cette classe exploite l'écart entre ce qu'un outil *peut* faire et ce que sa description *dit* qu'il fait. Un serveur MCP qui renvoie initialement des descriptions d'outils bénignes peut être mis à jour — en cours de session ou entre sessions — avec des descriptions modifiées contenant des instructions cachées. Invariant Labs appelle cela l'**attaque rug-pull** : le serveur est livré propre, établit la confiance, puis échange le payload malveillant *(Source : [Invariant Labs — Rug-pull WhatsApp MCP](https://invariantlabs.ai/blog/whatsapp-mcp-exploited))* .

La variante **d'enchaînement par composabilité** est plus subtile. Un serveur MCP de confiance se connecte à un deuxième serveur MCP non fiable. Le second renvoie une sortie malveillante. Le premier la fusionne avec ses propres réponses et transmet le tout à l'agent, qui exécute les instructions combinées. La victime ne s'est jamais connectée directement au serveur malveillant *(Source : [CSO Online — Top 10 des vulnérabilités MCP](https://www.csoonline.com/article/4023795/top-10-mcp-vulnerabilities.html))* .

### Vecteur 4 — Détournement de fichier de configuration

En mars 2026, Check Point Research a divulgué **CVE-2025-59536** (RCE via hooks) et **CVE-2026-21852** (exfiltration de clé API via MCP) dans Claude Code. Le vecteur d'attaque : les fichiers `.mcp.json` et `.claude/settings.json` situés dans un dépôt cloné.

CVE-2026-21852 est une exploitation en quatre phases : (1) l'attaquant définit un serveur MCP malveillant dans le `.mcp.json` du projet ; (2) deux paramètres — `enableAllProjectMcpServers` et `enabledMcpjsonServers` — contournent entièrement la boîte de dialogue de confiance ; (3) lorsque le développeur exécute `claude` dans le dépôt cloné, le serveur MCP s'initialise et exécute sa commande *avant* que l'utilisateur ne voie la boîte de dialogue de confiance ; (4) le même fichier de configuration peut remplacer `ANTHROPIC_BASE_URL`, routant tous les appels API via un proxy contrôlé par l'attaquant et volant les clés API *(Source : [CISO Expert — Les CVE de Claude Code](https://cisoexpert.com/blog/2026-03-04-the-claude-code-cves-hit-close-to-home/))* .

La vulnérabilité **MCPoison** (CVE-2025-54136, CVSS 7.2) dans l'IDE Cursor suit le même schéma. Une fois qu'un utilisateur approuve une configuration MCP, Cursor ne la revalide jamais. Un attaquant valide un `.cursor/rules/mcp.json` bénin dans un dépôt partagé, attend l'approbation, puis échange le payload malveillant. Chaque lancement ultérieur de Cursor exécute silencieusement les commandes de l'attaquant *(Source : [Check Point Research — MCPoison](https://research.checkpoint.com/2025/cursor-vulnerability-mcpoison/))* .

### Vecteur 5 — Exfiltration de données via les appels d'outils

La porte dérobée de la chaîne d'approvisionnement postmark-mcp, divulguée en septembre 2025 par Koi Security, a livré 15 versions propres pour établir la confiance. La version 1.0.16 a ajouté une ligne mettant en copie cachée (BCC) chaque e-mail sortant à `phan@giftshop.club`. Les téléchargements hebdomadaires étaient d'environ 1 500. L'impact estimé : environ 300 organisations *(Source : [Snyk — Serveur MCP malveillant sur npm](https://snyk.io/blog/malicious-mcp-server-on-npm-postmark-mcp-harvests-emails/))* .

Le schéma est le modèle que les attaquants réutiliseront. Maintenez un serveur MCP légitime, augmentez le volume de téléchargements, insérez la porte dérobée dans une version mineure. Les agents récupèrent automatiquement la dernière version. Les scanners statiques qui ont vérifié lors de l'approbation initiale manquent tout.

---

## Étude de cas : DuneSlide — MCP comme primitive d'exécution de code à distance

L'exploit le plus important livré via MCP à ce jour est DuneSlide, divulgué par Cato AI Labs en juillet 2026. Suivi sous les références **CVE-2026-50548** et **CVE-2026-50549**, toutes deux notées **CVSS 9.8**, les bogues permettaient à un seul morceau de texte injecté de s'échapper du sandbox du terminal de Cursor et d'exécuter des commandes arbitraires. Aucun clic, aucune boîte de dialogue d'approbation, aucun dépôt malveillant cloné manuellement. Toutes les versions antérieures à Cursor 3.0 sont concernées.

Le vecteur de livraison : **une réponse MCP empoisonnée ou un résultat de recherche web**. L'attaquant ne touche jamais à l'éditeur. Il place des instructions dans quelque chose que l'agent lit pour le compte de l'utilisateur — une réponse d'outil, une page récupérée — et l'agent fait le reste *(Source : [Cato AI Labs — Divulgation de DuneSlide](https://www.catonetworks.com/blog/duneslide-two-critical-rce-vulnerabilities/))* .

**CVE-2026-50548** exploite la confiance du sandbox dans les propres paramètres de l'agent. L'outil `run_terminal_cmd` prend un paramètre `working_directory`, et lorsque l'agent le définit, Cursor ajoute ce chemin à l'ensemble accessible en écriture sans validation. Une instruction injectée oriente le modèle pour écrire des fichiers dans le répertoire personnel de l'utilisateur — `.zshrc`, `.zshenv` ou `LaunchAgents` — tous exécutables lors de la prochaine connexion shell.

**CVE-2026-50549** attaque la barrière de protection des liens symboliques. La vérification de canonicalisation de Cursor confirme que la cible réelle d'un lien symbolique se trouve à l'intérieur du projet. Lorsque la canonicalisation *échoue* (la cible n'existe pas, les permissions sont supprimées), Cursor abandonne et fait confiance au chemin du lien symbolique dans le projet — un classique fail-open. Un lien symbolique en écriture seule pointant vers le binaire du sandbox de Cursor passe et permet à l'attaquant de remplacer le binaire même qui contient l'agent *(Source : [Start Debugging — Analyse technique de DuneSlide](https://startdebugging.net/2026/07/cursor-duneslide-prompt-injection-sandbox-escape-rce/))* .

La leçon plus profonde : `run_terminal_cmd` n'est pas un utilisateur tapant des commandes. C'est un outil que le modèle invoque avec des arguments que le modèle a choisis, et ces arguments proviennent du texte que le modèle a lu. Une fois que vous acceptez que tout contenu entrant dans la fenêtre de contexte est potentiellement adversarial, un paramètre comme `working_directory` cesse de ressembler à une configuration et commence à ressembler à une entrée d'attaquant.

> *Pour une analyse complète de la chaîne d'exploitation DuneSlide, consultez notre article compagnon : [/2026/07/cursor-duneslide-prompt-injection-sandbox-escape-cve-2026/](/2026/07/cursor-duneslide-prompt-injection-sandbox-escape-cve-2026/)*

---

## Réponse de l'industrie : Outils, directives et lacunes

### Anthropic : Flux d'authentification et directives mises à jour

Anthropic a introduit des flux d'authentification et d'approbation MCP dans ses mises à jour du serveur et du SDK de la mi-2026. Claude prend désormais en charge OAuth 2.1 avec PKCE pour les serveurs MCP distants, et le flux d'approbation nécessite un consentement explicite avant la connexion. Les directives de sécurité publiées après la divulgation d'OX Security ont ajouté des avertissements concernant les adaptateurs STDIO — mais n'ont pas modifié le comportement sous-jacent du protocole. Anthropic maintient que `StdioServerParameters` est une interface de bas niveau conçue pour lancer des processus, et que l'assainissement est la responsabilité du développeur du client *(Source : [Anthropic — Documentation sur l'authentification MCP](https://claude.com/docs/connectors/building/authentication))* .

### OWASP : Top 10 MCP et récapitulatif des exploits du T1 2026

Le projet OWASP GenAI Security a publié son **Récapitulatif des exploits du T1 2026** couvrant janvier à début avril 2026. Le rapport documente huit incidents réels où des systèmes d'IA ont été compromis, et mentionne spécifiquement MCP comme vecteur d'injection de prompt, de compromission de la chaîne d'approvisionnement et d'exécution de code à distance. Le framework **MCP Top 10** de l'OWASP mappe les vulnérabilités MCP connues aux catégories établies : empoisonnement des outils (A1), lacunes d'autorisation (A2), injection de commandes (A3), path traversal (A4) et portes dérobées de la chaîne d'approvisionnement (A5), entre autres *(Source : [OWASP GenAI Exploit Round-up Q1 2026](https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/) et [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/))* .

### AgentSeal : Le registre public

Le dépôt [awesome-mcp-security](https://github.com/getagentseal/awesome-mcp-security) d'AgentSeal est l'inventaire public le plus complet du risque des serveurs MCP. Neuf analyseurs attribuent des scores de confiance (0–100) mesurant la sécurité avec laquelle un agent IA peut utiliser chaque serveur — pas la qualité du code du serveur lui-même, mais la surface d'attaque qu'un adversaire pourrait exploiter via l'injection de prompt ou l'empoisonnement des outils. Mis à jour quotidiennement, le registre sert de couche de vérification pré-installation pour toute équipe intégrant des serveurs MCP publics *(Source : [Registre MCP d'AgentSeal](https://agentseal.org/mcp))* .

### Cisco : « Le tissu conjonctif est terriblement peu sécurisé »

Le **Rapport sur l'état de la sécurité de l'IA 2026** de Cisco, publié le 19 février 2026, a signalé le Model Context Protocol comme un vecteur de menace émergent. Le rapport a caractérisé MCP — et les protocoles agent-à-agent similaires — comme le « tissu conjonctif » de l'écosystème IA dont la vulnérabilité « a créé une vaste surface d'attaque souvent non surveillée ». Il a spécifiquement cité les agents sur-privilégiés et les vulnérabilités dans MCP et le protocole Agent-to-Agent (A2A) de Google comme des préoccupations majeures pour les équipes de sécurité des entreprises *(Source : [Cybersecurity Dive — Cisco met en garde contre MCP](https://www.cybersecuritydive.com/news/ai-agents-model-context-protocol-cisco-report/812580/) et [Cisco — État de la sécurité de l'IA 2026](https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report))* .

### Azure AI Foundry

Le service Agent d'Azure AI Foundry de Microsoft prend désormais en charge MCP avec des bonnes pratiques de sécurité publiées couvrant la vérification des intentions, la réduction des risques et les contrôles de gouvernance — y compris les politiques d'accès par outil, le tracing avec OpenTelemetry et l'intégration d'identité managée. La collection d'outils MCP de Microsoft Sentinel peut être attachée aux agents IA dans Foundry, appliquant le même modèle RBAC qui régit l'accès humain aux données de sécurité *(Source : [Microsoft — Bonnes pratiques de sécurité pour les serveurs MCP Foundry](https://learn.microsoft.com/en-us/azure/foundry/mcp/security-best-practices))* .

---

## Atténuations pour les entreprises : Ce qui fonctionne aujourd'hui

### 1. Mise sur liste blanche et vérification des serveurs MCP

Avant d'installer un serveur MCP : vérifiez la source, examinez les permissions demandées et recoupez avec le registre d'AgentSeal. Un serveur qui fournit des images de chats n'a pas besoin d'accès au système de fichiers. Le proxy Pipelock de Pipelab scanne récursivement les définitions d'outils pour détecter les modèles d'injection avant qu'ils n'entrent dans le contexte de l'agent *(Source : [PipeLab — Référence des vulnérabilités MCP](https://pipelab.org/learn/mcp-vulnerabilities/))* .

### 2. Politiques d'outils en lecture seule

Le contrôle au retour sur investissement le plus élevé : auditez chaque outil connecté MCP et rétrogradez les permissions d'écriture lorsque l'accès en lecture seule est suffisant. La notation d'AgentSeal montre que les serveurs avec des capacités d'écriture étendues (système de fichiers, exécution shell, sortie réseau) présentent 3 à 5 fois plus de résultats de sécurité que leurs équivalents en lecture seule.

### 3. Cadence de révision des permissions

CVE-2025-54136 (MCPoison) nous a appris qu'une approbation unique équivaut à une absence d'autorisation. Chaque modification de configuration MCP doit déclencher une nouvelle approbation liée à un hachage actuel du serveur et des définitions d'outils. Check Point recommande une revalidation à chaque modification de configuration, pas seulement lors de l'installation initiale.

### 4. Exécution en sandbox

Conteneurisez chaque serveur MCP. Chrootez l'accès au système de fichiers. Montez par liaison (bind-mount) uniquement les répertoires dont le serveur a besoin. Pour les serveurs basés sur STDIO, exécutez-les sous un utilisateur dédié avec des permissions de moindre privilège. L'exploit DuneSlide a réussi parce que le sandbox faisait confiance aux paramètres choisis par l'agent — la frontière du sandbox elle-même nécessite un examen minutieux.

### 5. Surveillance de l'intégrité des fichiers de configuration

Surveillez `.mcp.json`, `.claude/settings.json`, `.cursor/rules/mcp.json` et les fichiers équivalents dans chaque dépôt. Traitez les modifications de ces fichiers avec les mêmes contrôles de révision que les modifications du YAML du pipeline CI. N'activez jamais `enableAllProjectMcpServers` ou les indicateurs d'approbation automatique globale équivalents. Verrouillez `ANTHROPIC_BASE_URL` et les points de terminaison API équivalents à leurs valeurs par défaut.

### 6. DLP d'exécution sur la sortie des outils

Scannez les réponses des outils pour détecter les modèles d'injection avant qu'ils n'entrent dans le contexte de l'agent. Le scan de réponse en six passes de Pipelock couvre le texte normalisé, les tentatives avec caractères invisibles, le leetspeak, les variantes d'espaces blancs, le repliement des voyelles et le décodage base64/hex — reconnaissant que les adversaires modifieront les chaînes pour contourner la correspondance de modèles simple.

---

## Problèmes ouverts : Ce que le protocole ne résout toujours pas

**Absence d'authentification standardisée.** La spécification MCP définit les transports et les formats de messages. Les serveurs individuels implémentent l'authentification — ou pas. OAuth 2.1 avec PKCE émerge comme la référence mais reste optionnel. De vastes pans de l'écosystème sont livrés sans aucune authentification.

**Absence de modèle de permissions dans la spécification.** MCP n'a pas de concept d'accès aux outils limité par périmètre. Un agent connecté à un serveur MCP GitHub dispose des permissions complètes du jeton OAuth — il n'y a aucun moyen de dire « lire les problèmes mais pas le code » au sein du protocole lui-même. C'est une lacune architecturale que les passerelles (Docker MCP Gateway, MintMCP, Stacklok) comblent en tant que middleware, mais elle devrait être au niveau du protocole.

**Lacunes en matière de limitation de débit.** Aucun mécanisme dans la spécification n'empêche un outil d'effectuer 10 000 appels en une minute. La fatigue de consentement de l'utilisateur — inonder la boîte de dialogue d'approbation de requêtes inoffensives jusqu'à ce que l'utilisateur approuve automatiquement la requête malveillante — est un modèle d'attaque documenté sans défense au niveau du protocole *(Source : [Palo Alto Networks — La sécurité MCP exposée](https://live.paloaltonetworks.com/t5/community-blogs/mcp-security-exposed-what-you-need-to-know-now/ba-p/1227143))* .

**Absence d'intégrité des réponses.** Le protocole n'a aucun mécanisme pour vérifier que la sortie de l'outil n'a pas été falsifiée entre le serveur et l'agent. Dans l'attaque d'enchaînement par composabilité, l'agent ne peut pas distinguer une sortie propre d'une sortie empoisonnée — et le protocole ne l'aide pas.

**Absence de détection de dérive entre sessions.** Un serveur qui passe l'inspection à l'installation peut modifier ses descriptions d'outils lors de la prochaine mise à jour. L'empreinte numérique par hachage et la détection de dérive existent en tant que solutions tierces (Pipelock), mais le protocole lui-même n'a aucune facilité pour cela.

---

## Perspectives : Spécification MCP v2 et révision de juillet 2026

La révision de la spécification du 28 juillet 2026 — la plus importante depuis le lancement de MCP — comble certaines de ces lacunes, mais pas toutes. Changements clés *(Source : [Stacklok — Guide de préparation à l'entreprise pour la mise à jour de la spécification MCP de juillet 2026](https://stacklok.com/resources/enterprise-readiness-guide-for-the-july-2026-mcp-spec-update/))* :

- **Protocole sans état.** Les sessions de protocole et la poignée de main d'initialisation sont supprimées. La version du protocole, l'identité et les capacités voyagent avec chaque requête. Cela élimine une partie de la surface d'attaque au niveau de la session mais transfère la charge de la gestion d'état au code de l'application.
- **OAuth/OIDC formalisé.** La révision ajoute des exigences OAuth 2.1 et OpenID Connect — la première fois que l'authentification apparaît dans la spécification elle-même.
- **Contexte de trace W3C.** Propagation formalisée de `traceparent`, `tracestate` et `baggage` pour un tracing compatible OpenTelemetry. Les pistes d'audit deviennent au niveau du protocole, et non des réflexions après coup.
- **JSON Schema 2020-12.** Prise en charge complète de la validation de schéma moderne, permettant des contrats d'entrée/sortie plus stricts.
- **Découverte comme citoyen de première classe.** Les serveurs doivent implémenter `server/discover` pour annoncer les versions, les capacités et l'identité.

Ce qui n'est **pas** traité : un modèle de permissions pour l'accès aux outils limité par périmètre, la vérification de l'intégrité des réponses, la limitation de débit ou la détection de dérive entre sessions. Ceux-ci restent dans la couche écosystème — passerelles, proxys et outils d'inspection d'exécution — plutôt que dans le protocole.

La révision est un pas en avant, mais les entreprises adoptant MCP en production ne devraient pas attendre les correctifs au niveau du protocole. La pile de défense en profondeur — contrôle du trafic réseau sortant, authentification basée sur une passerelle, analyse statique, inspection d'exécution et audit sensible à l'identité — est ce qui fonctionne aujourd'hui. La spécification rattrapera son retard. La surface d'attaque n'attendra pas.

---

## FAQ

**Q : Ces vulnérabilités se trouvent-elles dans le protocole lui-même ou dans les implémentations des serveurs ?**

La plupart des CVE attribuées se trouvent dans les implémentations de serveurs qui héritent des choix de conception du SDK. Le problème sous-jacent — le transport STDIO exécutant des commandes non assainies — est une propriété architecturale du protocole. Anthropic le considère « par conception » ; la communauté de la sécurité le considère comme un anti-patron. Les deux sont corrects de leurs points de vue respectifs.

**Q : Ma configuration Claude Code / Cursor / Copilot est-elle vulnérable ?**

Vérifiez votre version. DuneSlide pour Cursor est corrigé dans la version 3.0+. Les CVE des hooks/MCP de Claude Code sont corrigées dans les versions postérieures à janvier 2026. Les serveurs MCP que vous avez installés manuellement sont *votre* responsabilité — auditez-les, figez leurs versions et n'activez jamais `enableAllProjectMcpServers`.

**Q : Comment auditer mes serveurs MCP ?**

Commencez par le registre d'AgentSeal pour tout serveur public que vous utilisez. Pour les serveurs internes, appliquez la liste de contrôle d'Endor Labs : vérifiez le path traversal (82 % des serveurs sont vulnérables), les modèles d'injection de commandes (34 %) et exécutez des scanners statiques (Cisco mcp-scanner, Snyk agent-scan). Acheminez le trafic en direct via un proxy d'inspection d'exécution.

**Q : La révision de la spécification de juillet 2026 corrige-t-elle tout ?**

Non. Elle ajoute OAuth et le tracing, mais les modèles de permissions, l'intégrité des réponses, la limitation de débit et la détection de dérive restent des responsabilités de l'écosystème. Attendez-vous à cela dans une future révision, probablement fin 2026 ou début 2027.

**Q : Quelle est la chose numéro un que je devrais faire aujourd'hui ?**

Désactivez l'installation automatique de serveurs MCP à partir de registres publics. Déplacez chaque serveur MCP interne dans un conteneur isolé. Auditez les permissions des outils que vos agents utilisent réellement et rétrogradez de l'écriture à la lecture lorsque c'est possible. Cela élimine à lui seul la majorité de la surface d'attaque documentée ici.

---

## Lectures complémentaires

- [PipeLab — Vulnérabilités MCP : Risques connus et défenses](https://pipelab.org/learn/mcp-vulnerabilities/) — Référence canonique pour les neuf classes d'attaque MCP
- [OX Security — The Mother of All AI Supply Chains](https://pasqualepillitteri.it/en/news/1151/anthropic-mcp-vulnerability-200000-ai-servers-rce) — Avis original avec la liste complète des CVE
- [Cato AI Labs — DuneSlide : Deux vulnérabilités RCE critiques](https://www.catonetworks.com/blog/duneslide-two-critical-rce-vulnerabilities/) — Divulgation de CVE-2026-50548/50549
- [Check Point Research — MCPoison dans l'IDE Cursor](https://research.checkpoint.com/2025/cursor-vulnerability-mcpoison/) — CVE-2025-54136
- [CSO Online — Top 10 des vulnérabilités MCP](https://www.csoonline.com/article/4023795/top-10-mcp-vulnerabilities.html) — Taxonomie complète par Maria Korolov
- [AgentSeal — awesome-mcp-security](https://github.com/getagentseal/awesome-mcp-security) — Scores de risque mis à jour quotidiennement pour plus de 800 serveurs MCP
- [OWASP — MCP Top 10](https://owasp.org/www-project-mcp-top-10/) — Cadre de classification des vulnérabilités
- [OWASP — Récapitulatif des exploits GenAI T1 2026](https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/) — Huit incidents d'exploitation d'IA réels
- [Cisco — État de la sécurité de l'IA 2026](https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report) — Paysage des menaces pour les entreprises avec analyse MCP
- [Stacklok — Guide de préparation à l'entreprise pour la spécification MCP de juillet 2026](https://stacklok.com/resources/enterprise-readiness-guide-for-the-july-2026-mcp-spec-update/) — Planification de la migration pour la révision du protocole
- [Invariant Labs — Vulnérabilité GitHub MCP](https://invariantlabs.ai/blog/mcp-github-vulnerability) — Injection de prompt via les réponses des outils
- [Endor Labs — Analyse AppSec MCP](https://www.endorlabs.com/learn/classic-vulnerabilities-meet-ai-infrastructure-why-mcp-needs-appsec) — Analyse statique de 2 614 implémentations