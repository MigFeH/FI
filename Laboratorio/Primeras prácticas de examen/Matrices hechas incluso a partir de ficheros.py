# MÓDULO DIC2.py (Clase Teoría Jueves 2/DIC)

#  MATRICES RECTANGULARES CON LISTAS DE LISTAS
#  (ap.2.6.8 apuntes)

from random import randint,random

def crearMatriz(f,c,valor):
    """Va creando memoria para una matriz rectangular
    de f filas,c columnas y todos sus compenentes igual
    a valor. Al final retorna dicha matriz  """
    m=[]
    for i in range(f):
        m.append(c*[valor])
    return m

##m1=crearMatriz(4,3,3)
##print (m1)



def escribirMatriz(m):
    """Recibe una matriz rectangular m y la escribe por
    pantalla de forma clásica"""
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j],end="\t")
        print()
    print()

##m1=crearMatriz(2,3,"PEPE")
##escribirMatriz(m1)



def matrizValoresFichero(nombre,f,c):
    """Genera y devuelve una matriz f*c, con elementos
    enteros, leidos desde un fichero nombre"""
    m=crearMatriz(f,c,0)
    fich=open(nombre,'r')
    i=0
    for linea in fich:
        lista=linea.strip("\n").split()
        j=0
        for x in lista:
            m[i][j]=int(x)
            j=j+1
        i=i+1
    return m

##print("MATRIZ A=")
#a=matrizValoresFichero("zm1.txt",4,3)
##escribirMatriz(a)
##print()
##print("MATRIZ B=")
#b=matrizValoresFichero("zm2.txt",4,3)
##escribirMatriz(b)
##print()
##print("MATRIZ C=")
#c=matrizValoresFichero("zm3.txt",3,2)
##escribirMatriz(c)
##print()


def matrizEnterosAleatorios(f,c,inf,sup):
    """Genera y devuelve una matriz f*c, con elementos
    enteros en el rango [inf..sup] """
    m=crearMatriz(f,c,0)
    for i in range(f):
        for j in range(c):
            m[i][j]=randint(inf,sup)
    return m

##m4=matrizEnterosAleatorios(6,8,10,99)
##escribirMatriz(m4)



def matrizRealesAleatorios(f,c,inf,sup):
    """Genera y devuelve una matriz f*c, con elementos
    reales en el rango [inf..sup] """
    m=crearMatriz(f,c,1)
    for i in range(f):
        for j in range(c):
            m[i][j]=round(inf+(sup-inf)*random(),2)
    return m

##m5=matrizRealesAleatorios(3,4,10,20)
##escribirMatriz(m5)



def simetrica(m):
    """
    Si m es cuadrada retorna:
        True  si es simétrica
        False si no lo es
    Si m no es cuadrada retorna REPASA MATRICES """

    if len(m)!=len(m[0]):
        return "REPASA MATRICES"
    else:
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j]!=m[j][i]:
                    return False
        return True

##m6=matrizEnterosAleatorios(2,2,10,11)
##escribirMatriz(m6)
##print(simetrica(m6))
##print(simetrica(a))



def matrizTraspuesta(m):
    """Genera y devuelve la transpuesta de la recibida m"""
    if len(m)==len(m[0]):
        f=len(m)
        c=len(m[0])
        tras=crearMatriz(f,c,0)
        for i in range(len(m)):
            for j in range(len(m[i])):
                tras[i][j]=m[j][i]
        return tras
    else:
        print("La matriz no es cuadrada, no es posible hacer su traspuesta")

##matriz=matrizEnterosAleatorios(5,5,2,8)
##print("---Matriz original---")
##escribirMatriz(matriz)
##mtr=matrizTraspuesta(matriz)
##print("---Matriz traspuesta---")
##escribirMatriz(mtr)


