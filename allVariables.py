pathToDownload = ""  # chemin vers dossier "Scenario" où enregistrer le site aspiré
pathToApache = "/var/www/html/" # chemin vers seveur local d'Apache
allLinks = "" # chemin vers allLinks.txt contenant la liste des sites récupérés
pathToSave  = "" # chemin vers fichier "jsonAlyze.txt" où enregistrer le json généré par Alyze
onionSites = "" # chemin vers fichier "sitesOnion.txt" avec les sites à analyser
dirMirorSite = "" # chemin vers fichier "index.html" du site aspiré
filesJsonAlyze = "" # chemin vers fichier "jsonAlyze.txt" correspondant au json renvoyé par Alyze
sudoPassword='' # password de session
urlSsh = ""  # url renvoyé après l'appel de la cmd : ssh -tt -R 80:localhost:8080 ssh.localhost.run
listJson = "" # chemin vers fichier "listejson.txt" correspondant au json global
errorLinks = "" # chemin vers fichier "errorLinks.json" correspondant au json des sites avec erreur
categories = "" # chemin vers fichier "categories.json" correspondant à la BDD de classification
classificationFile = "" # chemin vers fichier "classification.txt" correspondant au json global final avec classification
apiAlyze = "" # url de l'API d'alyze jusqu'à "url="
