import random
import math

def binario(n):
    """Recibe un número en base 10 y lo retorna en base 2"""
    div=2
    bas2=[]
    while 0<1:
        res=n%div
        coc=n//div
        if coc==0:
            bas2.append(res)
            break
        bas2.append(res)
        n=coc
    return bas2[::-1]

##print(binario(164))


# Escribir un rectángulo de asteriscos de i de largo y j de ancho

##i=-1
##j=-1
##while i<1:
##    i=int(input("Dame base >=1: "))
##while j<1:
##    j=int(input("Dame altura >=1: "))
##print()
##for y in range(i):
##    for x in range(j):
##        print("*",end=" ")
##    print()


# Devuelve la posición del máximo y mínimo de una lista

def posMayorMenor(l):
    """Recibe una lista de enteros y retorna, de ella, la posición del mayor elemento y del menor"""
    posMayor=0
    posMenor=0
    mayor=0
    menor=0
    for i in range(len(l)):
        if l[i]>mayor:
            mayor=l[i]
            posMayor=i
        if l[i]<menor:
            menor=l[i]
            posMenor=i
        return posMayor,posMenor


# Función que cree una lista de n enteros aleatorios en un rango determinado por parámetro

def crearListaEnteros(n,inf,sup):
    """Hace lo del enunciado"""
    ls=[]
    for i in range(n):
        ls.append(random.randint(inf,sup))
    return ls

##print(crearListaEnteros(5,1,9))


# Función que cree una lista de n reales aleatorios en un rango determinado por parámetro

def crearListaReales(n,inf,sup):
    """Hace lo del enunciado"""
    ls=[]
    for i in range(n):
        x=random.random()
        x=round(inf+(sup-inf)*x,3)
        ls.append(x)
    return ls

##print(crearListaReales(5,5,8))


# Función que cuenta el número de vocales en un fichero y retorna dicho número con cada vocal encontrada

def numeroVocales(f):
    """Hace lo del enunciado"""
    f1=open(f,'r')
    l=[]
    contA=0
    contE=0
    contI=0
    contO=0
    contU=0
    for linea in f1:
        l=linea.strip("\n").split(" ")
        for x in l:
            if "a" in x or "A" in x or "á" in x or "Á" in x:
                contA=contA+1
            if "e" in x or "E" in x or "é" in x or "É" in x:
                contE=contE+1
            if "i" in x or "I" in x or "í" in x or "Í" in x:
                contI=contI+1
            if "o" in x or "O" in x or "ó" in x or "Ó" in x:
                contO=contO+1
            if "u" in x or "U" in x or "ú" in x or "Ú" in x:
                contU=contU+1
    f1.close()
    print("VOCALES")
    print("Número de apariciones de la vocal 'a':",contA)
    print("Número de apariciones de la vocal 'e':",contE)
    print("Número de apariciones de la vocal 'i':",contI)
    print("Número de apariciones de la vocal 'o':",contO)
    print("Número de apariciones de la vocal 'u':",contU)
    print()


##numeroVocales('practica.txt')


def numeroConsonantes(f):
    """Hace lo mismo que la anterior función pero para las consonantes"""
    f1=open(f,'r')
    l=[]
    cons=0
    for linea in f1:
        l=linea.strip("\n").split(" ")
        for x in l:
            if "a" not in x or "A" not in x or "á" not in x or "Á" not in x:
                cons=cons+1
            if "e" not in x or "E" not in x or "é" not in x or "É" not in x:
                cons=cons+1
            if "i" not in x or "I" not in x or "í" not in x or "Í" not in x:
                cons=cons+1
            if "o" not in x or "O" not in x or "ó" not in x or "Ó" not in x:
                cons=cons+1
            if "u" not in x or "U" not in x or "ú" not in x or "Ú" not in x:
                cons=cons+1
    f1.close()
    print("CONSONANTES")
    print("Número de consonantes:",cons)
    print()


##numeroConsonantes("practica.txt")



