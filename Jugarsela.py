from informacion_api import informacion_api
from passlib.hash import pbkdf2_sha256
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from datetime import datetime
from io import BytesIO
import random
import requests
import time
import csv
import os

def diccionario_api(API: dict) -> list:
    """
    PRE: Un parámetro dict. Recopila toda la información que se va a emplear (o no) a lo largo
         del programa en una lista de diccionarios.
    POST: Un valor de retorno list. Devuelve una lista con los tres diccionarios creados.
    """
    imprimir_carga(0)

    temporadas: dict = diccionario_temporadas(API)
    equipos: dict = diccionario_equipos(API, temporadas)
    fixtures: dict = diccionario_fixtures (API)

    informacion_api: list = [temporadas, equipos, fixtures]

    imprimir_carga(4)
    time.sleep(0.5)

    return(informacion_api)

def imprimir_carga(tiempo: int) -> None:
    """
    PRE: Un parámetro int. Recibe el valor de un número entero.
    POST: Ningún valor de retorno. Imprime la cadena que se encuentra en la posición del entero ingresado.
    """
    CARGA: list = [
    "0% ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ 100%", "33% ▮ ▮ ▮ ▯ ▯ ▯ ▯ ▯ ▯ ▯ 100%",
    "66% ▮ ▮ ▮ ▮ ▮ ▮ ▯ ▯ ▯ ▯ 100%", "99% ▮ ▮ ▮ ▮ ▮ ▮ ▮ ▮ ▮ ▯ 100%",
    "100% ▮ ▮ ▮ ▮ ▮ ▮ ▮ ▮ ▮ ▮ 100%", "Cargando..."
    ]

    os.system("cls")
    print(CARGA[5])
    print(CARGA[tiempo])

    return(None)

def diccionario_temporadas(API: dict) -> dict:
    """
    PRE: Un parámetro dict. Crea el diccionario "temporadas" el cual almacena los años de la liga
         como clave, y los resultados de las posiciones como sus valores.
    POST: Un valor de retorno dict. Devuelve el diccionario "temporadas" ordenado por años de forma
          ascendente.
    """
    temporadas: dict = {}
    response: list = ((requests.request("GET", API["URL"] + API["ENDPOINTS"]["temporadas"], headers=API["HEADERS"])).json()).get("response")
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

    temporadas: dict = informacion_posiciones(API, temporadas)
    imprimir_carga(1)

    return(temporadas)

def diccionario_equipos(API: dict, temporadas: dict) -> dict:
    """
    PRE: Dos parámetros dict. La función extrae, de cada temporada, los datos necesarios de los
         equipos que alguna vez participaron en la liga y almacena los nombres como claves, y
         los datos dentro de otro diccionario.
    POST: Un valor de retorno dict. Devuelve el diccionario "equipos" con la información detallada.
    """
    equipos: dict = {}

    for key in temporadas:
        
        time.sleep(6.0)
        response: list = ((requests.request("GET", API["URL"] + API["ENDPOINTS"]["equipos"] + str(key), headers=API["HEADERS"])).json()).get("response")

        for i in range (len(response)):

            nombre_equipo: str = response[i]["team"]["name"]
            code: str = str(response[i]["team"]["id"])
            año: str = str(response[i]["team"]["founded"])
            escudo: str = response[i]["team"]["logo"]
            nombre_estadio: str = response[i]["venue"]["name"]
            direccion: str = response[i]["venue"]["address"]
            ciudad: str = response[i]["venue"]["city"]
            capacidad: str = str(response[i]["venue"]["capacity"])
            superficie: str = traducir_dato(response[i]["venue"]["surface"].lower())
            foto: str = response[i]["venue"]["image"]

            if (int(key) != 2023):

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
                
                plantel: list = informacion_planteles(API, code)
                estadistica: dict = informacion_estadisticas(API, code)

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

                else:
                    equipos[nombre_equipo]["plantel"] = plantel
                    equipos[nombre_equipo]["estadisticas"] = estadistica
    
    imprimir_carga(2)

    return(equipos)

def diccionario_fixtures(API: dict) -> dict:
    """
    PRE: Un parámetro dict. La función extrae los datos necesarios del fixture 2023 y los almacena
         por id en el diccionario "fixtures".
    POST: Un valor de retorno dict. Devuelve el diccionario "fixtures" con la información detallada.
    """
    time.sleep(6.0)

    fixtures: dict = {}
    hoy: str = fecha_actual()
    response: list = ((requests.request("GET", API["URL"] + API["ENDPOINTS"]["fixtures"], headers=API["HEADERS"])).json()).get("response")

    for i in range (len(response)):

        fecha: tuple = reordenar_fecha(response[i]["fixture"]["date"])

        if (fecha[0]+fecha[1]+fecha[2] >= hoy):

            code: str = str(response[i]["fixture"]["id"])
            local: str = response[i]["teams"]["home"]["name"]
            visitante: str = response[i]["teams"]["away"]["name"]

            if (code not in fixtures):
                fixtures[code] = {
                "fecha": fecha,
                "local": local,
                "visitante": visitante,
                }

    imprimir_carga(3)

    return(fixtures)

