import random
import os
import time

#Armado de mazo:
cartas = [
    ('1', 'Espada', 14), ('1', 'Basto', 13), 
    ('7', 'Espada', 12), ('7', 'Oro', 11),
    ('3', 'Espada', 10), ('3', 'Basto', 10), ('3', 'Copa', 10), ('3', 'Oro', 10),
    ('2', 'Espada', 9), ('2', 'Basto', 9), ('2', 'Copa', 9), ('2', 'Oro', 9),
    ('1', 'Copa', 8), ('1', 'Oro', 8),
    ('12', 'Espada', 7), ('12', 'Basto', 7), ('12', 'Oro', 7), ('12', 'Copa', 7),
    ('11', 'Espada', 6), ('11', 'Basto', 6), ('11', 'Oro', 6), ('11', 'Copa', 6),
    ('10', 'Espada', 5), ('10', 'Basto', 5), ('10', 'Oro', 5), ('10', 'Copa', 5),
    ('7', 'Copa', 4), ('7', 'Basto', 4),
    ('6', 'Espada', 3), ('6', 'Basto', 3), ('6', 'Oro', 3), ('6', 'Copa', 3),
    ('5', 'Espada', 2), ('5', 'Basto', 2), ('5', 'Oro', 2), ('5', 'Copa', 2),
    ('4', 'Espada', 1), ('4', 'Basto', 1), ('4', 'Oro', 1), ('4', 'Copa', 1),
    ]

# Función para mezclar el mazo
def mezclarMazo():
    global mazo
    mazo = cartas.copy()
    random.shuffle(mazo)

# crear jugadores
jugadores = {
    'Jugador': {'Nombre': 'Jugador', 'cartas': [], 'puntos': 0},
    'Máquina': {'Nombre': 'Máquina', 'cartas': [], 'puntos': 0}
}




# Función para repartir cartas alternadamente
def repartir_cartas_alternadamente(jugadores):
    jugador_index = 0  # Comienza con el primer jugador
    cont = 0
    while cont < 6:
        jugadores[jugador_index]['cartas'].append(mazo[cont])
        if jugador_index == 0:
            jugador_index = 1
        else:
            jugador_index = 0
        cont += 1 
    
   

def config():
    print("CONFIGURACIÓN DE LA PARTIDA.\n")
    flor = int(input("¿Activar flor? (SI = 1 | NO = 2) "))
    while flor < 1 or flor > 2:
        flor = int(input("Respuesta no válida. Intente denuevo. ¿Activar flor? (SI = 1 | NO = 2) "))
    pMax = int(input("\nIndique la puntuación máxima. (15 | 30) "))
    while pMax != 15 and pMax != 30:
        pMax = int(input("Respuesta no válida. Intente denuevo. Indique la puntuación máxima. (15 | 30) "))
    
    os.system("cls")

    print("Mezclando el mazo y repartiendo", end="", flush=True)
    time.sleep(1)
    print(".", end="", flush=True)
    time.sleep(1)
    print(".", end="", flush=True)
    time.sleep(1)
    print(".", flush=True)
    time.sleep(1)

    tusCartas()

def tusCartas():
    cartas = jugadores[0]['cartas']
    cartas_formateadas = [f"{numero} de {palo}" for numero, palo, _ in cartas]
    ancho_carta = 14

    carta1 = cartas_formateadas[0].center(ancho_carta)
    carta2 = cartas_formateadas[1].center(ancho_carta)
    carta3 = cartas_formateadas[2].center(ancho_carta)
    
    print("    ________________     ________________     ________________ ")
    print("   |Carta 1         |   |Carta 2         |   |Carta 3         |")
    print("   |                |   |                |   |                |")
    print("   |                |   |                |   |                |")
    print(f"   | {carta1} |   | {carta2} |   | {carta3} |")
    print("   |                |   |                |   |                |")
    print("   |                |   |                |   |                |")
    print("   |                |   |                |   |                |")
    print("   |________________|   |________________|   |________________|")
    print(" ")

    
def ejecutar():
    creandoJugadores() # Crear los jugadores
    mezclarMazo() # Mezclar el mazo
    repartir_cartas_alternadamente(jugadores)  # Repartir las cartas  
    config()


