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
        "predicciones": "predictions?fixture=",
        "planteles": "fixtures/lineups?fixture=",
        "posiciones": "standings?league=128&season=" #HECHO
    }

    headers: dict = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': "e31e12366af164902d3401b1d8e03718"
        }

    posiciones_temporadas: dict = diccionario_temporadas(url, endpoints, headers)

    equipos: dict = diccionario_equipos(url, endpoints, headers, posiciones_temporadas)

    fixtures: dict = diccionario_fixtures (url, endpoints, headers, posiciones_temporadas)

def diccionario_temporadas(url: str, endpoints: dict, headers: dict) -> dict:
    """
    PRE: Un parámetro str. Dos parámetros dict. Crea el diccionario troncal del programa, el cual
         almacena las posiciones de cada temporada.
    POST: Un valor de retorno dict. Devuelve el diccionario "posiciones_temporadas" ordenado por fechas de forma
          ascendente.
    """
    posiciones_temporadas: dict = {}

    respuesta_temporadas: dict = requests.request("GET", url + endpoints["temporadas"], headers=headers)

    response: list = (respuesta_temporadas.json()).get("response")
    seasons: dict = (response[0]).get("seasons")

    for season in seasons:
        if (season.get("year") not in posiciones_temporadas):
            posiciones_temporadas[season.get("year")] = []
    
    posiciones_temporadas: dict = diccionario_posiciones(url, endpoints, headers, posiciones_temporadas)

def diccionario_posiciones(url: str, endpoints: dict, headers: dict, posiciones_temporadas: dict) -> dict:
    """
    PRE: Un parámetro str. Tres parámetros dict. La función extrae, por temporada, las posiciones
         de los equipos en la liga y los almacena en orden en el diccionario "posiciones".
    POST: Un valor de retorno dict. Devuelve el diccionario "posiciones" con la información.
    """
    for key in posiciones_temporadas:
        respuesta_posiciones: dict = requests.request("GET", url + endpoints["posiciones"] + str(key), headers=headers)

        response: list = (respuesta_posiciones.json()).get("response")
        league: dict = (response[0]).get("league")

        for i in range (len(league["standings"][1])):

            posiciones_temporadas[key].append(str(league["standings"][1][i]["team"]["name"]))
    
    return(posiciones_temporadas)

def diccionario_equipos(url: str, endpoints: dict, headers: dict, posiciones_temporadas: dict) -> dict:
    """
    PRE: Un parámetro str. Tres parámetros dict. La función extrae, por temporada, los datos
         necesarios de los equipos participantes y los almacena por nombre en el diccionario "equipos".
    POST: Un valor de retorno dict. Devuelve el diccionario "equipos" con la información.
    """
    equipos: dict = {}

    for key in posiciones_temporadas:

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

        if (code not in fixtures):
            fixtures[code] = (fecha, (local, "L"), (visitante, "V"))

    return(fixtures)







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
    
    fecha = datetime.now()
    año= str(fecha.year)
    mes = str(fecha.month)
    dia = str(fecha.day)
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

def mostrar_fixture(equipo,fiture:dict):
    pass
def validar_apuesta_lv(lov:str):
    pass
def validar_apuesta_dinero(cantidad:int):
    pass
def resultados_apuesta(apuesta):
    pass
def definir_apuesta(): 
    #ARGUMENTOS A DEFINIR, FUNCION INCOMPLETA
    local_o_visitante = input("Ingrese a que equipo apostara (L/V)")
    validar_apuesta_lv(local_o_visitante)
    cantidad_apostada = int(input("Ingrese la cantidad de dinero a apostar"))
    validar_apuesta_dinero(cantidad_apostada)
    
    valor_apuesta = [local_o_visitante,cantidad_apostada]
    return valor_apuesta
    
def  menu_apuesta():
    #ARGUMENTOS A DEFINIR, FUNCION INCOMPLETA
    equipo = input("Ingrese el equipo")
    partido = mostrar_fixture(equipo)
    local,visitante,fecha,prediccion = partido
    apuesta = definir_apuesta()
    tipo,dinero_a_modificar = resultados_apuesta
    registro_transacciones("PLACEHOLDER",tipo,dinero_a_modificar)
    #MODIFICAR LA CANTIDAD DE DINERO EN EL DOCUMENTO DE USUARIOS
    pass
def main () -> None:

    return()

main()