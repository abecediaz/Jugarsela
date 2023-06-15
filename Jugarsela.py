import csv 
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
    print(f"Bienvenido a la interfaz, seleccione lo que desea hacer")
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

def registrarse() -> None:
    print(f"-"*20)
    print(f"Proporcione sus datos para crear una nueva cuenta")
    email = str(input("Email: ")) 
    usuario = str(input("Nombre de Usuario: "))
    contraseña = str(input("Contraseña: "))

def iniciar_sesion() -> None:
    #validacion dentro con el csv!!!
    print(f"-"*20)
    print(f"Inicio de Sesion")
    email = str(input("Email: ")) 
    contraseña = str(input("Contraseña: "))

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

def transacciones_csv_to_diccionario(transacciones_diccionario: dict) -> None:
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

def main () -> None:
    usuarios_diccionario = {} # email(id):[usuario, contraseña, cantidad_apostada, fecha_última_apuesta, dinero_disponible]
    transacciones_diccionario = {} # email(id):[fecha, resultado, importe]

    usuarios_csv_to_diccionario(usuarios_diccionario)
    transacciones_csv_to_diccionario(transacciones_diccionario)

    print(f"Bienvenido")
    print_bienvenida()
    opt = opt_bienvenida()
    while opt != "3":
        if opt == "1":
            iniciar_sesion()
        elif opt == "2":
            registrarse()

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

        print_bienvenida()
        opt = opt_bienvenida()
main()