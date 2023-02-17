import json
import requests
import os


def run():

    resultados = []

    # Crear la carpeta 'documentos' si no existe
    if not os.path.exists('documentos'):
        os.makedirs('documentos')

    # Crear el archivo 'respuesta.json' si no existe
    if not os.path.exists('documentos/respuesta.json'):
        with open('documentos/respuesta.json', 'w') as f:
            f.write('{}')

    

    # Api Key
    api_key = 'k_ion9kur5/'

    # Endpoint
    endpoint = 'https://imdb-api.com/en/API/SearchSeries/'

    # Request
    query = input("Enter the name of the Movie/TV Show you want to query: ")
    params = {'apikey': api_key, 'q': query}
    r = requests.get(endpoint+api_key+query)

    # Check response status
    if r.status_code == requests.codes.ok:
        # Parse response
        data = json.loads(r.text)

        # Guardar en un archivo en formato JSON formateado
        with open('documentos/respuesta.json', 'w') as f:
            json.dump(data, f, indent=4)
    else:
        print(f"Error: {r.status_code}")

    with open('documentos/respuesta.json', 'r') as f:
        data = json.load(f)

    serie_1986 = []
    contador = 0

    for serie in data['results']:
        if '1986' in serie['description']:
            serie_1986.append(serie)
            contador+=1
    

    with open('documentos/series_1986.json', 'w') as x:
        json.dump({'series': serie_1986}, x, indent=4)
            
            

        # Output
        print("El numero de series encontrado es: "+str(contador))
        
    

if __name__ == '__main__':
    run()
