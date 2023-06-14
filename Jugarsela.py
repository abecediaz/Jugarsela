def opt_menu() -> None:
    opt = str(input("Ingrese una opcion: "))
    while opt not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]: opt = str(input("Ingrese una opcion valida: "))
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
    opt = str(input("Ingrese una opcion: "))
    while opt not in ["1", "2", "3"]: opt = str(input("Ingrese una opcion valida: "))
    return opt

def print_bienvenida() -> None:
    print(f"-"*20)
    print(f"1. Iniciar Sesion")
    print(f"2. Registrarse")
    print(f"3. Salir")
    print(f"-"*20)

def main () -> None:
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
        while opt != "9":
            opcion = opt_menu()

        opt = opt_bienvenida()
main()