def informacion_planteles(API: dict, code: str) -> list:
    """
    PRE: Un parámetro dict. Un parámetro str. Por cada equipo participante de la temporada 2023, la
         función extrae los datos disponibles del plantel y los almacena en una lista.
    POST: Un valor de retorno list. Devuelve la lista "plantel" con la información detallada.
    """
    time.sleep(6.0)

    plantel: list = []
    response: list = ((requests.request("GET", API["URL"] + API["ENDPOINTS"]["planteles"] + code, headers=API["HEADERS"])).json()).get("response")

    for i in range (len(response)):

        nombre_completo: str = response[i]["player"]["firstname"] + " " + response[i]["player"]["lastname"] 
        posicion: str = traducir_dato((response[i]["statistics"][0]["games"]["position"]).lower())

        if ((response[i]["statistics"][0]["games"]["captain"]) == True):
            dato_completo: str = f"{nombre_completo} ({posicion}), CAPITÁN"

        else:
            dato_completo: str = f"{nombre_completo} ({posicion})"

        plantel.append(dato_completo)

    return(plantel)

def informacion_posiciones(API: dict, temporadas: dict) -> dict:
    """
    PRE: Dos parámetros dict. La función extrae, por temporada, las posiciones
         y los puntos de los equipos en la liga y los almacena en el diccionario "temporadas" por orden.
    POST: Un valor de retorno dict. Devuelve el diccionario "temporadas" con la información nueva agregada.
    """
    for key in temporadas:

        time.sleep(6.0)

        response: list = ((requests.request("GET", API["URL"] + API["ENDPOINTS"]["posiciones"] + str(key), headers=API["HEADERS"])).json()).get("response")
        league: dict = (response[0]).get("league")

        if (int(key) < 2020):
            temporadas: dict = posiciones_sistema_antiguo(key, league, temporadas)

        elif (int(key) == 2020):
            temporadas: dict = posiciones_sistema_2020(key, league, temporadas)

        else:
            temporadas: dict = posiciones_sistema_nuevo(key, league, temporadas)

    return(temporadas)

def posiciones_sistema_antiguo(key: str, league: dict, temporadas: dict) -> dict:
    """
    PRE: Un parámetro str. Dos parámetros dict. Si la temporada es previa al 2019 (inclusive) la función
         ordena la información segun como haya funcionado el sistema de posiciones de ese año.
    POST: Un valor de retorno dict. Devuelve el diccionario "temporadas" con la información detallada.
    """
    for i in range (len(league["standings"][0])):

        equipo: str = league["standings"][0][i]["team"]["name"]
        puntos: str = str(league["standings"][0][i]["points"])

        temporadas[key].append((equipo, puntos))

    return(temporadas)

def posiciones_sistema_2020(key: str, league: dict, temporadas: dict) -> dict:
    """
    PRE: Un parámetro str. Dos parámetros dict. Si la temporada es 2020 la función ordena la
         información segun como haya funcionado el sistema de posiciones de ese año.
    POST: Un valor de retorno dict. Devuelve el diccionario "temporadas" con la información detallada.
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

def posiciones_sistema_nuevo(key: str, league: dict, temporadas: dict) -> dict:
    """
    PRE: Un parámetro str. Dos parámetros dict. Si la temporada es a partir del 2021 (inclusive) la
         función ordena la información segun como haya funcionado el sistema de posiciones de ese año.
    POST: Un valor de retorno dict. Devuelve el diccionario "temporadas" con la información detallada.
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

def informacion_predicciones(API: dict, code: str) -> str:
    """
    PRE: Un parámetro dict. Un parámetro str. Por cada partido aún no jugado, la función extrae
         el nombre del equipo que la API cree será el ganador.
    POST: Un valor de retorno str. Devuelve la predicción.
    """
    response: list = ((requests.request("GET", API["URL"] + API["ENDPOINTS"]["predicciones"] + code, headers=API["HEADERS"])).json()).get("response")

    prediccion: str = response[0]["predictions"]["winner"]["name"]

    return(prediccion)

def informacion_estadisticas(API: dict, code: str) -> dict:
    """
    PRE: Un parámetro dict. Un parámetro str. La función extrae las estadísticas de goles por minuto de
         los equipos de la temporada 2023.
    POST: Un valor de retorno dict. Devuelve el diccionario "estadicticas" con la información detallada.
    """
    time.sleep(6.0)

    estadistica: dict = {}
    response: list = ((requests.request("GET", API["URL"] + API["ENDPOINTS"]["estadisticas"] + code, headers=API["HEADERS"])).json()).get("response")

    for intervalo in response["goals"]["for"]["minute"]:
        
        if (response["goals"]["for"]["minute"][intervalo]["total"] == None):
            goles: int = 0

        else:
            goles: int = response["goals"]["for"]["minute"][intervalo]["total"]
        
        estadistica[intervalo] = goles

    return(estadistica)

def traducir_dato(dato: str) -> str:
    """
    PRE: Un parámetros str. Recibe una palabra en inglés.
    POST: Un valor de retorno str. Devuelve la cadena traducida al español según corresponda.
    """
    if (dato == "grass"):
        traduccion: str = "pasto sintético"
        return(traduccion)

    elif (dato == "goalkeeper"):
        traduccion: str = "Arquero"
        return(traduccion)

    elif (dato == "defender"):
        traduccion: str = "Defensor"
        return(traduccion)

    elif (dato == "midfielder"):
        traduccion: str = "Mediocampista"
        return(traduccion)

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

def fecha_actual() -> str:
    """
    PRE: Ningún parámetro. Con la librería datetime se consigue la fecha actual y se modifica el formato.
    POST: Un valor de retorno str. Devuelve la fecha actual en el formato YYYYMMDD.
    """
    año = str((datetime.now()).year)
    mes = str((datetime.now()).month)
    dia = str((datetime.now()).day)

    if (len(mes) != 2):
        mes = "0"+mes

    cadena: str = (año + mes + dia)

    return(cadena)

