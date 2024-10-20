import random
import os
import time
import hashlib
import re
import getpass

########
# Mazo #
########

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

###################
# Mezclar el mazo #
###################

def mezclarMazo():
    global mazo
    mazo = cartas.copy()
    random.shuffle(mazo)

def comentariosJugadores(num):
    # num == 1 --> ronda ganada por el npc
    # num == 2 --> ronda perdida por el npc
    # num == 3 --> partida ganada por el npc
    # num == 4 --> partida perdida por el npc

    # Comentarios personalizados para cada NPC
    comentarios_por_npc = {
        "Enrique": {
            'a': ["Otra ronda ganada, ¡ya es cuestión de tiempo para llevarme la partida!", "Así se juega, aprendé un poco observándome."],
            'b': ["Perder es algo raro para mí, ¡debe haber sido pura suerte de tu parte!", "Tranquilo, no siempre se puede estar a mi nivel. ¡Ya verás la próxima!"],
            'c': ["¡Sabía que iba a ganar desde el principio! Lo mío no es suerte, es pura habilidad.", "Esto es lo que pasa cuando te enfrentas al mejor, ¡aprendé de mí!"],
            'd': ["¿Perdí? Debe haber sido pura suerte, ¡no puede ser por tu habilidad!", "Bueno, hasta los mejores tienen un mal día... no te acostumbres."]
        },
        "Dolores": {
            'a': ["¡Bien jugado! Esta ronda fue mía, pero aún queda mucho por delante.", "¡Qué linda ronda! Espero que sigamos así de parejos."],
            'b': ["¡Qué bien jugado, me ganaste esta vez! Vamos a ver qué pasa en la próxima ronda.", "Fue una buena mano, ¡me alegro por ti! Espero que sigamos con buen ánimo."],
            'c': ["¡Ganamos! Fue una partida muy divertida, gracias por jugar conmigo.", "Qué buena partida, ¡me alegra haber ganado! Pero lo importante es que lo disfrutamos."],
            'd': ["¡Qué bien jugado! Perdí la partida, pero la pasé genial jugando contigo.", "Hoy no fue mi día, pero me divertí mucho. ¡Felicitaciones!"]
        },
        "Ricardo": {
            'a': ["¡Esta ronda es mía! Ya voy tomando ritmo, te va a costar recuperarte.", "Una más en el bolsillo, ¡te dije que no me subestimes!"],
            'b': ["Esto no ha terminado, prepárate porque te voy a aplastar en la próxima.", "Perdí esta, pero ya verás cómo me recupero... ¡no me gusta perder!"],
            'c': ["¡Victoria! Te lo dije, no me gusta perder. ¡Te voy a ganar cada vez que juguemos!", "Gané, como lo esperaba. La próxima va a ser igual de intensa, ¡preparate!"],
            'd': ["Perder... esto no me sienta bien. ¡La próxima te vas a acordar de mí!", "Ok, ganaste esta vez, pero no creas que volverá a pasar. ¡Voy a mejorar para la revancha!"]
        },
        "Rosario": {
            'a': ["Ronda ganada como lo planeé... solo tengo que seguir enfocada.", "Una victoria en la ronda, pero todavía no me confío. Lo importante es la estrategia a largo plazo."],
            'b': ["Bueno, esa no la vi venir... tendré que ajustar mi estrategia para la próxima.", "Mmm, cometí un error, pero ya tengo un plan para la siguiente ronda."],
            'c': ["¡Partida ganada! Todo salió según mi plan, cada jugada fue clave.", "Sabía que la estrategia iba a dar frutos... esta victoria fue bien pensada."],
            'd': ["Perdí la partida... claramente tengo que ajustar mi estrategia.", "Fue una partida interesante, pero cometí algunos errores. ¡La próxima será diferente!"]
        },
        "Antonio": {
            'a': ["¡Mirá qué bien, gané la ronda! A ver qué viene ahora, esto se pone divertido.", "Otra ronda para mí, ¡pero tranqui, que lo importante es pasarla bien!"],
            'b': ["¡Ah, me ganaste! Bueno, da igual, lo importante es divertirse, ¿no?", "Perdí, pero no importa, ¡esto recién comienza!"],
            'c': ["¡Mirá, gané la partida! Fue divertido, eso es lo que cuenta, ¿no?", "¡Qué bien, gané! Aunque más que la victoria, me llevo un buen rato compartido."],
            'd': ["¡Ah, perdí! Bueno, no pasa nada, lo importante es que estuvo divertido.", "Perdí la partida, ¡pero qué bien la pasamos! Al final, eso es lo que importa."]
        },
        "Julieta": {
            'a': ["¡Te lo dije, esta ronda era mía! Ahora vamos a por la siguiente.", "¡Ganada! Vamos con todo para seguir sumando puntos."],
            'b': ["¡No puedo creer que perdí! ¡Esta mano era buenísima!", "Malas decisiones... ¡pero la próxima no te salvas, voy con todo!"],
            'c': ["¡Sí, gané la partida! ¡Sabía que iba a salir todo bien, lo sentí desde el principio!", "¡Esta partida es mía! Ahora vamos por la próxima, ¡no me quiero detener!"],
            'd': ["¡No puede ser que perdí! Esta partida estaba en mis manos.", "¡Qué bronca! Esta partida era mía, pero ya verás en la próxima."]
        },
        "Ernesto": {
            'a': ["Gané la ronda... interesante. Ahora a ver cómo sigue.", "Una ronda menos... me enfocaré en la siguiente."],
            'b': ["Perdí... esto no me gusta, pero no siempre se puede ganar.", "Bien jugado, veremos cómo sigue esto."],
            'c': ["Gané la partida... fue interesante, aunque prefiero mantener la calma.", "Una victoria bien trabajada. Ahora, a seguir mejorando para la próxima."],
            'd': ["Perdí... no fue mi mejor partida, pero bueno, a veces se gana y a veces se pierde.", "La partida no salió como esperaba... habrá una próxima vez."]
        },
        "Eugenia": {
            'a': ["Era obvio que iba a ganar esta ronda, todo salió según el plan.", "Gané, pero aún no es suficiente. No me detengo hasta la partida final."],
            'b': ["Esto no debería haber pasado, cometí un error. ¡Voy a hacerlo mejor!", "No puede ser... no juego para perder. ¡Voy a ajustar mi estrategia!"],
            'c': ["Gané, pero no me sorprende, todo salió exactamente como lo planeé.", "Una victoria bien merecida, pero aún así, siempre se puede mejorar. ¡A seguir adelante!"],
            'd': ["No debería haber perdido. Claramente cometí errores que no puedo permitirme.", "Perdí la partida... pero voy a analizar cada jugada y asegurarme de que no vuelva a pasar."]
        },
        "Alberto": {
            'a': ["¡Uy, gané otra ronda! ¡Qué sorpresa tan inesperada!", "Una ronda más, ¡qué emocionante! Supongo que no lo viste venir..."],
            'b': ["¡Oh, qué sorpresa! Perder una mano... nunca me había pasado, claro.", "Bueno, sí, claro, perdí... ¡porque obviamente las cartas estaban de tu lado!"],
            'c': ["¡Uy, gané! ¡Qué sorpresa tan inesperada! Pero claro, era solo cuestión de tiempo.", "Gané, ¡pero no sé si sentirme bien o mal por vos!"],
            'd': ["Ah, claro, perdí. ¡Todo parte de mi plan maestro de hacerte confiar!", "Perdí, sí, porque obviamente las cartas estaban en tu favor... ¡pero no me molesta para nada, no!"]
        },
        "Beatriz": {
            'a': ["¡Qué bueno, esta ronda es mía! Pero aún puede pasar de todo.", "¡Otra ronda para mí! La suerte me está sonriendo hoy."],
            'b': ["Perdí, pero está bien, ¡la suerte me acompañará la próxima!", "No fue mi mejor ronda, pero estoy segura de que la siguiente será mejor."],
            'c': ["¡Qué emoción, gané la partida! ¡Fue muy divertida, espero que la próxima sea igual!", "Hoy fue mi día, ¡pero lo mejor es que la pasamos genial! Vamos por otra."],
            'd': ["¡Perdí la partida! Pero bueno, ¡la próxima será diferente! Me quedo con lo bueno.", "Hoy no fue mi día, pero no me rindo. ¡La próxima será mía!"]
        },
    }

    for jugador in jugadores:
        if jugador['Nombre'] != jugadores[0]['Nombre']:
            npc_name = jugador['Nombre']

            if num == 1:
                comentario = random.choice(comentarios_por_npc[npc_name]['a'])
            elif num == 2:
                comentario = random.choice(comentarios_por_npc[npc_name]['b'])
            elif num == 3:
                comentario = random.choice(comentarios_por_npc[npc_name]['c'])
            elif num == 4:
                comentario = random.choice(comentarios_por_npc[npc_name]['d'])

            print(f"{npc_name} dice: {comentario}")
            time.sleep(2)
