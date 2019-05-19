import json
import allVariables
import os

listCateg = {"Virus", "Adult", "Money", "Market", "Crime", "Drug", "Other"}
dictionnary = {}
dictionnary["Virus"] = 0
dictionnary["Adult"] = 0
dictionnary["Money"] = 0
dictionnary["Market"] = 0
dictionnary["Crime"] = 0
dictionnary["Drug"] = 0
dictionnary["Other"] = 0
POIDS_TITLE = 10

with open(allVariables.categories) as json_file:
    dataCateg = json.load(json_file)
    for key in dataCateg.keys():
        print(key)

def findCateg(word, occ, category):
    if category != "Other" and word in dataCateg[category]:
        dictionnary[category]= int(dictionnary[category]+occ);


with open(allVariables.listJson) as json_file:
    data = json.load(json_file)

    for key in data.keys():
        print("*******************************************")

        auMoinsUn = False
        dictionnary["Virus"] = 0
        dictionnary["Adult"] = 0
        dictionnary["Money"] = 0
        dictionnary["Market"] = 0
        dictionnary["Crime"] = 0
        dictionnary["Drug"] = 0
        dictionnary["Other"] = 0

        print(key + " : ") # titre du site
        for nameKey in data[key]: # pour toutes les clefs du json
            print("\t" + nameKey + " : \n")
            if(nameKey == "info"):
                for value in data[key][nameKey]: # pour tous les champs de clef "info"
                    print("\t \t" + value + " : " + data[key][nameKey][value])
                    if value == "name": # travail d'analyse sur le nom du site
                        if (" " in data[key][nameKey][value].strip()): # plusieurs mots dans le nom
                            valStrip = data[key][nameKey][value].strip()
                            x = valStrip.split(" ")
                            for wordInValue in x:
                                if "/" in wordInValue: # mot avec des /
                                    xsplit = wordInValue.split("/")
                                    for wordXSplit in xsplit:
                                        if len(wordXSplit) > 2: # ne pas prendre les déterminants par ex.
                                            print("Mot a exploiter dans le titre avec /: " + wordXSplit.lower())
                                            for valCat in listCateg:
                                                findCateg(wordXSplit.lower(), POIDS_TITLE, valCat)
                                else:
                                    if len(wordInValue) > 2:
                                        print("Mot a exploiter dans le titre : " + wordInValue.lower())
                                        for valCat in listCateg:
                                            findCateg(wordInValue.lower(), POIDS_TITLE, valCat)
            else: # keywords
                for value in data[key][nameKey]: # pour tous les keywords
                    print("\t \t" + value + " : " + str(data[key][nameKey][value]['occurrences']))    
                    if(" " in value.strip()): # si le keyword contient plusieurs mots
                        valStrip = value.strip()
                        x = valStrip.split(" ")
                        for wordInValue in x:
                            print("Mot a exploiter : " + wordInValue)
                            for valCat in listCateg:
                                findCateg(wordInValue, data[key][nameKey][value]['occurrences'], valCat)
                    else:
                        for valCat in listCateg:
                            findCateg(value, data[key][nameKey][value]['occurrences'], valCat)

        for valDic in dictionnary:
            if dictionnary[str(valDic)] != 0:
                auMoinsUn=True

        if auMoinsUn==False:
            dictionnary['Other'] = 1
        print(dictionnary)




        if os.path.getsize("./wordClassification/classification.txt") > 0:
            with open("./wordClassification/classification.txt", 'r') as d:
                ljson = json.load(d)
                if(key not in ljson):#le site n'existe pas dans le fichier txt classification
                    ljson[key]=data[key]
                if("classification" in ljson[key]):
                    print("le site " + key + " a déjà été analysé !")
                    ljson[key]["classification"] = dictionnary #on le met quand même à jour
                else: #on n'a pas encore ajouté la classification au fichier txt classification
                    ljson[key]["classification"] = dictionnary

        else:
            print('ERROR readjson')

        with open("./wordClassification/classification.txt", 'w') as outfile:
            json.dump(ljson, outfile)

