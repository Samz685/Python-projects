import json
import requests
import os

# Api Key
api_key = 'k_ion9kur5/'

resultados = []

urlTrailer = ""

def run():

    
    # Crear la carpeta 'documentos' si no existe
    if not os.path.exists('documentos'):
        os.makedirs('documentos')


    
    switcher(4)

def switcher(valor):
    switcher = {
        1: cuantasSeries,
        2: trailerSerie,
        3: numEpisodios,
        4: ultimoEpisodio

        }
    func = switcher.get(valor, caso_default)
    return func()





def caso_default():
    print('No has seleccionado una opcion válida')

def cuantasSeries():

    contador = 0

    # Endpoint
    endpoint = 'https://imdb-api.com/en/API/SearchSeries/'

    # Request
    query = input("Enter the name of the Movie/TV Show you want to query: ")
    r = requests.get(endpoint+api_key+query)

    # Check response status || en data se almacena el json en forma de lista python para poder iterarlo y leerlo
    if r.status_code == requests.codes.ok:
        # Parse response
        data = json.loads(r.text)

        # Guardar en un archivo en formato JSON formateado
        with open('documentos/respuesta.json', 'w') as f:
            json.dump(data, f, indent=4)
    else:
        print(f"Error: {r.status_code}")

    # Iteramos data para contar los elementos que buscamos y almacenarlos en la lista 'resultados'
    for serie in data['results']:
        resultados.append(serie)
        contador+=1
    
    # Creamos un json nuevo donde le introducimos el elemento 'series' y dentro los resultados (cada serie)
    with open('documentos/series_1986.json', 'w') as x:
        json.dump({'series': resultados}, x, indent=4)
            
            

    # Output
    print("El numero de series encontrado es: "+str(contador))
        

def getIdSerie():

    # Endpoint
    endpoint = 'https://imdb-api.com/en/API/SearchSeries/'

    # Request
    query = "Dragon Ball"
    r = requests.get(endpoint+api_key+query)

    # Check response status || en data se almacena el json en forma de lista python para poder iterarlo y leerlo
    if r.status_code == requests.codes.ok:
        # Parse response
        data = json.loads(r.text)

        # Guardar en un archivo en formato JSON formateado
        with open('documentos/respuesta.json', 'w') as f:
            json.dump(data, f, indent=4)
    else:
        print(f"Error: {r.status_code}")

    # Iteramos data para contar los elementos que buscamos y almacenarlos en la lista 'resultados'
    for serie in data['results']:
        if '1986' in serie['description']:
            idSerie = serie['id']
            resultados.append(serie)

    if idSerie == "":
        print("No existe una serie con estos parametros")
        idSerie = "ID no existe"
        return idSerie
    else:
        print(idSerie)

    return idSerie

def trailerSerie():

    idSerie = "tt0088509/"
    
    # Endpoint
    endpoint = 'https://imdb-api.com/en/API/Trailer/'

    # Request
    r = requests.get(endpoint+api_key+idSerie)

    # Check response status || en data se almacena el json en forma de lista python para poder iterarlo y leerlo
    if r.status_code == requests.codes.ok:
        # Parse response
        data = json.loads(r.text)

        # Guardar en un archivo en formato JSON formateado
        with open('documentos/respuesta.json', 'w') as f:
            json.dump(data, f, indent=4)
    else:
        print(f"Error: {r.status_code}")

    # Iteramos data para contar los elementos que buscamos y almacenarlos en la lista 'resultados'
    for key in data:
        if key == 'link':
            urlTrailer = data[key]
            print("Esta es la url del trailer de Dragon Ball: "+str(urlTrailer))
            return urlTrailer
        
    
    
    

def numEpisodios():

    contador = 0

    idSerie = "tt0088509/"
     # Endpoint
    endpoint = 'https://imdb-api.com/en/API/SeasonEpisodes/'

    query = input("Introduce el numero de la temporada: ")

    # Request
    r = requests.get(endpoint+api_key+idSerie+query)

    # Check response status || en data se almacena el json en forma de lista python para poder iterarlo y leerlo
    if r.status_code == requests.codes.ok:
        # Parse response
        data = json.loads(r.text)

        # Guardar en un archivo en formato JSON formateado
        with open('documentos/respuestaEpisodios.json', 'w') as f:
            json.dump(data, f, indent=4)

        for episode in data['episodes']:
            contador+=1
        print("Numero de episodios de la primera temporada: "+str(contador))
        return contador
            
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

    # Check response status || en data se almacena el json en forma de lista python para poder iterarlo y leerlo
    if r.status_code == requests.codes.ok:
        # Parse response
        data = json.loads(r.text)

        # Guardar en un archivo en formato JSON formateado
        with open('documentos/respuestaLastEpisode.json', 'w') as f:
            json.dump(data, f, indent=4)

        for episode in data['episodes']:
            if episode['episodeNumber'] == "153":
                fechaEpisodio = episode['released']
                argumento = episode['plot']

        print("Fecha emision último episodio: "+str(fechaEpisodio))
        print("Argumento: "+str(argumento))
        
            
    else:
        print(f"Error: {r.status_code}")

   

if __name__ == '__main__':
    run()