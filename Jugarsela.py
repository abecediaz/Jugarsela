import requests
import time
import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime

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
    
    imprimir_carga(2)

    return(equipos)

def diccionario_fixtures(API: dict) -> dict:
    """
    PRE: Un parámetro dict. La función extrae los datos necesarios del fixture 2023 y los almacena
         por id en el diccionario "fixtures".
    POST: Un valor de retorno dict. Devuelve el diccionario "fixtures" con la información detallada.
    """
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
    estadistica: dict = {}

    response: list = ((requests.request("GET", API["URL"] + API["ENDPOINTS"]["estadisticas"] + code, headers=API["HEADERS"])).json()).get("response")

    for intervalo in response[0]["goals"]["for"]["minute"]:
        
        if (response[0]["goals"]["for"]["minute"][intervalo]["total"] == None):
            goles: int = 0

        else:
            goles: int = response[0]["goals"]["for"]["minute"][intervalo]["total"]
        
        estadistica[intervalo] = goles

    return(estadistica)

def traducir_dato(dato: str) -> str:
    """
    PRE: Un parámetros str. Recibe una palabra en inglés.
    POST: Un valor de retorno str. Devuelve la cadena traducida al español según corresponda.
    """
    if (dato == "grass"):
        traduccion: str = "Pasto sintético"

    elif (dato == "goalkeeper"):
        traduccion: str = "Arquero"

    elif (dato == "defender"):
        traduccion: str = "Defensor"

    elif (dato == "midfielder"):
        traduccion: str = "Mediocampista"

    return(dato)

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



def registro_transacciones(mail:str,tipo:int,importe:int,lista_transacciones:list):
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
    lista_transacciones.append(datos_de_escritura)
    
def definir_partidos(equipo:str,fixture:dict)->list:
    partidos = []
    local = 1
    visitante = 2
    for partido in fixture:
        if equipo == partido[local] or equipo == partido[visitante]:
            partidos.append(partido)
    return partidos

def encuadrado(objeto:str)->str:
    objeto = objeto + " " * (35 - (len(objeto)))
    return objeto

def mostrar_fixture(equipo:str,fixture:dict):
    fecha = 0
    local = 1
    visitante = 2
     
    
    lista_partidos = definir_partidos(equipo,fixture)
    indice = 0
    if len(lista_partidos)> 0:
        print(" |"+"Local"+" "*30+"|"+"visitante"+" "*26+"|"+"Fecha"+" "*3+"|")
        for partido in lista_partidos:
            indice=indice+1
            partido_fecha = reordenar_fecha(partido[fecha])
            partido_local = partido[local]
            partido_visitante = partido[visitante]
            
            #AGREGO ESPACIADO PARA EL CUADRO
            partido_local = encuadrado(partido_local)
            partido_visitante = encuadrado(partido_visitante)
            print(f"|{indice}{partido_local}|{partido_visitante}|{partido_fecha}|")
            
        partido_elegido = input("Elija un partido")
        return lista_partidos[partido_elegido-1] # El numero 1 es el 0 de la lista.
    
    return lista_partidos # REESTRUCTURAR DE FORMA MAS INGENIOSA

def validar_apuesta_lv()-> str:
    lov = input("Ingrese a que equipo apostara (L/V)")
    validado = False
    
    while validado is False:
        lov = lov.upper()
        if lov != "L" or "V": 
            lov = input("El termino ingresado no es correcto, ingrese L o V")
        else:
            validado = True
            
    return lov

def apuesta_dinero(dinero_disponible:int)->int:
    #FALTA AGREGAR LA FUNCION QUE AGREGA DINERO EN LA CUENTA
    cantidad_apostada = int(input("Ingrese la cantidad de dinero a apostar"))
    apuesta_check = False
    
    
    while apuesta_check is False:
        if cantidad_apostada > dinero_disponible:
            
            print("La cantidad de dinero que quieres apostar no se encuentra disponible en tu cuenta")
            print("1. Cargar mas dinero a la cuenta")
            print("2. Cambiar la cantidad apostada")
            print("3. Cancelar la operacion")
            respuesta = input("Que curso de accion desea tomar?")
            
            
            if respuesta == "1":
                #ACA VA LA FUNCION QUE CARGA PLATA A LA CUENTA
                pass
            
            elif respuesta == "2":
                cantidad_apostada = input("Ingrese la nueva cantidad a apostar")
                
            elif respuesta == "3":
                cantidad_apostada = -1
                apuesta_check = True
        else:
            apuesta_check = True
            
    return cantidad_apostada
                 
def resultados_apuesta(apuesta):
    #COMPLETAR MAÑANA XD
    pass

