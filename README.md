# methodoDarkWeb
Implémentation d'une méthodologie et d'un logiciel pour surveiller et avoir un aperçu rapide d'un site, ou d'un ensemble de sites, du dark web.

Prérequis :
- Python3 ;
- Apache2 ;
- torsocks : `sudo apt-get install torsocks` ;
- accès à l'Api du site Alyze : https://alyze.info/ ;

Important :
- renseigner les bons chemins dans le fichier  `allVariables.py ` ;
- pour l'api d'Alyze, dans ce fichier, s'arrêter à `url=`, par exemple comme ceci : `https://user:password@api.alyze.info/v1?url=` ;
- pour la variable `urlSsh`, lancer une première fois la commande `ssh -tt -R 80:localhost:8080 ssh.localhost.run` et copier/coller l'une des deux url dans la variable `urlSsh` ;

### Extraire des urls du dark web pour se créer une base de sites à jour :
Lancer  `extractUrl.py `. Les urls sont rangées dans  `allLinks.txt `. Soit copier/coller l'intégralité de ces urls dans  `sitesOnion.txt `, soit lancer  `extractRandomLinks.py ` pour remplir aléatoirement  `sitesOnion.txt ` depuis les liens présents dans  `allLinks.txt `. A noter que l'on peut paramétrer le nombre de liens à extraire aléatoirement dans  `extractRandomLinks.py ` en changeant la variable  `NB_MAX_URLS_TO_EXTRACT`.

### Enrichir la base de données de classification :
Dans `/wordClassification/enrichirDB.py`, renseigner la variable `field` avec le mot pour lequel un réseau de mots associés est souhaité pour enrichir la base de données. Tout en bas, `addWord(it['item'],"Categorie")`, remplacer `Categorie` par la catégorie souhaitée (parmi uniquement celles-ci : Drug, Money, Market, Adult, Virus, Crime). Attention à respecter la casse comme présenté ici pour les différentes catégories. Ainsi, on ajoute les mots associés à `field` dans la catégorié mentionnée. La base de classification est accessible au format json dans `categories.json`.

### Ordre des scripts à lancer
- `python3 scenarioLoop.py` (un deuxième terminal avec le tunnel SSH va s'ouvrir) ;
- `python3 readJson.py` ;
- Dans dossier Graphique : `python3 interface.py` ;

Admettons qu'on veuille faire l'analyse de nouveaux sites, alors :
- les renseigner dans `sitesOnion.txt` de la façon souhaitée (manuellement, random, ...) ;
- `python3 scenarioLoop.py` : le fichier json global des différentes analyses sera mis à jour automatiquement ;
- `python3 readJson.py` : permet de renseigner la partie classification des sites venant juste d'être analysés ;
- `python3 interface.py` : pour la visualisation graphique ;

### Remarques
- Si première analyse, copier/coller le fichier `listeJson.txt` de Scenario, dans `classification.txt` de wordClassification.
- Différents correctifs seront apportés prochainement.