def registro_transacciones(mail: str, tipo: int, importe: int, lista_transacciones: list) -> None:
    """
    PRE: Un parámetro str. Dos parámetros int. Un parámetro list. 
    POST: Ningún valor de retorno. 
    """
    #El type in del mail se puede modificar
    #Toma la fecha de hoy
    #El tipo de transaccion se determina con los valores 0, 1 y 2 de la siguiente manera
    if tipo == 0:
        resultado = "deposita"

    elif tipo==1:
        resultado = "gana"
        
    elif tipo==2:
        resultado="pierde"
        
    fecha = fecha_actual()
    datos_de_escritura = [[mail,fecha,resultado,importe]]
    lista_transacciones.append(datos_de_escritura)
    
def validacion_temporada_2023(equipo_elegido: str, numero_fase: dict) -> bool:
    """
    PRE: Un parámetro str. Un parámetro dict. Valida que el equipo ingresado forma parte de la temporada 2023.
    POST: Un valor de retorno bool. Devuelve True/False según corresponda.
    """
    equipos_temporada: list = []
    for fase in numero_fase:

        for i in range (len(numero_fase[fase])):
            equipo: str = (numero_fase[fase][i][0]).title()

            if equipo not in equipos_temporada:
                equipos_temporada.append(equipo)
    
    if equipo_elegido in equipos_temporada: return(False)
    else: return(True)

def mayor_ganador (usuarios_diccionario: dict, transacciones_listado: list) -> None:
    """
    PRE: Un parámetro dict. Un parámetro list. Itera la lista de transacciones y con un contador define
         el usuario que más veces ganó.
    POST: Ningún valor de retorno. Imprime una leyenda con el nombre del usuario y la cantidad de
          veces ganadas.
    """
    cantidad_apuestas = {} # usuario: cantidad
    mayor_ganador = ""
    mayor_veces_ganado = 0

    for i in range(len(transacciones_listado)):
        if transacciones_listado[i][2] == "Gana":
            if transacciones_listado[i][0] not in cantidad_apuestas:
                cantidad_apuestas[transacciones_listado[i][0]] = 1
            else: cantidad_apuestas[transacciones_listado[i][0]] += 1

    for i in cantidad_apuestas:
        if cantidad_apuestas[i] >= mayor_veces_ganado:
            mayor_veces_ganado = cantidad_apuestas[i]
            mayor_ganador = i

    print(f"El usuario que más veces ganó es {usuarios_diccionario[mayor_ganador][0]} con un total de {mayor_veces_ganado} de veces.")
    
def mayor_apostador (usuarios_diccionario: dict) -> None:
    """
    PRE: Un parámetro dict. Itera el diccioanrio_usuarios y con un contador define el usuario que más veces apostó.
    POST: Ningún valor de retorno. Imprime una leyenda con el nombre del usuario y la cantidad de veces apostadas.
    """
    mayor_apostador = ""
    mayor_cantidad_apostada = float(0)

    for i in usuarios_diccionario:
        if usuarios_diccionario[i][2] >= mayor_cantidad_apostada:
            mayor_cantidad_apostada = usuarios_diccionario[i][2]
            mayor_apostador = usuarios_diccionario[i][0]

    print(f"El usuario que más dinero apostó es {mayor_apostador} con un total de {mayor_cantidad_apostada}.")

def cargar_dinero (email: str, usuarios_diccionario: dict, transacciones_listado: list) -> None:
    """
    PRE: Un parámetro str. Un parámetro dict. Un parámetro list. Solicita al usuario ingresar un monto de dinero
         para depositar en su cuenta. Suma dicho monto al ya existente en el diccionario de usuarios.
    POST: Ningún valor de retorno. Notifica al usuario de la acción.
    """
    print("\x1B[3mCargar dinero a la cuenta\x1B[0m")

    dinero = float(input("Ingrese la cantidad de dinero que quiere ingresar a su cuenta: "))
    while dinero <= 0: dinero = float(input("Monto inválido. Ingrese la cantidad de dinero que quiere ingresar en su cuenta: "))
    
    usuarios_diccionario[email][4] += dinero
    fecha = fecha_actual()

    transacciones_listado.append([email,fecha,"Deposita",dinero])
    print(f"Dinero disponible: {usuarios_diccionario[email][4]}")

def grafica_goles (informacion_api: list) -> None:
    """
    PRE: Un parámetro list. Solicita al usuario elegir un equipo de la temporada 2023.
    POST: Ningún valor de retorno. Muestra un gráfico de barras los goles por minuto que realizó el equipo ingresado.
    """
    print("\x1B[3mEstadisticas - Goles por minutos\x1B[0m")
    equipo: str = input("Ingrese el equipo para ver sus estadísticas: ").title()

    while validacion_temporada_2023(equipo, informacion_api[0][2023]):
        equipo: str = input("El equipo que ingresó no es válido o no forma parte de la temporada 2023. Inténtelo nuevamente: ").title()

    estadisticas = informacion_api[1][equipo]["estadisticas"]
    minutos: list = []
    goles: list = []
    
    for tiempo in estadisticas:
        minutos.append(tiempo)
        goles.append(estadisticas[tiempo])

    plt.xlabel('MINUTOS')
    plt.ylabel('GOLES')
    plt.title('GOLES REALIZADOS POR INTERVALO DE TIEMPO')

    plt.bar(minutos, goles)
    plt.axis('off')
    plt.show()

