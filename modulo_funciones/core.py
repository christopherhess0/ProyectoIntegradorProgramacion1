import random

#Variables
jugadores = []

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
    random.shuffle(cartas)

# Función para crear jugadores
def creandoJugadores():
    for i in range(2):
        jugador = {'nombre': f'Jugador {i+1}', 'cartas': []}
        jugadores.append(jugador)

# Función para repartir cartas alternadamente
def repartir_cartas_alternadamente(jugadores):
    jugador_index = 0  # Comienza con el primer jugador
    cont = 0
    while cont < 6:
        jugadores[jugador_index]['cartas'].append(cartas[cont])
        if jugador_index == 0:
            jugador_index = 1
        else:
            jugador_index = 0
        cont += 1