# juego de truco en consola
import random
import extras
import mezclarCartas

def mezclarMazo():
    random.shuffle(cartas)

#Armo mazo:
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
    ('6', 'Espada', 3), ('6', 'Basto', 3), ('6', 'Oro', 3), ('6', 'Copa', 3), 

    ]
# Funcion Crear Jugadores
def creandoJugadores():
    num_jugadores = int(input("Ingrese número de jugadores: "))
    jugadores = []

    for i in range(1, num_jugadores + 1):
        jugador = {
            'nombre': f'Jugador {i}',
            'cartas': []
        }
        jugadores.append(jugador)

    # Imprimir la lista de jugadores para verificar
    print(jugadores)