def mentiras():
    for jugador in jugadores:
        if jugador['Nombre'] == 'Enrique':
            jugador['valorMentira'] = 1
        elif jugador['Nombre'] == 'Dolores':
            jugador['valorMentira'] = 2
        elif jugador['Nombre'] == 'Ricardo':
            jugador['valorMentira'] = 3
        elif jugador['Nombre'] == 'Rosario':
            jugador['valorMentira'] = 4
        elif jugador['Nombre'] == 'Antonio':
            jugador['valorMentira'] = 5
        elif jugador['Nombre'] == 'Julieta':
            jugador['valorMentira'] = 6
        elif jugador['Nombre'] == 'Ernesto':
            jugador['valorMentira'] = 7
        elif jugador['Nombre'] == 'Eugenia':
            jugador['valorMentira'] = 8
        elif jugador['Nombre'] == 'Alberto':
            jugador['valorMentira'] = 9
        elif jugador['Nombre'] == 'Beatriz':
            jugador['valorMentira'] = 10
    numeroRandom = random.randint(1, 10)
    if numeroRandom <= jugador['valorMentira']:
      return True
    else:
        return False


##########
# LOG-IN #
##########

# Estado loggin:

LogginState = False

# Función para encriptar la contraseña
def encriptar_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()

# Función para validar el nombre de usuario
def es_valido(cadena):
    # La expresión regular permite a-z, A-Z, 0-9, _, -, y .
    return bool(re.match("^[a-zA-Z0-9_.-]+$", cadena))

# Función para registrar un nuevo usuario
def registrar_usuario():
    usuario = input("Ingrese su nombre de usuario: ")
    
    # Validar el nombre de usuario
    while not es_valido(usuario) or verificar_usuario_existe(usuario) or len(usuario) > 10:
        usuario = input("El nombre de usuario no está disponible. Intente nuevamente: ")
    
    contraseña = getpass.getpass("\nIngrese su contraseña (no se muestra en pantalla): ")
    contraseña_encriptada = encriptar_contraseña(contraseña)

    if True:
        with open("usuarios.txt", "a") as archivo:
            archivo.write(f"{usuario},{contraseña_encriptada}\n")
        print("\nUsuario registrado con éxito.")
    time.sleep(3)
    return usuario 

# Función para verificar si un usuario ya existe
def verificar_usuario_existe(usuario):
    if not os.path.exists("usuarios.txt"):
        return False
    
    with open("usuarios.txt", "r") as archivo:
        for linea in archivo:
            usuario_guardado, _ = linea.strip().split(',')
            if usuario_guardado == usuario:
                return True
    return False

# Función para iniciar sesión
def iniciar_sesion():
    global LogginState
    correcto = False
    while correcto == False:
        usuario = input("Ingrese su nombre de usuario: ")
        
        # Validar el nombre de usuario
        while not es_valido(usuario):
            usuario = input("El nombre de usuario contiene caractéres inválidos. Intente nuevamente: ")
        
        contraseña = getpass.getpass("\nIngrese su contraseña (no se muestra en pantalla): ")
        contraseña_encriptada = encriptar_contraseña(contraseña)
        
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                usuario_guardado, contraseña_guardada = linea.strip().split(',')
                if usuario == usuario_guardado and contraseña_encriptada == contraseña_guardada:
                    LogginState = True
                    os.system("cls")
                    print("Inicio de sesión exitoso.")
                    time.sleep(2)
                    correcto = True
            if correcto == False:
                print("\nUsuario o contraseña incorrectos. Intentelo nuevamente.")
                time.sleep(2)
                os.system("cls")
    os.system("cls")
    return usuario

# Funcion para Salir de la cuenta si el usuario toca Desloggearse
def salir_cuenta():
    global LogginState
    print("¿Desea salir de la cuenta?")
    respuesta = input("Ingrese 'salir' para cambiar de cuenta: ")
    if respuesta.lower() == 'salir':
        os.system("cls")
        LogginState = False
        print("Deslogueado con éxito.")
        time.sleep(3)
        menuLogin()
    else:
        print("Continúa logueado.")

# Función principal del programa
def menuLogin():
    global usuario
    usuario = None   
    os.system("cls")
    print("   ■■■■■■■■■■■■■■■■■■■■■■■     ■■■■■■■■■■■■■■■■■■■■■■■")
    print("   █  1. Iniciar sesión  █     █   2. Registrarse    █")
    print("   ■■■■■■■■■■■■■■■■■■■■■■■     ■■■■■■■■■■■■■■■■■■■■■■■")
    op = input("\nIngrese una opción: ")

    if op == "1":
        os.system("cls")
        usuario = iniciar_sesion()
    elif op == "2":
        os.system("cls")
        usuario = registrar_usuario()
    else:
        os.system("cls")                                                                                                   
        print("                                                                                                               ")
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
        time.sleep(2)                                                                              
        input("\nPresione 'ENTER' para volver al menú...")
        os.system("cls")
        menuLogin()


###################
# Crear jugadores #
###################

def creandoJugadores():
    global jugadores
    jugadores = []
    num = random.randint(0, 9)
    nombres = ["Enrique", "Dolores", "Ricardo", "Rosario", "Antonio", "Julieta", "Ernesto", "Eugenia", "Alberto", "Beatriz"]
    npc = nombres[num]
    jugador = {'Nombre': f'{usuario}', 'cartas': []}
    jugadores.append(jugador)
    jugador = {'Nombre': f'{npc}', 'cartas': [], 'valorMentira': 0}
    jugadores.append(jugador)
    print(f"Tu rival es {npc}!\n")
    time.sleep(2)

##################################
# Repartir cartas alternadamente #
##################################

def repartir_cartas_alternadamente(jugadores):
    for i in range(2):
        jugadores[i]['cartas'].clear()
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
    elif tuTurno == False:
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
    flor = int(input("¿Activar flor? (Si = 1 | No = 2) "))
    while flor < 1 or flor > 2:
        flor = int(input("Respuesta no válida. Intente denuevo. ¿Activar flor? (SI = 1 | NO = 2) "))
    pMax = int(input("\nIndique la puntuación máxima. (15 | 30) "))
    while pMax != 15 and pMax != 30:
        pMax = int(input("Respuesta no válida. Intente denuevo. Indique la puntuación máxima. (15 | 30) "))

    os.system("cls")

    return flor, pMax