def informacion_equipo(informacion_api: list) -> None:
    """
    PRE: Un parámetro list. Solicita al usuario elegir un equipo de la temporada 2023.
    POST: Ningún valor de retorno. Imprime datos del equipo seleccionado y muestra dos imagenes.
    """
    equipos = (informacion_api[1])

    print("\x1B[3mCuriosidades de equipos\x1B[0m")

    equipo = input("Ingrese el nombre de un equipo para ver su información: ")
    while equipo not in list(informacion_api[1].keys()):
        equipo = input("Equipo no encontrado, ingrese el nombre de otro equipo para ver su informacion: ")

    print(f'El estadio de {equipo} fue bautizado como {equipos[equipo]["estadio"]}. El mismo se encuentra en {equipos[equipo]["direccion"]}, {equipos[equipo]["ciudad"]}. Tiene una capacidad total de {equipos[equipo]["capacidad"]} espectadores, y su superficie está hecha de {equipos[equipo]["superficie"]}.')

    estadio = requests.get(url = equipos[equipo]["foto"])

    archivo_estadio = BytesIO(estadio.content)
    imagen_estadio = mpimg.imread(archivo_estadio, format="jpg")

    imagen_final = plt.imshow(imagen_estadio)
    plt.axis('off')
    plt.show()

    print(f"Y su escudo, es el siguiente.")

    escudo = requests.get(url = equipos[equipo]["escudo"])

    archivo_escudo = BytesIO(escudo.content)
    imagen_escudo = mpimg.imread(archivo_escudo, format="jpg")

    imagen_final = plt.imshow(imagen_escudo)
    plt.axis('off')
    plt.show()

def tabla_posiciones(informacion_api: list) -> None:
    """
    PRE: Un parámetro list. Solicita al usuario ingresar una temporada de la liga.
    POST: Ningún valor de retorno. Imprime la tabla de posiciones del año seleccionado.
    """
    temporadas = informacion_api[0]

    print("\x1B[3mTabla de posiciones de la Liga Profesional\x1B[0m")
    temporada = int(input("Ingrese la temporada de la cual quiere ver su ranking: "))
    while temporada < 2015 or temporada > 2023:
        temporada = int(input("Las temporadas disponibles son 2015-2023. Ingrese la temporada de la cual quiere ver su ranking: "))

    print("\n")
    print(f"Temporada {temporada} - Posiciones y puntos")

    if temporada <= 2019:
        for i in range(len(temporadas[temporada])):
            print(f"{i+1}) {temporadas[temporada][i][0]} - {temporadas[temporada][i][1]} puntos.")

    elif temporada == 2020:
        for grupo in informacion_api[0][2020]:
            print("\n")
            print(grupo)
            for i in range (len(informacion_api[0][2020][grupo])):
                equipo: str = informacion_api[0][2020][grupo][i][0]
                puntos: str = informacion_api[0][2020][grupo][i][1]
                print(f"{i+1}) {equipo} - {puntos} puntos.")

    elif temporada >= 2021:
        for fase in informacion_api[0][2023]:
            print("\n")
            print(fase)
            for i in range (len(informacion_api[0][2023][fase])):
                equipo: str = informacion_api[0][2023][fase][i][0]
                puntos: str = informacion_api[0][2023][fase][i][1]
                print(f"{i+1}) {equipo} - {puntos} puntos.")

def listado_equipos(informacion_api: list) -> None:
    """
    PRE: Un parámetro list. Imprime la lista de equipos de la temporada 2023 y solicita al usuario elegir un equipo.
    POST: Ningún valor de retorno. Imprime el plantel del equipo seleccionado.
    """
    equipos: list = []

    print("\x1B[3mEquipos - Liga Profesional Argentina, temporada 2023\x1B[0m")
    
    for fase in informacion_api[0][2023]:
        for i in range(len(informacion_api[0][2023][fase])):
            equipo: str = informacion_api[0][2023][fase][i][0]
            if equipo not in equipos:
                equipos.append(informacion_api[0][2023][fase][i][0])
    
    for i in range (len(equipos)):
        print(equipos[i])
    
    equipo: str = input("Ingrese el nombre de un equipo para ver su plantel: ").title()

    while validacion_temporada_2023(equipo, informacion_api[0][2023]):
        equipo: str = input("El equipo que ingresó no es válido o no forma parte de la temporada 2023. Inténtelo nuevamente: ").title()

    for jugador in range(len(informacion_api[1][equipo]["plantel"])):
        print(informacion_api[1][equipo]["plantel"][jugador])

def definir_partidos(equipo: str, fixtures: dict) -> dict:
    """
    PRE: Un parámetro str. Un parámetro dict. Itera el diccionario fixtures y verifica los partidos en los que
         participa el equipo definido.
    POST: Un valor de retorno dict. Devuelve un diccionario con los partidos.
    """
    partidos = {}
   
    for partido in fixtures:
        local = fixtures[partido]["local"].upper()
        visitante = fixtures[partido]["visitante"].upper()

        if equipo == local or equipo == visitante:
            info_partidos: list = fixtures[partido]
            partidos[partido] = info_partidos   

    return(partidos)

def encuadrado(objeto: str) -> str:
    """
    Funcion estetica que sirve para agregar el espacio necesario en el cuadro de los partidos (Ver mostrar_fixture)
    PRE: Un parámetro str. 
    POST: Un valor de retorno str. 
    """
    objeto = objeto + " " * (35 - (len(objeto)))

    return(objeto)

