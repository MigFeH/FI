
##Guión listas II (trabajar sobre él)
##Clase de prácticas sobre cadenas/ficheros

def nuestra_strip(cad,x):
    """Que devuelva otra cadena que sea cad, pero
    quitando los caractéres x por ambos extremos
    y programarlo"""
# programarlo
    res=[]
    y=str(x)
    for linea in cad:
        res.append(linea)
    while len(res)!=0 and res[len(res)-1]==y:
        res.pop(len(res)-1)
    while len(res)!=0 and res[0]==y:
        res.pop(0)
    cadf=''.join(res)
    return cadf

def nuestra_rstrip(cad,x):
    """Que devuelva otra cadena que sea cad, pero
    quitando los caractéres x por el extremo derecho
    y programarlo"""
# programarlo
    res=[]
    y=str(x)
    for linea in cad:
        res.append(linea)
    while len(res)!=0 and res[len(res)-1]==y:
        res.pop(len(res)-1)
    cadf=''.join(res)
    return cadf

def nuestra_lstrip(cad,x):
    """Que devuelva otra cadena que sea cad, pero
    quitando los caractéres x por el extremo izquierdo
    y programarlo"""
# programarlo
    res=[]
    y=str(x)
    for linea in cad:
        res.append(linea)
    while len(res)!=0 and res[0]==y:
        res.pop(0)
    cadf=''.join(res)
    return cadf

##recuerda que los strings son inmutables, tendremos que hacer una nueva cadena que se rellene con los elementos de la cadena parámetro

##n2="*****HOLA *Y* ADIOS**"
##print(n2)
##print(nuestra_strip(n2,"*")) ##quita los "*" tanto de la izquierda como de la derecha de la cadena entera (principio y fin de la cadena)
##print(nuestra_rstrip(n2,"*")) ##quita los "*" solo del principio de la cadena
##print(nuestra_lstrip(n2,"*")) ##quita los "*" solo del final de la cadena

## si damos de entrada una cadena "*****" nos tienen que devolver los tres ""




###Creación de ficheros.txt
##Zanimales1
##Zanimales2
##Zanimales3

# EJERCICIO 1

## Trabajo sobre fichero a nivel de carácter
def contarLetras(nombre,letra):
    """Se pasa nombre de un fichero y una letra y se ha devolver el número de letras total de fichero
    (excluidos blancos y saltos de línea) y el número de veces que aparece la letra"""
    f1=open(nombre,'r')
    y=str(letra)
    letrasTotales=0
    letrasABuscar=0
    lres=[]
    for linea in f1:
        lres=linea.strip("\n").split(" ")
        cadena=''.join(lres)
        for x in cadena:
            letrasTotales=letrasTotales+1
            if x==y:
                letrasABuscar=letrasABuscar+1
    f1.close
    return letrasTotales, letrasABuscar



##    contTotal=0
##    contLetra=0
##    f=open(nombre,"r")
###    lista=f.readlines() ##trae una lista de strings en la que cada línea es cada línea del fichero
##    for linea in f: ## linea son los elementos del fichero, lineas... dentro de las lineas hay otros elementos x
##        linea=linea[0:len(linea)-1:1]
##        # también valdría linea.strip("\n") o linea.strip()
##        # print(linea)
##        for x in linea:
##            if x!=" ":
##                contTotal=contTotal+1
##            if x==letra:
##                contLetra=contLetra+1
##    f.close ## primero cerramos (siempre antes de retornar)
##    return contTotal,contLetra  ## despues retornamos (siempre después de cerrar)

##nom=input("NOMBRE DEL FICHERO SIN EXTENSIÓN: ")
##nom=nom+".txt"
##le=input("LETRA A CONTAR: ")
##res=contarLetras(nom,le)
##print(res) ## escribirá la dupla al devolver dos cosas, devuelve en forma de lista (devuelve el número de letras total y el número de veces que se repite la letra parámetro)
##print(round(100*res[1]/res[0],2)) ## escribirá en porcentaje el % de la presencia de la letra que se repite con respecto al número total de letras


# EJERCICIO 2

#### Escribir una función que reciba de un fichero
#### y escriba QUÉ VOCAL MINÚSCULA APARECE MÁS
#### VECES EN EL FICHERO Y CUÁNTAS VECES APARECE?
#### En CASO DE EMPATE, HAY QUE PONERLAS TODAS

