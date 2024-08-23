from bs4 import BeautifulSoup
import requests
import re

#! DESCARGAR IMAGENES
def descargar_imagen(url, nombre_archivo):
    try:
        # Realizar la solicitud GET para obtener la imagen
        respuesta = requests.get(url)
        # Verificar si la solicitud fue exitosa
        if respuesta.status_code == 200:
            # Guardar la imagen en un archivo
            with open(nombre_archivo, 'wb') as archivo:
                archivo.write(respuesta.content)
            print(f"Imagen guardada como {nombre_archivo}")
        else:
            print("Error al descargar la imagen. Código de estado:", respuesta.status_code)
    except Exception as e:
        print("Ocurrió un error:", e)
#!

#*Adquiriendo archivo de la url
url = "https://pokemondb.net/pokedex/game/firered-leafgreen"
urlopc = "https://pokemondb.net/pokedex/game/scarlet-violet"
web_result = requests.get(url).text

#*nombrar el archivo
default_name = url.split("/")[-1]
name_json = input("Ingresa el nombre del archivo JSON\n") or (default_name)
name_json += ".json"

#*Convirtiendo a documento y parseando
doc = BeautifulSoup(web_result,"html.parser")

#*Acercando a los elementos clave
htmllists = doc.find_all(class_ = "infocard-list")


for htmllist in htmllists:
    divs = htmllist.find_all("div")

    #*Estructura de variables
    pokedex = []
    count = 0

    for div in divs:
        #* Cuenta del progreso
        count += 1; #contador
        print(f"{count} / {len(divs)}")

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

        #*Consiguiendo su descripcion en la pokedex
            #!PARA ROJO FUEGO Y VERDE HOJA
            #*Entrnado a las paginas de cada pokemon
        pokedex_url = f"https://pokemondb.net/pokedex/{name}"
        poke_result = requests.get(pokedex_url).text
        pokedoc = BeautifulSoup(poke_result,"html.parser")
        
            #Acercandonos a los datos generales por tabla
        #debug vital_tables = pokedoc.find_all(class_ = "vitals-table")
        
            #*Encontrando las descripciones en la pokedex (entries)
        try:
            description = pokedoc.find(class_ = "igame firered").parent.parent.td.text
        except:
            try:
                description = pokedoc.find(class_ = "igame firered").next_sibling.text
            except:
                pass
        #debug print(count)
        #debug print(description)
        
        #*Agregando pokemons (valores) a la pokedex (diccionario)
        pokedex.append({
            "id": num,
            "name": name,
            "type": types,
            "img-url": imgs,
            "description" : description
            })

        #!DESCARGAR IMGS
        # nombre_archivo = f"{name}.png"
        # descargar_imagen(imgs, nombre_archivo)

#* Exportar como JSON
import json
with open(name_json, "w") as file_json:
    json.dump(pokedex, file_json, indent=4)

#! DEBUG 🫠
# print(pokedex) #*imprimiendo en terminal el JSON
# print(len(divs))
# print(divs)