##############################################
# Funciones que muestran tus cartas (visual) #
##############################################

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

############################    
# Número de ronda (visual) #
############################

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

############################
# Estrategia de la máquina #
############################

def estrategiaNPC(ronda, tuCarta, ganadorPR):
    if ronda == 1:
        if tuTurno:
            lista = jugadores[1]['cartas'][:]
            for i in range (len(jugadores[1]['cartas']) - 1, -1, -1):
                if jugadores[1]['cartas'][i][2] <= tuCarta[2]:
                    lista.pop(i)
            if len(lista) > 1:
                cBaja = 15
                carta = 0 
                for i in range(len(lista)):
                    if lista[i][2] < cBaja:
                        cBaja = lista[i][2]
                        carta = i
                eleccion = lista[carta]
                jugadores[1]['cartas'].remove(eleccion)
                return eleccion
            elif len(lista) == 1:
                eleccion = lista[0]
                jugadores[1]['cartas'].remove(eleccion)
                return eleccion
            elif len(lista) == 0:
                cBaja = 15
                carta = 0 
                for i in range(len(jugadores[1]['cartas'])):
                    if jugadores[1]['cartas'][i][2] < cBaja:
                        cBaja = jugadores[1]['cartas'][i][2]
                        carta = i
                eleccion = jugadores[1]['cartas'][carta]
                jugadores[1]['cartas'].remove(eleccion)
                return eleccion
        elif tuTurno == False:
            for i in range(len(jugadores[1]['cartas'])):
                if jugadores[1]['cartas'][i][2] == 10 or jugadores[1]['cartas'][i][2] == 11:
                    eleccion = jugadores[1]['cartas'][i]
                    jugadores[1]['cartas'].remove(eleccion)
                    return eleccion
            cBaja = 15
            carta = 0 
            for i in range(len(jugadores[1]['cartas'])):
                if jugadores[1]['cartas'][i][2] < cBaja:
                    cBaja = jugadores[1]['cartas'][i][2]
                    carta = i
            eleccion = jugadores[1]['cartas'][carta]
            jugadores[1]['cartas'].remove(eleccion)
            return eleccion
    elif ronda == 2:
        if ganadorPR == 0:
            cAlta = 0
            carta = 0 
            for i in range(len(jugadores[1]['cartas'])):
                if jugadores[1]['cartas'][i][2] > cAlta:
                    cAlta = jugadores[1]['cartas'][i][2]
                    carta = i
            eleccion = jugadores[1]['cartas'][carta]
            jugadores[1]['cartas'].remove(eleccion)
            return eleccion
        elif ganadorPR == 2:
            for i in range(len(jugadores[1]['cartas'])):
                if jugadores[1]['cartas'][i][2] == 8:
                    eleccion = jugadores[1]['cartas'][i]
                    jugadores[1]['cartas'].remove(eleccion)
                    return eleccion
            for i in range(len(jugadores[1]['cartas'])):
                if jugadores[1]['cartas'][i][2] == 7:
                    eleccion = jugadores[1]['cartas'][i]
                    jugadores[1]['cartas'].remove(eleccion)
                    return eleccion
            for i in range(len(jugadores[1]['cartas'])):
                if jugadores[1]['cartas'][i][2] == 6 or jugadores[1]['cartas'][i][2] == 5:
                    eleccion = jugadores[1]['cartas'][i]
                    jugadores[1]['cartas'].remove(eleccion)
                    return eleccion
            for i in range(len(jugadores[1]['cartas'])):
                if jugadores[1]['cartas'][i][2] < 5:
                    eleccion = jugadores[1]['cartas'][i]
                    jugadores[1]['cartas'].remove(eleccion)
                    return eleccion
            cBaja = 15
            carta = 0 
            for i in range(len(jugadores[1]['cartas'])):
                if jugadores[1]['cartas'][i][2] < cBaja:
                    cBaja = jugadores[1]['cartas'][i][2]
                    carta = i
            eleccion = jugadores[1]['cartas'][carta]
            jugadores[1]['cartas'].remove(eleccion)
            return eleccion
        elif ganadorPR == 1:
            lista = jugadores[1]['cartas'][:]
            for i in range (len(jugadores[1]['cartas']) - 1, -1, -1):
                if jugadores[1]['cartas'][i][2] <= tuCarta[2]:
                    lista.pop(i)
            if len(lista) > 1:
                cBaja = 15
                carta = 0 
                for i in range(len(lista)):
                    if lista[i][2] < cBaja:
                        cBaja = lista[i][2]
                        carta = i
                eleccion = lista[carta]
                jugadores[1]['cartas'].remove(eleccion)
                return eleccion
            elif len(lista) == 1:
                eleccion = lista[0]
                jugadores[1]['cartas'].remove(eleccion)
                return eleccion
            elif len(lista) == 0:
                cBaja = 15
                carta = 0 
                for i in range(len(jugadores[1]['cartas'])):
                    if jugadores[1]['cartas'][i][2] < cBaja:
                        cBaja = jugadores[1]['cartas'][i][2]
                        carta = i
                eleccion = jugadores[1]['cartas'][carta]
                jugadores[1]['cartas'].remove(eleccion)
                return eleccion
    elif ronda == 3:
        return jugadores[1]['cartas'][0]

def cartasVersus(jugador, maquina):
    carta_jugador = f"{jugador[0]} de {jugador[1]}"
    carta_maquina = f"{maquina[0]} de {maquina[1]}"
    ancho_carta = 14

    carta1 = carta_jugador.center(ancho_carta)
    carta2 = carta_maquina.center(ancho_carta)

    nombre = jugadores[0]['Nombre'] 

    for i in range(10 - len(jugadores[0]['Nombre'])):
        nombre += " "
    
    print("    ________________    |    ________________ ")
    print(f"   |Carta {nombre}|   |   |Carta {jugadores[1]['Nombre']}   |")
    print("   |                |   |   |                |")
    print("   |                |   |   |                |")
    print(f"   | {carta1} |   |   | {carta2} |")
    print("   |                |   |   |                |")
    print("   |                |   |   |                |")
    print("   |                |   |   |                |")
    print("   |________________|   |   |________________|")
    print("                        |")
    time.sleep(1.5)

#########################
# Mezclando... (visual) #
#########################

def cartaRival(eleccion):
    carta = f"{eleccion[0]} de {eleccion[1]}"
    ancho_carta = 14

    carta1 = carta.center(ancho_carta)

    print("    ________________    ")
    print("   |                |")
    print("   |                |")
    print("   |                |")
    print(f"   | {carta1} |")
    print("   |                |")
    print("   |                |")
    print("   |                |")
    print("   |________________|")
    print("                        ")
    print("------------------------")

######################
# Lógica de una mano #
######################

