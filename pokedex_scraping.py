from bs4 import BeautifulSoup
import requests
import re

#*Adquiriendo archivo de la url
url = "https://pokemondb.net/pokedex/game/firered-leafgreen"
web_result = requests.get(url).text

#*Convirtiendo a documento y parseando
doc = BeautifulSoup(web_result,"html.parser")

#*Acercandome a los elementos clave
htmllist = doc.find(class_ = "infocard-list")
divs = htmllist.find_all("div")

#*Estructura de variables
pokemons = len(divs) #Cantidad de pokemons

pokedex = []

for div in divs:

    #*Consiguiendo los nombres
    a_s = div.find_all("a")
    for a in a_s[1:2]:
        name = a.string
        #debug print(a.string)
        #debug print()
    #*Consiguiendo los numeros
    numbers = div.small
    for number in numbers:
        num = number
        #debug print(number)
        #debug print()
    #*Consiguiendo los tipos
    for a in a_s[2:]:
        types = a.string
        print(types)
        #debug print()
    #*Consiguiendo url de las imagenes
    imgs = div.img.attrs["src"]
    #debug print(imgs)

    print(num,name,types,imgs)




#! DEBUG 🫠
print(pokedex)
# print(len(divs))
# print(divs)