def menu():
    repetir = True
    while repetir:
        os.system("cls") #limpia la pantalla
        print("   ■■■■■■■■■■■■■■■■■■■■■■■     ■■■■■■■■■■■■■■■■■■■■■■■■      ■■■■■■■■■■■■■■■■■■■■■■■     ■■■■■■■■■■■■■■■■■■■■■■■        ")
        print("   █      1. Equipo      █     █  2. introducciones   █      █     3. Ejecutar     █     █      4. Salir       █        ")
        print("   ■■■■■■■■■■■■■■■■■■■■■■■     ■■■■■■■■■■■■■■■■■■■■■■■■      ■■■■■■■■■■■■■■■■■■■■■■■     ■■■■■■■■■■■■■■■■■■■■■■■        ")
        print("")
        try:
            op = int(input("Ingrese una opción: "))
            print()
            if op == 1:
                os.system("cls")
                print("Programa desarollado por: ")
                print(" ")
                print("   _____________        ")
                print("  |Carta 1      |       ")
                print("  |             |       ")
                print("  |             |       ")
                print("  |   Juliana   |       ")
                print("  |   Galiano   |       ")
                print("  |             |       ")
                print("  |             |       ")
                print("  |_____________|       ")
                time.sleep(1)
                os.system("cls")
                print("Programa desarollado por: ")
                print(" ")
                print("   _____________      _____________         ")
                print("  |Carta 1      |    |Carta 2      |        ")
                print("  |             |    |             |        ")
                print("  |             |    |             |        ")
                print("  |   Juliana   |    |  Agustín    |        ")
                print("  |   Galiano   |    |  Fernandéz  |        ")
                print("  |             |    |  Durán      |        ")
                print("  |             |    |             |        ")
                print("  |_____________|    |_____________|        ")
                time.sleep(1)
                os.system("cls")
                print("Programa desarollado por: ")
                print(" ")
                print("   _____________      _____________      _____________    ")
                print("  |Carta 1      |    |Carta 2      |    |Carta 3      |   ")
                print("  |             |    |             |    |             |   ")
                print("  |             |    |             |    |             |   ")
                print("  |   Juliana   |    |  Agustín    |    | Christopher |   ")
                print("  |   Galiano   |    |  Fernandéz  |    | Hess        |   ")
                print("  |             |    |  Durán      |    |             |   ")
                print("  |             |    |             |    |             |   ")
                print("  |_____________|    |_____________|    |_____________|   ")
                time.sleep(1)
                os.system("cls")
                print("Programa desarollado por: ")
                print(" ")
                print("   _____________      _____________      _____________      _____________     ")
                print("  |Carta 1      |    |Carta 2      |    |Carta 3      |    |Carta 4      |    ")
                print("  |             |    |             |    |             |    |             |    ")
                print("  |             |    |             |    |             |    |             |    ")
                print("  |   Juliana   |    |  Agustín    |    | Christopher |    |  Valentino  |    ")
                print("  |   Galiano   |    |  Fernandéz  |    | Hess        |    |  Ferretti   |    ")
                print("  |             |    |  Durán      |    |             |    |             |    ")
                print("  |             |    |             |    |             |    |             |    ")
                print("  |_____________|    |_____________|    |_____________|    |_____________|    ")
                print(" ")
                tecla = input("\nPresione 'ENTER' para volver al menú...")
            elif op == 2:
                os.system("cls")
                print("        ")
                print("                                                                                                                                                                                            ")
                print("       • El Truco se juega con una baraja española de 40 cartas (sin ningún 8, 9 o 10).                                                                                                     ")
                print("       • Participan 2, 4 o 6 jugadores, organizados en 2 equipos donde cada jugador recibe 3 cartas y el objetivo es alcanzar 15 o 30 puntos, según la modalidad                            ")
                print("       • El juego se desarrolla por manos donde se lleva puntos quien gane 2 de 3 enfrentamientos.                                                                                          ")
                print("""       • Los jugadores pueden cantar "truco"  para desafiar al adversario, aumentando la apuesta de puntos;                                                                               """)
                print("""         el rival puede aceptar, rechazar, o subir la apuesta con "re-truco" o "vale cuatro"                                                                                              """)
                print("""       • También se puede "Cantar Envido" antes de usar la primer carta, apostando por el mejor par de cartas del mismo palo.                                                             """)
                print("""       • Además, si un jugador tiene las tres cartas del mismo palo, puede "Cantar Flor" para ganar puntos extras (aunque se debe aclarar si está permitida al comienzo de la partida)    """)
                print("       • Por último, los puntos se otorgan según el resultado de las manos y las apuestas realizadas.                                                                                        ")
                print("")
    
                tecla = input("\nPresione 'ENTER' para volver al menú...")
            elif op == 3:
                os.system("cls")
                ejecutar()
                tecla = input("\nPresione 'ENTER' para volver al menú...")
            elif op == 4:
                os.system("cls")
                repetir = False
                print("Gracias por jugar.")
            else: 
                os.system("cls")
                input("Parece que ingresaste una opción no válida. ¡Presiona 'ENTER' y volvé a intentarlo!")
        except:
              os.system("cls")
              print(" ")
              print("       _____                                     ")
              print("      | ____|                                    ")
              print("      | |___  _ __ _ __ ___  _ __                ")
              print("      |  ___|| '__|'__ / _ \| '__|               ")
              print("      | |___ | | | |  | |_| | |                  ")
              print("      |_____||_| |_|   \___/|_|                  ")
              input()
           
menu()