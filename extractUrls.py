from bs4 import BeautifulSoup, SoupStrainer
import requests
import allVariables

new_days = open(allVariables.allLinks,'w')
url = "https://ahmia.fi/address/"

page = requests.get(url)
data = page.text
soup = BeautifulSoup(data, "lxml")
nb = 0;

for link in soup.find_all('a'):
    if "onion" in link.get('href') and len(link.get('href').split('/')[2])==22:
        # print("--> ", link.get('href').split('/')[2])
        new_days.write(link.get('href').split('/')[2]+"\n")
        nb += 1

print("Nombre d'urls onion = ", nb)
new_days.close()
