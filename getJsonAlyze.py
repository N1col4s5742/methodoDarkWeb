import os, sys
import allVariables

url = sys.argv[1]
pathToSave  = allVariables.filesJsonAlyze
os.system("curl -L " + allVariables.apiAlyze + " + url + " -o " + pathToSave)