def mostrar_fixture(equipo: str, fixture: dict) -> dict:
    """
    Muestra al usuario un cuadra con todos los partidos A JUGAR del equipo seleccionado, el usuario elige uno. Se valida la eleccion.
    
    PRE: Un parámetro str. Un parámetro dict. Imprime el fixture de los partidos que va a jugar el equipo
         ingresado y solicita al usuario seleccionar uno de esos partidos.
    POST: Un valor de retorno dict. Devuelve la información del partido elegido.
    """
    partidos_a_alegir = (definir_partidos(equipo,fixture)).items()
    indice = 0

    if len(partidos_a_alegir)> 0:
        print("|\t|"+"Local"+" "*31+"|"+"visitante"+" "*26+"|"+"Fecha"+" "*5+"|")
        for partido in partidos_a_alegir:
            indice=indice+1
            año,mes,dia = partido[1]["fecha"]
            partido_fecha = año+"-"+mes+"-"+dia
            partido_local = partido[1]["local"]
            partido_visitante = partido[1]["visitante"]
            
            #AGREGO ESPACIADO PARA EL CUADRO
            partido_local = encuadrado(partido_local)
            partido_visitante = encuadrado(partido_visitante)
            print(f"|{indice}\t| {partido_local}|{partido_visitante}|{partido_fecha}|")
            
        
        partido_elegido = (input("Elija un partido indicando su número \n"))
        partido_valido = False

        #Validacion
        while partido_valido is False:
            if partido_elegido.isnumeric():
                partido_elegido = int(partido_elegido)
                if partido_elegido <= len(partidos_a_alegir):
                    partidos_a_alegir = list(partidos_a_alegir)
                    partido_valido = True
                    continue

                else:
                    partido_elegido = (input("Por favor, elija un partido de la lista \n"))
            else:
                partido_elegido = input("Debe ingresar el NUMERO del partido \n")
    #En caso de que el equipo elegido no tenga partidos a jugar, devuelve un diccionario vacio
    else:
        partido_elegido = 1
        partidos_a_alegir = [{}]
        
    return(partidos_a_alegir[partido_elegido-1]) # El numero 1 es el 0 de la lista.
    
def validar_apuesta_lv() -> int:
    """
    PRE: Ningún parámetro. Solicita al usuario ingrese su resultado deseado del partido.
    POST: Un valor de retorno int. Devuelve el valor del tipo de la apuesta según corresponda.
    """
    lov = input("Ingrese la opción a la que apostara Ganador(L)/Empate/Ganador(V): ")
    validado = False
    
    while validado is False:
        lov = lov.upper()

        if lov != "GANADOR(L)" and lov != "EMPATE" and lov != "GANADOR(V)": 
            lov = input("El termino ingresado no es correcto, Ganador(L)/Empate/Ganador(V)")

        else:
            validado = True

            if lov == "GANADOR(L)":
                apuesta = 1

            if lov == "EMPATE":
                apuesta = 2

            if lov == "GANADOR(V)":
                apuesta = 3
                
    return apuesta
def apuesta_dinero(dinero_disponible:int)->int:
    """
    Permite al usuario definir la cantidad de dinero a apostar. Permite al usuario cancelar la operacion en caso de no tener el monto deseado

    Args:
        dinero_disponible (int): Dinero en la cuenta del usuario

    Returns:
        int: Devuelve la cantidad de dinero apostada
    """
    print(f"Actualmente tiene {dinero_disponible}$ en la cuenta")
    
    cantidad_apostada = (input("Ingrese la cantidad de dinero a apostar \n"))
    apuesta_check = False
    
    while apuesta_check is False:
        if cantidad_apostada.isnumeric():
            cantidad_apostada = int(cantidad_apostada)
            if cantidad_apostada > dinero_disponible:
                
                print("La cantidad de dinero que quieres apostar no se encuentra disponible en tu cuenta.")
                print(f"Actualmente tiene {dinero_disponible}$ en la cuenta.")
                print("1) Cambiar la cantidad apostada")
                print("2) Cancelar la operacion")
                respuesta = input("¿Qué curso de acción desea tomar?\n")
                
                if respuesta == "1":
                    cantidad_apostada = (input("Ingrese la nueva cantidad a apostar: \n"))
                
                elif respuesta == "2":
                    cantidad_apostada = -1
                    apuesta_check = True
                    continue      
            else:
                apuesta_check = True
                continue
        else:
             cantidad_apostada = (input("La cantidad apostada debe ser un numero entero: \n"))
            
    return(cantidad_apostada)
        
def definir_apuesta(datos_del_partido:dict, dinero_en_cuenta: float) -> list:
    """
    Define la apuesta, el usuario decide si apostar a visitante, local o empate y el monto a apostar

    Args:
        datos_del_partido (dict): datos del partido
        dinero_en_cuenta (float): Dinero en la cuenta del usuario

    Returns:
        list: Devuelve una lista con [(resultado apostado),(monto apostado)]
    """
    local = datos_del_partido[1]["local"]
    visitante = datos_del_partido[1]["visitante"] 
    print(f"{local}(L) - {visitante}(V)")
    local_o_visitante =  validar_apuesta_lv()
   
    cantidad_apostada = apuesta_dinero(dinero_en_cuenta)
    
    valor_apuesta: list = [local_o_visitante,cantidad_apostada]

    return(valor_apuesta)

