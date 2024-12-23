# Movimiento en el tablero hecho por Miguel
import random
from Coordenadas import *
ubicacionJugador = [0,0]


def mostrarTablero(tablero,tableroBanderas):
    """Muestra por consola un tablero de juego recibido como parámetro junto con una leyenda
    explicando los controles del juego"""
    # Salida por consola del tablero
    for i in range(len(tablero)): ## para cada fila del tablero...
        for j in range(len(tablero[i])): ## para cada elemento de cada fila del tablero...
           ## imprimir el elemento seleccionado
            if i == ubicacionJugador[0] and j == ubicacionJugador[1]:
                print ("X",end= " ")
            elif tableroBanderas[i][j]=="%":
                print("%",end=" ")
            else:
                print(tablero[i][j], end=" ")
        print() ## salto de línea para cada fila
    # Leyenda con los controles
    print()
    print()
    print("'w' para moverte hacia arriba")
    print("'a' para moverte hacia la izquierda")
    print("'s' para moverte hacia abajo")
    print("'d' para moverte hacia la derecha")
    print("'m' para marcar")
    print("'c' para desmarcar")
    print("'e' para desactivar bomba")
    print()
    print()


def cambiarElemento(tablero,cambio,fila,columna):
    """Recibe un tablero y cambia en el tablero el elemento de las coordenadas dadas como parámetros por otro nuevo.
    Retorna el nuevo tablero"""
    tablero[fila][columna]=cambio
    return tablero


def movimientoDelJugador(tablero,tableroBanderas,letra):
    """A partir del parámetro de tipo carácter, el jugador se desplazará por el tablero de juego, dado como parámetro,
    mediante las letras "a" o "A" (movimiento hacia la izquierda), "d" o "D" (movimiento hacia la derecha),
    "s" o "S" (movimiento hacia abajo) y "w" o "W" (movimiento hacia arriba)"""
    movimiento=letra
    if movimiento=='a' or movimiento=='A':
        if ubicacionJugador[1]-1 >= 0:
            ubicacionJugador[1] = ubicacionJugador[1] - 1
    elif movimiento=='d' or movimiento=='D':
        if ubicacionJugador[1]+1 < (len(tablero)):
            ubicacionJugador[1] = ubicacionJugador[1] + 1
    elif movimiento=='w' or movimiento=='W':
        if ubicacionJugador[0]-1 >= 0:
            ubicacionJugador[0] = ubicacionJugador[0] -1
    elif movimiento=='s' or movimiento=='S':
        if ubicacionJugador[0]+1 < (len(tablero)):
            ubicacionJugador[0] = ubicacionJugador[0] + 1

    elif movimiento=='m' or movimiento=='M':
        tableroBanderas[ubicacionJugador[0]][ubicacionJugador[1]]="%"
    elif movimiento=='c' or movimiento=='C':
        tableroBanderas[ubicacionJugador[0]][ubicacionJugador[1]]="0"

    elif movimiento=='e' or movimiento=='E':
        if tablero[ubicacionJugador[0]][ubicacionJugador[1]]==" ":
            return False
    return True