def mano(flor):
    ronda = 1
    
    ganadorPR = 0
    contNos = 0
    contEllos = 0
    tuCarta = 0

    contRondasNos = 0
    contRondasEllos = 0

    while ronda <= 3:
        rondArt(ronda)
        time.sleep(2)
        os.system("cls")

        if ronda == 1: # TERMINAR 
            '''
            envido = int(input("¿Querés cantar envido? (Si = 1 | No = 2) "))
            while envido != 1 and envido != 2:
                envido = int(input("Error. Intente devuelta. ¿Querés cantar envido? (Si = 1 | No = 2) "))
                if envido == 1:
                    envido(flor)
            os.system("cls")'''

            if tuTurno == False:
                cartaMaq = estrategiaNPC(ronda, tuCarta, ganadorPR)
                print(f"{jugadores[1]['Nombre']} jugó la siguiente carta: \n")
                cartaRival(cartaMaq)
                tusCartas()
                carta = int(input("¿Que carta querés jugar? (1, 2 o 3) "))
                while carta != 1 and carta != 2 and carta != 3:
                    carta = int(input("Error. ¿Que carta querés jugar? (1, 2 o 3) "))
                carta -= 1
                os.system("cls")
            elif tuTurno:
                tusCartas()
                carta = int(input("¿Que carta querés jugar? (1, 2 o 3) "))
                while carta != 1 and carta != 2 and carta != 3:
                    carta = int(input("Error. ¿Que carta querés jugar? (1, 2 o 3) "))
                carta -= 1
                os.system("cls")
                tuCarta = jugadores[0]['cartas'][carta]
                cartaMaq = estrategiaNPC(ronda, tuCarta, ganadorPR)

            cartasVersus(jugadores[0]['cartas'][carta], cartaMaq)
            print()
           
            if jugadores[0]['cartas'][carta][2] < cartaMaq[2]:
                contRondasEllos += 1
                ganadorPR = 2
                print(f"{jugadores[1]['Nombre']} se llevó la ronda!")
                time.sleep(2)
            elif jugadores[0]['cartas'][carta][2] > cartaMaq[2]:
                contRondasNos += 1
                ganadorPR = 1
                print("Te llevaste la ronda!")
                time.sleep(2)
            elif jugadores[0]['cartas'][carta][2] == cartaMaq[2]:
                contRondasNos += 1
                contRondasEllos += 1
                print("Parda la mejor!")
                time.sleep(2)

            os.system("cls")
            cartas = jugadores[0]['cartas']
            cartas.pop(carta)
            
        elif ronda == 2:
            if ganadorPR == 2:
                cartaMaq = estrategiaNPC(ronda, tuCarta, ganadorPR)
                print(f"{jugadores[1]['Nombre']} jugó la siguiente carta: \n")
                cartaRival(cartaMaq)
                tusCartas2(cartas)
                carta = int(input("¿Que carta querés jugar? (1 o 2) "))
                while carta != 1 and carta != 2:
                    carta = int(input("Error. ¿Que carta querés jugar? (1 o 2) "))
                carta -= 1
                os.system("cls")
            elif ganadorPR == 1:
                tusCartas2(cartas)
                carta = int(input("¿Que carta querés jugar? (1 o 2) "))
                while carta != 1 and carta != 2:
                    carta = int(input("Error. ¿Que carta querés jugar? (1 o 2) "))
                carta -= 1
                os.system("cls")
                tuCarta = jugadores[0]['cartas'][carta]
                cartaMaq = estrategiaNPC(ronda, tuCarta, ganadorPR)
            
            cartasVersus(cartas[carta], cartaMaq)
            print() 

            if cartas[carta][2] < cartaMaq[2]:
                contRondasEllos += 1
                print(f"{jugadores[1]['Nombre']} se llevó la ronda!")
                time.sleep(2)
            elif cartas[carta][2] > cartaMaq[2]:
                contRondasNos += 1
                print("Te llevaste la ronda!")
                time.sleep(2)
            elif cartas[carta][2] == cartaMaq[2]:
                contRondasNos += 1
                contRondasEllos += 1
                print("Parda!")
                time.sleep(2)
            os.system("cls")
            if contRondasEllos == 2 and contRondasNos != 2:
                print(f"{jugadores[1]['Nombre']} gana la mano!\n")
                comentariosJugadores(1)
                contEllos += 1
                ronda = 4
            elif contRondasNos == 2 and contRondasEllos != 2:
                print("Vos ganás la mano!\n")
                comentariosJugadores(2)
                contNos += 1
                ronda = 4
            else:
                cartas.pop(carta)       

        elif ronda == 3:
            cartaMaq = estrategiaNPC(ronda, jugadores[0]['cartas'][0], ganadorPR)
            cartasVersus(cartas[0], cartaMaq)
            print()
            
            if cartas[0][2] < cartaMaq[2]:
                print(f"{jugadores[1]['Nombre']} gana la mano!\n")
                comentariosJugadores(1)
                contEllos += 1
                ronda = 4
            elif cartas[0][2] > cartaMaq[2]:
                print("Vos ganás la mano!\n")
                comentariosJugadores(2)
                contNos += 1
                ronda = 4
            elif cartas[0][2] == cartaMaq[2]:
                if ganadorPR == 1:
                    print("Vos ganás la mano!\n")
                    comentariosJugadores(2)
                    contNos += 1
                    ronda = 4
                elif ganadorPR == 2:
                    print(f"{jugadores[1]['Nombre']} gana la mano!\n")
                    comentariosJugadores(1)
                    contEllos += 1
                    ronda = 4
                elif ganadorPR == 0:
                    if tuTurno:
                        print("Vos ganás la mano!\n")
                        comentariosJugadores(2)
                        contNos += 1
                        ronda = 4
                    elif tuTurno == False:
                        print(f"{jugadores[1]['Nombre']} gana la mano!\n")
                        comentariosJugadores(1)
                        contEllos += 1
                        ronda = 4
                
        ronda += 1

    time.sleep(2)    
    os.system("cls")
    return contNos, contEllos

############################
# Truco hasta que uno gane #
############################

def juego(nos, ellos):
    global tuTurno
    num = random.randint(1, 2)

    if num == 1:
        tuTurno = True
    elif num == 2:
        tuTurno = False

    mezclarMazo() # Mezclar el mazo
    repartir_cartas_alternadamente(jugadores)  # Repartir las cartas  
    flor, pmax = config()

    while nos <= pmax and ellos <= pmax:
        tablero(nos, ellos)
        time.sleep(1.5)
        print("\nPresione una tecla...", end="")
        input()
        os.system("cls")  
        nos_val, ellos_val = mano(flor)
        nos += nos_val
        ellos += ellos_val
        tuTurno = not(tuTurno)
        mezclarMazo() # Mezclar el mazo
        repartir_cartas_alternadamente(jugadores)  # Repartir las cartas  

    if nos >= pmax:
        print("Ganaste!\n")
        comentariosJugadores(4)
        tecla = input("\nPresione 'ENTER'...")
        os.system("cls")
        felicidades()
    elif ellos >= pmax:
        print(f"{jugadores[1]['Nombre']} ganó la partida!\n")
        comentariosJugadores(3)

############################
# Si jugador gana (visual) #
############################