def pago_apuesta(resultado_apostado: int, dinero_apostado: int, prediccion: int, resultado_final: int, ratio_pago: int) -> tuple:
    """
    Define el pago de la apuesta del usuario dependiendo los argumentos de la funcion

    Args:
        resultado_apostado (int): resultado al cual aposto el usuario (1: Local, 2: Empate, 3:Visitante)
        dinero_apostado (int): Cantidad de dinero apostada por el usuario
        prediccion (int): Prediccion del ganador dada por la API
        resultado_final (int): Resultado final del partido  (1: Local, 2: Empate, 3:Visitante) (simulado)
        ratio_pago (int): Cantidad de dinero pagada por apuesta (Random entre 1 y 4 )

    Returns:
        tuple: Devuelve una tupla con Balance Final(puede ser positivo o negativo) y el tipo (Si perdio o gano) 
    """
    balance_final = 0
    tipo = ""
    
    if resultado_apostado == resultado_final:
        tipo = "Gana"

        if resultado_apostado == 2:
            balance_final = dinero_apostado + (dinero_apostado*ratio_pago)/2

        elif resultado_apostado == prediccion:
            balance_final = dinero_apostado + (dinero_apostado*ratio_pago)/10

        else:
            balance_final = dinero_apostado + (dinero_apostado*ratio_pago)
    else:
        tipo = "Pierde"
        balance_final = -dinero_apostado
        
    return (balance_final,tipo) 

def predicciones(partido,api)->int:
    """
    Solicita la prediccion a la api y la transfarma en un valor int (1: Gana Local, 3: Gana visitante)
    Args:
        partido (_type_): Informacion del partido [0] = id del partido, [1] diccionario con data del partido
        api (_type_): Indicaciones necesarias para llamar a la api

    Returns:
        int: Prediccion evaluada en numero entero
    """
    id = partido[0]
    local = partido[1]["local"].upper()
    visitante = partido[1]["visitante"].upper()
    prediccion_str = informacion_predicciones(api, id).upper()

    if prediccion_str == local:
        prediccion_int = 1

    elif prediccion_str == visitante:
        prediccion_int = 3
    
    return prediccion_int

def anunciar_resultado(dinero:float,partido:dict,resultado_final:int)->None:
    """
    Muestra el resultado del partido y de la apuesta en la consola

    Args:
        dinero (float): La cantidad de dinero ganada/perdida
        partido (dict): Informacion del partido (Sin jugar)
        resultado_final (int): Ganador del partido (Simulado)
    """
    local = partido[1]["local"]
    visitante = partido[1]["visitante"]
    print(f"-"*20)
    print(f"{local} - {visitante}")
    
    if resultado_final == 1:
        print(f"Ganador {local}")
    elif resultado_final == 2:
        print("Partido termina en empate")
    elif resultado_final == 3:
        print(f"Ganador {visitante}")
        
    if dinero < 0:
        print(f"Has perdido {-dinero}$")
    elif dinero > 0:
        print(f"Has ganado {dinero}$")
        
    print(f"-"*20)    
    input("presione enter para continuar")
        
def resultados_apuesta(apuesta,partido,api:dict)->tuple:
    """
    Realiza la "simulacion" del partido, llama a la funcion pago_apuesta para definir el pago y el tipo y lo devuelve

    Args:
        apuesta (_type_): Tiene la informacion de la apuesta, el monto y el resultado apostado
        partido (_type_): Tiene toda la informacion del partido (Ver dict de fixture)
        api (dict): Tiene la informacion necesaria para hacer pedidos a la api

    Returns:
        tuple: Devuelve una tupla con el balance final y el tipo de transaccion(Perdida,ganancia)
    """
    
    resultado_apostado,dinero_apostado = apuesta
    prediccion = predicciones(partido,api)
    ganador = random.randint(1,3)
    ratio_pago = random.randint(1,4)
    
    balance_y_tipo = pago_apuesta(resultado_apostado,dinero_apostado,prediccion,ganador,ratio_pago)
    
    
    anunciar_resultado(balance_y_tipo[0],partido,ganador)
    return balance_y_tipo

def printear_equipos_disponibles(equipos:dict)->None:
    """
    Muestra una lista de todos los equipos del torneo

    Args:
        equipos (dict): Diccionario con la informacion de los equipos, se utilizan sus keys.
    """
    i = 0

    for equipo in equipos.keys():
        i = i + 1
        print(f"{i}. {equipo}")
        
def validar_equipos(lista_equipos: dict) -> str:
    """
    PRE: Un parámetro dict. Verifica que el equipo ingresado se encuentre en la lista disponible.
    POST: Un valor de retorno str. Devuelve el equipo ingresado.
    """
    printear_equipos_disponibles(lista_equipos)

    equipo: str = input("Ingrese el nombre del equipo \n")
    valido: bool = False

    while valido is False:
        equipo: str = equipo.upper()

        for equipo_en_lista in lista_equipos:
            equipo_en_lista = equipo_en_lista.upper()

            if (equipo == equipo_en_lista):
                valido = True
                continue
            
        if (valido is False):
            printear_equipos_disponibles(lista_equipos)
            equipo = input("Equipo invalido. Ingrese un equipo que se encuentre en la lista \n")
            
    return(equipo)



