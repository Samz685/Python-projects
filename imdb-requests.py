from PIL import Image
import json
import requests
import os
import sys



# Api Key
api_key = 'k_59y68kxq/'

resultados = []

urlTrailer = ""

def run():

    
    # Crear la carpeta 'documentos' si no existe
    if not os.path.exists('documentos'):
        os.makedirs('documentos')
    
    menu()

def menu():
    
    print("¡Bienvenido a la App de consultas de IMDB!")
    print("------------------------------------------------")
    print("1- Número series registradas de Dragon Ball")
    print("2- Url del trailer de Dragon Ball del año 1986")
    print("3- Total episodios de primera temporada")
    print("4- Fecha y argumento del último episodio")
    print("5- Poster de la pelicula Akira (1988)")
    print("6- Reporte completo de la pelicula Akira")
    print("7- SALIR")
    print("------------------------------------------------")
    
    while True:
        print("")
        valor = int(input("Elije tu consulta: \n"))
        switcher(valor)

def switcher(valor):
    switcher = {
        1: cuantasSeries,
        2: trailerSerie,
        3: numEpisodios,
        4: ultimoEpisodio,
        5: posterAkira,
        6: reporteAkira,
        7: salir
        }
    func = switcher.get(valor, caso_default)
    return func()


def caso_default():
    print('No has seleccionado una opcion válida')

def salir():
    print("¡Hasta pronto!")
    sys.exit()

def cuantasSeries():

    contador = 0

    # Endpoint
    endpoint = 'https://imdb-api.com/en/API/SearchSeries/'
    serie= "Dragon Ball"

    # Request
    r = requests.get(endpoint+api_key+serie)

    # Comprobación solicitud, se guarda en forma de lista en data
    if r.status_code == requests.codes.ok:
        # Parse response
        data = json.loads(r.text)

        # Guardar en un archivo en formato JSON formateado
        with open('documentos/respuestaTodasSeries.json', 'w') as f:
            json.dump(data, f, indent=4)
    else:
        print(f"Error: {r.status_code}")

    # Iteramos data para contar los elementos que buscamos y almacenarlos en la lista 'resultados'
    for serie in data['results']:
        contador+=1

    # Output
    print("El numero de series encontrado es: "+str(contador))
        

def trailerSerie():

    idSerie = "tt0088509/"
    
    # Endpoint
    endpoint = 'https://imdb-api.com/en/API/Trailer/'

    # Request
    r = requests.get(endpoint+api_key+idSerie)

    # Comprobación solicitud
    if r.status_code == requests.codes.ok:
        # Parse response
        data = json.loads(r.text)

        # Guardar en un archivo en formato JSON formateado
        with open('documentos/respuestaTrailerSerie.json', 'w') as f:
            json.dump(data, f, indent=4)
    else:
        print(f"Error: {r.status_code}")

    # Iteramos data para encontrar la url del trailer
    for key in data:
        if key == 'link':
            urlTrailer = data[key]
            print("Esta es la url del trailer de Dragon Ball: "+str(urlTrailer))

def numEpisodios():

    contador = 0
    idSerie = "tt0088509/"

     # Endpoint
    endpoint = 'https://imdb-api.com/en/API/SeasonEpisodes/'

    query = input("Introduce el numero de la temporada: ")

    # Request
    r = requests.get(endpoint+api_key+idSerie+query)

    # Comprobación solicitud
    if r.status_code == requests.codes.ok:
        # Parse response
        data = json.loads(r.text)

        # Guardar en un archivo en formato JSON formateado
        with open('documentos/numeroEpisodios.json', 'w') as f:
            json.dump(data, f, indent=4)

        for episode in data['episodes']:
            contador+=1
        print("Numero de episodios de la primera temporada: "+str(contador))
            
    else:
        print(f"Error: {r.status_code}")

def ultimoEpisodio():

    fechaEpisodio = ""
    argumento = ""

    idSerie = "tt0088509/"
     # Endpoint
    endpoint = 'https://imdb-api.com/en/API/SeasonEpisodes/'

    query = input("Introduce el numero de la temporada: ")

    # Request
    r = requests.get(endpoint+api_key+idSerie+query)

    # Comprobación solicitud
    if r.status_code == requests.codes.ok:
        # Parse response
        data = json.loads(r.text)

        # Guardar en un archivo en formato JSON formateado
        with open('documentos/ultimotEpisodio.json', 'w') as f:
            json.dump(data, f, indent=4)

        # Buscar el último episodio y guardar en variables la fecha y argumento
        for episode in data['episodes']:
            if episode['episodeNumber'] == "153":
                fechaEpisodio = episode['released']
                argumento = episode['plot']

        print("Fecha emision último episodio: "+str(fechaEpisodio))
        print("Argumento: "+str(argumento))
    
    else:
        print(f"Error: {r.status_code}")

def posterAkira():
     # Endpoint
    endpoint = 'https://imdb-api.com/API/ResizeImage?apiKey=k_59y68kxq&size=2000x3000&url='
    urlPoster = ('https://m.media-amazon.com/images/M/MV5BM2ZiZTk1ODgtMTZkNS00NTYxLWIxZTUtNWE'
                'xZGYwZTRjODViXkEyXkFqcGdeQXVyMTE2MzA3MDM@._V1_Ratio0.6757_AL_.jpg')

    # Request
    r = requests.get(endpoint+urlPoster)

    # Comprobación solicitud || guardar en variable imagen el poster redimensionado
    if r.status_code == requests.codes.ok:
        # Parse response
        imagen = r.content

        # Guardar contenido en archivo poster en formato jpg
        with open('documentos/posterAkira.jpg', 'wb') as f:
            f.write(imagen)

        # Con la funcion Image.open podemos abrir la imagen
        imagen = Image.open('documentos/posterAkira.jpg')
        imagen.show()
    else:
        print(f"Error: {r.status_code}")
    

def reporteAkira():
     # Endpoint
    endpoint = "https://imdb-api.com/en/API/Report/"
    idSerie = "tt0094625/"
    param = "FullActor"

    # Request
    r = requests.get(endpoint+api_key+idSerie+param)

    # Comprobación solicitud || guardar en variable imagen el reporte-poster
    if r.status_code == requests.codes.ok:
        # Parse response
        imagen = r.content

        # Guardar contenido en archivo reporte en formato jpg
        with open('documentos/reporteAkira.jpg', 'wb') as f:
            f.write(imagen)

        # Con la funcion Image.open podemos abrir la imagen
        imagen = Image.open('documentos/reporteAkira.jpg')
        imagen.show()    
    else:
        print(f"Error: {r.status_code}")
   

if __name__ == '__main__':
    run()