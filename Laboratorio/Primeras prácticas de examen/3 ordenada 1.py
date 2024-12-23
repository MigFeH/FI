# Ejercicio 3

# Sin usar la función sorted, escriba una función booleana llamada ordenada, que reciba una lista homogénea de cualquier tipo y devuelva True si está ordenada crecientemente o False en caso contrario.
# Haga un pequeño programa de prueba. Ejemplos de uso:

# - Llamada con la lista [9,11,10,20], debe devolver False
# - Llamada con la lista ["Ana","Juan","Teresa"] debe devolver True

def ordenada(lista):
    """Hace lo del enunciado"""
    for i in range(1,len(lista)):
        if lista[i]<lista[i-1]:
            return False
    return True


print(ordenada([9,11,10,20]))
print(ordenada(["Ana","Juan","Teresa"]))










