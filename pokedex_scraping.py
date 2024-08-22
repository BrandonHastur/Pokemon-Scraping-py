from bs4 import BeautifulSoup
import requests
import re

#*Adquiriendo archivo de la url
url1 = "https://pokemondb.net/pokedex/game/firered-leafgreen"
url = "https://pokemondb.net/pokedex/game/scarlet-violet"
web_result = requests.get(url).text

#*nombrar el archivo
default_name = url.split("/")[-1]
name_json = input("Ingresa el nombre del archivo JSON") or (f"{default_name}.json")

#*Convirtiendo a documento y parseando
doc = BeautifulSoup(web_result,"html.parser")

#*Acercando a los elementos clave
htmllists = doc.find_all(class_ = "infocard-list")

for htmllist in htmllists:
    divs = htmllist.find_all("div")

    #*Estructura de variables
    pokedex = []

    for div in divs:
        count = 1; #no hace nada

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
        itypes = div.find("small").find_next_sibling("small")
        itype1 = itypes.find_all("a")[0].string
        #!Accion a tomar si el segundo tipo (index) no existe
        try:
            itype2 = itypes.find_all("a")[1].string
        except IndexError:
            itype2 = ''
        if itype2 == '':
            del itype2
        #!Accion a tomar si no hay segundo tipo
        try:
            types = [itype1,itype2]
        except NameError:
            types = itype1
        #debug print(types)

        #*Consiguiendo url de las imagenes
        imgs = div.img.attrs["src"]
        #debug print(imgs)
        #debug print(num,name,types,imgs)
        ++count #no hace nada

        #Consiguiendo su des

        #*Agregando pokemons (valores) a la pokedex (diccionario)
        pokedex.append({
            "id": num,
            "name": name,
            "type": types,
            "img-url": imgs
            })

# Exportar como JSON
import json
with open(name_json, "w") as file_json:
    json.dump(pokedex, file_json, indent=4)

#! DEBUG 🫠
# print(pokedex) #*imprimiendo en terminal el JSON
# print(len(divs))
# print(divs)