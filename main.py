import modulo_funciones.core as c


# Ejecución del juego
c.creandoJugadores() # Crear los jugadores
c.mezclarMazo() # Mezclar el mazo
c.repartir_cartas_alternadamente(c.jugadores)  # Repartir las cartas

# Imprimir jugadores con sus cartas
for jugador in c.jugadores:
    print(f"{jugador['nombre']} tiene las cartas: {jugador['cartas']}")