#aspirer site et le mettre dans www/html
import os
import subprocess
import time
import json
import allVariables

def aspire(urlArg):
    url = urlArg
    nameFile = "mirorSite";  # nouveau nom du fichier
    pathToDownload = allVariables.pathToDownload
    # wget -p https://www.fcmetz.com/
    request = "torify wget http://" + url + " -P " + pathToDownload + " -t 1 -T 10";  # requête wget
    pathToApache = allVariables.pathToApache  # "/var/www/html/";
    sudoPassword = allVariables.sudoPassword


    ## call wget command ##
    p = subprocess.Popen(request, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    ## Wait for wget to terminate. Get return returncode ##
    p_status = p.wait()
    print("Command output : ", output)
    print("Command exit status/return code : ", p_status)

    if (p_status == 8 or p_status == 0):
        # request2 = "mv " + pathToDownload + url + " " + pathToDownload + nameFile;  # changement de nom
        # os.system(request2);

        request2 = "mv " + pathToDownload + "index.html" + " " + pathToApache;
        p = os.system('echo %s|sudo -S %s' % (sudoPassword, request2))
        # os.system(request2)
        error = "ok"
    else:
        print("Erreur dans l'url")
        error = "nok"
    time.sleep(2)
    return error

def saveErrorSite(url):
    x = {
        "url": url,
        "date": time.strftime("%d/%m/%Y")
    }
    with open(allVariables.errorLinks, 'a+') as outfile:
        json.dump(x, outfile)
    print(url, " enregistree dans fichier json erreur")


