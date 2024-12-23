# Ejercicio 1

# Escriba una función que reciba como parámetros dos listas de cualquier tipo y que devuelva la distancia entre ambas.
# Esta distancia entre listas quedará definida como la suma de la diferencia entre longitudes de cada lista y el número de elementos distintos en cada posición.
# De esta manera tenemos que la distancia entre [1.9,1.4,1.2,0,1.7] y [1.7,1.4,0.1,0,1.7] es 2.

# Entre [1.5,0.4,1.3,0] y [0.2,0.4,1.3,0] es 1.
# Entre [1.9,1.7,0,1.9,1.4] y [1.2,2,0.4,1.1,0] es 5.
# Entre [0.2,0,0.1,0,1.1,0.6,0,1.7] y [0.2,0,0.1,0,1.1,1.1,1.4] es 3.

# Haga un pequeño programa para verificar su correcto funcionamiento.

## (len a - len b) + numero de elementos distintos en cada posicion ##

def distancia(a,b):
    """Hace lo del enunciado"""
    long=len(a)-len(b)
    distintos=0
    if len(a)<len(b):
        for i in range(len(a)):
            if a[i]!=b[i]:
                distintos=distintos+1
    elif len(b)<len(a):
        for i in range(len(b)):
            if b[i]!=a[i]:
                distintos=distintos+1
    else:
        for i in range(len(a)):
            if a[i]!=b[i]:
                distintos=distintos+1
    return (long+distintos)

print(distancia([1.5,0.4,1.3,0],[0.2,0.4,1.3,0]))
print(distancia([1.9,1.7,0,1.9,1.4],[1.2,2,0.4,1.1,0]))
print(distancia([0.2,0,0.1,0,1.1,0.6,0,1.7],[0.2,0,0.1,0,1.1,1.1,1.4]))

print(distancia([1.9,1.4,1.2,0,1.7],[1.7,1.4,0.1,0,1.7]))
print(distancia([0.2,0,0.1,0,1.1,0.6,0,1.7],[0.2,0,0.1,0,1.1,1.1,1.4]))