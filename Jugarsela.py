import requests

class Equipo:
    def __init__(self, clave, nombre, año, escudo):
        self.clave = clave
        self.nombre = nombre
        self.año = año
        self.escudo = escudo

class Estadio:
    def __init__(self, nombre, direccion, ciudad, capacidad, superficie, foto):
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.capacidad = capacidad
        self.superficie = superficie
        self.foto = foto

def dato_api() -> None:

    url: str = "https://v3.football.api-sports.io/"
    
    endpoints: tuple = (
        "leagues?id=128", "teams?league=128&season=", "fixtures?league=128&season=",
        ("teams/statistics?league=128&season=", "&team="), "predictions?fixture=",
        "fixtures/lineups?fixture="
    )

    headers: dict = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': "e31e12366af164902d3401b1d8e03718"
        }

    diccionario_temporadas(url, endpoints, headers)

def diccionario_temporadas(url: str, endpoints: tuple, headers: dict) -> dict:
    
    temporadas: dict = {}

    respuesta_temporadas: dict = requests.request("GET", url + endpoints[0], headers=headers)

    response: dict = (respuesta_temporadas.json()).get("response")
    seasons = (response[0]).get("seasons")

    for season in seasons:
        if (season.get("year") not in temporadas):
            temporadas[season.get("year")] = []
    
    diccionario_equipos(url, endpoints, headers, temporadas)
    

def diccionario_equipos(url: str, endpoints: tuple, headers: dict, temporadas: dict) -> dict:

    equipos: dict = {}

    for key in temporadas:
        respuesta_equipos: dict = requests.request("GET", url + endpoints[1] + str(key), headers=headers)

        response: dict = (respuesta_equipos.json()).get("response")

    print(response)

        # for i in range (len(response)):

        #     response[i][0]




def main () -> None:

    dato_api()

    return()

main()