def definir_apuesta(datos_del_partido,dinero_en_cuenta): 
    #ARGUMENTOS A DEFINIR, FUNCION INCOMPLETA
    local_o_visitante =  validar_apuesta_lv()
   
    cantidad_apostada = apuesta_dinero(dinero_en_cuenta)
   
    
    valor_apuesta = [local_o_visitante,cantidad_apostada]
    return valor_apuesta
    
def printear_equipos_disponibles(equipos:dict)->None:
    i = 0
    for equipo in equipos.keys():
        i == i + 1
        print(f"{i}. {equipo}")
        
def validar_equipos(equipo:str,lista_equipos:dict):
    equipo = equipo.upper()
    valido = False
    while valido is False:
        for equipo_en_lista in lista_equipos:
            equipo_en_lista = equipo_en_lista.upper()
            if equipo == equipo_en_lista:
                valido = True
        
        if valido is False:
            printear_equipos_disponibles(lista_equipos)
            equipo = input("Equipo invalido, ingrese un equipo que se encuentre en la lista")
    
def menu_apuesta(mail:str,dict_usuarios:dict,dict_transacciones:dict,dict_equipos:dict):
    #FUNCION INCOMPLETA
    
    dinero_en_cuenta = int(dict_usuarios[mail][4])
    is_partido_elegido = False
    while is_partido_elegido is False:
        printear_equipos_disponibles()
        equipo = input("Ingrese el nombre del equipo")
        validar_equipos(equipo)
        
        partido = mostrar_fixture(dict_equipos,equipo)
        if len(partido)>0: 
            is_partido_elegido = True
        else:
            print("No existen partidos del equipo elegido. Por favor elija otro equipo")
    #local,visitante,fecha,prediccion = partido
    
    apuesta = definir_apuesta(partido,dinero_en_cuenta)
    if apuesta[1] != -1:
        tipo,dinero_a_modificar = resultados_apuesta()
        registro_transacciones(mail,tipo,dinero_a_modificar,dict_transacciones)
        #AGREGAR: MODIFICAR LA CANTIDAD DE DINERO EN EL DOCUMENTO DE USUARIOS
        pass

# from passlib.hash import pbkdf2_sha256

def apuesta_main () -> None:
    print("Menu de apuestas")

def mayor_ganador () -> None:
    print("El usuario que más veces ganó es... ")
    
def mayor_apostador () -> None:
    print("El usuario que más dinero apostó es... ")

def cargar_dinero () -> None:
    print("Carga de Dinero")

def grafica_goles () -> None:
    print("grafica de goles")

def informacion_equipo() -> None:
    print("info")

def tabla_posiciones() -> None:
    print("Tabla de posiciones de la Liga Profesional")

def listado_equipos() -> None:
    print("Listado de equipos de la Liga Profesional correspondiente temporada 2023")

def opt_menu() -> None:
    opt = str(input("Ingrese una opción: "))
    while opt not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]: opt = str(input("Ingrese una opción valida: "))
    return opt

def print_menu() -> None:
    print(f"-"*20)
    print(f"Esta es la interfaz, seleccione lo que desea hacer")
    print(f"1. Ver el listado de equipos")
    print(f"2. Ver la tabla de posiciones de la Liga profesional")
    print(f"3. Ver informacion de un equipo")
    print(f"4. Ver grafica de goles por equipo")
    print(f"5. Cargar dinero")
    print(f"6. Ver el usuario que más dinero apostó")
    print(f"7. Ver el usuario que más veces ganó ")
    print(f"8. Apostar")
    print(f"9. Cerrar sesion")
    print(f"-"*20)

def registrarse(usuarios_diccionario:dict) -> None:
    print(f"-"*20)
    print(f"Proporcione sus datos para crear una nueva cuenta")
    email = str(input("Email: ")) 
    usuario = str(input("Nombre de Usuario: "))
    contraseña = str(input("Contraseña: "))

    for i in usuarios_diccionario:
        if email == i:
            print(f"-"*20)
            print("Usuario ya existente, elija una opcion para continuar")
            return
    

    print(f"-"*20)
    print("Usuario creado exitosamente, inicie seion para continuar")
    usuarios_diccionario[email] = [usuario, contraseña] #agregar los vlaores que faltan

def iniciar_sesion(usuarios_diccionario:dict) -> None:
    print(f"-"*20)
    print(f"Inicio de Sesion")
    email = str(input("Email: ")) 
    contraseña = str(input("Contraseña: "))

    for i in usuarios_diccionario:
        if email == i and contraseña == usuarios_diccionario[i][1]:
            print(f"-"*20)
            print(f"Bienvenido {usuarios_diccionario[i][0]}")
            return email

    print(f"-"*20)
    print("Combinacion de usuario y contraseña incorecta, elija una opcion para continuar")
    email = ""
    return email

