import os
import json

field = "crime" # Mot à tester
urlWordAssociation = "" # url API WordAssociations
query = urlWordAssociation + field + "&lang=en"

categ = "../wordClassification/categories.json"
pathToSave = "./wordassociation.json"
os.system("wget '"+query+"' -O "+pathToSave)


if os.path.getsize(categ) > 0:
    with open(categ, 'r') as d:
        ljson = json.load(d)
        myDictObj = {"Drug": ["cannabis", "drug", "heroine"], "Money": ["bitcoin", "credit", "money"],
                     "Adult": ["porn", "adult", "porno"], "Market": ["sale", "market", "card"],
                     "Crime": ["crime", "hitmen", "assassination"],"Virus": ["virus", "malware", "ransomware"]}
        myDictObj.update(ljson)  # ajouter le json deja existant
else:
    myDictObj = {"Drug": ["cannabis", "drug", "heroine"], "Money": ["bitcoin", "credit", "money"],
                 "Adult": ["porn", "adult", "porno"], "Market": ["sale", "market", "card"],
                 "Crime": ["crime", "hitmen", "assassination"], "Virus": ["virus", "malware", "ransomware"]}


def addWord(word, category):
    if word.lower() not in myDictObj[category]:
        print(word + " entre dans json")
        myDictObj[category].append(word.lower())
    else:
        print(word + " existe deja")

    with open(categ, 'w') as outfile:
        json.dump(myDictObj, outfile)


with open(pathToSave) as json_file:
    data = json.load(json_file)
    # print(data['response'][0]['items'])
    for it in data['response'][0]['items']:
        print(it['item'])
        addWord(it['item'],"Crime") # Changer la Catégorie "Crime", "Adult", "Money", "Market", "Drug", "Virus"
