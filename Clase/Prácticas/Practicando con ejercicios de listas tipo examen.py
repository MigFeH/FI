# Escriba una función que reciba como parámetros dos listas de cualquier tipo y que devuelva la distancia entre ambas.
# Esta distancia entre listas quedará definida como la suma de la diferencia entre longitudes de cada lista y el número de elementos distintos en cada posición.
# De esta manera tenemos que la distancia entre [1.9,1.4,1.2,0,1.7] y [1.7,1.4,0.1,0,1.7] es 2.







# Haga una función llamada extrae_negativos que reciba como parámetro una lista de números y extraiga de esa lista pasada como parámetro los números negativos y los devuelva en otra lista como resultado.
# Además debe eliminar estos números negativos de la lista original.

def extrae_negativos(l):
    """Hace lo del enunciado"""
    res=[]
    for i in l:
        if i not in res and float(i)<0:
            res.append(i)
    for i in range(0,len(l),1):
        if l[i]<0:
            l.pop(i)
    return l,res

## Ejemplo, si la lista antes de la llamada es [10,11,-7,4.5,-2,-2,6.3,8,-1],
## después de la llamada debe ser [10,11,4.5,6.3,8] y además la función debe devolver [-7,-2,-2,-1].
lista1=[10,11,-7,4.5,-2,-2,6.3,8,-1]
##print(extrae_negativos(lista1))





# Sin usar la función sorted,
# escriba una función booleana llamada ordenada, que reciba una lista homogénea de cualquier tipo y devuelva True si está ordenada crecientemente o False en caso contrario.
# Haga un pequeño programa de prueba. Ejemplos de uso:
# - Llamada con la lista [9,11,10,20], debe devolver False
# - Llamada con la lista ["Ana","Juan","Teresa"] debe devolver True

def ordenada(l):
    """Recibe una lista homogénea de cualquier tipo y retorna True si está ordenada o False en caso contrario"""
    for x in l:
        for y in l[l.index(x)+1:len(l):1]:
            if x<y:
                continue
            else:
                return False
    return True

lista2=[9,11,10,20]
lista3=["Ana","Juan","Teresa"]
##print(ordenada(lista2))
##print(ordenada(lista3))



# Haga una función llamada inserta_ceros, que reciba como parámetro una lista de números, y modifique esa lista insertando
# un cero delante de cada número negativo. La función no debe devolver nada.

def inserta_ceros(lista):
    """Hace lo del enunciado"""
    for x in range(len(lista)-1,-1,-1): ## se empieza al final de la lista PARA NO ALTERAR EL ORDEN
        if lista[x]<0:
            lista.insert(x,0)
    return lista

## Ejemplo, si la lista antes de la llamada es [10,11,-7,4.5,-2,-2,6.3,8,-1], después de la llamada debe ser [10,11,0,-7,4.5,0,-2,0,-2,6.3,8,0,-1].
## Haga un pequeño programa de prueba con estos datos para comprobar su correcto funcionamiento.

lista4=[10,11,-7,4.5,-2,-2,6.3,8,-1]
lista5=inserta_ceros(lista4)
print(lista5)