def menu_apuesta(mail: str, dict_usuarios: dict, lista_transacciones: list, dict_equipos: dict, fixture: dict, API: dict) -> None:
    """
    Llama a las demas funciones de apuesta y guarda los resultados en las estructuras de datos que luego se guardaran en archivos.

    Args:
        mail (str): Mail del usuario.
        dict_usuarios (dict): Estructura de datos con la informacion del usuario.
        lista_transacciones (list): Lista con todas las trasacciones (Es donde se guardara si gana o pierde).
        dict_equipos (dict): Diccionario con la informacion de todos los equipos.
        fixture (dict): Diccionario con la informacion de todos los partidos.
        API (dict): Intrucciones varias para llamar a la API.
    """
    dinero_en_cuenta: int = int(dict_usuarios[mail][4])
    is_partido_elegido: bool = False

    while is_partido_elegido is False:
        equipo = validar_equipos(dict_equipos)
        partido = mostrar_fixture(equipo, fixture)

        if (len(partido) > 0): 
            is_partido_elegido: bool = True

        else:
            print("No existen partidos del equipo elegido. Por favor, seleccione otro.")
            input("Presione enter para continuar...")
    apuesta = definir_apuesta(partido, dinero_en_cuenta)

    if (apuesta[1] != -1):
        dinero_a_modificar,tipo = resultados_apuesta(apuesta,partido,API)
        lista_transacciones.append([mail,fecha_actual(),tipo,dinero_a_modificar])

        dict_usuarios[mail][4] += dinero_a_modificar
        

def opt_menu() -> str:
    """
    PRE: Ningún parámetro. Valida que el termino ingresado forma parte del intervalo definido.
    POST: Un valor de retorno str. Devuelve el termino.
    """
    opt: str = input("Ingrese el número correspondiente a la opción que quiera realizar: ")

    while opt not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]: opt: str = (f"El término que ingresó, '{opt}', no es válido. Inténtelo nuevamente: ")

    print(f"-"*20)

    return(opt)

def print_menu() -> None:
    """
    PRE: Ningún parámetro. Imprime el menú principal del programa.
    POST: Ningún valor de retorno. 
    """
    os.system("cls")
    print(f"-"*20)
    print(f"Ingrese el número correspondiente a la acción que quiera realizar: ")
    print(f"1. Consultar plantel")
    print(f"2. Tabla de posiciones")
    print(f"3. Curiosidades de equipos")
    print(f"4. Estadística de goles 2023")
    print(f"5. Cargar dinero a la cuenta")
    print(f"6. Usuario que más dinero apostó")
    print(f"7. Usuario que más veces ganó")
    print(f"8. Realizar apuesta")
    print(f"9. Cerrar sesión")
    print(f"-"*20)

def registrarse(usuarios_diccionario: dict) -> None:
    """
    PRE: Un parámetro dict. Solicita los datos para registrar un usuario nuevo y lo agrega al diccionario.
    POST: Ningún valor de retorno. De encontrarse ya registrado o de haber un error, lo notifica y
          vuelve al menú de inicio de sesión.
    """
    os.system("cls")
    print(f"-"*20)
    print(f"Ingrese sus datos para crear una nueva cuenta.")

    email = str(input("Email: ")) 
    usuario = str(input("Nombre de usuario: "))
    contraseña = str(input("Contraseña: "))
    hash = pbkdf2_sha256.hash(contraseña)

    for i in usuarios_diccionario:

        if email == i:
            print(f"-"*20)
            print("Usuario ya existente. Elija una opción para continuar: ")

            return(None)

        if "@" and ".com" not in email:
            print(f"-"*20)
            print("Formato de email incorrecto. Elija una opción para continuar: ")

            return(None)

    print(f"-"*20)
    print("Usuario creado exitosamente. Inicie sesión para continuar.")

    usuarios_diccionario[email] = [usuario, hash, float(0), 00000000, float(0)] 

def iniciar_sesion(usuarios_diccionario: dict) -> str:
    """
    PRE: Un parámetro dict. Lee el diccionario de usuarios y valida si el email y la contraseña se
         encuentran registrados. En caso contrario, lo notifica.
    POST: Un valor de retorno str. Devuelve el email ingresado o en blanco según corresponda.
    """
    os.system("cls")
    print(f"-"*20)
    print(f"Inicio de sesión")

    email: str = input("Email: ")
    contraseña: str = input("Contraseña: ")

    for i in usuarios_diccionario:
        if ((email == i) and (pbkdf2_sha256.verify(contraseña, usuarios_diccionario[email][1]))):
            print(f"-"*20)
            print(f"¡Bienvenido, {usuarios_diccionario[i][0]}!")
            continuar: str = input("\x1B[3mPresione Enter para continuar.\x1B[0m")
            return (email)

    print(f"-"*20)
    print("Combinación de usuario y contraseña incorrecta. Elija una opción para continuar: ")
    email: str = ""

    return (email)

def opt_bienvenida() -> str:
    """
    PRE: Ningún parámetro. Valida que el termino ingresado forma parte del intervalo definido.
    POST: Un valor de retorno str. Devuelve el termino.
    """
    opt: str = input("Ingrese el número correspondiente a la opción que quiera realizar: ")

    while opt not in ["1", "2", "3"]: opt: str = input(f"El término que ingresó, '{opt}', no es válido. Inténtelo nuevamente: ")

    return(opt)

def print_bienvenida() -> None:
    """
    PRE: Ningún parámetro. Imprime el menú de inicio de sesión.
    POST: Ningún valor de retorno.
    """
    os.system("cls")
    print(f"Bienvenido")
    print(f"-"*20)
    print(f"1) Iniciar sesion")
    print(f"2) Registrarse")
    print(f"3) Salir")
    print(f"-"*20)

