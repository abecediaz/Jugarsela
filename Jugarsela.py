import requests
from datetime import datetime
import csv

class Equipo:
    def __init__(self, nombre, code, año, escudo):
        self.nombre = nombre
        self.code = code
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

class Fixture:
    def __init__(self, fecha, local, visitante, ganador):
        self.fecha = fecha
        self.local = local
        self.visitante = visitante
        self.ganador = ganador

def dato_api() -> dict:
    """
    PRE: Ningún parámetro. .
    POST: Un valor de retorno dict.
    """
    url: str = "https://v3.football.api-sports.io/"

    year: str = str(datetime.now().year)

    endpoints: dict = {
        "temporadas": "leagues?id=128", #HECHO
        "equipos": "teams?league=128&season=", #HECHO
        "fixtures": "fixtures?league=128&season=" + year, #HECHO
        "estadisticas": "teams/statistics?league=128&season=" + year + "&team=", 
        "predicciones": "predictions?fixture=", #HECHO
        "planteles": "players?league=128&season=" + year + "&team=", #EN_PROCESO
        "posiciones": "standings?league=128&season=" #HECHO
    }

    headers: dict = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': "e31e12366af164902d3401b1d8e03718"
        }

    temporadas: dict = diccionario_temporadas(url, endpoints, headers)

    equipos: dict = diccionario_equipos(url, endpoints, headers, temporadas)

    fixtures: dict = diccionario_fixtures (url, endpoints, headers, temporadas)

def diccionario_temporadas(url: str, endpoints: dict, headers: dict) -> dict:
    """
    PRE: Un parámetro str. Dos parámetros dict. Crea el diccionario troncal del programa, el cual
         almacena las posiciones de cada temporada.
    POST: Un valor de retorno dict. Devuelve el diccionario "temporadas" ordenado por fechas de forma
          ascendente.
    """
    temporadas: dict = {}

    respuesta_temporadas: dict = requests.request("GET", url + endpoints["temporadas"], headers=headers)

    response: list = (respuesta_temporadas.json()).get("response")
    seasons: dict = (response[0]).get("seasons")

    for season in seasons:
        if (season.get("year") not in temporadas):
            temporadas[season.get("year")] = []
    
    temporadas: dict = informacion_posiciones(url, endpoints, headers, temporadas)

def informacion_posiciones(url: str, endpoints: dict, headers: dict, temporadas: dict) -> dict:
    """
    PRE: Un parámetro str. Tres parámetros dict. La función extrae, por temporada, las posiciones
         de los equipos en la liga y los almacena en orden en el diccionario "temporadas".
    POST: Un valor de retorno dict. Devuelve el diccionario "temporadas" con la información nueva agregada.
    """
    for key in temporadas:
        respuesta_posiciones: dict = requests.request("GET", url + endpoints["posiciones"] + str(key), headers=headers)

        response: list = (respuesta_posiciones.json()).get("response")
        league: dict = (response[0]).get("league")

        for i in range (len(league["standings"][1])):

            temporadas[key].append(str(league["standings"][1][i]["team"]["name"]))
    
    return(temporadas)

def diccionario_equipos(url: str, endpoints: dict, headers: dict, temporadas: dict) -> dict:
    """
    PRE: Un parámetro str. Tres parámetros dict. La función extrae, por temporada, los datos
         necesarios de los equipos participantes y los almacena por nombre en el diccionario "equipos".
    POST: Un valor de retorno dict. Devuelve el diccionario "equipos" con la información.
    """
    equipos: dict = {}

    for key in temporadas:

        respuesta_temporadas: dict = requests.request("GET", url + endpoints["equipos"] + key, headers=headers)

        response: list = (respuesta_temporadas.json()).get("response")

        for i in range (len(response)):

            nombre_equipo: str = response[i]["team"]["name"]

            code: str = str(response[i]["team"]["id"])
            año: str = str(response[i]["team"]["founded"])
            escudo: str = response[i]["team"]["logo"]

            nombre_estadio: str = response[i]["venue"]["name"]
            direccion: str = response[i]["venue"]["address"]
            ciudad: str = response[i]["venue"]["city"]
            capacidad: str = str(response[i]["venue"]["capacity"])
            superficie: str = response[i]["venue"]["surface"]
            foto: str = response[i]["venue"]["image"]

            estadio = Estadio(nombre_estadio, direccion, ciudad, capacidad, superficie, foto)
            equipo = Equipo(nombre_equipo, code, año, escudo)

            if (nombre_equipo not in equipos):
                    equipos[nombre_equipo] = (equipo, estadio)
    
    return(equipos)

