
"""
  reglas.py
  Este archivo tiene el objetivo de establecer la sprincipales reglas del juego.

"""
# Usamos 1 = libre, 0 = no libre, 3 = queso
# Cada regla = (izq, arr, der, abajo)
reglas = {
    (1,1,1,1): "ir arriba",
    (1,1,1,0): "ir arriba",
    (1,1,0,1): "ir arriba",
    (1,1,0,0): "ir arriba",
    (1,0,1,1): "ir izquierda",
    (1,0,1,0): "ir derecha",
    (1,0,0,1): "ir izquierda",
    (1,0,0,0): "ir izquierda",
    (0,1,1,1): "ir arriba",
    (0,1,1,0): "ir derecha",
    (0,1,0,1): "ir abajo",
    (0,1,0,0): "ir arriba",
    (0,0,1,1): "ir derecha",
    (0,0,1,0): "ir derecha",
    (0,0,0,1): "ir abajo",
}
