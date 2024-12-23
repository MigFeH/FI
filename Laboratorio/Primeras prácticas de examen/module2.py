
# Ejercicio 1

# Escribe una función que, dada una matriz tridimensional cuadrada, tome todos los valores de dicha matriz en el triángulo superior.
# Para borrar los valores anteriores, se les asignará 0. Esta función tiene que asegurarse de que la matriz recibida, es bidimensional y cuadrada.
# En caso de que esta condición no se cumpla, tiene que devolver la lista vacía. Posteriormente, escribe un programa que pruebe dicha función.

















# Ejercicio 2

# Escribe una función que, dada una lista de listas, devuelva como resultado otra lista de listas, donde

# la primera lista contenga los primeros elementos de las listas de entrada,
# la segunda lista contenga los segundos elementos de las listas de entrada,
# la tercera lista contenga los terceros elementos de las listas de entrada
# y así sucesivamente hasta terminar de procesar la lista más pequeña de todas las que se introdujeron.

# Posteriormente, escribe un programa que pruebe dicha función

##def entrelazaListas(l):
##    """Hace lo del enunciado"""
##    l1=[]
##    l2=[]
##    a=0
##    for i in range(len(l)):
##        for j in range(len(l[i])):
##
##
##            l1.append(l[i][a])
##        a=a+1
##    return l1
##
##print(entrelazaListas ([[1, 2, 3], [4, 5, 6]]))















# Ejercicio 3

# Escribe una función que, dada una cadena de caracteres que contiene números enteros separados por puntos y comas (;),
# devuelva una lista con los números enteros positivos que se encuentran dentro de ella.
# Posteriormente, escribe un programa que pruebe dicha función

def extraeNumerosPositivos(cad):
    """Hace lo del enunciado"""
    lista1=cad.split(";")
    lista2=[]
    for x in range(len(lista1)):
        if int(lista1[x])>0:
            lista2.append(lista1[x])
    return lista2

##print(extraeNumerosPositivos("1 ; -2; 3; -4; -5; 6"))





# Ejercicio 4

# Escribe una función que, dados una cadena de caracteres y un tamaño n entero positivo, devuelva una lista con los n-gramas que no contengan espacios
# que se pueden extraer de la lista de caracteres.

# Si el tamaño es 3, la función tiene que extraer 3-gramas, es decir, subcadenas de tamaño 3.
# Si el tamaño es 5, la función debe devolver 5-grams, es decir, subcadenas de tamaño 5.

# La función debe comproba que la cadena de caracteres no esté vacía, en caso contrario devolverá la lista vacía.
# Posteriormente, escribe un programa que pruebe dicha función



def extraerNGramas(cad):
    """Hace lo del enunciado"""
















































