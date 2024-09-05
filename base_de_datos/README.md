# ProyectoIntegradorProgramacion1
Este es el proyecto integrados que vamos a desarrollar en la materia Programacion 1 de la UADE

---------------------------------------
Backlog:

Semana 1-2: Mazo y repartija
  * Armar mazo ✓ 
  * Repartir por turnos ✓
  * Guardar cartas de NPC sin mostrarlas ✓
  * Obviar repeticiones ✓

Semana 3-4: Lógica de una mano
  * Comparación de cartas en juego
  * Sistema de turnos
  * Elección de juegos
  * Truco, re-truco, vale-cuatro

Semana 5-6: Envido y variaciones
  * Suma de puntos
  * Comparación de valores
  * Elección de juegos
  * Envido, real envido o falta envido

Semana 7-8: Comportamiento del NPC
  * Técnica
  * Comentarios
  * Mentiras
  * Agresividad

Semana 9-10: Configuración de una partida
  * Puntuación máxima
  * Juego con "flor" o sin
  * Modos de juego (1v1/2v2/3v3)

Semana 11-12: Partida completa
  * Tablero
  * Suma de puntos
  * Manos indefinidas hasta puntuación limite

La duracion por cada tarea es estimada y puede variar a medida que se vayan completando.
---------------------------------------
Historias de usuario:

Como: jugador
Quiero: poder elegir el nivel de dificultad de las partidas 
Para: poder mejorar en el juego o aprender

Como: jugador
Quiero: poder elegir contra cuantas personas jugar 
Para: hacerlo más entretenido

Como: jugador 
Quiero: poder retirarme de la partida y empezar otra 
Para: evitar perder y quedarme atras

Como: jugador
Quiero: que se me notifique cuando sea mi turno
Para: saber cuando es mi turno

Como: principiante en el juego
Quiero: poder elegir ver un breve resumen de las reglas y valor de las cartas antes de comenzar una partida 
Para: poder jugar con un conocimiento previo

Como: jugador 
Quiero: poder elegir jugar una revancha 
Para: poder ganarle al oponente si perdi. 

Como: jugador
Quiero: poder elegir la cantidad de puntos para ganar las partidas 
Para: hacer partidas que duren más o que duren menos 

Como: jugador
Quiero: poder calcular la suma de los puntos de mis cartas automáticamente
Para: no tener que hacerlo manualmente.
  
Como: jugador 
Quiero: poder ver una tabla de posiciones en tiempo real durante la partida 
Para: saber quién está ganando.

Como: jugador principiante 
Quiero: poder elegir que el juego me sugiera la mejor jugada posible basándose en las cartas en mi mano y en la mesa
Para: tener una ayuda, y aprender mejores jugadas. 

Como: jugador
Quiero: que el juego calcule automáticamente el puntaje del envido de cada jugador,
Para: saber quién tiene el envido más alto y ganar los puntos correspondientes.

Como: jugador 
Quiero: que el juego indique quien gana en cada mano 
Para: poder llevar un seguimiento de la jugada 

Como: jugador
Quiero: que al finalizar la partida se muestre un mensaje personalizado dependiendo si gane o perdi
Para: añadir diversion

---------------------------------------


Dado: que el jugador quiere realizar un envido 
Cuando: la partida ya está empezada 
Entonces: da error 

Dado: que el jugador intenta salir de la partida durante una mano
Cuando: presiona el botón de salir
Entonces: el juego le muestra una advertencia de que perderá automáticamente la ronda si abandona.

Dado: que el jugador intenta jugar una carta 
Cuando: aún no es su turno
Entonces: cuando selecciona una carta fuera de su turno el juego muestra un mensaje de error y no permite la acción.

Dado: que el jugador intenta cantar "Vale Cuatro" sin que se haya cantado "Truco" y
"Retruco"
Cuando: selecciona la opción de "Vale Cuatro" directamente
Entonces: el juego impide el canto y explica que debe seguir el orden de cantos 

Dado: que el jugador quiere cantar flor 
Cuando: no tiene las 3 cartas del mismo palo 
Entonces: le salta error y explica el porque no puede hacerlo