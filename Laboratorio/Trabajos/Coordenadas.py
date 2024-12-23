# Módulo minas hecho por Néstor
import random

def colocarMinas(tablero,minas,nNumeroDeMinas):
    """Recibiendo como parámetros un tablero de juego, el carácter que define una mina, y un número de minas no nulo ni negativo,
    colocará en el tablero las minas con unas coordenadas, y retornará el tablero """
    for i in range(nNumeroDeMinas):
        x=random.randint(0,len(tablero)-1)
        y=random.randint(0,len(tablero)-1)
        while tablero[x][y]==minas:
            x=random.randint(0,len(tablero)-1)
            y=random.randint(0,len(tablero)-1)
        tablero[x][y]=minas
    return tablero




def ocultarMinas(tablero):
    """Recibe un tablero con minas como parámetro y oculta las minas sustituyendo los elementos "minas" en el tablero
    por elementos vacíos. Retornará el nuevo tablero"""
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j]!=0:
                tablero[i][j]=" "
    return tablero
