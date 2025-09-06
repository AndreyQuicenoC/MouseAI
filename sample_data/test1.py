
from funciones import buscarQueso
"""
  test1.py
  Este archivo tiene el objetivo de probar el juego.
"""

laberinto_primer_test = [
    [1, 1, 1, 1],
    [1, 0, 0, 3],
    [2, 0, 1, 1],
    [1, 1, 1, 0]
]

filas = len(laberinto_primer_test)
columnas = len(laberinto_primer_test[0])

pos = buscarQueso(laberinto_primer_test, filas, columnas)

if pos is None:
    print("\nEl ratón no pudo encontrar el queso.")
else:
    fila, columna = pos
    print(f"\nEl queso fue encontrado en la posición: fila {fila+1}, columna {columna+1}")

for fila in laberinto_primer_test:
    print(" ".join(str(x) for x in fila))
