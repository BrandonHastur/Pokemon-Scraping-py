from bs4 import BeautifulSoup
import requests
import re

pokedex = {}

url = "https://pokemondb.net/pokedex/game/firered-leafgreen"
result = requests.get(url).text

doc = BeautifulSoup(result,"html.parser")
# infocard_list = doc.find(class_ = "infocard-list")

# imgs = infocard_list.find_all("img")
# for img in imgs:
#     img_src = img["src"] 
#     print(img_src)

# numberslgdata = infocard_list.find_all(class_ = "infocard-lg-data")
# for number in numberslgdata:
#     print(number.small.string)
#     print()

# names = infocard_list.find_all(class_="ent-name")
# for name in names:
#     print(name.string)
#     print()

# types = infocard_list.find_all("small")
# for type_ in types:
#     print(type_.text)
#     print()

infocards = doc.find_all(class_ = "infocard")
for infocard in infocards:
    num = infocard.small.string
    name = infocard.find_all(class_="ent-name")

    print(num)
    print(name)