# Función que permite escribir un fichero desde cero que no existe, en caso de existir, lo escribe de cero
# Termina la escritura en el fichero al pasar por teclado la palabra "fin"


def escribirNuevoFichero(f):
    """Hace lo del enunciado"""
    f1=open(f,'w')
    teclado=str(input("Línea del texto. Escribe fin para terminar: "))
    linea=teclado+"\n"
    while teclado!="fin":
        f1.write(linea)
        teclado=str(input("Línea del texto. Escribe fin para terminar: "))
        linea=teclado+"\n"
    f1.close()

##nombre=str(input("Nombre del fichero: "))
##escribirNuevoFichero(nombre+".txt")



def continuarFichero(f):
    """A partir de un fichero ya existente, se podrá continuar escribiendo en él.
    La escritura finaliza al introducir por teclado la palabra "fin" """
    f1=open(f,'a')
    teclado=str(input("Línea del texto. Escribe fin para terminar: "))
    linea="\n"+teclado+"\n"
    while teclado!="fin":
        f1.write(linea)
        teclado=str(input("Línea del texto. Escribe fin para terminar: "))
        linea=teclado+"\n"
    f1.close()

##continuarFichero("prueba1.txt")



def mostrarFichero(f):
    """A partir de un fichero existente, mostrará por consola su contenido"""
    f1=open(f,'r')
    for linea in f1:
        print(linea.strip("\n"))

##mostrarFichero("prueba1.txt")



# Funciones sobre matrices

def creaMatriz(filas,columnas,valor):
    """Recibe un número de filas y columnas que serán las dimensiones de la matriz rellenada con los elementos
    recibidos como valor. Retornará la matriz resultante"""
    matriz=[]
    for i in range(filas):
        matriz.append([valor]*columnas)
    return matriz


def muestraMatriz(m):
    """Recibe una matriz y la muestra por consola"""
    for i in range(len(m)):
        print()
        for j in range(len(m[0])):
            print(m[i][j],end=" ")


##m=creaMatriz(5,5,1)
##muestraMatriz(m)

def creaMatrizAleatorios(filas,columnas,inf,sup):
    """Hace lo mismo que la funcion creaMatriz pero la rellena de valores enteros aleatorios comprendidos en un intervalo
    acotado superiormente por sup e inferiormente por inf. Retorna la matriz resultante"""
    matriz=[]
    for i in range(filas):
        matriz.append([random.randint(inf,sup)]*columnas)
    return matriz

##m=creaMatrizAleatorios(8,8,0,100)
##muestraMatriz(m)





#####################################################################################################################################


####### OPERACIONES CON RANDOM #######

# Randint():

    # Con intervalo:
        # random.randint(extemo inferior del intervalo, extremo superior del intervalo)
        # EL INTERVALO QUE COGE ES [inf, sup], ES DECIR, INCLUYE LOS EXTREMOS DEL INTERVALO
        ##random.randint(inf,sup)

    # Sin intervalo:
        # random.randint()
        # DEVUELVE UN ENTERO ALEATORIO CUALQUIERA, ES DECIR, EL INTERVALO QUE COGE ES (-infinito, +infinito)
        ##random.randint()

# Random():

    # Con intervalo:
        # Extremo inferior + (extremo superior - extremo inferior) * random.random()
        # El intervalo que coge es [inferior, superior]

        # Ejemplo de uso:
            ##print(5.2+1.3*random.random())

    # Sin intervalo:
        # random.random()
        # DEVUELVE UN REAL CUALQUIERA CON PRECISIÓN DE 16 DECIMALES. LO PODEMOS REDONDEAR CON round (normalmente a 3 decimales)

        # Ejemplo de uso:
            ##print(round(random.random(),3))





####### FACTORIAL #######

# A partir de un número introducido por teclado, mostrar por consola su factorial

##n=-3
##while n<0:
##    n=int(input("Dame natural: "))
##i=1
##f=1
##while i<=n:
##    f=f*i
##    i=i+1
##print("El factorial de",n,"es",f)