def vocalesModa(nombre):
    """Hace lo del enunciado"""
    f1=open(nombre,'r')
    vocales=["a","e","i","o","u"]
    lres=[]
    lrep=[]
    numA=0
    numE=0
    numI=0
    numO=0
    numU=0
    for linea in f1:
        lres=linea.strip("\n").split(" ")
        for x in lres:
            for y in x:
                if y==vocales[0]:
                    numA=numA+1
                if y==vocales[1]:
                    numE=numE+1
                if y==vocales[2]:
                    numI=numI+1
                if y==vocales[3]:
                    numO=numO+1
                if y==vocales[4]:
                    numU=numU+1
    lrep1=max(numA,numE,numI,numO,numU)
    lrep2=[numA,numE,numI,numO,numU]
    lrep3=[]
    for x in lrep2:
        if x==lrep1:
            lrep3.append(x)
        else:
            lrep3.append(0)
    for x in range(len(vocales)):
        if lrep3[x]!=0:
            print(vocales[x],lrep3[x])
    f1.close
    return lrep3



##    vocales=["a","e","i","o","u"]
##    contVocales=[]
##    for x in vocales: ## x son los elementos de la lista vocales
##        contVocales.append(contarLetras(nombre,x)[1]) ## el número total de letras está almacenado en una lista en contarLetras junto con número de veces que una letra se repite (el nº de letras está almacenado en la posición [0] y el nª de veces que se repite la letra está almacenado en [1]
##    print(contVocales)
##    ma=max(contVocales) ## si no nos dejasen usar max, se haría con un for para hallar el elemento máximo (ya lo hicimos en clase, repásalo)
##    print("VOCALES MAYORITARIAS")
##    for i in range(len(vocales)): ## (nivel de posición)
##        if contVocales[i]==ma:
##            print(vocales[i],"VECES= ",ma)

##nom=input("NOMBRE DEL FICHERO SIN EXTENSIÓN: ")
##nom=nom+".TXt"
##vocalesModa(nom)


# EJERCICIO 3

def contarPalabras(nombre,palabra):
    """Pasan nombre de un fichero y una palabra y se ha de devolver el
    número de veces que está la palabra en el fichero"""
    f1=open(nombre,'r')
    y=str(palabra)
    cont=0
    for linea in f1:
        linea=linea.strip("\n").split(" ")
        for x in linea:
            if x==y:
                cont=cont+1
    f1.close
    return cont




##    cont=0
##    f=open(nombre,"r")
##    # hacedlo con f.readlines()
##    for linea in f: ## el for se ejecutará tantas veces como lineas tenga el fichero
##        lista=linea[:len(linea)-1:].split(" ") ## lista tendrá como elementos los elementos de cada línea
##        ## usamos el operador de corte para evitar el salto de línea
##        ## el split transforma de cadena a lista!!!... por defecto toma los caractéres blancos(" "); por defecto elimina los tabuladores, saltos de línea y espacios
##        # también linea.strip().split()
##        #print(lista)
##        for x in lista:
##            if x==palabra:  ## 'oso\n' != 'oso'
##                cont=cont+1
##    f.close()
##    return cont

##nom=input("NOMBRE DEL FICHERO SIN EXTENSIÓN: ")
##nom=nom+".TXt"
##pa=input("Animal? ")
##print(contarPalabras(nom,pa))


# EJERCICIO 4

#### ¿QUÉ PALABRA (animal) APARECE MÁS VECES EN UN FICHERO
#### Y CUÁNTAS VECES APARECE?
#### EN CASO DE EMPATE, HAY QUE PONERLOS TODOS LOS ANIMALES
#### ORDENADOS ALFABÉTICAMENTE


def modaAnimales(nombre):
    """Retorna del fichero nombre el animal que más veces se repite y,
    en caso de repetirse más de un animal con el mismo número de repeticiones,
    retorna todos ellos"""
    f1=open(nombre,'r')
    animales=[]
    l=[]
    n=[]
    for linea in f1:
        l=linea.strip("\n").split(" ")
        for x in l:
            if x not in animales:
                animales.append(x)
                n.append(0)
        for i in l:
            if i in animales:
                n[animales.index(i)]=n[animales.index(i)]+1
    m=max(n)
    for x in range(len(n)):
        if n[x]==m:
            print(animales[x])
    f1.close


nom=input("NOMBRE DEL FICHERO SIN EXTENSIÓN= ")
nom=nom+".TXt"
modaAnimales(nom)