def diccionario_fixtures(url: str, endpoints: dict, headers: dict) -> dict:
    """
    PRE: Un parámetro str. Dos parámetros dict. La función extrae los datos necesarios
         del fixture 2023 y los almacena por id en el diccionario "fixtures".
    POST: Un valor de retorno dict. Devuelve el diccionario "fixtures" con la información.
    """
    fixtures: dict = {}

    respuesta_fixtures: dict = requests.request("GET", url + endpoints["fixtures"], headers=headers)

    response: list = (respuesta_temporadas.json()).get("response")

    for i in range (len(response)):

        code: str = str(response[i]["fixture"]["id"])

        fecha: tuple = reordenar_fecha(response[i]["fixture"]["date"])
        local: str = response[i]["teams"]["home"]["name"]
        visitante: str = response[i]["teams"]["away"]["name"]
        ganador: str = informacion_predicciones(url, code, endpoints, headers)

        fixture = Fixture(fecha, local, visitante, ganador)

        if (code not in fixtures):
            fixtures[code] = fixture

    return(fixtures)

def informacion_predicciones(url: str, code: str, endpoints: dict, headers: dict) -> str:
    """
    PRE: Dos parámetros str. Dos parámetros dict.
    POST: Un valor de retorno dict.
    """

    respuesta_predicciones: dict = requests.request("GET", url + endpoints["predicciones"] + code, headers=headers)
    response: list = (respuesta_predicciones.json()).get("response")

    ganador: str = response[0]["predictions"]["winner"]["name"]

    return(ganador)

def diccionario_planteles(url: str, endpoints: dict, headers: dict, equipos: dict) -> dict:
    """
    PRE:
    POST:
    """
    for equipo in equipos:
        respuesta_predicciones: dict = requests.request("GET", url + endpoints["planteles"] + (equipos[equipo]).code, headers=headers)
        
        response: list = (respuesta_predicciones.json()).get("response")

        for i in range (len(response)):

            jugador: str = response[i]["player"]["name"]
            nombre_completo: str = response[i]["player"]["firstname"] + response[i]["player"]["lastname"] 
            posicion: str = traducir_posicion(response[i]["statistics"][0]["games"]["position"])

            if (len(equipos[equipo]) == 1):
                equipos[equipo].append([(jugador, nombre_completo, posicion)])
            else:
                equipos[equipo].append((jugador, nombre_completo, posicion))

    return(equipos)

def traducir_posicion(posicion: str) -> str:
   """
   PRE: Un parámetros str. Recibe el nombre en inglés de una posición de juego en el futbol.
   POST: Un valor de retorno str. Devuelve la cadena traducida al español según corresponda.
   """

    if (posicion == "Goalkeeper"):
        posicion: str = "Arquero"

    elif (posicion == "Defender"):
        posicion: str = "Defensor"

    elif (posicion == "Midfielder"):
        posicion: str = "Mediocampista"

    return(posicion)






def reordenar_fecha(fecha: str) -> tuple:
    """
    PRE: Un parámetro str. Recibe una fecha y hora con la siguiente forma 'XXXX-XX-XXTXX:XX:XX+XX:XX',
         extrae unicamente la fecha y le da un nuevo formato.
    POST: Un valor de retorno tuple. Devuelve la fecha en una tupla '(año, mes, día)'.
    """
    año: str = fecha[:4:]
    mes: str = fecha[5:7:]
    dia: str = fecha[8:10:]

    return ((año, mes, dia))

def fecha_actual()->str:
    #Devuelve un string en el formato YYYYMMDD de la fecha actual
    
    año = str((datetime.now()).year)
    mes = str((datetime.now()).month)
    dia = str((datetime.now()).day)
    if len(mes)!=2:
        mes = "0"+mes
    cadena = (año+mes+dia)
    return cadena

def registro_transacciones(mail:str,tipo:int,importe:int):
    #El type in del mail se puede modificar
    #Toma la fecha de hoy
    #El tipo de transaccion se determina con los valores 0,1 y 2 de la siguiente manera
    if tipo == 0:
        resultado = "deposita"
    elif tipo==1:
        resultado = "gana"
    elif tipo==2:
        resultado="pierde"
        
    fecha = fecha_actual()
    datos_de_escritura = [[mail,fecha,resultado,importe]]
    
    with open("transacciones.csv","a") as transacciones:
        escritura_csv = csv.writer(transacciones)
        escritura_csv.writerows(datos_de_escritura)
        
def main () -> None:

    return()

main()