def opt_bienvenida() -> None:
    opt = str(input("Ingrese una opción: "))
    while opt not in ["1", "2", "3"]: opt = str(input("Ingrese una opción valida: "))
    return opt

def print_bienvenida() -> None:
    print(f"-"*20)
    print(f"1. Iniciar Sesion")
    print(f"2. Registrarse")
    print(f"3. Salir")
    print(f"-"*20)

def transacciones_lista_to_csv(lista_transacciones:list)->None:
    with open("transacciones.csv","a") as transacciones:
        escritura_csv = csv.writer(transacciones)
        escritura_csv.writerows(lista_transacciones)
    
def transacciones_csv_to_diccionario(transacciones_diccionario: dict) -> None: #EL DOCUMENTO TRANSACCIONES ES UN REGISTRO, NO HACE FALTA LEERLO; HAGO FUNCION PARA ESCRIBIR EN APPEND
    with open("transacciones.csv", newline='', encoding="UTF-8") as transacciones_csv:
        csv_reader = csv.reader(transacciones_csv, delimiter=',')
        next(csv_reader) 
        for fila in csv_reader:
            transacciones_diccionario[fila[0]] = [(fila[1]),(fila[2]),(fila[3])]

def usuarios_csv_to_diccionario(usuarios_diccionario: dict) -> None:
    with open("usuarios.csv", newline='', encoding="UTF-8") as usarios_csv:
        csv_reader = csv.reader(usarios_csv, delimiter=',')
        next(csv_reader) 
        for fila in csv_reader:
            usuarios_diccionario[fila[0]] = [(fila[1]),(fila[2]),(fila[3]),(fila[4]),(fila[5])]


    print(usuarios_diccionario[fila[0]][2])
    
def finalizar_programa(lista_transacciones,lista_usuarios):
    transacciones_lista_to_csv(lista_transacciones)
    #ACA IRIA LA FUNCION QUE MODIFICA EL ARCHIVO DE USUARIOS ()
    
def main () -> None:

    API: dict = {
        "URL": "https://v3.football.api-sports.io/",

        "ENDPOINTS": {
            "temporadas": "leagues?id=128", #8 INTENTOS
            "equipos": "teams?league=128&season=", #8 INTENTOS
            "fixtures": "fixtures?league=128&season=2023", #1 INTENTO
            "estadisticas": "teams/statistics?league=128&season=2023" + "&team=", #28 INTENTOS
            "predicciones": "predictions?fixture=", #DESCONOCIDOS
            "planteles": "players?league=128&season=2023" + "&team=", #28 INTENTOS
            "posiciones": "standings?league=128&season=" #8 INTENTOS
            },

        "HEADERS": {
            'x-rapidapi-host': "v3.football.api-sports.io",
            'x-rapidapi-key': "d6b40bb947b90f57f825bd5d2508b001"
            }
        }
    #informacion_api: list = diccionario_api(API)
    lista_transacciones = [] # Lista con los registros que hay que agregar al archivo transacciones
    usuarios_diccionario = {} # email(id):[usuario, contraseña, cantidad_apostada, fecha_última_apuesta, dinero_disponible]
    transacciones_diccionario = {} # email(id):[fecha, resultado, importe]
    email = ""
    usuarios_csv_to_diccionario(usuarios_diccionario)
    transacciones_csv_to_diccionario(transacciones_diccionario)

    print(f"Bienvenido")
    print_bienvenida()
    opt = opt_bienvenida()
    while opt != "3":
        if opt == "1":
            email = iniciar_sesion(usuarios_diccionario)
        elif opt == "2":
            registrarse(usuarios_diccionario)

        while email != "":
            print_menu()
            opcion = opt_menu()

            while opcion != "9":
                if opcion == "1":
                    listado_equipos() 
                elif opcion == "2":
                    tabla_posiciones()
                elif opcion == "3":
                    informacion_equipo()
                elif opcion == "4":
                    grafica_goles()
                elif opcion == "5":
                    cargar_dinero()
                elif opcion == "2":
                    tabla_posiciones()
                elif opcion == "6":
                    mayor_apostador()
                elif opcion == "7":
                    mayor_ganador()
                elif opcion == "8":
                    apuesta_main()

                print_menu()
                opcion = opt_menu()
            email = ""

        print_bienvenida()
        opt = opt_bienvenida()
        
main()