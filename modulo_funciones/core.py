import random
import os
import time

# Armado de mazo:
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

# Función para crear jugadores
def creandoJugadores():
    global jugadores
    jugadores = []
    for i in range(2):
        jugador = {'Nombre': f'Jugador {i+1}', 'cartas': []}
        jugadores.append(jugador)

tuTurno = True

# Función para repartir cartas alternadamente
def repartir_cartas_alternadamente(jugadores):
    if tuTurno:
        jugador_index = 0  # Comienza con el primer jugador
        cont = 0
        while cont < 6:
            jugadores[jugador_index]['cartas'].append(mazo[cont])
            if jugador_index == 0:
                jugador_index = 1
            else:
                jugador_index = 0
            cont += 1
    else:
        jugador_index = 1  # Comienza con el segundo jugador
        cont = 0
        while cont < 6:
            jugadores[jugador_index]['cartas'].append(mazo[cont])
            if jugador_index == 0:
                jugador_index = 1
            else:
                jugador_index = 0
            cont += 1

def config():
    print("Configuración de la partida.\n")
    time.sleep(1)
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

    return flor, pMax

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


def tusCartas2(cartas):
    cartas_formateadas = [f"{numero} de {palo}" for numero, palo, _ in cartas]
    ancho_carta = 14

    carta1 = cartas_formateadas[0].center(ancho_carta)
    carta2 = cartas_formateadas[1].center(ancho_carta)

    print("    ________________     ________________ ")
    print("   |Carta 1         |   |Carta 2         |")
    print("   |                |   |                |")
    print("   |                |   |                |")
    print(f"   | {carta1} |   | {carta2} |")
    print("   |                |   |                |")
    print("   |                |   |                |")
    print("   |                |   |                |")
    print("   |________________|   |________________|")
    print(" ")

    return jugadores[0]['cartas']

def tusCartas3(carta):
    cartas_formateadas = [f"{numero} de {palo}" for numero, palo, _ in carta]
    ancho_carta = 14

    carta1 = cartas_formateadas[0].center(ancho_carta)

    print("    ________________ ")
    print("   |Carta 1         |")
    print("   |                |")
    print("   |                |")
    print(f"   | {carta1} |")
    print("   |                |")
    print("   |                |")
    print("   |                |")
    print("   |________________|")
    print(" ")

