# módulo de nombre NOV23pr
# CLASE PRÁCTICA DEL 23/NOV (martes),24/NOV (Miércoles),
# 25/NOV (Jueves) y 3/DIC (Viernes) sobre LISTAS

# VAMOS A IMPLEMENTAR ALGUNAS FUNCIONES BÁSICAS DE LISTAS.
# LAS PROBAREMOS CON LISTAS DE enteros, PERO VALEN PARA
# LISTAS DE ELEMENTOS DE OTROS TIPOS: reales, strings,
# elementos mixtos (sería cosa de probarlas)

from math import pow,sqrt

#FUNCIÓN 1
def contar(l,x):
    """devuelve el número de elementos iguales a x en la
    lista l"""
    c=0
    for y in l:
        if y==x:
            c=c+1
    return c

lista1=[6,8,9,5,6,3,7,4,8,2,6,9,14]
print(contar(lista1,6))
print(contar(lista1,4))
print(contar(lista1,11))

lista2=[9,0,4,2,7,4,9,8,1,-3,20]



#FUNCIÓN 2
def quitaRepetidos(l):
    """Se le pasa una lista l (que puede tener elementos
    repetidos) y retorna  otra lista en la que los elementos
    de l no están repetidos.
    En definitiva, devuelve un conjunto de elementos"""
    lsal=[]
    for x in l:
        if not x in lsal:
            lsal.append(x)
    return lsal

#lista1=quitaRepetidos(lista1)
#print(lista1)
#print(sorted(lista1))
#lista2=quitaRepetidos(lista2)
#print(lista2)



#FUNCIÓN 3
def union(l1,l2):
    """recibe dos listas l1 y l2 sin elementos repetidos
    (en cada una de ellas) y retorna otra lista unión de
    l1 y l2 (los elementos que están en l1 or l2 sin repetir)
    en la lista de salida"""
    lsal=l1
    for x in l2:
        if not x in l1:
            lsal.append(x)
    return lsal

#listaUnion=union(lista1,lista2)
#print(listaUnion)
#print(sorted(listaUnion))



#FUNCIÓN 4
def interseccion(l1,l2):
    """recibe dos listas l1 y l2 sin elementos repetidos
    (en cada una de ellas) y retorna otra lista intersección de
    l1 y l2 (los elementos que están en l1 and l2 sin repetir)
    en la lista de salida"""
    lsal=[]
    for x in l1:
        if x in l2:  #intentar hacer esto con un bucle
            lsal.append(x)
    return lsal
#listaInter=interseccion(lista1,lista2)
#print(listaInter)
#print(sorted(listaInter))



#FUNCIÓN 5
def diferencia(l1,l2):
    """recibe dos listas l1 y l2 sin elementos repetidos
    (en cada una de ellas) y retorna otra lista diferencia
    l1-l2 (los elementos que están en l1 y no están en l2)"""
    lsal=[]
    for x in l1:
        if not x in l2:
            lsal.append(x)
    return lsal

#listaDif=diferencia(lista2,lista1)
#print(listaDif)
#print(sorted(listaDif))



#FUNCIÓN 6
def eliminar1(l,x):
    """se le pasa una lista l y un posible elemento x de la
    lista y retorna otra lista donde está eliminado el
    elemento x (tantas veces como aparezca)"""
    lsal=[]
    for y in l:
        if x!=y:
            lsal.append(y)
    return lsal

#lista1=[3,3,3,8,3,3,3]
#lista2=eliminar1(lista1,2)
#lista2=eliminar1(lista1,3)
#print(lista2)


#FUNCIóN 7
def eliminar2(l,x):
    """se le pasa una lista l y un posible elemento x de
    la lista y sobre la misma lista l hay que eliminar
    los elementos de valor x que haya)"""
###PRIMER INTENTO FRUSTRADO
#    for y in l:
#        if y==x:
#            l.remove(y)
#        print(l)
###SEGUNDO INTENTO FRUSTRADO
#    for i in range(len(l)):
#        if l[i]==x:
#            l.pop(i)

###TERCER INTENTO  BUENO
#    for y in l[::-1]:
#        if y==x:
#           l.remove(y)

