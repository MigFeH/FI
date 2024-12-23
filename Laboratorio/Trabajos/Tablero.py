# Tablero de juego hecho por Miguel
import random
from Coordenadas import *
from Movimiento import *



def crearTablero(filas,columnas,valor):
    """Crea y retorna un tablero de juego con unas dimensiones (filas x columnas) recibidas
    como parámetros, y asigna a cada posición del tablero un valor por defecto
    que representará una casilla sin minas"""
    tablero=[]
    for i in range(filas):
        tablero.append([])
        for j in range(columnas):
            tablero[i].append(valor)
    return tablero


def pistasSobreMinas(tablero):
    """Recibiendo un tablero, cambiará los elementos que no sean minas y serán sustituidos por un número que significará cuántas
    minas hay en sus casillas vecinas. Retornará el nuevo tablero"""
    for i in range(len(tablero)):   # Recorrido por filas
        for j in range(len(tablero[i])):    # Recorrido por columnas
            if tablero[i][j]!=" ":  ## Si el elemento no es mina...

                # Si el elemento no mina está en la esquina superior izquierda...
                if i==0 and j==0:
                    nuevoValor=0
                    for a in range(i+2): ## Recorrido de las filas
                        for b in range(j+2):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":    ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor

                # Si el elemento no mina está en la esquina superior derecha...
                if i==0 and j==len(tablero)-1:
                    nuevoValor=0
                    for a in range(i+2):  ## Recorrido de las filas
                        for b in range(j-1,len(tablero),1):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":   ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor

                # Si el elemento no mina está en la primera fila...
                if i==0 and j!=0 and j!=len(tablero)-1:
                    nuevoValor=0
                    for a in range(i,i+2,1):  ## Recorrido de las filas
                        for b in range(j-1,j+2,1):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":  ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor

                # Si el elemento no mina está en la última fila...
                if i==len(tablero)-1 and j!=0 and j!=len(tablero)-1:
                    nuevoValor=0
                    for a in range(i-1,i+1,1):  ## Recorrido de las filas
                        for b in range(j-1,j+2,1):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":  ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor

                # Si el elemento no mina está en la esquina inferior izquierda...
                if i==len(tablero)-1 and j==0:
                    nuevoValor=0
                    for a in range(i-1,len(tablero),1): ## Recorrido de las filas
                        for b in range(j+2):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":    ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor

                # Si el elemento no mina está en la primera columna...
                if i!=0 and i!=len(tablero)-1 and j==0:
                    nuevoValor=0
                    for a in range(i-1,i+2,1): ## Recorrido de las filas
                        for b in range(j+2):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":    ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor

                # Si el elemento no mina está en la última columna...
                if i!=0 and i!=len(tablero)-1 and j==len(tablero)-1:
                    nuevoValor=0
                    for a in range(i-1,i+2,1): ## Recorrido de las filas
                        for b in range(j-1,len(tablero),1):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":    ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor

                # Si el elemento no mina está en la esquina inferior derecha...
                if i==len(tablero)-1 and j==len(tablero)-1:
                    nuevoValor=0
                    for a in range(i-1,i+1,1): ## Recorrido de las filas
                        for b in range(j-1,j+1,1):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":    ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor

                # Si el elemento no mina está en el interior del tablero...
                if i!=len(tablero)-1 and j!=len(tablero)-1 and i!=0 and j!=0:
                    nuevoValor=0
                    for a in range(i-1,i+2,1): ## Recorrido de las filas
                        for b in range(j-1,j+2,1):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":    ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor
    return tablero


def comprobarFin(tableroDeBanderas,tableroDeMinas):
    """Recibe un tablero de banderas y un tablero de minas, y si en una posición hay bandera y no hay bomba, devuelve False porque el juego no termimó,
    y si hay bomba y no está marcada, tampoco termina"""
    for i in range(len(tableroDeBanderas)):
        for j in range(len(tableroDeBanderas[i])):
            if not(tableroDeBanderas[i][j]=="%" and tableroDeMinas[i][j]==" "):
                return False
    return True


valor=0   ## casillas vacías (sin minas)
filas=11    ## filas del tablero de juego
columnas=11     ## columnas del tablero de juego
minas="M"

# Creamos un tablero
Tablero=crearTablero(filas,columnas,valor)

# Al tablero creado le colocamos las minas
TableroConMinasVisibles=colocarMinas(Tablero,minas,30)

# Al tablero le ocultamos las minas
TableroConMinasNoVisibles=ocultarMinas(TableroConMinasVisibles)

# Al tablero le cambiamos los elementos que no son minas por pistas
TableroConPistas=pistasSobreMinas(TableroConMinasNoVisibles)

TableroBanderas=crearTablero(filas,columnas,"0")


# Mostramos por consola el tablero
mostrarTablero(TableroConPistas,TableroBanderas)

condición1=True
condición2=True

while condición1 and condición2:
    condición2=movimientoDelJugador(TableroConPistas,TableroBanderas,input("w,a,s,d para moverte; m para marcar, c para desmarcar, e para desactivar bomba: "))
    mostrarTablero(TableroConPistas,TableroBanderas)
    condición1=not(comprobarFin(TableroBanderas,TableroConMinasNoVisibles))


