def rondArt(ronda):
    if ronda == 1:
        print("                                                                                                               ")
        print("                                                                   dddddddd                                    ")
        print("RRRRRRRRRRRRRRRRR                                                  d::::::d                         1111111    ")
        print("R::::::::::::::::R                                                 d::::::d                        1::::::1    ")
        print("R::::::RRRRRR:::::R                                                d::::::d                       1:::::::1    ")
        print("RR:::::R     R:::::R                                               d:::::d                        111:::::1    ")
        print("  R::::R     R:::::R   ooooooooooo   nnnn  nnnnnnnn        ddddddddd:::::d   aaaaaaaaaaaaa           1::::1    ")
        print("  R::::R     R:::::R oo:::::::::::oo n:::nn::::::::nn    dd::::::::::::::d   a::::::::::::a          1::::1    ")
        print("  R::::RRRRRR:::::R o:::::::::::::::on::::::::::::::nn  d::::::::::::::::d   aaaaaaaaa:::::a         1::::1    ")
        print("  R:::::::::::::RR  o:::::ooooo:::::onn:::::::::::::::nd:::::::ddddd:::::d            a::::a         1::::l    ")
        print("  R::::RRRRRR:::::R o::::o     o::::o  n:::::nnnn:::::nd::::::d    d:::::d     aaaaaaa:::::a         1::::l    ")
        print("  R::::R     R:::::Ro::::o     o::::o  n::::n    n::::nd:::::d     d:::::d   aa::::::::::::a         1::::l    ")
        print("  R::::R     R:::::Ro::::o     o::::o  n::::n    n::::nd:::::d     d:::::d  a::::aaaa::::::a         1::::l    ")
        print("  R::::R     R:::::Ro::::o     o::::o  n::::n    n::::nd:::::d     d:::::d a::::a    a:::::a         1::::l    ")
        print("RR:::::R     R:::::Ro:::::ooooo:::::o  n::::n    n::::nd::::::ddddd::::::dda::::a    a:::::a      111::::::111 ")
        print("R::::::R     R:::::Ro:::::::::::::::o  n::::n    n::::n d:::::::::::::::::da:::::aaaa::::::a      1::::::::::1 ")
        print("R::::::R     R:::::R oo:::::::::::oo   n::::n    n::::n  d:::::::::ddd::::d a::::::::::aa:::a     1::::::::::1 ")
        print("RRRRRRRR     RRRRRRR   ooooooooooo     nnnnnn    nnnnnn   ddddddddd   ddddd  aaaaaaaaaa  aaaa     111111111111 ")
    elif ronda == 2:
        print("                                                                                                                       ")
        print("                                                                   dddddddd                                            ")
        print("RRRRRRRRRRRRRRRRR                                                  d::::::d                        222222222222222     ")
        print("R::::::::::::::::R                                                 d::::::d                       2:::::::::::::::22   ")
        print("R::::::RRRRRR:::::R                                                d::::::d                       2::::::222222:::::2  ")
        print("RR:::::R     R:::::R                                               d:::::d                        2222222     2:::::2  ")
        print("  R::::R     R:::::R   ooooooooooo   nnnn  nnnnnnnn        ddddddddd:::::d   aaaaaaaaaaaaa                    2:::::2  ")
        print("  R::::R     R:::::R oo:::::::::::oo n:::nn::::::::nn    dd::::::::::::::d   a::::::::::::a                   2:::::2  ")
        print("  R::::RRRRRR:::::R o:::::::::::::::on::::::::::::::nn  d::::::::::::::::d   aaaaaaaaa:::::a               2222::::2   ")
        print("  R:::::::::::::RR  o:::::ooooo:::::onn:::::::::::::::nd:::::::ddddd:::::d            a::::a          22222::::::22    ")
        print("  R::::RRRRRR:::::R o::::o     o::::o  n:::::nnnn:::::nd::::::d    d:::::d     aaaaaaa:::::a        22::::::::222      ")
        print("  R::::R     R:::::Ro::::o     o::::o  n::::n    n::::nd:::::d     d:::::d   aa::::::::::::a       2:::::22222         ")
        print("  R::::R     R:::::Ro::::o     o::::o  n::::n    n::::nd:::::d     d:::::d  a::::aaaa::::::a      2:::::2              ")
        print("  R::::R     R:::::Ro::::o     o::::o  n::::n    n::::nd:::::d     d:::::d a::::a    a:::::a      2:::::2              ")
        print("RR:::::R     R:::::Ro:::::ooooo:::::o  n::::n    n::::nd::::::ddddd::::::dda::::a    a:::::a      2:::::2       222222 ")
        print("R::::::R     R:::::Ro:::::::::::::::o  n::::n    n::::n d:::::::::::::::::da:::::aaaa::::::a      2::::::2222222:::::2 ")
        print("R::::::R     R:::::R oo:::::::::::oo   n::::n    n::::n  d:::::::::ddd::::d a::::::::::aa:::a     2::::::::::::::::::2 ")
        print("RRRRRRRR     RRRRRRR   ooooooooooo     nnnnnn    nnnnnn   ddddddddd   ddddd  aaaaaaaaaa  aaaa     22222222222222222222 ")
    else:
        print("                                                                                                                      ")
        print("                                                                   dddddddd                                           ")
        print("RRRRRRRRRRRRRRRRR                                                  d::::::d                        333333333333333    ")
        print("R::::::::::::::::R                                                 d::::::d                       3:::::::::::::::33  ")
        print("R::::::RRRRRR:::::R                                                d::::::d                       3::::::33333::::::3 ")
        print("RR:::::R     R:::::R                                               d:::::d                        3333333     3:::::3 ")
        print("  R::::R     R:::::R   ooooooooooo   nnnn  nnnnnnnn        ddddddddd:::::d   aaaaaaaaaaaaa                    3:::::3 ")
        print("  R::::R     R:::::R oo:::::::::::oo n:::nn::::::::nn    dd::::::::::::::d   a::::::::::::a                   3:::::3 ")
        print("  R::::RRRRRR:::::R o:::::::::::::::on::::::::::::::nn  d::::::::::::::::d   aaaaaaaaa:::::a          33333333:::::3  ")
        print("  R:::::::::::::RR  o:::::ooooo:::::onn:::::::::::::::nd:::::::ddddd:::::d            a::::a          3:::::::::::3   ")
        print("  R::::RRRRRR:::::R o::::o     o::::o  n:::::nnnn:::::nd::::::d    d:::::d     aaaaaaa:::::a          33333333:::::3  ")
        print("  R::::R     R:::::Ro::::o     o::::o  n::::n    n::::nd:::::d     d:::::d   aa::::::::::::a                  3:::::3 ")
        print("  R::::R     R:::::Ro::::o     o::::o  n::::n    n::::nd:::::d     d:::::d  a::::aaaa::::::a                  3:::::3 ")
        print("  R::::R     R:::::Ro::::o     o::::o  n::::n    n::::nd:::::d     d:::::d a::::a    a:::::a                  3:::::3 ")
        print("RR:::::R     R:::::Ro:::::ooooo:::::o  n::::n    n::::nd::::::ddddd::::::dda::::a    a:::::a      3333333     3:::::3 ")
        print("R::::::R     R:::::Ro:::::::::::::::o  n::::n    n::::n d:::::::::::::::::da:::::aaaa::::::a      3::::::33333::::::3 ")
        print("R::::::R     R:::::R oo:::::::::::oo   n::::n    n::::n  d:::::::::ddd::::d a::::::::::aa:::a     3:::::::::::::::33  ")
        print("RRRRRRRR     RRRRRRR   ooooooooooo     nnnnnn    nnnnnn   ddddddddd   ddddd  aaaaaaaaaa  aaaa      333333333333333    ")
