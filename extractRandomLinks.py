from random import randint
import allVariables

f = open(allVariables.allLinks)
lines = f.readlines()

links = open(allVariables.onionSites,'w')

NumberOfLine = 0
for line in lines:
    NumberOfLine += 1

precedentNumbers = []
NB_MAX_URLS_TO_EXTRACT = 1 #nombre de sites à extraire de allVariables.allLinks
exist = True
# On suppose que NumberOfLine > NB_MAX_URLS_TO_EXTRACT
for x in range(0, NB_MAX_URLS_TO_EXTRACT):
    exist = True
    while exist:
        random = randint(0, int(NumberOfLine))
        print(random)
        if random not in precedentNumbers:
            print('ok')
            precedentNumbers.append(random)
            exist = False
            links.write(lines[random])
        else:
            print('existe deja')
            exist = True
links.close()


