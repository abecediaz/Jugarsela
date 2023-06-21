################################### INFORMACION_API ###################################

información_api: list = ["temporadas", "equipos", "fixtures"]
#			                 [0]	      [1]        [2]

##################################### TEMPORADAS #####################################

temporadas: dict = {
    
    "2015-2019": {"1er Año": [(1er Equipo, Puntos), (2er Equipo, Puntos), (3er Equipo, Puntos) ...],
                  "2do Año": [(1er Equipo, Puntos), (2er Equipo, Puntos), (3er Equipo, Puntos) ...],
                  "3er Año": [(1er Equipo, Puntos), (2er Equipo, Puntos), (3er Equipo, Puntos) ...],
                  }#             [0] = Rank 1           [1] = Rank 2          [2] = Rank 3     ...

    "2020": {"Nombre del Grupo 1": [(1er Equipo, Puntos), (2er Equipo, Puntos), (3er Equipo, Puntos) ...],
             "Nombre del Grupo 2": [(1er Equipo, Puntos), (2er Equipo, Puntos), (3er Equipo, Puntos) ...],
             "Nombre del Grupo 3": [(1er Equipo, Puntos), (2er Equipo, Puntos), (3er Equipo, Puntos) ...], 
             }#                         [0] = Rank 1          [1] = Rank 2          [2] = Rank 3     ...

    "2021-2023": {"Primera Fase": [(1er Equipo, Puntos), (2er Equipo, Puntos), (3er Equipo, Puntos) ...],
                  "Segunda Fase": [(1er Equipo, Puntos), (2er Equipo, Puntos), (3er Equipo, Puntos) ...],
                  }#                  [0] = Rank 1           [1] = Rank 2          [2] = Rank 3     ...

                  }

El diccionario "temporadas" almacena como las claves los años en los que se efectuaron
los partidos. El valor para cada año es distinto según el año:

    - Para las temporadas entre 2015 y 2019: El valor para cada año será una lista de tuplas, con las
      posiciones finales de cada equipo y su puntaje final; empezando con el primer lugar, y terminando
      con el último. Para imprimir los datos:

                    for temporada in temporadas:
                        if (int(temporada) < 2020):
                                print(temporadas[temporada][i][0]) #EQUIPOS
                                print(temporadas[temporada][i][0]) #PUNTOS


    - Para la temporada 2020: El valor será otro diccionario, cuyas claves contendrán el nombre del grupo
      y el valor para cada grupo es una lista de tuplas, con las posiciones finales de cada equipo y su
      puntaje final; empezando con el primer lugar, y terminando con el último. TENER EN CUENTA QUE CADA
      GRUPO TIENE SU RANKING INDIVIDUAL. Para imprimir los datos:

                    for temporada in temporadas:
                        if (int(temporada) == 2020):
                            for grupo in temporadas[temporada]:
                                print(temporadas[temporada][grupo][i][0]) #EQUIPOS
                                print(temporadas[temporada][grupo][i][0]) #PUNTOS


    - Para las temporadas entre 2021 y 2023: El valor será otro diccionario con dos claves: "Primera Fase"
      y "Segunda Fase".Cada una tiene su propio ranking, por eso la distinción. Los valores para cada fase,
      serán una lista de tuplas con las posiciones finales de cada equipo y su puntaje final; empezando con el
      primer lugar, y terminando con el último. Para imprimir los datos:

                    for temporada in temporadas:
                        if (int(temporada) > 2020):

                            for i in range (len(temporadas[temporada]["Primera Fase"])):
                                print(temporadas[temporada]["Primera Fase"][i][0]) #EQUIPOS
                                print(temporadas[temporada]["Primera Fase"][i][0]) #PUNTOS

                            for i in range (len(temporadas[temporada]["Segunda Fase"])):
                                print(temporadas[temporada]["Segunda Fase"][i][0]) #EQUIPOS
                                print(temporadas[temporada]["Segunda Fase"][i][0]) #PUNTOS

###################################### EQUIPOS ######################################