def cartaMaquina():
    pass

def mano(flor):
    ronda = 1
    
    contNos = 0
    contEllos = 0

    contRondasNos = 0
    contRondasEllos = 0

    while ronda <= 3:
        rondArt(ronda)
        time.sleep(2)
        os.system("cls")

        if ronda == 1: # TERMINAR 
            '''tusCartas()
            envido = int(input("¿Querés cantar envido? (Si = 1 | No = 2) "))
            while envido != 1 and envido != 2:
                envido = int(input("Error. Intente devuelta. ¿Querés cantar envido? (Si = 1 | No = 2) "))
                if envido == 1:
                    envido(flor)
            os.system("cls")'''

            tusCartas()
            carta = int(input("¿Que carta querés jugar? (1, 2 o 3) "))
            while carta != 1 and carta != 2 and carta != 3:
                carta = int(input("Error. ¿Que carta querés jugar? (1, 2 o 3) "))
            carta -= 1
            # Posiblemente puede optimizarse
            cartaMaq = 2 #cartaMaquina()  

            if jugadores[0]['cartas'][carta][2] < cartaMaq:
                contRondasEllos += 1
                print("Ellos")
                time.sleep(2)
            elif jugadores[0]['cartas'][carta][2] > cartaMaq:
                contRondasNos += 1
                print("Nos")
                time.sleep(2)
            elif jugadores[0]['cartas'][carta][2] == cartaMaq:
                contRondasNos += 1
                contRondasEllos += 1

            os.system("cls")
            cartas = jugadores[0]['cartas']
            cartas.pop(carta)
            
        elif ronda == 2:
            tusCartas2(cartas)
            carta = int(input("¿Que carta querés jugar? (1 o 2) "))
            while carta != 1 and carta != 2:
                carta = int(input("Error. ¿Que carta querés jugar? (1 o 2) "))
            carta -= 1
            
            cartaMaq = 5 #cartaMaquina()

            if cartas[carta][2] < cartaMaq:
                contRondasEllos += 1
                print("Ellos")
                time.sleep(2)
            elif cartas[carta][2] > cartaMaq:
                contRondasNos += 1
                print("Nos")
                time.sleep(2)
            elif cartas[carta][2] == cartaMaq:
                contRondasNos += 1
                contRondasEllos += 1
            os.system("cls")
            if contRondasEllos == 2 and contRondasNos != 2:
                print("La máquina gana la mano!")
                contEllos += 1
                ronda = 4
            elif contRondasNos == 2 and contRondasEllos != 2:
                print("Vos ganás la mano!")
                contNos += 1
                ronda = 4
            else:
                cartas.pop(carta)
                tusCartas3(cartas)        

        elif ronda == 3:
            if cartas[0][2] < cartaMaq:
                print("La máquina gana la mano!")
                contEllos += 1
                ronda = 4
            elif cartas[0][2] > cartaMaq:
                print("Vos ganás la mano!")
                contNos += 1
                ronda = 4
            elif cartas[0][2] == cartaMaq:
                if tuTurno:
                    print("Vos ganás la mano!")
                    contNos += 1
                    ronda = 4
                elif tuTurno == False:
                    print("La máquina gana la mano!")
                    contEllos += 1
                    ronda = 4
                
        ronda += 1
    return contNos, contEllos