def felicidades():
    print("                            ")
    print("                                                                  ")
    print("FFFFFFFFFFFFFFFFFFFFFF        ")
    print("F::::::::::::::::::::F          ")
    print("F::::::::::::::::::::F           ")
    print("FF::::::FFFFFFFFF::::F         ")
    print("  F:::::F       FFFFFF      ")
    print("  F:::::F               ")
    print("  F::::::FFFFFFFFFF ")
    print("  F:::::::::::::::F")
    print("  F:::::::::::::::F ")
    print("  F::::::FFFFFFFFFF ")
    print("  F:::::F         ")
    print("  F:::::F                ")
    print("FF:::::::FF          ")
    print("F::::::::FF         ")
    print("F::::::::FF         ")
    print("FFFFFFFFFFF        ")
    print()
    time.sleep(0.3)
    os.system("cls")
    print("                                              ")
    print("                                                         ")
    print("FFFFFFFFFFFFFFFFFFFFFF                      ")
    print("F::::::::::::::::::::F                      ")
    print("F::::::::::::::::::::F                          ")
    print("FF::::::FFFFFFFFF::::F                   ")
    print("  F:::::F       FFFFFF eeeeeeeeeeee      ")
    print("  F:::::F            ee::::::::::::ee   ")
    print("  F::::::FFFFFFFFFF e::::::eeeee:::::ee ")
    print("  F:::::::::::::::Fe::::::e     e:::::e")
    print("  F:::::::::::::::Fe:::::::eeeee::::::e")
    print("  F::::::FFFFFFFFFFe:::::::::::::::::e  ")
    print("  F:::::F          e::::::eeeeeeeeeee   ")
    print("  F:::::F          e:::::::e                ")
    print("FF:::::::FF        e::::::::e             ")
    print("F::::::::FF         e::::::::eeeeeeee    ")
    print("F::::::::FF          ee:::::::::::::e   ")
    print("FFFFFFFFFFF            eeeeeeeeeeeeee  ")
    print()
    time.sleep(0.3)
    os.system("cls")
    print("                                                                         ")
    print("                                                                        ")
    print("FFFFFFFFFFFFFFFFFFFFFF                lllllll         ")
    print("F::::::::::::::::::::F                l:::::l       ")
    print("F::::::::::::::::::::F                l:::::l             ")
    print("FF::::::FFFFFFFFF::::F                l:::::l     ")
    print("  F:::::F       FFFFFF eeeeeeeeeeee    l::::l     ")
    print("  F:::::F            ee::::::::::::ee  l::::l    ")
    print("  F::::::FFFFFFFFFF e::::::eeeee:::::eel::::l  ")
    print("  F:::::::::::::::Fe::::::e     e:::::el::::l   ")
    print("  F:::::::::::::::Fe:::::::eeeee::::::el::::l   ")
    print("  F::::::FFFFFFFFFFe:::::::::::::::::e l::::l  ")
    print("  F:::::F          e::::::eeeeeeeeeee  l::::l    ")
    print("  F:::::F          e:::::::e           l::::l        ")
    print("FF:::::::FF        e::::::::e         l::::::l     ")
    print("F::::::::FF         e::::::::eeeeeeee l::::::l  ")
    print("F::::::::FF          ee:::::::::::::e l::::::l ")
    print("FFFFFFFFFFF            eeeeeeeeeeeeee llllllll")
    print()
    time.sleep(0.3)
    os.system("cls")
    print("                                                                ")
    print("                                                                  ")
    print("FFFFFFFFFFFFFFFFFFFFFF                lllllll   iiii                 ")
    print("F::::::::::::::::::::F                l:::::l  i::::i            ")
    print("F::::::::::::::::::::F                l:::::l   iiii                  ")
    print("FF::::::FFFFFFFFF::::F                l:::::l                 ")
    print("  F:::::F       FFFFFF eeeeeeeeeeee    l::::l iiiiiii       ")
    print("  F:::::F            ee::::::::::::ee  l::::l i:::::i     ")
    print("  F::::::FFFFFFFFFF e::::::eeeee:::::eel::::l  i::::i  ")
    print("  F:::::::::::::::Fe::::::e     e:::::el::::l  i::::i ")
    print("  F:::::::::::::::Fe:::::::eeeee::::::el::::l  i::::i ")
    print("  F::::::FFFFFFFFFFe:::::::::::::::::e l::::l  i::::i ")
    print("  F:::::F          e::::::eeeeeeeeeee  l::::l  i::::i   ")
    print("  F:::::F          e:::::::e           l::::l  i::::i          ")
    print("FF:::::::FF        e::::::::e         l::::::li::::::i        ")
    print("F::::::::FF         e::::::::eeeeeeee l::::::li::::::i   ")
    print("F::::::::FF          ee:::::::::::::e l::::::li::::::i  ")
    print("FFFFFFFFFFF            eeeeeeeeeeeeee lllllllliiiiiiii ")
    print()
    time.sleep(0.3)
    os.system("cls")
    print("                                                                                                                                                               ")
    print("                                                                                                       ")
    print("FFFFFFFFFFFFFFFFFFFFFF                lllllll   iiii                                        ")
    print("F::::::::::::::::::::F                l:::::l  i::::i                                 ")
    print("F::::::::::::::::::::F                l:::::l   iiii                                          ")
    print("FF::::::FFFFFFFFF::::F                l:::::l                                                   ")
    print("  F:::::F       FFFFFF eeeeeeeeeeee    l::::l iiiiiii     cccccccccccccccc   ")
    print("  F:::::F            ee::::::::::::ee  l::::l i:::::i   cc:::::::::::::::c ")
    print("  F::::::FFFFFFFFFF e::::::eeeee:::::eel::::l  i::::i  c:::::::::::::::::c ")
    print("  F:::::::::::::::Fe::::::e     e:::::el::::l  i::::i c:::::::cccccc:::::c ")
    print("  F:::::::::::::::Fe:::::::eeeee::::::el::::l  i::::i c::::::c     ccccccc ")
    print("  F::::::FFFFFFFFFFe:::::::::::::::::e l::::l  i::::i c:::::c              ")
    print("  F:::::F          e::::::eeeeeeeeeee  l::::l  i::::i c:::::c             ")
    print("  F:::::F          e:::::::e           l::::l  i::::i c::::::c     ccccccc         ")
    print("FF:::::::FF        e::::::::e         l::::::li::::::ic:::::::cccccc:::::c     ")
    print("F::::::::FF         e::::::::eeeeeeee l::::::li::::::i c:::::::::::::::::c ")
    print("F::::::::FF          ee:::::::::::::e l::::::li::::::i  cc:::::::::::::::c ")
    print("FFFFFFFFFFF            eeeeeeeeeeeeee lllllllliiiiiiii    cccccccccccccccc ")
    print()
    time.sleep(0.3)
    os.system("cls")
    print("                                                                                                                                                               ")
    print("                                                                                                              ")
    print("FFFFFFFFFFFFFFFFFFFFFF                lllllll   iiii                        iiii                               ")
    print("F::::::::::::::::::::F                l:::::l  i::::i                      i::::i                            ")
    print("F::::::::::::::::::::F                l:::::l   iiii                        iiii                         ")
    print("FF::::::FFFFFFFFF::::F                l:::::l                                                              ")
    print("  F:::::F       FFFFFF eeeeeeeeeeee    l::::l iiiiiii     cccccccccccccccciiiiiii      ")
    print("  F:::::F            ee::::::::::::ee  l::::l i:::::i   cc:::::::::::::::ci:::::i   ")
    print("  F::::::FFFFFFFFFF e::::::eeeee:::::eel::::l  i::::i  c:::::::::::::::::c i::::i ")
    print("  F:::::::::::::::Fe::::::e     e:::::el::::l  i::::i c:::::::cccccc:::::c i::::i ")
    print("  F:::::::::::::::Fe:::::::eeeee::::::el::::l  i::::i c::::::c     ccccccc i::::i ")
    print("  F::::::FFFFFFFFFFe:::::::::::::::::e l::::l  i::::i c:::::c              i::::i  ")
    print("  F:::::F          e::::::eeeeeeeeeee  l::::l  i::::i c:::::c              i::::i  ")
    print("  F:::::F          e:::::::e           l::::l  i::::i c::::::c     ccccccc i::::i          ")
    print("FF:::::::FF        e::::::::e         l::::::li::::::ic:::::::cccccc:::::ci::::::i        ")
    print("F::::::::FF         e::::::::eeeeeeee l::::::li::::::i c:::::::::::::::::ci::::::i  ")
    print("F::::::::FF          ee:::::::::::::e l::::::li::::::i  cc:::::::::::::::ci::::::i  ")
    print("FFFFFFFFFFF            eeeeeeeeeeeeee lllllllliiiiiiii    cccccccccccccccciiiiiiii")
    print()
    time.sleep(0.3)
    os.system("cls")
    print("                                                                                                                                                               ")
    print("                                                                                              dddddddd                                    ")
    print("FFFFFFFFFFFFFFFFFFFFFF                lllllll   iiii                        iiii              d::::::d                                        ")
    print("F::::::::::::::::::::F                l:::::l  i::::i                      i::::i             d::::::d                                   ")
    print("F::::::::::::::::::::F                l:::::l   iiii                        iiii              d::::::d                                        ")
    print("FF::::::FFFFFFFFF::::F                l:::::l                                                 d:::::d                                        ")
    print("  F:::::F       FFFFFF eeeeeeeeeeee    l::::l iiiiiii     cccccccccccccccciiiiiii     ddddddddd:::::d     ")
    print("  F:::::F            ee::::::::::::ee  l::::l i:::::i   cc:::::::::::::::ci:::::i   dd::::::::::::::d    ")
    print("  F::::::FFFFFFFFFF e::::::eeeee:::::eel::::l  i::::i  c:::::::::::::::::c i::::i  d::::::::::::::::d ")
    print("  F:::::::::::::::Fe::::::e     e:::::el::::l  i::::i c:::::::cccccc:::::c i::::i d:::::::ddddd:::::d")
    print("  F:::::::::::::::Fe:::::::eeeee::::::el::::l  i::::i c::::::c     ccccccc i::::i d::::::d    d:::::d  ")
    print("  F::::::FFFFFFFFFFe:::::::::::::::::e l::::l  i::::i c:::::c              i::::i d:::::d     d:::::d   ")
    print("  F:::::F          e::::::eeeeeeeeeee  l::::l  i::::i c:::::c              i::::i d:::::d     d:::::d   ")
    print("  F:::::F          e:::::::e           l::::l  i::::i c::::::c     ccccccc i::::i d:::::d     d:::::d           ")
    print("FF:::::::FF        e::::::::e         l::::::li::::::ic:::::::cccccc:::::ci::::::id::::::ddddd::::::dd      ")
    print("F::::::::FF         e::::::::eeeeeeee l::::::li::::::i c:::::::::::::::::ci::::::i d:::::::::::::::::d ")
    print("F::::::::FF          ee:::::::::::::e l::::::li::::::i  cc:::::::::::::::ci::::::i  d:::::::::ddd::::d   ")
    print("FFFFFFFFFFF            eeeeeeeeeeeeee lllllllliiiiiiii    cccccccccccccccciiiiiiii   ddddddddd   ddddd ")
    print()
    time.sleep(0.3)
    os.system("cls")
    print("                                                                                                                                                    ")
    print("                                                                                              dddddddd                                  ")
    print("FFFFFFFFFFFFFFFFFFFFFF                lllllll   iiii                        iiii              d::::::d                                ")
    print("F::::::::::::::::::::F                l:::::l  i::::i                      i::::i             d::::::d                                ")
    print("F::::::::::::::::::::F                l:::::l   iiii                        iiii              d::::::d                                ")
    print("FF::::::FFFFFFFFF::::F                l:::::l                                                 d:::::d                                 ")
    print("  F:::::F       FFFFFF eeeeeeeeeeee    l::::l iiiiiii     cccccccccccccccciiiiiii     ddddddddd:::::d   aaaaaaaaaaaaa         ")
    print("  F:::::F            ee::::::::::::ee  l::::l i:::::i   cc:::::::::::::::ci:::::i   dd::::::::::::::d   a::::::::::::a           ")
    print("  F::::::FFFFFFFFFF e::::::eeeee:::::eel::::l  i::::i  c:::::::::::::::::c i::::i  d::::::::::::::::d   aaaaaaaaa:::::a        ")
    print("  F:::::::::::::::Fe::::::e     e:::::el::::l  i::::i c:::::::cccccc:::::c i::::i d:::::::ddddd:::::d            a::::a       ")
    print("  F:::::::::::::::Fe:::::::eeeee::::::el::::l  i::::i c::::::c     ccccccc i::::i d::::::d    d:::::d     aaaaaaa:::::a       ")
    print("  F::::::FFFFFFFFFFe:::::::::::::::::e l::::l  i::::i c:::::c              i::::i d:::::d     d:::::d   aa::::::::::::a        ")
    print("  F:::::F          e::::::eeeeeeeeeee  l::::l  i::::i c:::::c              i::::i d:::::d     d:::::d  a::::aaaa::::::a      ")
    print("  F:::::F          e:::::::e           l::::l  i::::i c::::::c     ccccccc i::::i d:::::d     d:::::d a::::a    a:::::a  ")
    print("FF:::::::FF        e::::::::e         l::::::li::::::ic:::::::cccccc:::::ci::::::id::::::ddddd::::::dda::::a    a:::::a   ")
    print("F::::::::FF         e::::::::eeeeeeee l::::::li::::::i c:::::::::::::::::ci::::::i d:::::::::::::::::da:::::aaaa::::::a   ")
    print("F::::::::FF          ee:::::::::::::e l::::::li::::::i  cc:::::::::::::::ci::::::i  d:::::::::ddd::::d a::::::::::aa:::a         ")
    print("FFFFFFFFFFF            eeeeeeeeeeeeee lllllllliiiiiiii    cccccccccccccccciiiiiiii   ddddddddd   ddddd  aaaaaaaaaa  aaaa    ")
    print()
    time.sleep(0.3)
    os.system("cls")
    print("                                                                                                                                                    ")
    print("                                                                                              dddddddd                             dddddddd         ")
    print("FFFFFFFFFFFFFFFFFFFFFF                lllllll   iiii                        iiii              d::::::d                             d::::::d         ")
    print("F::::::::::::::::::::F                l:::::l  i::::i                      i::::i             d::::::d                             d::::::d         ")
    print("F::::::::::::::::::::F                l:::::l   iiii                        iiii              d::::::d                             d::::::d         ")
    print("FF::::::FFFFFFFFF::::F                l:::::l                                                 d:::::d                              d:::::d          ")
    print("  F:::::F       FFFFFF eeeeeeeeeeee    l::::l iiiiiii     cccccccccccccccciiiiiii     ddddddddd:::::d   aaaaaaaaaaaaa      ddddddddd:::::d          ")
    print("  F:::::F            ee::::::::::::ee  l::::l i:::::i   cc:::::::::::::::ci:::::i   dd::::::::::::::d   a::::::::::::a   dd::::::::::::::d          ")
    print("  F::::::FFFFFFFFFF e::::::eeeee:::::eel::::l  i::::i  c:::::::::::::::::c i::::i  d::::::::::::::::d   aaaaaaaaa:::::a d::::::::::::::::d          ")
    print("  F:::::::::::::::Fe::::::e     e:::::el::::l  i::::i c:::::::cccccc:::::c i::::i d:::::::ddddd:::::d            a::::ad:::::::ddddd:::::d          ")
    print("  F:::::::::::::::Fe:::::::eeeee::::::el::::l  i::::i c::::::c     ccccccc i::::i d::::::d    d:::::d     aaaaaaa:::::ad::::::d    d:::::d          ")
    print("  F::::::FFFFFFFFFFe:::::::::::::::::e l::::l  i::::i c:::::c              i::::i d:::::d     d:::::d   aa::::::::::::ad:::::d     d:::::d          ")
    print("  F:::::F          e::::::eeeeeeeeeee  l::::l  i::::i c:::::c              i::::i d:::::d     d:::::d  a::::aaaa::::::ad:::::d     d:::::d          ")
    print("  F:::::F          e:::::::e           l::::l  i::::i c::::::c     ccccccc i::::i d:::::d     d:::::d a::::a    a:::::ad:::::d     d:::::d          ")
    print("FF:::::::FF        e::::::::e         l::::::li::::::ic:::::::cccccc:::::ci::::::id::::::ddddd::::::dda::::a    a:::::ad::::::ddddd::::::dd         ")
    print("F::::::::FF         e::::::::eeeeeeee l::::::li::::::i c:::::::::::::::::ci::::::i d:::::::::::::::::da:::::aaaa::::::a d:::::::::::::::::d         ")
    print("F::::::::FF          ee:::::::::::::e l::::::li::::::i  cc:::::::::::::::ci::::::i  d:::::::::ddd::::d a::::::::::aa:::a d:::::::::ddd::::d         ")
    print("FFFFFFFFFFF            eeeeeeeeeeeeee lllllllliiiiiiii    cccccccccccccccciiiiiiii   ddddddddd   ddddd  aaaaaaaaaa  aaaa  ddddddddd   ddddd         ")
    print()
    time.sleep(0.3)
    os.system("cls")
    print("                                                                                                                                                               ")
    print("                                                                                              dddddddd                             dddddddd                    ")
    print("FFFFFFFFFFFFFFFFFFFFFF                lllllll   iiii                        iiii              d::::::d                             d::::::d                    ")
    print("F::::::::::::::::::::F                l:::::l  i::::i                      i::::i             d::::::d                             d::::::d                    ")
    print("F::::::::::::::::::::F                l:::::l   iiii                        iiii              d::::::d                             d::::::d                    ")
    print("FF::::::FFFFFFFFF::::F                l:::::l                                                 d:::::d                              d:::::d                     ")
    print("  F:::::F       FFFFFF eeeeeeeeeeee    l::::l iiiiiii     cccccccccccccccciiiiiii     ddddddddd:::::d   aaaaaaaaaaaaa      ddddddddd:::::d     eeeeeeeeeeee    ")
    print("  F:::::F            ee::::::::::::ee  l::::l i:::::i   cc:::::::::::::::ci:::::i   dd::::::::::::::d   a::::::::::::a   dd::::::::::::::d   ee::::::::::::ee  ")
    print("  F::::::FFFFFFFFFF e::::::eeeee:::::eel::::l  i::::i  c:::::::::::::::::c i::::i  d::::::::::::::::d   aaaaaaaaa:::::a d::::::::::::::::d  e::::::eeeee:::::ee")
    print("  F:::::::::::::::Fe::::::e     e:::::el::::l  i::::i c:::::::cccccc:::::c i::::i d:::::::ddddd:::::d            a::::ad:::::::ddddd:::::d e::::::e     e:::::e")
    print("  F:::::::::::::::Fe:::::::eeeee::::::el::::l  i::::i c::::::c     ccccccc i::::i d::::::d    d:::::d     aaaaaaa:::::ad::::::d    d:::::d e:::::::eeeee::::::e")
    print("  F::::::FFFFFFFFFFe:::::::::::::::::e l::::l  i::::i c:::::c              i::::i d:::::d     d:::::d   aa::::::::::::ad:::::d     d:::::d e:::::::::::::::::e ")
    print("  F:::::F          e::::::eeeeeeeeeee  l::::l  i::::i c:::::c              i::::i d:::::d     d:::::d  a::::aaaa::::::ad:::::d     d:::::d e::::::eeeeeeeeeee  ")
    print("  F:::::F          e:::::::e           l::::l  i::::i c::::::c     ccccccc i::::i d:::::d     d:::::d a::::a    a:::::ad:::::d     d:::::d e:::::::e           ")
    print("FF:::::::FF        e::::::::e         l::::::li::::::ic:::::::cccccc:::::ci::::::id::::::ddddd::::::dda::::a    a:::::ad::::::ddddd::::::dde::::::::e          ")
    print("F::::::::FF         e::::::::eeeeeeee l::::::li::::::i c:::::::::::::::::ci::::::i d:::::::::::::::::da:::::aaaa::::::a d:::::::::::::::::d e::::::::eeeeeeee  ")
    print("F::::::::FF          ee:::::::::::::e l::::::li::::::i  cc:::::::::::::::ci::::::i  d:::::::::ddd::::d a::::::::::aa:::a d:::::::::ddd::::d  ee:::::::::::::e  ")
    print("FFFFFFFFFFF            eeeeeeeeeeeeee lllllllliiiiiiii    cccccccccccccccciiiiiiii   ddddddddd   ddddd  aaaaaaaaaa  aaaa  ddddddddd   ddddd    eeeeeeeeeeeeee  ")
    print()
    time.sleep(0.3)
    os.system("cls")
    print("                                                                                                                                                                                ")
    print("                                                                                              dddddddd                             dddddddd                                     ")
    print("FFFFFFFFFFFFFFFFFFFFFF                lllllll   iiii                        iiii              d::::::d                             d::::::d                                     ")
    print("F::::::::::::::::::::F                l:::::l  i::::i                      i::::i             d::::::d                             d::::::d                                     ")
    print("F::::::::::::::::::::F                l:::::l   iiii                        iiii              d::::::d                             d::::::d                                     ")
    print("FF::::::FFFFFFFFF::::F                l:::::l                                                 d:::::d                              d:::::d                                      ")
    print("  F:::::F       FFFFFF eeeeeeeeeeee    l::::l iiiiiii     cccccccccccccccciiiiiii     ddddddddd:::::d   aaaaaaaaaaaaa      ddddddddd:::::d     eeeeeeeeeeee        ssssssssss   ")
    print("  F:::::F            ee::::::::::::ee  l::::l i:::::i   cc:::::::::::::::ci:::::i   dd::::::::::::::d   a::::::::::::a   dd::::::::::::::d   ee::::::::::::ee    ss::::::::::s  ")
    print("  F::::::FFFFFFFFFF e::::::eeeee:::::eel::::l  i::::i  c:::::::::::::::::c i::::i  d::::::::::::::::d   aaaaaaaaa:::::a d::::::::::::::::d  e::::::eeeee:::::eess:::::::::::::s ")
    print("  F:::::::::::::::Fe::::::e     e:::::el::::l  i::::i c:::::::cccccc:::::c i::::i d:::::::ddddd:::::d            a::::ad:::::::ddddd:::::d e::::::e     e:::::es::::::ssss:::::s")
    print("  F:::::::::::::::Fe:::::::eeeee::::::el::::l  i::::i c::::::c     ccccccc i::::i d::::::d    d:::::d     aaaaaaa:::::ad::::::d    d:::::d e:::::::eeeee::::::e s:::::s  ssssss ")
    print("  F::::::FFFFFFFFFFe:::::::::::::::::e l::::l  i::::i c:::::c              i::::i d:::::d     d:::::d   aa::::::::::::ad:::::d     d:::::d e:::::::::::::::::e    s::::::s      ")
    print("  F:::::F          e::::::eeeeeeeeeee  l::::l  i::::i c:::::c              i::::i d:::::d     d:::::d  a::::aaaa::::::ad:::::d     d:::::d e::::::eeeeeeeeeee        s::::::s   ")
    print("  F:::::F          e:::::::e           l::::l  i::::i c::::::c     ccccccc i::::i d:::::d     d:::::d a::::a    a:::::ad:::::d     d:::::d e:::::::e           ssssss   s:::::s ")
    print("FF:::::::FF        e::::::::e         l::::::li::::::ic:::::::cccccc:::::ci::::::id::::::ddddd::::::dda::::a    a:::::ad::::::ddddd::::::dde::::::::e          s:::::ssss::::::s")
    print("F::::::::FF         e::::::::eeeeeeee l::::::li::::::i c:::::::::::::::::ci::::::i d:::::::::::::::::da:::::aaaa::::::a d:::::::::::::::::d e::::::::eeeeeeee  s::::::::::::::s ")
    print("F::::::::FF          ee:::::::::::::e l::::::li::::::i  cc:::::::::::::::ci::::::i  d:::::::::ddd::::d a::::::::::aa:::a d:::::::::ddd::::d  ee:::::::::::::e   s:::::::::::ss  ")
    print("FFFFFFFFFFF            eeeeeeeeeeeeee lllllllliiiiiiii    cccccccccccccccciiiiiiii   ddddddddd   ddddd  aaaaaaaaaa  aaaa  ddddddddd   ddddd    eeeeeeeeeeeeee    sssssssssss    ")
    print()
    time.sleep(3)
        