def escritura_usuarios(usuarios_diccionario: dict) -> None:
    """
    PRE: Un parámetro dict. Recibe el diccionario con los datos de los usuarios.
    POST: Ningún valor de retorno. Vuelca toda la información del diccionario en el archivo
          "usuarios.csv" y lo cierra.
    """
    with open("usuarios.csv", "w", newline = "") as usuarios_csv:
        writer = csv.writer(usuarios_csv)
        writer.writerow(["email","usuario","contrasena","cantidad apostada","fecha ultima apuesta","dinero"])
        
        for i in usuarios_diccionario:
            writer.writerow([i,usuarios_diccionario[i][0],usuarios_diccionario[i][1],usuarios_diccionario[i][2],usuarios_diccionario[i][3],usuarios_diccionario[i][4]])

def escritura_transacciones(transacciones_listado: list)-> None:
    """
    PRE: Un parámetro list. Recibe la lista con las transacciones realizadas.
    POST: Ningún valor de retorno. Vuelca toda la información de la lista en el archivo "transacciones.csv".
    """
    with open("transacciones.csv", "w", newline = "") as transacciones_csv:
        writer = csv.writer(transacciones_csv)
        writer.writerow(["email","fecha","resultado","importe"])

        for i in range(len(transacciones_listado)):
            writer.writerow(transacciones_listado[i])

def finalizar_programa(transacciones_listado: list, usuarios_diccionario: dict) -> None:
    """
    PRE: Un parámetro list. Un parámetro dict. Recibe la lista de las transacciones y el diccionario de
         usuarios y los traslada a las funciones correspondientes.
    POST: Ningún valor de retorno. Tras realizarse las funciones dentro de esta, se cierra el programa.
    """
    os.system("cls")
    print("Finalizando programa...")

    escritura_transacciones(transacciones_listado)
    escritura_usuarios(usuarios_diccionario)
    
def transacciones_csv_to_listado(transacciones_listado: list) -> None:
    """
    PRE: Un parámetro dict. Recibe la estructura "transacciones_listado" vacía y lee el archivo "transacciones_csv".
    POST: Ningún valor de retorno. Vuelca los datos del archivo en la lista.
    """
    with open("transacciones.csv", newline='', encoding="UTF-8") as transacciones_csv:
        csv_reader = csv.reader(transacciones_csv, delimiter=',')
        next(csv_reader) 

        for fila in csv_reader:
            transacciones_listado.append([fila[0],fila[1],fila[2],float(fila[3])])

def usuarios_csv_to_diccionario(usuarios_diccionario: dict) -> None:
    """
    PRE: Un parámetro dict. Recibe la estructura "usuarios_diccionario" vacía y lee el archivo "usuarios_csv".
    POST: Ningún valor de retorno. Vuelca los datos del archivo en el diccionario.
    """
    with open("usuarios.csv", newline='', encoding="UTF-8") as usarios_csv:
        csv_reader = csv.reader(usarios_csv, delimiter=',')
        next(csv_reader)

        for fila in csv_reader:
            usuarios_diccionario[fila[0]] = [(fila[1]),(fila[2]), float(fila[3]),int(fila[4]), float(fila[5])]

def main () -> None:
    TEMPORADAS = 0 
    EQUIPOS = 1
    FIXTURE = 2

    API: dict = {
        "URL": "https://v3.football.api-sports.io/",

        "ENDPOINTS": {
            "temporadas": "leagues?id=128",
            "equipos": "teams?league=128&season=",
            "fixtures": "fixtures?league=128&season=2023",
            "estadisticas": "teams/statistics?league=128&season=2023" + "&team=",
            "predicciones": "predictions?fixture=",
            "planteles": "players?league=128&season=2023" + "&team=",
            "posiciones": "standings?league=128&season="
            },

        "HEADERS": {
            'x-rapidapi-host': "v3.football.api-sports.io",
            'x-rapidapi-key': "2dd5cdf12ff3a61bb332ad97d9fa2164"#"d6b40bb947b90f57f825bd5d2508b001"
            }
        }
    
    #informacion_api: list = diccionario_api(API)

    usuarios_diccionario: dict = {}
    # email(id):[usuario, contraseña, cantidad_apostada, fecha_última_apuesta, dinero_disponible]

    transacciones_listado: list = []
    # email(id):[fecha, resultado, importe]

    email: str = ""
    usuarios_csv_to_diccionario(usuarios_diccionario)
    transacciones_csv_to_listado(transacciones_listado)

    print_bienvenida()
    opt: str = opt_bienvenida()

    while opt != "3":

        if opt == "1":
            email = iniciar_sesion(usuarios_diccionario)

        elif opt == "2":
            registrarse(usuarios_diccionario)

        while email != "":

            print_menu()
            opcion: str = opt_menu()

            while opcion != "9":

                if opcion == "1":
                    listado_equipos(informacion_api) 

                elif opcion == "2":
                    tabla_posiciones(informacion_api)

                elif opcion == "3":
                    informacion_equipo(informacion_api)

                elif opcion == "4":
                    grafica_goles(informacion_api)

                elif opcion == "5":
                    cargar_dinero(email, usuarios_diccionario, transacciones_listado)

                elif opcion == "6":
                    mayor_apostador(usuarios_diccionario)

                elif opcion == "7":
                    mayor_ganador(usuarios_diccionario,transacciones_listado)

                elif opcion == "8":
                    menu_apuesta(email, usuarios_diccionario, transacciones_listado, informacion_api[1], informacion_api[2], API)

                print_menu()
                opcion = opt_menu()

            email: str = ""

        print_bienvenida()
        opt: str = opt_bienvenida()

    finalizar_programa(transacciones_listado, usuarios_diccionario)

main()