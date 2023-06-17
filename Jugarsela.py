import requests
from datetime import datetime
import csv

def dato_api() -> list:
    """
    PRE: Ningún parámetro. Recopila toda la información que se va a emplear (o no) a lo largo
         del programa.
    POST: Un valor de retorno list. Devuelve una lista con los tres diccionarios creados.
    """
    url: str = "https://v3.football.api-sports.io/"

    year: str = str(datetime.now().year)

    endpoints: dict = {
        "temporadas": "leagues?id=128",
        "equipos": "teams?league=128&season=",
        "fixtures": "fixtures?league=128&season=" + year,
        "estadisticas": "teams/statistics?league=128&season=" + year + "&team=",
        "predicciones": "predictions?fixture=",
        "planteles": "players?league=128&season=" + year + "&team=",
        "posiciones": "standings?league=128&season="
    }

    headers: dict = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': "d6b40bb947b90f57f825bd5d2508b001"
        }

    temporadas: dict = diccionario_temporadas(url, year, endpoints, headers)
    equipos: dict = diccionario_equipos(url, year, endpoints, headers, temporadas)
    fixtures: dict = diccionario_fixtures (url, year, endpoints, headers)

    informacion_api: list = [temporadas, equipos, fixtures]

    return(informacion_api)

def diccionario_temporadas(url: str, year: str, endpoints: dict, headers: dict) -> dict:
    """
    PRE: Dos parámetros str. Dos parámetros dict. Crea el diccionario "temporadas" el cual
         almacena los años de la liga como clave, y los resultados de las posiciones como sus valores.
    POST: Un valor de retorno dict. Devuelve el diccionario "temporadas" ordenado por años de forma
          ascendente.
    """
    temporadas: dict = {}
    response: list = ((requests.request("GET", url + endpoints["temporadas"], headers=headers)).json()).get("response")
    seasons: dict = (response[0]).get("seasons")

    for season in seasons:
        if (season.get("year") not in temporadas):
            if (int(season.get("year")) < 2020):
                temporadas[season.get("year")] = []

            elif (int(season.get("year")) == 2020):
                temporadas[season.get("year")] = {}

            else:
                temporadas[season.get("year")] = {
                "Primera Fase": [],
                "Segunda Fase": []
                }

    temporadas: dict = informacion_posiciones(url, year, endpoints, headers, temporadas)
    return(temporadas)

def diccionario_equipos(url: str, year: str, endpoints: dict, headers: dict, temporadas: dict) -> dict:
    """
    PRE: Dos parámetros str. Tres parámetros dict. La función extrae, de cada temporada, los datos
         necesarios de los equipos que alguna vez participaron en la liga y almacena los nombres como
         claves, y los datos dentro de otro diccionario.
    POST: Un valor de retorno dict. Devuelve el diccionario "equipos" con la información detallada.
    """
    equipos: dict = {}

    for key in temporadas:

        response: list = ((requests.request("GET", url + endpoints["equipos"] + str(key), headers=headers)).json()).get("response")

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

            if (int(key) != int(year)):

                if (nombre_equipo not in equipos):
                    equipos[nombre_equipo] = {
					"id": code,
					"año": año,
					"escudo": escudo,
					"estadio": nombre_estadio,
					"direccion": direccion,
					"ciudad": ciudad,
					"capacidad": capacidad,
					"superficie": superficie,
					"foto": foto,
					"plantel": None,
					"estadisticas": None
					}

            else:
            
                plantel: list = informacion_planteles(url, year, code, endpoints, headers)
                estadistica: dict = informacion_estadisticas(url, year, code, endpoints, headers)

                if (nombre_equipo not in equipos):
                    equipos[nombre_equipo] = {
					"id": code,
					"año": año,
					"escudo": escudo,
					"estadio": nombre_estadio,
					"direccion": direccion,
					"ciudad": ciudad,
					"capacidad": capacidad,
					"superficie": superficie,
					"foto": foto,
					"plantel": plantel,
					"estadisticas": estadistica
					}

    return(equipos)

def diccionario_fixtures(url: str, year: str, endpoints: dict, headers: dict) -> dict:
    """
    PRE: Dos parámetros str. Dos parámetros dict. La función extrae los datos necesarios
         del fixture 2023 y los almacena por id en el diccionario "fixtures".
    POST: Un valor de retorno dict. Devuelve el diccionario "fixtures" con la información detallada.
    """
    fixtures: dict = {}
    hoy: str = fecha_actual()
    response: list = ((requests.request("GET", url + endpoints["fixtures"], headers=headers)).json()).get("response")

    for i in range (len(response)):

        fecha: tuple = reordenar_fecha(response[i]["fixture"]["date"])

        if (fecha[0]+fecha[1]+fecha[2] >= hoy):

            code: str = str(response[i]["fixture"]["id"])
            local: str = response[i]["teams"]["home"]["name"]
            visitante: str = response[i]["teams"]["away"]["name"]
            prediccion: str = informacion_predicciones(url, year, code, endpoints, headers)

            if (code not in fixtures):
                fixtures[code] = {
                                "fecha": fecha,
                                "local": local,
                                "visitante": visitante,
                                "prediccion": prediccion
                                }

    return(fixtures)