def juego(nos, ellos):
    mezclarMazo() # Mezclar el mazo
    repartir_cartas_alternadamente(jugadores)  # Repartir las cartas  
    flor, pmax = config()
    print(nos, ellos)
    time.sleep(2)
    os.system("cls")
    while nos <= pmax and ellos <= pmax:    
        nos_val, ellos_val = mano(flor)
        nos += nos_val
        ellos += ellos_val
        mezclarMazo() # Mezclar el mazo
        repartir_cartas_alternadamente(jugadores)  # Repartir las cartas  
        time.sleep(2)
        print(nos, ellos)
        time.sleep(2)
        os.system("cls")

def envido(flor):
    if flor == 1:
        if jugadores[0]['cartas'][0][1] == jugadores[0]['cartas'][1][1] and jugadores[0]['cartas'][0][1] == jugadores[0]['cartas'][2][1]:
            pass

    
def ejecutar():
    nos = 0
    ellos = 0
    creandoJugadores() # Crear los jugadores
    juego(nos, ellos)


def menu():
    repetir = True
    while repetir:
        os.system("cls") #limpia la pantalla
        print("   ■■■■■■■■■■■■■■■■■■■■■■■     ■■■■■■■■■■■■■■■■■■■■■■■■      ■■■■■■■■■■■■■■■■■■■■■■■     ■■■■■■■■■■■■■■■■■■■■■■■        ")
        print("   █      1. Equipo      █     █  2. Instrucciones    █      █     3. Ejecutar     █     █      4. Salir       █        ")
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
                
        except ValueError ():
              os.system("cls")                                                                                                   
              print("                                                                                                    ")
              print("EEEEEEEEEEEEEEEEEEEEEE                                                                              ")
              print("E::::::::::::::::::::E                                                                              ")
              print("E::::::::::::::::::::E                                                                              ")
              print("EE::::::EEEEEEEEE::::E                                                                              ")
              print("  E:::::E       EEEEEErrrrr   rrrrrrrrr   rrrrr   rrrrrrrrr      ooooooooooo   rrrrr   rrrrrrrrr    ")
              print("  E:::::E             r::::rrr:::::::::r  r::::rrr:::::::::r   oo:::::::::::oo r::::rrr:::::::::r   ")
              print("  E::::::EEEEEEEEEE   r:::::::::::::::::r r:::::::::::::::::r o:::::::::::::::or:::::::::::::::::r  ")
              print("  E:::::::::::::::E   rr::::::rrrrr::::::rrr::::::rrrrr::::::ro:::::ooooo:::::orr::::::rrrrr::::::r ")
              print("  E:::::::::::::::E    r:::::r     r:::::r r:::::r     r:::::ro::::o     o::::o r:::::r     r:::::r ")
              print("  E::::::EEEEEEEEEE    r:::::r     rrrrrrr r:::::r     rrrrrrro::::o     o::::o r:::::r     rrrrrrr ")
              print("  E:::::E              r:::::r             r:::::r            o::::o     o::::o r:::::r             ")
              print("  E:::::E       EEEEEE r:::::r             r:::::r            o::::o     o::::o r:::::r             ")
              print("EE::::::EEEEEEEE:::::E r:::::r             r:::::r            o:::::ooooo:::::o r:::::r             ")
              print("E::::::::::::::::::::E r:::::r             r:::::r            o:::::::::::::::o r:::::r             ")
              print("E::::::::::::::::::::E r:::::r             r:::::r             oo:::::::::::oo  r:::::r             ")
              print("EEEEEEEEEEEEEEEEEEEEEE rrrrrrr             rrrrrrr               ooooooooooo    rrrrrrr             ")                                                                              
              input()
           
menu() 
