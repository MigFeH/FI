# Ejercicio 2

# Haga una función llamada extrae_negativos que reciba como parámetro una lista de números y extraiga de esa lista pasada como parámetro los números negativos
# y los devuelva en otra lista como resultado. Además debe eliminar estos números negativos de la lista original.

# Ejemplo, si la lista antes de la llamada es [10,11,-7,4.5,-2,-2,6.3,8,-1], después de la llamada debe ser [10,11,4.5,6.3,8] y además la función debe devolver [-7,-2,-2,-1].

# Haga un pequeño programa de prueba con estos datos para comprobar su correcto funcionamiento.


def extrae_negativos(lista):
    """Hace lo del enunciado"""
    negativos=[]
    i=0
    while i<len(lista):
        if lista[i]<0:
            negativos.append(lista[i])
        i=i+1
    for x in negativos:
        lista.remove(x)
    return negativos



mi_lista=[10,11,-7,4.5,-2,-2,6.3,8,-1]
print("mi lista antes",mi_lista)
negativos=extrae_negativos(mi_lista)
print("mi lista después",mi_lista)
print("negativos",negativos)