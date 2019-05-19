import os
import signal
import time

from aspireSite import aspire
from aspireSite import saveErrorSite
from testOnionExist import existUrl
import allVariables

import subprocess

if __name__ == '__main__':

    os.system('gnome-terminal -e "ssh -tt -R 80:localhost:8080 ssh.localhost.run"')
    time.sleep(3)

    with open(allVariables.onionSites) as f:
        for line in f:
            print("URL A ANALYSER = |", line.rstrip('\n').strip(),"|")
            sudoPassword=allVariables.sudoPassword
            #Supprimer fichier existant de l'analyse precedente
            if os.path.isfile(allVariables.dirMirorSite):
                os.system("rm " + allVariables.dirMirorSite)
            if os.path.isfile(allVariables.filesJsonAlyze):
                os.system("rm " + allVariables.filesJsonAlyze)
            if os.path.isdir(allVariables.pathToApache):
                rmWWW = "rm -rf " + allVariables.pathToApache+"*" # -r = recursivement dans les dossiers non vides ; -f ignorer fichiers inexistants
                p = os.system('echo %s|sudo -S %s' % (sudoPassword, rmWWW))

            url = line.rstrip('\n').strip();

            urlSsh = allVariables.urlSsh

            if existUrl(url) == "false": #tester si l'url a deja ete analysee
                #lancer aspiration site + mettre les fichiers au bon endroit
                aspireError = aspire(url)
                print("Error Aspire = " + aspireError)

                if(aspireError == "ok"):
                    #recuperer fichier JSON sur Alyze
                    os.system("python3 getJsonAlyze.py " + urlSsh)
                    #remplir le fichier json global
                    os.system("python3 fillInGlobalJson.py " + url)
                else:
                    print("Erreur wget pour aspirer le site : ", url)
                    saveErrorSite(url)
            else:
                print("Url : ", url, " existe déjà !")
            time.sleep(2)
            os.system('sudo trash-empty')
