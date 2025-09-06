
from reglas import reglas
"""
  funciones.py
  Este archivo tiene el objetivo de establecer las funciones del juego.
"""

# Esta función tiene el objetivo de detectar el estado de cada posición alrededor del ratón
def obtener_sensores(laberinto, pos, filas, columnas):
    x, y = pos

    # Verificamos en cada dirección si hay camino libre (1 o 3) o muro (0)
    izq   = 1 if y > 0 and laberinto[x][y-1] != 0 else 0
    arr   = 1 if x > 0 and laberinto[x-1][y] != 0 else 0
    der   = 1 if y < columnas-1 and laberinto[x][y+1] != 0 else 0
    abajo = 1 if x < filas-1 and laberinto[x+1][y] != 0 else 0

    return (izq, arr, der, abajo)

# Esta función permite recorrer toda la matriz hasta encontrar y devolver la posición del ratón
def buscarRaton (matriz, filas, columnas):
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == 2:
                return (i, j)
    return None

# ESta fucnión encuentra la ubicación del queso y la devuelve
def buscarQueso(matriz, filas, columnas):
  pos = buscarRaton(matriz, filas, columnas)

  if pos is None:
      return None

  i, j = pos

  acum = 1

  if (i,j) == None:
    return None

  while True:


    if acum == 2*(filas*columnas):
      return None

    for clave in reglas:
      if clave == obtener_sensores(matriz, (i,j), filas, columnas):
        direccion = reglas[clave]
        print(direccion)
        if direccion == "ir arriba" and i > 0:
            i -= 1
        elif direccion == "ir abajo" and i < filas-1:
            i += 1
        elif direccion == "ir izquierda" and j > 0:
            j -= 1
        elif direccion == "ir derecha" and j < columnas-1:
            j += 1
        else:
            return None  # se intentó un movimiento inválido
        print("Pasos dados: ", acum)
        acum += 1
        break

    if matriz[i][j] == 3:
      return (i,j)
