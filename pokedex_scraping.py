from bs4 import BeautifulSoup
import requests
import re

pokedex = {}

url = "https://pokemondb.net/pokedex/game/firered-leafgreen"
result = requests.get(url).text

doc = BeautifulSoup(result,"html.parser")
infocards = doc.find(class_ = "infocard-list")



imgs = infocards.find_all("img")
for img in imgs:
    img_src = img["src"] 
    # print(img_src)

numbers = infocards.find_all("small")
for num in numbers:
    print(num.contents[0])