equipos: dict = {

    "Nombre Equipo 1": {"id": número de id (str),
                        "escudo": logo del escudo (str),
                        "estadio": nombre del estadio (str),
                        "direccion": dirección del estadio (str),
                        "ciudad": dónde está el estadio (str),
                        "capacidad": capacidad de espectadores (str),
                        "superficie": tipo de suelo del estadio (str),
                        "foto": foto del estadio (str),
                        "plantel": [jugador1, jugador2, jugador3, ..., jugadorN]
                        "estadisticas": {"intervalo de tiempo 1": cantidad de goles
                                         "intervalo de tiempo 2": cantidad de goles
                                         "intervalo de tiempo 3": cantidad de goles
                                         ...
                                        }
                        }

    "Nombre Equipo 2": {"id": número de id (str),
                        "escudo": logo del escudo (str),
                        "estadio": nombre del estadio (str),
                        "direccion": dirección del estadio (str),
                        "ciudad": dónde está el estadio (str),
                        "capacidad": capacidad de espectadores (str),
                        "superficie": tipo de suelo del estadio (str),
                        "foto": foto del estadio (str),
                        "plantel": [jugador1, jugador2, jugador3, ..., jugadorN] (list),
                        "estadisticas": {"intervalo de tiempo 1": cantidad de goles
                                         "intervalo de tiempo 2": cantidad de goles
                                         "intervalo de tiempo 3": cantidad de goles
                                         ...
                                        }
                        }

    ...
}

El diccionario "equipos" almacena como claves los nombres de todos los equipos que alguna
vez participaron en la liga (desde el primer año, hasta el último. Obviamente no se repiten).
El valor para cada equipo es otro diccionario; consultar arriba en detalle. Para poder acceder
a un valor, simplemente se itera el diccionario de la siguiente forma:

                    equipos["nombre del equipo"]["dato al que se quiera acceder"]

Y para imprimir el plantel:

                    for i in range (len(equipos["nombre del equipo"]["plantel"])):
                        print(equipos["nombre del equipo"]["plantel"][i])

Lo cual devolvería lo siguiente:

                            Nombre completo del jugador 1 (Posición)
                            Nombre completo del jugador 2 (Posición)
                            Nombre completo del jugador 3 (Posición)
                            ...
                            Nombre completo del jugador N (Posición)

NOTA: Si alguno de los jugadores listados es el capitán, aparecerá de la siguiente forma:

                            Nombre completo del jugador (Posición), CAPITÁN

Para emplear las estadísticas con matplotlib:

                            minutos: list = []
                            goles: list = []

                            for tiempo in estadisticas:
                                minutos.append(tiempo)
                                goles.append(estadisticas[tiempo])

                            plt.xlabel('MINUTOS')
                            plt.ylabel('GOLES')
                            plt.title('GOLES REALIZADOS POR INTERVALO DE TIEMPO')

                            plt.bar(minutos, goles)
                            plt.show()

IMPORTANTE: Si el equipo NO PARTICIPA en la temporada 2023, el mismo VA A TENER VALOR "NONE" EN
LA CLAVE "PLANTEL" Y EN "ESTADISTICAS", puesto que únicamente se debe mostrar el plantel/las estadísticas
de los equipos que juegan la temporada 2023.

####################################### FIXTURES #######################################

fixtures: dict = {

    "id 1": {"fecha": fecha en la que se juega el partido (tupla: (año, mes, dia)),
             "local": nombre del equipo que juega de local (str),
             "visitante": nombre del equipo que juega de visitante (str)
            }

    "id 2": {"fecha": fecha en la que se juega el partido (tupla: (año, mes, dia)),
             "local": nombre del equipo que juega de local (str),
             "visitante": nombre del equipo que juega de visitante (str)
            }

    "id 3": {"fecha": fecha en la que se juega el partido (tupla: (año, mes, dia)),
             "local": nombre del equipo que juega de local (str),
             "visitante": nombre del equipo que juega de visitante (str)
            }

    ...
}

El diccionario "fixtures" almacena como claves los id de todos los partidos que AÚN NO
SE JUGARON (o sea, desde la fecha en la que se corre el programa en adelante). El valor
para cada fixture es otro diccionario; consultar arriba en detalle. Para poder acceder
a un valor, simplemente se itera con un ciclo for y un if para las condiciones:

EJEMPLO: Si quiero extraer las fechas en las que juega Racing ya sea de local o de visitante...

        for fixture in fixtures:
            if ((fixtures[fixture]["local"] == "Racing") or (fixtures[fixture]["visitante"] == "Racing"))
            fecha_partido_racing: str = fixtures[fixture]["fecha"]