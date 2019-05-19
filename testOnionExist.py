# tester si l'url à analyser existe déjà dans le fichier JSON
import json
import os
import allVariables

def existUrl(urlArg):
    if os.path.getsize(allVariables.listJson) > 0:
        with open(allVariables.listJson, 'r') as f:
            jsonArray = json.load(f)

        for entry in jsonArray:
            if jsonArray[entry]['info']['url'] == urlArg:
                return "true"
        return "false"
    else:
        return "false"

