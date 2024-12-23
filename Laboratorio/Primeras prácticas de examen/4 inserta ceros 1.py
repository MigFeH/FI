# Ejercicio 4

# Haga una función llamada inserta_ceros, que reciba como parámetro una lista de números, y modifique esa lista insertando un cero delante de cada número negativo.
# La función no debe devolver nada.

# Ejemplo, si la lista antes de la llamada es [10,11,-7,4.5,-2,-2,6.3,8,-1], después de la llamada debe ser [10,11,0,-7,4.5,0,-2,0,-2,6.3,8,0,-1].

# Haga un pequeño programa de prueba con estos datos para comprobar su correcto funcionamiento.



def inserta_ceros(lista):
    """Hace lo del enunciado"""
    for i in range(len(lista)-1,-1,-1):
        if lista[i]<0:
            lista.insert(i,0) ## inserta un elemento en una posición antes de la dada como parámetro

mi_lista=[10,11,-7,4.5,-2,-2,6.3,8,-1]
print("lista antes:",mi_lista)
inserta_ceros(mi_lista)
print("lista después:",mi_lista)