###CUARTO INTENTO  BUENO
#    for i in range(len(l)-1,-1,-1):
#        if l[i]==x:
#            l.pop(i)

##lista1=[3,3,3,8,3,3,3]
##eliminar2(lista1,8)
##print(lista1)



#FUNCIÓN 8
def menorMayor(l):
    """recibe una lista no vacía (precondición) de elementos
    comparables y retorna las posiciones del menor y del mayor
    (en ese orden). En caso de elementos repetidos devuelve
    la última posición"""
    ma=l[0]
    mi=l[0]
    posmi=0
    posma=0
    for i in range(len(l)): ##for x in l  OJO!
        if l[i]<=mi: # <= es LIFO (última posición)
            mi=l[i]
            posmi=i
        if l[i]>ma:  # <= lo mismo que antes
            ma=l[i]
            posma=i
    return posmi,posma

#lista=["PEPE","JUANA","JUAN","PEPE"]
#res=menorMayor(lista)
#print(res)
#print("MENOR=",lista[res[0]],"POSICIÓN=",res[0])
#print("MAYOR=",lista[res[1]],"POSICIÓN=",res[1])



#FUNCIÓN 9
def posicionesDescendente(l,x):
    """recibe una lista l y un elemento x y retorna todas
    las posiciones (en orden descendente) en las que se
    encuentra x en la lista l"""
    lpos=[]
    for i in range(len(l)):
        if x==l[i]:
            lpos.insert(0,i)
    return lpos

#lista=[5,3,5,5,8,10,2,5,9,2,2,2]
#lista=[3,3,3,3,3,3,3]
#lista=[1,2,3,4,5,6]
#print (posicionesDescendente(lista,11))



#FUNCIÓN 10
def media(l):
    """recibe una lista de valores numéricos (enteros y/o reales)
    y retorna su media aritmética
    No funciona para lista vacía"""
    s=0
    for x in l:
        s=s+x
    return s/len(l)

#print(media(lista))



#FUNCIÓN 11
def varianza(l):
    """retorna la varianza de los elementos de l"""
    s=0
    m=media(l)
    for x in l:
        s=s+pow(x-m,2)
    return s/len(l)

#print(varianza(lista))



#FUNCIÓN 12
def desvTipica(l):
    return sqrt(varianza(l))

#print(desvTipica(lista))



#FUNCIÓN13
def moda(l):
    """recibe una lista de enteros no vacía y devuelve el que más
    abunda. En caso de empate, vale cualquiera"""
    cont=contar(l,l[0])
    mod=l[0]
    for x in l:
        nVeces=contar(l,x)
        if nVeces>cont:
            mod=x
            cont=nVeces
    return mod

####moda es 5 o el 2 (aparece 4 veces)
#mo=moda(lista)
#print("ELEMENTO=",mo," * VECES=",contar(lista,mo) )



#FUNCIÓN 14
def modaMultiple(l):
    """recibe una lista de enteros no vacía y devuelve el que más
    abunda. En caso de empate, los hay que devolver todos
    en cualquier orden"""
    nVeces=contar(l,moda(l))
    ls=[]
    for x in l:
        if contar(l,x)==nVeces and not x in ls:
            ls.append(x)
    return ls

####modaMultiple es [5,2]
#mo=modaMultiple(lista)
#print("ELEMENTOS=",mo," *  VECES=",contar(lista,mo[0]))



#FUNCIÓN 15
def mediana(l):
    """recibe una lista no vacía y devuelve el central o
    centrales, o sea, el que tiene tantos valores
    mayores él, como menores a él"""
    lord=sorted(l)
    if len(lord)%2==1:
        return [lord[len(l)//2]]
    else:
        return lord[len(l)//2-1],lord[len(l)//2]


####mediana: sería ordenar  con el sorted y devolver el n//2
#me=mediana(lista)
#if len(me)==1:
#    print("ELEMENTO MEDIANA por número impar=",me[0] )
#else:
#    print("DOS ELEMENTOS MEDIANAS por número par=",me[0],"y",me[1])