def sumaMatrices(m1,m2):
    """Genera la matriz suma matricial m1+m2 y la devuelve-
    m1 y m2 han de ser de la misma dimensión f*c"""
    if len(m1)==len(m1[0]) and len(m2)==len(m2[0]) and len(m1)==len(m2) and len(m1[0])==len(m2[0]):
        m3=crearMatriz(len(m1),len(m1[0]),0)
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                m3[i][j]=m1[i][j]+m2[i][j]
        return m3
    else:
        print("Dimensiones de las matrices parámetro no válidas")

##msuma=sumaMatrices(a,b)
##escribirMatriz(msuma)
##msuma=sumaMatrices(a,c)
##escribirMatriz(msuma)



def productoMatrices(m1,m2):
    """genera la matriz producto matricial m1*m2 y lo devuelve
    Estudia si el producto se puede realizar (columnas de la
    primera es igual a filas de la segunda)
    y si no se puede devuelve NO"""
    f1=len(m1)
    c1=len(m1[0])
    f2=len(m2)
    c2=len(m2[0])
    if c1==f2:
        m3=crearMatriz(f1,c2,0)
        for i in range(f1):
            for j in range(c2):
                m3[i][j]=0
                for k in range (c1):
                    m3[i][j]=m3[i][j]+m1[i][k]*m2[k][j]
        return m3
    else:
        return ("NO")

#res=productoMatrices(a,c)
#res=productoMatrices(sumaMatrices(a,b),c)
#res=productoMatrices(a,b)   # en este caso devuelve "NO"
#if res=="NO":
#    print("DIMENSIONES INCORRECTAS")
#else:
#    escribirMatriz(res)


#### A CONTINUACIÓN:
#### FUNCIONES YA HECHAS EN LA CLASE DE TEORÍA DEL 23/NOV
#### REPASARLAS


def posMinimo(m):
    """Devuelve la fila y columna donde está el mínimo de m
    En caso de empate, vale cualquiera"""
    p=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]>=p:
                p=m[i][j]
    minimo=p
    filaMinimo=0
    columnaMinimo=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]<=minimo:
                minimo=m[i][j]
                filaMinimo=i
                columnaMinimo=j
    return filaMinimo,columnaMinimo

##matriz=matrizEnterosAleatorios(4,4,7,22)
##escribirMatriz(matriz)
##print("Posición del mínimo:",posMinimo(matriz))

def posMaximo(m):
    """Devuelve la fila y columna donde está el máximo de m
    En caso de empate vale cualquiera"""
    maximo=0
    filaMaximo=0
    columnaMaximo=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]>=maximo:
                maximo=m[i][j]
                filaMaximo=i
                columnaMaximo=j
    return filaMaximo,columnaMaximo

##matriz=matrizEnterosAleatorios(4,4,7,22)
##escribirMatriz(matriz)
##print("Posición del máximo:",posMaximo(matriz))


def suma(m):
    """Devuelve la suma de todos los elementos de m
    (m es de valores enteros y/o reales)"""
    s=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            s=m[i][j]+s
    return s

##matriz=matrizEnterosAleatorios(4,4,7,22)
##escribirMatriz(matriz)
##print("Suma de todos los elementos de la matriz:",suma(matriz))


def sumaFilas(m):
    """Devuelve una lista con la suma de cada fila de m
    (m es de valores enteros y/o reales)"""
    sumaFila=[]
    s=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            s=m[i][j]+s
        sumaFila.append(s)
        s=0
    return sumaFila

##matriz=matrizEnterosAleatorios(4,4,7,22)
##escribirMatriz(matriz)
##print(sumaFilas(matriz))


def sumaColumnas(m):
    """Devuelve una lista con la suma de cada columna de m
    (m es de valores enteros y/o reales)"""
    sumaColumna=[]
    s=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            s=m[j][i]+s
        sumaColumna.append(s)
        s=0
    return sumaColumna

##matriz=matrizEnterosAleatorios(4,4,7,22)
##escribirMatriz(matriz)
##print(sumaColumnas(matriz))