################
# Puntuaciones #
################

def tablero(nos, ellos):
    if nos <= 15:
        puntosNos = "Malas "
    else: 
        puntosNos = "Buenas"
    if ellos <= 15:
        puntosEllos = "Malas "
    else: 
        puntosEllos = "Buenas"
    
    if nos < 10:
        nos = str(nos) + " "
    if ellos < 10:
        ellos = str(ellos) + " "

    nombre = jugadores[0]['Nombre'].center(12)

    print("   _________________________ ")
    print("  |         TABLERO         |")
    print("  |—————————————————————————|")
    print(f"  |{nombre}|  {jugadores[1]['Nombre']}   |")
    print("  | ", nos, "puntos | ", ellos, "puntos |")
    print(f"  |   {puntosNos}   |   {puntosEllos}   |")
    print("  |____________|____________|")

########################
# Lógica de minijuegos #
########################

def truco():
    pass

def envido(flor):
    if flor == 1:
        if jugadores[0]['cartas'][0][1] == jugadores[0]['cartas'][1][1] and jugadores[0]['cartas'][0][1] == jugadores[0]['cartas'][2][1]:
            pass

#########################
# Funciones de arranque #
#########################

def menu():
    menuLogin()
    repetir = True
    while repetir:
        os.system("cls") #limpia la pantalla
        print(f"   Bienvenido {usuario}!")
        print("")
        print("   ■■■■■■■■■■■■■■■■■■■■■■■     ■■■■■■■■■■■■■■■■■■■■■■■■      ■■■■■■■■■■■■■■■■■■■■■■■     ■■■■■■■■■■■■■■■■■■■■■■■     ■■■■■■■■■■■■■■■■■■■■■■■        ")
        print("   █      1. Equipo      █     █  2. Instrucciones    █      █     3. Ejecutar     █     █  4. Cambiar Sesion  █     █      5. Salir       █        ")
        print("   ■■■■■■■■■■■■■■■■■■■■■■■     ■■■■■■■■■■■■■■■■■■■■■■■■      ■■■■■■■■■■■■■■■■■■■■■■■     ■■■■■■■■■■■■■■■■■■■■■■■     ■■■■■■■■■■■■■■■■■■■■■■■        ")
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
                print("• El Truco se juega con una baraja española de 40 cartas (sin ningún 8, 9 o 10).                                                                                                     ")
                print("• Participan 2, 4 o 6 jugadores, organizados en 2 equipos donde cada jugador recibe 3 cartas y el objetivo es alcanzar 15 o 30 puntos, según la modalidad                            ")
                print("• El juego se desarrolla por manos donde se lleva puntos quien gane 2 de 3 enfrentamientos.                                                                                          ")
                print("""• Los jugadores pueden cantar "truco"  para desafiar al adversario, aumentando la apuesta de puntos;                                                                               """)
                print("""el rival puede aceptar, rechazar, o subir la apuesta con "re-truco" o "vale cuatro"                                                                                              """)
                print("""• También se puede "Cantar Envido" antes de usar la primer carta, apostando por el mejor par de cartas del mismo palo.                                                             """)
                print("""• Además, si un jugador tiene las tres cartas del mismo palo, puede "Cantar Flor" para ganar puntos extras (aunque se debe aclarar si está permitida al comienzo de la partida)    """)
                print("• Por último, los puntos se otorgan según el resultado de las manos y las apuestas realizadas.                                                                                        ")
                print("")

                tecla = input("\nPresione 'ENTER' para volver al menú...")
            elif op == 3:
                os.system("cls")
                ejecutar()
                tecla = input("\nPresione 'ENTER' para volver al menú...")
            elif op == 4:
                os.system("cls")
                salir_cuenta()
            elif op == 5:
                os.system("cls")
                repetir = False
                print("Gracias por jugar.")
            else: 
                os.system("cls")
                input("Parece que ingresaste una opción no válida. ¡Presiona 'ENTER' y volvé a intentarlo!")
        except:
              os.system("cls")                                                                                                   
              print("                                                                                                               ")
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