####### PRIMOS #######
# Recuerda que un número es primo si tiene como divisores solo el 1 y él mismo #

# Escribir los numeros primos que hay en el intervalo [2..200]

##for i in range(2,201,1):
##    primo=True
##    for j in range(2,i):
##        if i%j==0:
##            primo=False
##    if primo:
##        print(i,end=" ")
##print("fin")





# Dado un número natural n, escribe un programa que clasifique dicho número en: perfecto, abundante, o, defectivo.
# Además, en este último caso, deberá indicarse si es o no primo.
# Definición: Un número natural se dice que es perfecto si es igual a la suma de todos sus divisores propios
# (exceptuando él mismo), abundante si la suma es mayor que él y defectivo si la suma es menor.

# Ejemplo de salida del programa:
#   El número 6 es perfecto (ya que 1 + 2 + 3 = 6)
#   El número 12 es abundante (ya que 1 + 2 + 3 + 4 + 6 > 12)
#   El número 11 es defectivo y primo (ya que 1 < 11)

##n=0
##while n<1:
##    n=int(input("Dame natural: "))
##s=0
##for i in range(1,n,1):
##    if n%i==0:
##        s=s+i
##if s==n:
##    print(n,"Es perfecto")
##elif s>n:
##    print(n,"Es abundante")
##elif s<n:
##    print(n,"Es defectivo y no primo")
##elif s==1:
##    print(n,"Es defectivo y primo")



# Dado un número natural n, escribe un programa para generar (escribir en pantalla) la secuencia de los n primeros números de Perrin.
# Los tres primeros números de esta secuencia son P(0)=3, P(1)=0 y P(2)=2 y el resto se obtienen en la forma:
# P(n) = P(n-2) + P(n-3) si n>2.
# Números de Perrin: 3, 0, 2, 3, 2, 5, 5, 7, 10, 12, 17, 22, 29 …

##n=-1
##while n<0:
##    n=int(input("Dame natural: "))
##P=[3,0,2]
##for i in range(3,n+1,1):
##    P.append((P[i-2])+(P[i-3]))
##print(P)





####### FIBONACCI #######

# Leer un entero n>=10 y escribir los números de Fibonacci <=n

##n=8
##while n<10:
##    n=int(input("Dame entero: "))
##x=0
##y=1
##z=x+y
##print(x,y,end=" ")
##while z<=n:
##    print(z,end=" ")
##    x=y
##    y=z
##    z=x+y



####### FUNCIÓN QUE CALCULA Y RETORNA EL NÚMERO e HASTA 1/n! #######

# La serie que determina dicho número es: 1+(1/1!)+(1/2!)+(1/3!)+...+(1/n!)

def nE(n):
    """Calcula y retorna el número e hasta 1/n!"""
    s=1
    for i in range(1,n+1):
        s=s+(1/math.factorial(i))
    return s

##print(math.e)
##print(nE(20))




####### FUNCIÓN SENO DE TAYLOR #######

# La serie que lo determina es: ((x*1)/1!) - ((x*3)/3!) + ((x*5)/5!) - ((x*7)/7!) ... x
#                              <---------------------------K SUMANDOS------------------->

def senTaylor(x,k):
    """Calcula el seno por Taylor del ángulo x con k sumandos"""
    s=0
    signo=1
    for i in range(1,1+k):
        s=s+signo*x**(2*i-1)/math.factorial(2*i-1)
        signo=signo*(-1)
    return s

##print(senTaylor(1,10))
##print(math.sin(1),math.sin(math.pi/2))



#####################################################################################################################################

# Dado un número natural n, escribir un programa que muestre todos sus divisores en la forma:
# Los divisores de 12 son: 1 2 3 4 6 12

##n=-1
##while n<0:
##    n=int(input("Dame natural: "))
##print("Los divisores de",n,"son:",end=" ")
##for i in range(1,n+1,1):
##    if n%i==0:
##        print(i,end=" ")


































































































