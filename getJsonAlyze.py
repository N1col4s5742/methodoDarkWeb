import os, sys
import allVariables

url = sys.argv[1]
pathToSave  = allVariables.filesJsonAlyze
os.system("curl -L https://irdarkweb:u8NEM6y867@api.alyze.info/v1?url=" + url + " -o " + pathToSave)