def ejecutar():
    nos = 0
    ellos = 0
    creandoJugadores() # Crear los jugadores
    juego(nos, ellos)

def inicio():
    os.system("cls")
    print("                                                                                                               ")
    print("TTTTTTTTTTTTTTTTTTTTTTT                                                                           ")
    print("T:::::::::::::::::::::T                                                                           ")
    print("T:::::::::::::::::::::T                                                                           ")
    print("T:::::TT:::::::TT:::::T                                                                           ")
    print("TTTTTT  T:::::T  TTTTTTrrrrr   rrrrrrrrr   uuuuuu    uuuuuu      cccccccccccccccc   ooooooooooo   ")
    print("        T:::::T        r::::rrr:::::::::r  u::::u    u::::u    cc:::::::::::::::c oo:::::::::::oo ")
    print("        T:::::T        r:::::::::::::::::r u::::u    u::::u   c:::::::::::::::::co:::::::::::::::o")
    print("        T:::::T        rr::::::rrrrr::::::ru::::u    u::::u  c:::::::cccccc:::::co:::::ooooo:::::o")
    print("        T:::::T         r:::::r     r:::::ru::::u    u::::u  c::::::c     ccccccco::::o     o::::o")
    print("        T:::::T         r:::::r     rrrrrrru::::u    u::::u  c:::::c             o::::o     o::::o")
    print("        T:::::T         r:::::r            u::::u    u::::u  c:::::c             o::::o     o::::o")
    print("        T:::::T         r:::::r            u:::::uuuu:::::u  c::::::c     ccccccco::::o     o::::o")
    print("      TT:::::::TT       r:::::r            u:::::::::::::::uuc:::::::cccccc:::::co:::::ooooo:::::o")
    print("      T:::::::::T       r:::::r             u:::::::::::::::u c:::::::::::::::::co:::::::::::::::o")
    print("      T:::::::::T       r:::::r              uu::::::::uu:::u  cc:::::::::::::::c oo:::::::::::oo ")
    print("      TTTTTTTTTTT       rrrrrrr                uuuuuuuu  uuuu    cccccccccccccccc   ooooooooooo   ")
    print()
    print("                                                                           _   _    _    ___   ___ ")
    print("                                                                          | | | |  /_\  |   \ | __|")
    print("                                                                          | |_| | / _ \ | |) || _| ")
    print("                                                                          \_____//_/ \_\|___/ |___|")
    time.sleep(3)
    print("\nPresione una tecla...", end="")
    input()
    menu()