def informacion_planteles(url: str, year: str, code: str, endpoints: dict, headers: dict) -> list:
    """
    PRE: Tres parámetros str. Dos parámetros dict. Por cada equipo participante de la temporada 2023,
         la función extrae los datos disponibles del plantel y los almacena en una lista.
    POST: Un valor de retorno list. Devuelve la lista "plantel" con la información detallada.
    """
    plantel: list = []
    response: list = ((requests.request("GET", url + endpoints["planteles"] + code, headers=headers)).json()).get("response")

    for i in range (len(response)):

        nombre_completo: str = response[i]["player"]["firstname"] + " " + response[i]["player"]["lastname"] 
        posicion: str = traducir_posicion(response[i]["statistics"][0]["games"]["position"])

        if ((response[i]["statistics"][0]["games"]["captain"]) == True):
            dato_completo: str = f"{nombre_completo} ({posicion}), CAPITÁN"

        else:
            dato_completo: str = f"{nombre_completo} ({posicion})"

        plantel.append(dato_completo)

    return(plantel)

def informacion_posiciones(url: str, year: str, endpoints: dict, headers: dict, temporadas: dict) -> dict:
    """
    PRE: Dos parámetros str. Tres parámetros dict. La función extrae, por temporada, las posiciones
         y los puntos de los equipos en la liga y los almacena en el diccionario "temporadas" por orden.
    POST: Un valor de retorno dict. Devuelve el diccionario "temporadas" con la información nueva agregada.
    """
    for key in temporadas:

        response: list = ((requests.request("GET", url + endpoints["posiciones"] + str(key), headers=headers)).json()).get("response")
        league: dict = (response[0]).get("league")

        if (int(key) < 2020):
            temporadas: dict = sistema_antiguo(key, league, temporadas)

        elif (int(key) == 2020):
            temporadas: dict = sistema_2020(key, league, temporadas)

        else:
            temporadas: dict = sistema_nuevo(key, league, temporadas)

    return(temporadas)

def sistema_antiguo(key: str, league: dict, temporadas: dict) -> dict:
    """
    PRE: 
    POST:
    """
    for i in range (len(league["standings"][0])):

        equipo: str = league["standings"][0][i]["team"]["name"]
        puntos: str = str(league["standings"][0][i]["points"])

        temporadas[key].append((equipo, puntos))

    return(temporadas)

def sistema_2020(key: str, league: dict, temporadas: dict) -> dict:
    """
    PRE: 
    POST:
    """
    for i in range (len(league["standings"])):

        for j in range (len(league["standings"][i])):

            grupo: str = league["standings"][i][j]["group"]
            equipo: str = league["standings"][i][j]["team"]["name"]
            puntos: str = str(league["standings"][i][j]["points"])

            if (grupo not in temporadas[key]):
                temporadas[key][grupo] = []
            
            if (i <= 4):
                    temporadas[key][grupo].append((equipo, puntos))
            
            else:
                    temporadas[key][grupo].append((equipo, puntos))
    
    return(temporadas)

def sistema_nuevo(key: str, league: dict, temporadas: dict) -> dict:
    """
    PRE: 
    POST:
    """
    for i in range (len(league["standings"][0])):

        equipo: str = league["standings"][0][i]["team"]["name"]
        puntos: str = str(league["standings"][0][i]["points"])

        temporadas[key]["Segunda Fase"].append((equipo, puntos))

    for i in range (len(league["standings"][1])):

        equipo: str = league["standings"][1][i]["team"]["name"]
        puntos: str = str(league["standings"][1][i]["points"])

        temporadas[key]["Primera Fase"].append((equipo, puntos))
    
    return(temporadas)

def informacion_predicciones(url: str, year: str, code: str, endpoints: dict, headers: dict) -> str:
    """
    PRE: Tres parámetros str. Dos parámetros dict. Por cada partido aún no jugado, la función extrae el
         nombre del equipo que la API cree será el ganador.
    POST: Un valor de retorno str. Devuelve la predicción.
    """
    response: list = ((requests.request("GET", url + endpoints["predicciones"] + code, headers=headers)).json()).get("response")

    prediccion: str = response[0]["predictions"]["winner"]["name"]

    return(prediccion)

def informacion_estadisticas(url: str, year: str, code: str, endpoints: dict, headers: dict) -> dict:
    """
    PRE: Tres parámetros str. Dos parámetros dict. La función extrae las estadísticas de goles por minuto
         de los equipos de la temporada 2023.
    POST: Un valor de retorno dict. Devuelve el diccionario "estadicticas" con la información detallada.
    """
    estadistica: dict = {}

    response: list = ((requests.request("GET", url + endpoints["estadisticas"] + code, headers=headers)).json()).get("response")

    for intervalo in response["goals"]["for"]["minute"]:
        
        if (response["goals"]["for"]["minute"][intervalo]["total"] == None):
            goles: int = 0

        else:
            goles: int = response["goals"]["for"]["minute"][intervalo]["total"]
        
        estadistica[intervalo] = goles

    return(estadistica)

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
        osicion: str = "Mediocampista"

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
    
def menu_apuesta():
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