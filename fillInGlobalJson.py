#remplir fichier json global

import json
from pprint import pprint
import time
import os
import sys
import allVariables

url = sys.argv[1]
NB_MAX_KEYWORDS = 10
print("URL dans fichier JSON = " + url)
with open(allVariables.filesJsonAlyze, 'r') as f:
    jsonArray = json.load(f)

if os.path.getsize(allVariables.listJson) > 0:
	with open(allVariables.listJson, 'r') as d:
		ljson = json.load(d)
		newJson = {jsonArray["info"]["title"]:
					   {"info":
							{"name": jsonArray["info"]["title"],
							 "date": time.strftime("%d/%m/%Y"),
							 "url": url},
						"keywords":
							{},
						},
				   }
		newJson.update(ljson) #ajouter le json deja existant
else:
	newJson = { jsonArray["info"]["title"]:
	{"info":
		{"name":jsonArray["info"]["title"],
		"date":time.strftime("%d/%m/%Y"),
		"url":url},
	"keywords":
		{},
	}
	}


### Voir quelles occurrences dans le fichier json initial
listOcc = [];
for key in jsonArray.keys():  # boucle sur toutes les keys du json
	if key == "keywords":  # que la categorie keyword
		for nameKeyWord in jsonArray[key]:  # pour tous les mots clefs
			listOcc.append(jsonArray[key][nameKeyWord]["occurrences"])

listOcc.sort(reverse=True)

if len(listOcc) >= 10:
	newSize = NB_MAX_KEYWORDS-len(listOcc) #taille max de 10
else:
	NB_MAX_KEYWORDS = 5;
	newSize = NB_MAX_KEYWORDS - len(listOcc)  # taille max de 5

listOcc = listOcc[:newSize]
print(listOcc);

nb=1;
###
for key in jsonArray.keys(): #boucle sur toutes les keys du json
	if key=="keywords": #que la categorie keyword
		for nameKeyWord in jsonArray[key]: #pour tous les mots
			if(nb<=NB_MAX_KEYWORDS):
				if(jsonArray[key][nameKeyWord]["occurrences"] in listOcc):
					newJson[jsonArray["info"]["title"]]['keywords'][nameKeyWord]={'occurrences':jsonArray[key][nameKeyWord]["occurrences"]}
					nb += 1
					listOcc.remove(jsonArray[key][nameKeyWord]["occurrences"])

serialized= json.dumps(newJson, sort_keys=True, indent=2)
#print(serialized)

if not os.path.getsize(allVariables.listJson) > 0:
	with open(allVariables.listJson, 'w') as outfile:
		json.dump(newJson, outfile)
else :
	if not jsonArray["info"]["title"] in ljson:
		with open(allVariables.listJson, 'w') as outfile:
			json.dump(newJson, outfile)
	else:
		print(jsonArray["info"]["title"]+ " Existe deja");