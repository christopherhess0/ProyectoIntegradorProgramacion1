valores_altos = [
    ('1', 'Espada', 14), ('1', 'Basto', 13), 
    ('7', 'Espada', 12), ('7', 'Oro', 11)
]

valores_medios = [
    ('3', 10), ('2', 9), ('1', 8), 
    ('12', 7), ('11', 6), ('10', 5)
]

valores_bajos = [
    ('7', 4), ('6', 3), ('5', 2), 
    ('4', 1)
]

palos = ['Espada', 'Basto', 'Copa', 'Oro']

# Generar el mazo
cartas = (
    valores_altos +
    [(valor, palo, puntos) for valor, puntos in valores_medios for palo in palos] +
    [(valor, palo, puntos) for valor, puntos in valores_bajos for palo in palos]
)