import math
import random

# Escribir una función en lenguaje Python que reciba como parámetro un número n
# y retorne el sumatorio de los n primeros número pares.

##n = int(input("Introduzca número: "))
##
##while(n <= 0):
##    n = int(input("Introduzca número: "))
##
##b = 0
##for i in range(2,n + 1,2):
##    b = b + i
##
##print("El sumatorio de los ",n," primeros números pares es de: ",b, end = '\n')


##for i in range (1,n+1, 1):
##    print (i+1,end=" " )
##
##i = 1
##while(i < n+1):
##    print (i+1,end=" " )
##    i = i + 1


##def cambiaVocales(l):
##    """Recibe una lista de caracteres y cambia cada letra ‘a’ por el carácter
##    ‘e’ y cada letra ‘e’ por el carácter ‘i’"""
##    for i in range(len(l)):
##        if(l[i] == 'a'):
##            l[i] = 'e'
##        elif(l[i] == 'e'):
##            l[i] = 'i'
##
##l = ['a','e','i','o','u']
##print(l)
##cambiaVocales(l)
##print(l)


##def cálculoMRUA(pos, vinicial, aceleracion, tiempo):
##    """ Recibe la posición inicial de un objeto, su velocidad y su aceleración
##    como datos de entrada, e imprime la posición de dicho objeto tras un tiempo,
##    también tomado como dato de entrada """
##
##    res = pos + (vinicial * tiempo) + ((1/2) * aceleracion * (tiempo ** 2))
##
##    print("Posición inicial (m): ", pos, end = '\n')
##    print("Velocidad inicial (m/s): ", vinicial, end = '\n')
##    print("Aceleración (m/s^2): ", aceleracion, end = '\n')
##    print("Tiempo (s): ", tiempo, end = '\n')
##    print("La posición del objeto tras ", tiempo, "s es ", round(res, 2), "m")
##
##
##cálculoMRUA(25,-3.2, 2.35, 10.5)


##def pitágoras(cateto1, cateto2):
##    """ Recibe dos parámetros que son las longitudes de los catetos de un
##    triángulo rectángulo (suponemos que los valores introducidos son válidos)
##    e imprime por pantalla la longitud de la hipotenusa usando dos posiciones
##    decimales """
##
##    res = sqrt((cateto1 ** 2) + (cateto2 ** 2))
##
##    print("Longitud del primer cateto: ", cateto1, end = '\n')
##    print("Longitud del segundo cateto: ", cateto2, end = '\n')
##    print("La longitud de la hipotenusa es ", round(res, 2), end = '\n')
##
##pitágoras(3.15, 8.9)


##def binario_hexadecimal(entero):
##    """ Recibe un número entero e imprime su representación binaria y su
##    representación hexadecimal (Suponemos que todos los valores introducidos por
##    el usuario son válidos) """
##
##    binario = bin(entero)
##    hexadecimal = hex(entero)
##
##    print("La representación binaria de", entero, "es", binario, end = '\n')
##    print("La representación hexadecimal de", entero, "es", hexadecimal, end = '\n')
##
##
##n = int(input("Introduce un número entero: "))
##
##while(n < 0):
##    n = int(input("Introduce un número entero: "))
##
##binario_hexadecimal(n)


##def media_y_desviación_típica(x1, x2, x3):
##    """ Recibe tres valores numéricos y calcula e imprime por pantalla la media
##    y desviación típica calculada con los valores numéricos recibidos (Suponemos
##    que los valores de entrada son válidos) """
##
##    sumatorio = x1 + x2 + x3
##    sumatorio_al_cuadrado = (x1 ** 2) + (x2 ** 2) + (x3 ** 2)
##
##    media = sumatorio / 3
##
##    varianza = (sumatorio_al_cuadrado / 3) - media ** 2
##
##    desviación = math.sqrt(varianza)
##
##    print("La media es", round(media, 2), "y la desviación típica es", round(desviación, 2), end = '\n')
##
##v1 = float(input("Introduce el primer valor: "))
##
##if(v1 < 0.0):
##    v1 = float(input("Introduce el primer valor: "))
##
##v2 = float(input("Introduce el segundo valor: "))
##
##if(v2 < 0.0):
##    v2 = float(input("Introduce el segundo valor: "))
##
##v3 = float(input("Introduce el tercer valor: "))
##
##if(v3 < 0.0):
##    v3 = float(input("Introduce el tercer valor: "))
##
##media_y_desviación_típica(v1, v2, v3)



# Escriba un programa que pida palabras por teclado. El programa finalizará
# cuando se introduzca la cadena vacía y en ese momento mostrará como resultado
# el número de veces que se ha introducido una palabra idéntica a la anterior.
# No se pueden emplear listas.

# Ejemplo: con la entrada de "esto", "es", "una", "prueba", "es" el programa
# debe mostrar un 1 como resultado puesto que "es" se repite una vez de forma
# consecutiva.

##ar = ""
##cont = 0
##while(0 < 1):
##    cad = str(input("Introduzca cadena. Introduzca la vacía para finalizar: "))
##    if(cad != ""):
##        if(cad in ar):
##            cont = cont + 1
##        ar = ar + cad
##    else:
##        print("Contador de palabras repetidas:", cont - 1)
##        break


# Dadas dos listas de palabras, se desea filtrar en la primera las palabras
# que cumplan unas determinadas condiciones.

# Se pide escribir la función filtrar(A,B,v) que recibe como parámetros dos
# listas de palabras (A y B) y un valor booleano.

# Si el valor es True, la función debe eliminar de A las palabras que están
# contenidas en B. En caso contrario debe eliminar de A las palabras que no
# están en B.

# En ambos casos se eliminarán también las palabras que tengan tres o menos
# caracteres. Observe que la función no debe devolver ningún valor sino
# modificar la lista A eliminando los elementos mencionados.

##def filtrar(A,B,v):
##    """ Recibe dos listas de palabras (A y B) y un valor booleano (v).
##    Si el valor es True, la función elimina de A las palabras que están
##    contenidas en B. En caso contrario elimina de A las palabras que no
##    están en B.
##    En ambos casos se eliminarán también las palabras que tengan tres o menos
##    caracteres. """

##    if(v): # elimina de A las palabras que estan en B
##        for i in range(len(B) - 1, -1, -1):
##            for j in range(len(A) - 1, -1, -1):
##                if(B[i] == A[j]):
##                    A.pop(j)
##                if(len(A[j]) <= 3):
##                    A.pop(j)
##    else: # elimina de A las palabras que NO estan en B
##        for i in A:
##            if(i not in B):
##                A.remove(i)
##            if(len(i) <= 3):
##                A.remove(i)


##A = ["hola", "adios", "chao", "hola", "buenas"]
##B = ["hola", "buenas", "adios"]
##v1 = True
##v2 = False

##print("Lista A sin filtrar:", A)
##print("Lista B sin filtrar:", B)
##print()

####filtrar(A,B,v1)
##filtrar(A,B,v2)

##print("Lista A tras filtrar:", A)
##print("Lista B tras filtrar:", B)


# Programa que pida un número tras otro hasta introducir 0, y que entonces
# devuelva el mayor número introducido y el menor (0 no incluido).
# No usar listas.

##n = int(input("Introduce número. Introducir el 0 para finalizar: "))
##low = n
##high = n
##while(1 != 0):
##    n = int(input("Introduce número. Introducir el 0 para finalizar: "))
##    if(n == 0):
##        break
##    if(n < low):
##        low = n
##    if(n > high):
##        high = n
##print("El mayor número introducido fue el:", high)
##print("El menor número introducido fue el:", low)


# Crear una función devuelve_enteros() que dada una lista de números como
# parámetro devuelva una lista como esa pero con todos los elementos positivos
# (es decir, que si tiene un -3.4 en la lista que devuelve tendrá un 3.4 y tal)

##def devuelve_enteros(l):
##    """ Recibe una lista de números y elimina en ella los números negativos """
##    for x in l:
##        if x < 0.0:
##            l.remove(x)
##
##l1 = [-34.0, 15, 5, -9]
##print("Lista antes de cambio:", l1)
##devuelve_enteros(l1)
##print("Lista después de cambio:", l1)


# Crear una función positiviza() que dada una lista de nums como parámetro
# modifique esa lista tal que todo num negativo pase a ser positivo
# (como lo de antes, - 3.4 pasa a 3.4)

##def positiviza(l):
##    """ Recibe una lista de números y cambia en ella los números negativos por
##    su equivalencia positiva """
##    for x in range(len(l)):
##        if l[x] < 0.0:
##            l[x] = -l[x]
##
##l1 = [-34.0, 15, 5, -9]
##print("Lista antes de cambio:", l1)
##positiviza(l1)
##print("Lista después de cambio:", l1)


# Programa que dadas las coordenadas de puntos en plano en formato (2.1,-1.2)
# en un fichero, que escriba en otro lo mismo y además su distancia al origen
# redondeada a 2 decimales

##def distancia_coordenadas(lectura, escritura):
##    """ Recibe el nombre de un fichero de coordenadas en formato (2.1,-1.2)
##    y escribe en otro fichero, cuyo nombre es también recibido, lo mismo además
##    de su distancia al origen redondeada a 2 decimales """
##    f1 = open(lectura,'r')
##    f2 = open(escritura,'w')
##
##    for x in f1:
##        lres = x.lstrip('(').strip(')\n').split(',')
##
##        cat1 = float(lres[0])
##        cat2 = float(lres[1])
##
##        cal = math.sqrt(math.pow(cat1,2) + math.pow(cat2,2))
##        line = "Coordenadas: " + x.strip('\n') + ". Distancia al origen: " + str(round(cal,2))
##        f2.writelines(line + '\n')
##
##    f1.close()
##    f2.close()
##
##distancia_coordenadas("coordenadas.txt","1.txt")


# Se pide desarrollar un programa en Python que, dados los valores de presión
# de los 4 neumáticos de un vehículo, indique cuáles de ellos se encuentran
# fuera del intervalo recomendado de presión de 2.5 ± 0.2 bar, por exceso o por
# defecto. Supón que todos los valores introducidos por el usuario son válidos.

##delizq = float(input("Introduce la presión del neumático delantero izquierdo (bar): "))
##delder = float(input("Introduce la presión del neumático delantero derecho (bar): "))
##
##trasizq = float(input("Introduce la presión del neumático trasero izquierdo (bar): "))
##trasder = float(input("Introduce la presión del neumático trasero derecho (bar): "))
##
##if(delizq < 2.3):
##    print("El neumático DELANTERO IZQUIERDO tiene PRESIÓN BAJA")
##
##if(delizq > 2.7):
##    print("El neumático DELANTERO IZQUIERDO tiene PRESIÓN ALTA")
##
##if(delder < 2.3):
##    print("El neumático DELANTERO DERECHO tiene PRESIÓN BAJA")
##
##if(delder > 2.7):
##    print("El neumático DELANTERO DERECHO tiene PRESIÓN ALTA")
##
##if(trasizq < 2.3):
##    print("El neumático TRASERO IZQUIERDO tiene PRESIÓN BAJA")
##
##if(trasizq > 2.7):
##    print("El neumático TRASERO IZQUIERDO tiene PRESIÓN ALTA")
##
##if(trasder < 2.3):
##    print("El neumático TRASERO DERECHO tiene PRESIÓN BAJA")
##
##if(trasder > 2.7):
##    print("El neumático TRASERO DERECHO tiene PRESIÓN ALTA")


# Escribe una función que reciba como parámetro el nombre del fichero y devuelva
# como resultado una lista con los números leídos del fichero. Aplica la función
# sum() de python sobre esta lista para averiguar la suma de todos los datos que
# has leído. Debe salirte 49195.

##def fichero_numeros(name):
##    """ Recibe el nombre de un fichero de números enteros y retorna una lista
##    con los números leídos del fichero """
##    f1 = open(name,'r')
##    lsal = []
##    for x in f1:
##        lsal.append(int(x.strip('\n')))
##
##    f1.close()
##    return lsal
##
##lista = fichero_numeros("datos.txt")
##print("Lista de los números del fichero:", lista)
##print()
##print("Sumatorio de los números de la lista:", sum(lista))


# Escribe código python para determinar el número total de alumnos

##def contador_alumnos(name):
##    """ Recibe el nombre de un fichero de texto con un nombre de alumno por
##    línea de texto y retorna el número de alumnos que hay en el fichero """
##    f1 = open(name,'r')
##    cont = 0
##    for x in f1:
##        cont = cont + 1
##    f1.close()
##    return cont

##print("El número de alumnos del fichero es de:",contador_alumnos("alumnos.txt"))

# Escribe una función que reciba dos parámetros: una línea leída del fichero y
# un apellido de persona, y la función debe retornar “True” si cualquiera de los
# dos apellidos de la persona coinciden con el apellido dado.

##def coincide_apellido(linea, apellido):
##    """ Recibe una línea del fichero de alumnos y un apellido y retorna True si
##    el apellido recibido coincide con el de la línea que describe los apellidos
##    y el nombre de un alumno, y retorna False en caso contrario """
##
##    aux = linea.split(',')
##    apellidos = aux[0].split(' ')
##
##    apellido1 = apellidos[0]
##    apellido2 = apellidos[1]
##
##    if((apellido == apellido1) or (apellido == apellido2)):
##        return True
##    return False

##print(coincide_apellido("Lopez Alvarez, Andres", "Lopez"))
##print(coincide_apellido("Lopez Alvarez, Andres", "Suarez"))
##print(coincide_apellido("Lopez Alvarez, Andres", "Andres"))

# Usando la función anterior, determina qué porcentaje de alumnos tiene
# “Fernandez” como alguno de sus dos apellidos (debe salirte el 15,256%)

##def contador_alumnos_mismo_apellido(name, apellido):
##    """ Recibe el nombre de un fichero de alumnos y contabiliza en este el
##    número de alumnos que tengan el mismo apellido, recibido tambien como
##    parámetro, ya sea primer apellido o segundo; y retorna la contabilización
##    de esos alumnos """
##
##    f1 = open(name,'r')
##    cont = 0
##    for x in f1:
##        res = coincide_apellido(x.strip('\n'), apellido)
##        if(res):
##            cont = cont + 1
##    f1.close()
##    return cont
##
##alumnos = contador_alumnos("alumnos.txt")
##alumnos_fernandez = contador_alumnos_mismo_apellido("alumnos.txt","Fernandez")
##
##porcentaje_alumnos_fernandez = round((alumnos_fernandez / alumnos) * 100, 3)
##print("El porcentaje de alumnos que tienen el apellido Fernandez es del:", porcentaje_alumnos_fernandez)


# Escriba una función cuenta_vocales(nombre, letra, veces) que a partir del
# nombre del fichero que se pasa como parámetro, escriba un fichero con la
# frecuencia de aparición de cada una de las vocales:
#
# a 24
# e 41
# i 16
# o 23
# u 8

def cuenta_vocales(leer, letra):
    """ Recibe el nombre de un fichero (leer) del que se lee una letra pasada
    por parámetro y retorna el número de veces que aparece esa vocal en el texto
    del fichero """
    f1 = open(leer,'r')
    cont = 0
    for x in f1:
        aux = x.strip('\n').split(" ")
        for y in aux:
            for z in y:
                if(letra == z):
                    cont = cont + 1
    f1.close()
    return cont

## print(cuenta_vocales("examen.txt", "a"))


##def escribe_vocales(escribir, vocales, veces):
##    """ Recibe el nombre de un fichero (escribir) en el que se escribirán una
##    lista de vocales (vocales) con sus apariciones (veces), ambas recibidas como
##    parámetros """
##    f1 = open(escribir,'w')
##    for x in range(len(vocales)):
##        f1.writelines(str(vocales[x]) + " " + str(veces[x]) + '\n')
##    f1.close()
##
##
##vocales = ['a','e','i','o','u']
##veces = []
##for x in vocales:
##    veces.append(cuenta_vocales("examen.txt",x))
##
##escribe_vocales("salida_examen.txt",vocales,veces)

# Haz una función que cree una matriz de enteros aleatorios en un rango [inf, sup]

##def crea_matriz(f,c,valor):
##    m = []
##    for i in range(f):
##        m.append(c * [valor])
##    return m
##
##def crea_matriz_enteros_aleatorios(f,c,inf,sup):
##    m = crea_matriz(f,c,0)
##    for i in range(f):
##        for j in range(c):
##            m[i][j] = random.randint(inf,sup)
##    return m
##
##def muestra_matriz(m):
##    """ Recibe una matriz y la muestra por consola """
##    for i in range(len(m)):
##        print()
##        for j in range(len(m[i])):
##            print(m[i][j], end = " ")
##
##matriz = crea_matriz_enteros_aleatorios(4,4,1,9)
##muestra_matriz(matriz)


##def crea_matriz(f,c,valor):
##    m = []
##    for i in range(f):
##        m.append(c * [valor])
##    return m

##def crea_matriz_reales_aleatorios(f,c,inf,sup):
##    m = crea_matriz(f,c,0)
##    for i in range(f):
##        for j in range(c):
##            v = random.random()
##            m[i][j] = round(inf + (sup - inf) * v, 1)
##    return m

##def muestra_matriz(m):
##    for i in range(len(m)):
##        print()
##        for j in range(len(m[i])):
##            print(m[i][j], end = " ")

##matriz = crea_matriz_reales_aleatorios(3,4,4,9)
##muestra_matriz(matriz)


##def matriz_valores_fichero(nombre,f,c):
##    """ Recibe el nombre de un fichero de valores y retorna una matriz de
##    dimensionas recibidas como parámetros (f y c) rellenada con los valores del
##    fichero """
##    m = crea_matriz(f,c,0)
##    f1 = open(nombre,'r')
##    i = 0
##    for x in f1:
##        linea = x.strip().split()
##        j = 0
##        for y in linea:
##            m[i][j] = int(y)
##            j = j + 1
##        i = i + 1
##    return m


def crecer_fichero(nombre):
    """ Recibe el nombre de un fichero y pide por teclado líneas a escribir en
    dicho fichero hasta que se introduce la cadena vacía para finalizar la
    escritura """
    f1 = open(nombre,'a')
    while(0 < 1):
        linea = str(input("Introduzca línea de texto. Introduzca la vacía para finalizar: "))
        if(linea != ""):
            f1.writelines(linea + '\n')
        else:
            break
    f1.close()

##crecer_fichero("crecimiento del fichero.txt")


def mostrar_fichero(nombre):
    """ Recibe el nombre de un fichero de texto y muestra por consola cada línea
    escrita de este """
    f1 = open(nombre,'r')
    for x in f1:
        print(x.strip('\n'))
    f1.close()

##mostrar_fichero("crecimiento del fichero.txt")


# Escriba un programa que pida palabras por teclado. El programa finalizará
# cuando se introduzca la cadena vacía y en ese momento mostrará como resultado
# el número de veces que se ha introducido una palabra idéntica a la anterior.
# No se pueden emplear listas.

# Ejemplo: con la entrada de "esto", "es", "una", "prueba", "es" el programa
# debe mostrar un 1 como resultado puesto que "es" se repite una vez de forma
# consecutiva.


##def contar_palabras_repetidas():
##    """ Pide palabras por teclado y retorna el número de veces que se ha
##    repetido una palabra. El programa finaliza al introducir la cadena vacía """
##    cont = 0
##    cad = ""
##    while(0 < 1):
##        n = str(input("Introduzca palabra. Introduzca la vacía para finalizar: "))
##        if(n != ""):
##            if(n in cad):
##                cont = cont + 1
##            cad = cad + n + " "
##        else:
##            print("Número de palabras repetidas:",cont - 1)
##            break

##contar_palabras_repetidas()


# Escribe código python para determinar el número total de alumnos

def contador_alumnos_fichero(nombre):
    """ Recibe el nombre de un fichero de texto de alumnos matriculados en un
    año de la EPI de Gijón en la asignatura de Fundamentos de Informática y
    retorna el número de alumnos que hay en dicho fichero. Cada línea del
    fichero está destinada a un alumno matriculado """
    f1 = open(nombre,'r')
    cont = 0
    for x in f1:
        cont = cont + 1
    f1.close()
    return cont

##alumnos_totales = contador_alumnos_fichero("alumnos.txt")
##print("Número de alumnos totales:", alumnos_totales)


# Escribe una función que reciba dos parámetros: una línea leída del fichero y
# un apellido de persona, y la función debe retornar “True” si cualquiera de los
# dos apellidos de la persona coinciden con el apellido dado.

def coincide_apellido(linea, apellido):
    """ Recibe una línea leída del fichero de texto de los alumnos de la EPI
    y un apellido. Retorna True si el alumno de la línea tiene como primer o
    segundo apellido el pasado por parámetro. Retorna False en caso contrario """
    aux1 = linea.split(', ')
    if(apellido in aux1[0]):
        return True
    else:
        return False


# Usando la función anterior, determina qué porcentaje de alumnos tiene
# “Fernandez” como alguno de sus dos apellidos (debe salirte el 15,256%)

def numero_alumnos_mismo_apellido(nombre, apellido):
    """ Recibe el nombre de un fichero de alumnos de la EPI a leer y un apellido.
    Retorna el número de alumnos que coinciden en el primer o segundo apellido
    con el pasado por parámetro """
    f1 = open(nombre,'r')
    cont = 0
    for x in f1:
        linea = x.strip('\n')
        aux = coincide_apellido(linea, apellido)
        if(aux):
            cont = cont + 1
    f1.close()
    return cont

##alumnos_fernandez = numero_alumnos_mismo_apellido("alumnos.txt","Fernandez")
##print("Número de alumnos con mismo apellido (Fernandez):",alumnos_fernandez)

##porcentaje_fernandez = (alumnos_fernandez / alumnos_totales) * 100
##print("Porcentaje de alumnos Fernandez:", round(porcentaje_fernandez, 3))

# Escribe una función que reciba como parámetro una línea del fichero y retorne
# un entero que indique cuántas palabras tiene el nombre

def palabras_en_nombre(linea):
    """ Recibe una línea leída del fichero de texto de los alumnos de la EPI y
    retorna el número de palabras que compone el nombre del alumno """
    aux1 = linea.split(', ')
    aux2 = aux1[1].split(' ')
    cont = 0
    for x in aux2:
        cont = cont + 1
    return cont

##print(palabras_en_nombre("Lopez Alvarez, Andres"))


# Usando la función anterior, escribe un programa que cuente cuántos alumnos
# tienen nombre simple (1 palabra), cuántos de 2 palabras, etc.
# Puedes usar una lista para cada posible número de palabras, de modo que
#
# numero_palabras[1] por ejemplo almacene cuántos tienen nombre simple,
# numero_palabras[2] cuántos tienen 2 palabras, etc..
#
# Puedes asumir que no habrá nadie con más de 7 palabras y por tanto darle a la
# lista un tamaño prefijado de 8 elementos (ya que el elemento [0],
# aunque no lo usaremos, está ahí)

def contador_tipo_nombre_alumnos(nombre):
    """ Recibe el nombre de un fichero de texto de los alumnos de la EPI y
    retorna una lista con la cantidad de alumnos que tienen un nombre formado
    por una sola palabra, por dos, por tres, y hasta un máximo de 7 palabras
    incluidas """
    f1 = open(nombre, 'r')
    lsal = [0,0,0,0,0,0,0,0]
    for x in f1:
        palabras = palabras_en_nombre(x.strip('\n'))
        lsal[palabras] = lsal[palabras] + 1
    f1.close()
    return lsal

##print("Contador de tipos de nombres de los alumnos:", contador_tipo_nombre_alumnos("alumnos.txt"))


def crea_matriz(f,c,valor):
    """ Recibe un número de filas (f), columnas (c) y un valor que será el mismo
    para todos los valores de la matriz que se creará y retornará de dimensiones
    filas (f) x columnas (c) """
    m = []
    for i in range(f):
        m.append(c * [valor])
    return m


def escribir_matriz(m):
    """ Recibe una matriz y la muestra por consola """
    for i in range(len(m)):
        print()
        for j in range(len(m[i])):
            print(m[i][j], end = ' ')

##escribir_matriz(crea_matriz(3,5,5))


def crea_matriz_enteros_aleatorios(f,c,inf,sup):
    """ Recibe un número de filas (f) y de columnas (c), y creará con esas
    dimensiones una matriz filas (f) x columnas (c) cuyos valores que la
    rellenan serán números enteros aleatorios situados dentro de un rango
    delimitado por un valor mínimo (inf) y máximo (sup) que son recibidos como
    parámetros también. Finalmente, retorna la matriz resultante """
    m = crea_matriz(f,c,0)
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = random.randint(inf,sup)
    return m

##escribir_matriz(crea_matriz_enteros_aleatorios(4,7,2,9))


def crea_matriz_reales_aleatorios(f,c,inf,sup):
    """ Recibe un número de filas (f) y de columnas (c), y creará con esas
    dimensiones una matriz filas (f) x columnas (c) cuyos valores que la
    rellenan serán números reales (con 2 decimales) aleatorios situados dentro
    de un rango delimitado por un valor mínimo (inf) y máximo (sup) que son
    recibidos como parámetros también. Finalmente, retorna la matriz resultante """
    m = crea_matriz(f,c,0)
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = round(inf + (sup - inf) * random.random(),2)
    return m

##escribir_matriz(crea_matriz_reales_aleatorios(4,6,1,6))


def crea_matriz_por_teclado():
    """ Crea y retorna una matriz de dimensión filas (f) x columnas (c), que
    serán pedidas por teclado, rellenada con valores introducidos por teclado """
    f = int(input("Dame un número de filas positivo (mayor que 0) y entero para la matriz: "))
    c = int(input("Dame un número de columnas positivo (mayor que 0) y entero para la matriz: "))

    while((f <= 0) or (type(f) != type(0))):
        f = int(input("Dame un número de filas positivo (mayor que 0) y entero para la matriz: "))
    while((c <= 0) or (type(c) != type(0))):
        c = int(input("Dame un número de columnas positivo (mayor que 0) y entero para la matriz: "))

    m = crea_matriz(f,c,0)

    for i in range(len(m)):
        for j in range(len(m[i])):
            valor = int(input("Dame entero: "))
            m[i][j] = valor
    return m

##escribir_matriz(crea_matriz_por_teclado())


def crea_matriz_valores_fichero(f,c,nombre):
    """ Recibe un número de filas (f), de columnas (c) y el nombre de un fichero
    de texto con valores numéricos que rellenarán la matriz que se creará y
    retornará de dimensiones (f)x(c) """
    m = crea_matriz(f,c,0)
    f1 = open(nombre,'r')
    i = 0
    for x in f1:
        linea = x.strip('\n').split(' ')
        j = 0
        for y in linea:
            m[i][j] = int(y)
            j = j + 1
        i = i + 1
    f1.close()
    return m

##escribir_matriz(crea_matriz_valores_fichero(4,4,"valores matriz.txt"))


def comprobar_matriz_simetrica(m):
    """ Recibe una matriz y retorna False si no tiene mismo número de filas que
    de columnas, o si la matriz no es simétrica. Retorna true si la matriz es
    simétrica y cuadrada """
    if(len(m) != len(m[0])):
        return False
    for i in range(len(m)):
        for j in range(len(m[i])):
            if(m[i][j] != m[j][i]):
                return False
    return True


def matriz_traspuesta(m):
    """ Recibe una matriz y retorna su traspuesta """
    f = len(m)
    c = len(m[0])
    mt = crea_matriz(f,c,0)
    for i in range(len(m)):
        for j in range(len(m[i])):
            mt[j][i] = m[i][j]
    return mt


def nuestra_strip(cad,x):
    """Que devuelva otra cadena que sea cad, pero
    quitando los caractéres x por ambos extremos
    y programarlo"""
    # programarlo
    res = []
    y = str(x)
    for linea in cad:
        res.append(linea)
    while((len(res) != 0) and (res[0] == y)):
        res.pop(0)
    while((len(res) != 0) and (res[len(res)-1] == y)):
        res.pop(len(res)-1)
    cadf = ''.join(res)
    return cadf


def nuestra_rstrip(cad,x):
    """Que devuelva otra cadena que sea cad, pero
    quitando los caractéres x por el extremo derecho
    y programarlo"""
    # programarlo
    res = []
    y = str(x)
    for linea in cad:
        res.append(linea)
    while((len(res) != 0) and (res[len(res)-1] == y)):
        res.pop(len(res)-1)
    cadf = ''.join(res)
    return cadf


def nuestra_lstrip(cad,x):
    """Que devuelva otra cadena que sea cad, pero
    quitando los caractéres x por el extremo izquierdo
    y programarlo"""
    # programarlo
    res = []
    y = str(x)
    for linea in cad:
        res.append(linea)
    while((len(res) != 0) and (res[0] == y)):
        res.pop(0)
    cadf = ''.join(res)
    return cadf


##n2="*****HOLA *Y* ADIOS**"
##print(n2)
##print(nuestra_strip(n2,"*")) ##quita los "*" tanto de la izquierda como de la derecha de la cadena entera (principio y fin de la cadena)
##print(nuestra_rstrip(n2,"*")) ##quita los "*" solo del principio de la cadena
##print(nuestra_lstrip(n2,"*")) ##quita los "*" solo del final de la cadena



# suma de elementos en la posición par de una lista (recorrido por elementos)
##l = [2,3,-6,3,9,1]
##s = 0
##for x in l[::2]:
##    s = s + x

# suma de elementos en la posición par de una lista (recorrido por posiciones)
##l = [2,3,-6,3,9,1]
##s = 0
##for x in range(0,len(l),2):
##    s = s + l[x]


def posicion_menor_mayor_lista(lista):
    """ Recibe una lista de números y retorna la posición en la que se encuentra
    el número de valor más bajo y el número de valor más alto """
    pos_mayor = 0
    pos_menor = 0
    mayor = lista[0]
    menor = lista[0]
    for x in range(len(lista)):
        if(lista[x] < menor):
            menor = lista[x]
            pos_menor = x
        if(lista[x] > mayor):
            mayor = lista[x]
            pos_mayor = x
    return pos_menor, pos_mayor

##l = [2,3,-6,3,9,1]
##print(posicion_menor_mayor_lista(l))


def fibonacci(n):
    x = 1
    y = 1
    if(n <= 1):
        return 1
    for i in range(2,n+1):
        z = x + y
        x = y
        y = z
    return z


def linea(n,c):
    """ Dibuja, en consola, una línea de "n" caracteres "c" y al final salta
    de línea """
    for i in range(n):
        print(c, end = '')
    print()

##linea(6,'s')
##linea(8,'a')


def linea_orla(n,c1,c2):
    """ Dibuja, en consola, una línea de "n" caracteres, los caracteres del
    interior de la línea serán los c2, y los estremos de la línea serán los c1 """
    for i in range(n):
        if((i == 0) or (i == n-1)):
            print(c1, end = '')
            continue
        print(c2, end = '')
    print()

##linea_orla(10,'+','*')
##linea_orla(10,'1','0')


def rectangulo(n,m,c):
    """ Dibuja, en consola, un rectángulo de "n" filas y "m" columnas de
    caracteres "c" """
    for i in range(n):
        print()
        for j in range(m):
            print(c, end = ' ')
    print()

##rectangulo(3,2,'*')
##rectangulo(4,7,'-')


def rectangulo_orla(n,m,c1,c2):
    """ Dibuja, en consola, un rectángulo de "n" filas y "m" columnas en el que
    el exterior del rectángulo tiene escrito el carácter "c2" y el interior
    está escrito con "c1" """
    for i in range(n):
        print()
        for j in range(m):
            if((i == 0) or (i == n-1)):
                print(c2, end = ' ')
                continue
            if((j == 0) or (j == m-1)):
                print(c2, end = ' ')
                continue
            print(c1, end = ' ')
    print()

##rectangulo_orla(4,4,'1','0')
##rectangulo_orla(3,7,'*','+')
##rectangulo_orla(6,6," ","*")


def suma_filas_matriz(m):
    """ Recibe una matriz (m) y retorna una lista en la que cada posición tiene
    el valor de la suma de todos los valores de las columnas de cada fila de la
    matriz """
    res = []
    for i in range(len(m)):
        s = 0
        for j in range(len(m[i])):
            s = s + m[i][j]
        res.append(s)
    return res

##lBid = [[2,9,6,2],[3,-2,6,9],[6,8,-1,3]]
##print(suma_filas_matriz(lBid))


def suma_columnas_matriz(m):
    """ Recibe una matriz (m) y retorna una lista en la que cada posición tiene
    el valor de la suma de todos los valores de las filas de cada columna de la
    matriz """
    res = []
    for j in range(len(m[0])):
        s = 0
        for i in range(len(m)):
            s = s + m[i][j]
        res.append(s)
    return res

##print(suma_columnas_matriz(lBid))


def escribir_fichero(nombre):
    """ Recibe el nombre de un fichero de texto y lo imprime por consola """
    f1 = open(nombre, 'r')
    for x in f1:
        print(x.strip('\n'))
    f1.close()

##escribir_fichero("examen.txt")


def listaAFichero(l,nombre):
    """ Crea un fichero nombre con el contenido de una lista de números enteros.
    El fichero creado tendrá un número por línea """
    f1 = open(nombre,'w')
    for x in l:
        f1.write(str(x) + '\n')
    f1.close()



def escritura_en_consola():
    """ Pide cadenas de texto por teclado y las imprime en consola. La ejecución
    del programa finalizará al introducir la cadena "FIN" o "fin" """
    cad = str(input("Introduce cadena a escribir. Introduce FIN para finalizar: "))
    while(cad.lower() != "fin"):
        print(cad)
        cad = str(input("Introduce cadena a escribir. Introduce FIN para finalizar: "))
    print()

##escritura_en_consola()


# Escriba un programa que pida palabras por teclado. El programa finalizará
# cuando se introduzca la cadena vacía y en ese momento mostrará como resultado
# el número de veces que se ha introducido una palabra idéntica a la anterior.
# No se pueden emplear listas.

# Ejemplo: con la entrada de "esto", "es", "una", "prueba", "es" el programa
# debe mostrar un 1 como resultado puesto que "es" se repite una vez de forma
# consecutiva.


def contador_palabras_repetidas_por_teclado():
    """ Pide palaras por teclado y retorna el número de veces que se repite
    una palabra que se haya pasado por teclado. El programa finaliza al
    introducir la cadena vacía """
    n = str(input("Introduzca palabra. Introduzca cadena vacía para finalizar: "))
    cad = ""
    cont = 0
    while(0 < 1):
        if(n == ""):
            print("Número de palabras idénticas a las que se han introducido:", cont)
            break
        if(cad in n):
            cont = cont + 1
        cad = cad + n
        n = str(input("Introduzca palabra. Introduzca cadena vacía para finalizar: "))

##contador_palabras_repetidas_por_teclado()


def convertidor_a_binario_natural(n):
    """ Recibe un número natural y retorna su equivalencia en valor binario """
    aux = ""
    res = ""
    while(0 < 1):
        if((n // 2) == 0):
            aux = aux + str(n % 2)
            break
        aux = aux + str(n % 2)
        n = n // 2
    for x in aux[::-1]:
        res = res + x
    return res

##print("El 2 en binario es el: " + convertidor_a_binario_natural(2))
##print("El 2 en binario es el: " + convertidor_a_binario_natural(8))


def convertidor_a_binario_entero(n):
    """ Recibe un número entero y retorna si equivalencia en valor binario """
    res = convertidor_a_binario_natural(abs(n))
    if(n < 0):
        return complemento_a_2(res)
    return res


def complemento_a_2(cad):
    """ Recibe una cadena que representa un número entero negativo en binario
    natural y retorna una cadena con su equivalencia en binario entero """
    proc = False
    res = ""
    for x in cad[::-1]: ## recorremos por la derecha
        if(proc): ## si en la anterior ejecución se había encontrado el primer 1...
            if(int(x) == 1):
                res = "0" + res
                continue
            elif(int(x) == 0):
                res = "1" + res
                continue
        if(int(x) == 1): ## si se encuentra con el primer 1...
            proc = True
        res = x + res
    return res

##print(convertidor_a_binario_entero(7)) ## tiene que salir 111
##print(convertidor_a_binario_entero(-7)) ## tiene que salir 001
##print(convertidor_a_binario_entero(8)) ## tiene que salir 1000


# Los 5 primeros múltiplos de 7 acabados en 23

##mult = 7
##aux_1 = 1
##res = 0
##encontrados = 0
##l = []
##while(encontrados != 5):
##    res = mult * aux_1
##    if((res % 100) == 23):
##        encontrados = encontrados + 1
##        l.append(res)
##    aux_1 = aux_1 + 1
##
##print("Lista de los 5 primeros múltiplos de 7 acabados en 23:", l)


################################################################################

# Un fichero contiene en cada línea los tres vértices de un triángulo siendo el
# formato:

    # (x1,y1) (x2,y2) (x3,y3)

# donde (x1,y1) (x2,y2) (x3,y3) son las coordenadas cartesianas de los vértices.
# Haga un programa que calcule la suma de las áreas de todos los triángulos
# empleando la siguiente fórmula del área donde a, b y c son los tres lados del
# triángulo:

    # s = (a + b + c) / 2

    # area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Utilice a modo de ejemplo el siguiente contenido para el fichero. En este caso
# debe obtenerse un 4 como suma total de los tres triángulos. Nótese que puede
# haber espacios sobrantes.


def suma_areas_triangulos_fichero(nombre):
    """ Recibe el nombre de un fichero de texto en el que cada línea tiene
    escritas las coordenadas cartesianas de los tres vértices de un triángulo.
    Por cada línea hay un triángulo, y retorna la suma de las áreas de todos los
    triángulos del fichero de texto """
    f1 = open(nombre,'r')
    ret = 0
    for x in f1:
        linea = x.strip('\n')
        ret = ret + sacar_area_triangulo(sacar_lados(sacar_coordenadas(procesar_linea(linea))))
    f1.close()
    return ret


def sacar_area_triangulo(lados):
    """ Recibe una lista con las longitudes de los lados de un triángulo y
    retorna el área de dicho triángulo """
    s = (lados[0] + lados[1] + lados[2]) / 2
    return round((s * (s - lados[0]) * (s - lados[1]) * (s - lados[2])) ** 0.5, 2)


def sacar_lados(coordenadas):
    """ Recibe una lista de coordenadas de los puntos cartesianos de un
    triángulo y retorna una lista con las longitudes de los lados de dicho
    triángulo """
    punto1_x = coordenadas[0][0]
    punto1_y = coordenadas[0][1]

    punto2_x = coordenadas[1][0]
    punto2_y = coordenadas[1][1]

    punto3_x = coordenadas[2][0]
    punto3_y = coordenadas[2][1]

    lado_A = (((punto2_x - punto1_x) ** 2) + ((punto2_y - punto1_y) ** 2)) ** 0.5 ## 1-2
    lado_B = (((punto3_x - punto1_x) ** 2) + ((punto3_y - punto1_y) ** 2)) ** 0.5 ## 1-3
    lado_C = (((punto3_x - punto2_x) ** 2) + ((punto3_y - punto2_y) ** 2)) ** 0.5 ## 2-3

    return [lado_A,lado_B,lado_C]


def sacar_coordenadas(lista):
    """ Recibe una lista de carácteres procesados y retorna una lista con las
    coordenadas cartesianas de un triángulo """
    lsal = []
    cad = ''.join(lista)
    aux1 = cad.split(')(')
    for x in aux1:
        aux2 = x.split(',')
        coordenada_x = float(aux2[0])
        coordenada_y = float(aux2[1])
        lsal.append([coordenada_x,coordenada_y])
    return lsal


def procesar_linea(linea):
    """ Recibe la línea de un fichero de texto y retorna una lista con los
    caracteres de la línea pero en un formato determinado para procesar """
    aux1 = linea.lstrip('(').rstrip(')')
    aux2 = []
    for x in aux1:
        aux2.append(x)
    for x in aux2:
        if((x == '\t') or (x == ' ')):
            aux2.pop(aux2.index(x))
    return aux2


##print("RESULTADO FINAL:", suma_areas_triangulos_fichero("puntos triangulos.txt"))

################################################################################


# Retorna una lista con los caracteres iniciales de la lista: ["esto","es","una","prueba"]

# iniciales = [s[0] for s in ["esto","es","una","prueba"]]
##print(iniciales)

# Retorna una lista con los caracteres finales de la lista: ["esto","es","una","prueba"]

# finales = [s[-1] for s in ["esto","es","una","prueba"]]
##print(finales)


# numeros = ["123\n","68.5\n","-4.1\n","9.9\n"]
##numeros = [float(x) for x in numeros]
##print(numeros)


# lista = [50,-22,10,60,30,-18]

##negativos = [x for x in lista if x < 0]
##positivos = [x for x in lista if x > 0]

##negativos = [lista[x] for x in range(len(lista)) if lista[x] < 0]
##positivos = [lista[x] for x in range(len(lista)) if lista[x] > 0]

##print("Negativos:", negativos)
##print("Positivos:", positivos)



##valor = round(0 + (2 - 0) * random.random(),1)
##while((valor != 0.0) and (valor != 2.0)):
##    valor = round(0 + (2 - 0) * random.random(),1)
##print(valor)


################################################################################

# lista = [0,1,2,3,4,5,6,7,8,9]
##print("Resultado de lista[:]:",lista[:]) ## Se imprime toda la lista
##print("Resultado de lista[::]:", lista[::]) ## Se imprime toda la lista

##print("Resultado de lista[:-1]:", lista[:-1]) ## Se imprime toda la lista menos el último elemento
##print("Resultado de lista[-1:]:", lista[-1:]) ## Se imprime el último elemento

##print("Resultado de lista[::-1]:", lista[::-1]) ## Se imprime toda la lista invertida
##print("Resultado de lista[-1::]:", lista[-1::]) ## Se imprime el último elemento

##print("Resultado de lista[1:3]:", lista[1:3]) ## Se imprime el elemento de índice 1 y el anterior al de índice 3
##print("Resultado de lista[::2]:", lista[::2]) ## Se imprimen los elementos de la lista con un paso 2

##print("Resultado de lista[2::]:", lista[2::]) ## Se imprimen todos los elementos de la lista a partir del elemento de índice 2

################################################################################


# paises = ["China", "India", "Estados Unidos", "Indonesia"]
# poblaciones = [1391, 1364, 327, 264]
##print(list(zip(paises, poblaciones)))



##def creamos_matriz(f,c,v):
##    m = []
##    for i in range(f):
##        m.append(c * [v])
##    return m

##def creamos_matriz_enteros_aleatorios(f,c,inf,sup):
##    m = creamos_matriz(f,c,0)
##    for i in range(len(m)):
##        for j in range(len(m[0])):
##            m[i][j] = random.randint(inf,sup)
##    return m

##def creamos_matriz_reales_aleatorios(f,c,inf,sup):
##    m = creamos_matriz(f,c,0)
##    for i in range(len(m)):
##        for j in range(len(m[0])):
##            valor = round(inf + (sup - inf) * random.random(), 1)
##            m[i][j] = valor
##    return m

##def creamos_matriz_valores_fichero(f,c,n):
##    m = creamos_matriz(f,c,0)
##    f1 = open(n,'r')
##    i = 0
##    for x in f1:
##        linea = x.strip('\n').split(' ')
##        j = 0
##        for y in linea:
##            m[i][j] = int(y)
##            j = j + 1
##        i = i + 1
##    f1.close()
##    return m

##def mostramos_matriz_consola(m):
##    for i in range(len(m)):
##        print()
##        for j in range(len(m[0])):
##            print(m[i][j], end = ' ')
##    print()

##mostramos_matriz_consola(creamos_matriz_enteros_aleatorios(4,4,1,5))
##mostramos_matriz_consola(creamos_matriz_enteros_aleatorios(2,5,0,9))

##mostramos_matriz_consola(creamos_matriz_reales_aleatorios(5,3,0,2))
##mostramos_matriz_consola(creamos_matriz_reales_aleatorios(2,8,1,9))


##def crece_fichero(nombre):
##    """ Recibe el nombre de un fichero de texto, y continua una escritura en
##    dicho archivo sin afectar a lo que se haya escrito anteriormente. Si el
##    nombre del fichero de texto no corresponde con alguno existente, se creará
##    un nuevo fichero de texto con el nombre pasado por parámetro.
##    El programa finaliza tras introducir la cadena "FIN" o "fin" """
##    f1 = open(nombre,'a')
##    n = str(input("Dame cadena a introducir en fichero. Introduce 'fin' para finalizar la escritura: "))
##    while(n.lower() != 'fin'):
##        f1.writelines(n + '\n')
##        n = str(input("Dame cadena a introducir en fichero. Introduce 'fin' para finalizar la escritura: "))
##    f1.close()

##nombre = str(input("Dame nombre de fichero (sin la extensión .txt): "))
##while(nombre == ''):
##    nombre = str(input("Dame nombre de fichero (sin la extensión .txt): "))
##crece_fichero(nombre + '.txt')


################################################################################

def inicio_juego():
    """ Imprime por pantalla un menú con los juegos disponibles e inicia el
    juego correspondiente """
    print("----- Elije un juego para jugar -----")
    print("1.Buscaminas")
    print()
    print("Introduce la tecla del número de juego que desees jugar")

    opcion = int(input("Escribe el número de juego: "))
    procesar_opcion(opcion)


def procesar_opcion(opcion):
    """ Recibe una opción, resultante de elegir un juego del menú, y en función
    de la opción pasada por parámetro, inicia un juego determinado """
    if(opcion == 1):
        jugar_buscaminas()


def jugar_buscaminas():
    """ Inicia una partida del juego del buscaminas pidiendo por teclado el
    número de filas y columnas del tablero de juego, la dificultad de juego
    e inicia la partida """
    presentacion_buscaminas()

    f = int(input("Dame número de filas para el tablero de juego (>0): "))
    c = int(input("Dame número de columnas para el tablero de juego (>0): "))

    while(f <= 0):
        f = int(input("Dame número de filas para el tablero de juego (>0): "))
    while(c <= 0):
        c = int(input("Dame número de columnas para el tablero de juego (>0): "))

    tablero = cargar_tablero_buscaminas(f,c)[0]
    tablero_con_minas_no_visibles = cargar_tablero_buscaminas(f,c)[1]

    tablero_con_banderas = crear_tablero(f,c,"0")

    mostrar_tablero(tablero,tablero_con_banderas)

    condicion1 = True
    condicion2 = True

    while (condicion1 and condicion2):
        condicion2 = movimiento_del_jugador(tablero,tablero_con_banderas,input("w,a,s,d para moverte; m para marcar, c para desmarcar, e para desactivar bomba: "))
        mostrar_tablero(tablero,tablero_con_banderas)
        condicion1 = not(comprobarFin(tablero_con_banderas, tablero_con_minas_no_visibles))

    print("#########################################################")
    print("#####################   GAME OVER   #####################")
    print("#########################################################")


def presentacion_buscaminas():
    """ Imprime por pantalla mensaje de bienvenida con los controles del
    buscaminas """
    print()
    print("#########################################################")
    print("######## BIENVENIDO AL JUEGO DEL BUSCAMINAS      ########")
    print("########                                         ########")
    print("######## Usa la tecla 'w' para ir arriba         ########")
    print("######## Usa la tecla 'a' para ir a la izquierda ########")
    print("######## Usa la tecla 's' para ir abajo          ########")
    print("######## Usa la tecla 'd' para ir a la derecha   ########")
    print("######## Usa la tecla 'm' para marcar            ########")
    print("######## Usa la tecla 'c' para desmarcar         ########")
    print("######## Usa la tecla 'e' para desactivar bomba  ########")
    print("########                                         ########")
    print("#########################################################")
    print()
    print()


def cargar_tablero_buscaminas(f,c):
    """ Recibe un número de filas y de columnas, y pide por teclado una
    dificultad de juego para la partida y en función de la dificultad se rellena
    de una cantidad u de otra el tablero de juego con minas. Al final retorna el
    tablero de juego resultante con las minas colocadas en función de la
    dificultad elegida. Y retorna otro tablero con solo las minas ocultadas """
    tablero = crear_tablero(f,c,0)

    diff = elegir_dificultad()

    if(diff == 1):
        buscaminas_facil(tablero)
    elif(diff == 2):
        buscaminas_normal(tablero)
    elif(diff == 3):
        buscaminas_dificil(tablero)

    ocultar_minas_tablero(tablero)
    tablero_con_minas_no_visibles = tablero
    pistas_sobre_minas(tablero)

    return tablero, tablero_con_minas_no_visibles


def crear_tablero(f,c,v):
    """ Recibe un número de filas, de columnas y un valor, y crea y retorna una
    matriz de dimensiones filas x columnas rellena con el valor recibido como
    parámetro """
    m = []
    for i in range(f):
        m.append(c * [v])
    return m


def elegir_dificultad():
    """ Imprime por pantalla un menú con las dificultades del juego disponibles
    y retorna el número de la dificultad elegida """
    print("---- Elije dificultad de juego ----")
    print("---- 1.Dificultad fácil        ----")
    print("---- 2.Dificultad normal       ----")
    print("---- 3.Dificultad difícil      ----")
    diff = int(input("Introduce el número de la dificultad: "))
    while((diff != 1) and (diff != 2) and (diff != 3)):
        diff = int(input("Dificultad no reconocida, inténtelo de nuevo. (1 = facil ; 2 = normal ; 3 = difícil): "))
    return diff


def buscaminas_facil(tablero):
    """ Recibe un tablero de juego del buscaminas y lo rellena con un número de
    minas tales que ocupen un 15% de todo el tablero de juego """
    numero_de_minas_15_por_ciento = calcular_numero_de_minas_en_tablero(tablero,15)
    for i in range(numero_de_minas_15_por_ciento):
        x = random.randint(0,len(tablero)-1)
        y = random.randint(0,len(tablero[0])-1)
        while(tablero[x][y] == '*'):
            x = random.randint(0,len(tablero)-1)
            y = random.randint(0,len(tablero[0])-1)
        tablero[x][y] = '*'


def buscaminas_normal(tablero):
    """ Recibe un tablero de juego del buscaminas y lo rellena con un número de
    minas tales que ocupen un 50% de todo el tablero de juego """
    numero_de_minas_50_por_ciento = calcular_numero_de_minas_en_tablero(tablero,50)
    for i in range(numero_de_minas_50_por_ciento):
        x = random.randint(0,len(tablero)-1)
        y = random.randint(0,len(tablero[0])-1)
        while(tablero[x][y] == '*'):
            x = random.randint(0,len(tablero)-1)
            y = random.randint(0,len(tablero[0])-1)
        tablero[x][y] = '*'


def buscaminas_dificil(tablero):
    """ Recibe un tablero de juego del buscaminas y lo rellena con un número de
    minas tales que ocupen un 75% de todo el tablero de juego """
    numero_de_minas_75_por_ciento = calcular_numero_de_minas_en_tablero(tablero,75)
    for i in range(numero_de_minas_75_por_ciento):
        x = random.randint(0,len(tablero)-1)
        y = random.randint(0,len(tablero[0])-1)
        while(tablero[x][y] == '*'):
            x = random.randint(0,len(tablero)-1)
            y = random.randint(0,len(tablero[0])-1)
        tablero[x][y] = '*'


def calcular_numero_de_minas_en_tablero(tablero,porc):
    """ Recibe un entero que será un tanto por ciento y calcula el número de
    casillas que componen el porcentaje pasado por parámetro en el tablero
    pasado por parámetro. Retorna el número de casillas calculadas """
    area_tablero = len(tablero) * len(tablero[0])
    return int(round(area_tablero * (porc / 100), 0))


def ocultar_minas_tablero(tablero):
    """ Recibe un tablero de juego del buscaminas y oculta las casillas marcadas
    como minas (marcadas con '*') """
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] != 0:
                tablero[i][j] = " "


def pistas_sobre_minas(tablero):
    """ Recibe un tablero de juego del buscaminas y cambia, en éste, los
    elementos que no sean minas (ocultadas por " ") y serán sustituidos por un
    número que significará cuántas minas hay en sus casillas vecinas """
    for i in range(len(tablero)):   # Recorrido por filas
        for j in range(len(tablero[i])):    # Recorrido por columnas
            if(tablero[i][j] != " "):  ## Si el elemento no es mina...

                # Si el elemento no mina está en la esquina superior izquierda...
                if(i == 0 and j == 0):
                    nuevoValor = 0
                    for a in range(i + 2): ## Recorrido de las filas
                        for b in range(j + 2):  ## Recorrido de las columnas
                            if (tablero[a][b] == " "):    ## Si el elemento seleccionado es mina...
                                nuevoValor = nuevoValor + 1
                                tablero[i][j] = nuevoValor

                # Si el elemento no mina está en la esquina superior derecha...
                if (i == 0 and j == len(tablero) - 1):
                    nuevoValor = 0
                    for a in range(i + 2):  ## Recorrido de las filas
                        for b in range(j - 1,len(tablero),1):  ## Recorrido de las columnas
                            if (tablero[a][b] == " "):   ## Si el elemento seleccionado es mina...
                                nuevoValor = nuevoValor + 1
                                tablero[i][j] = nuevoValor

                # Si el elemento no mina está en la primera fila...
                if i==0 and j!=0 and j!=len(tablero)-1:
                    nuevoValor=0
                    for a in range(i,i+2,1):  ## Recorrido de las filas
                        for b in range(j-1,j+2,1):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":  ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor

                # Si el elemento no mina está en la última fila...
                if i==len(tablero)-1 and j!=0 and j!=len(tablero)-1:
                    nuevoValor=0
                    for a in range(i-1,i+1,1):  ## Recorrido de las filas
                        for b in range(j-1,j+2,1):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":  ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor

                # Si el elemento no mina está en la esquina inferior izquierda...
                if i==len(tablero)-1 and j==0:
                    nuevoValor=0
                    for a in range(i-1,len(tablero),1): ## Recorrido de las filas
                        for b in range(j+2):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":    ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor

                # Si el elemento no mina está en la primera columna...
                if i!=0 and i!=len(tablero)-1 and j==0:
                    nuevoValor=0
                    for a in range(i-1,i+2,1): ## Recorrido de las filas
                        for b in range(j+2):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":    ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor

                # Si el elemento no mina está en la última columna...
                if i!=0 and i!=len(tablero)-1 and j==len(tablero)-1:
                    nuevoValor=0
                    for a in range(i-1,i+2,1): ## Recorrido de las filas
                        for b in range(j-1,len(tablero),1):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":    ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor

                # Si el elemento no mina está en la esquina inferior derecha...
                if i==len(tablero)-1 and j==len(tablero)-1:
                    nuevoValor=0
                    for a in range(i-1,i+1,1): ## Recorrido de las filas
                        for b in range(j-1,j+1,1):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":    ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor

                # Si el elemento no mina está en el interior del tablero...
                if i!=len(tablero)-1 and j!=len(tablero)-1 and i!=0 and j!=0:
                    nuevoValor=0
                    for a in range(i-1,i+2,1): ## Recorrido de las filas
                        for b in range(j-1,j+2,1):  ## Recorrido de las columnas
                            if tablero[a][b]==" ":    ## Si el elemento seleccionado es mina...
                                nuevoValor=nuevoValor+1
                                tablero[i][j]=nuevoValor


ubicacionJugador = [0,0]
def mostrar_tablero(tablero,tablero_con_banderas):
    """ Muestra por consola un tablero de juego recibido como parámetro junto
    con una leyenda explicando los controles del juego """
    # Salida por consola del tablero
    for i in range(len(tablero)): ## para cada fila del tablero...
        for j in range(len(tablero[i])): ## para cada elemento de cada fila del tablero...
           ## imprimir el elemento seleccionado
            if i == ubicacionJugador[0] and j == ubicacionJugador[1]:
                print ("X",end= " ")
            elif tablero_con_banderas[i][j]=="%":
                print("%",end=" ")
            else:
                print(tablero[i][j], end=" ")
        print() ## salto de línea para cada fila
    # Leyenda con los controles
    print()
    print()
    print("'w' para moverte hacia arriba")
    print("'a' para moverte hacia la izquierda")
    print("'s' para moverte hacia abajo")
    print("'d' para moverte hacia la derecha")
    print("'m' para marcar")
    print("'c' para desmarcar")
    print("'e' para desactivar bomba")
    print()
    print()


def movimiento_del_jugador(tablero,tableroBanderas,letra):
    """ A partir del parámetro de tipo carácter, el jugador se desplazará por el
    tablero de juego, dado como parámetro, mediante las letras "a" o "A"
    (movimiento hacia la izquierda), "d" o "D" (movimiento hacia la derecha),
    "s" o "S" (movimiento hacia abajo) y "w" o "W" (movimiento hacia arriba) """
    movimiento=letra
    if movimiento=='a' or movimiento=='A':
        if ubicacionJugador[1]-1 >= 0:
            ubicacionJugador[1] = ubicacionJugador[1] - 1
    elif movimiento=='d' or movimiento=='D':
        if ubicacionJugador[1]+1 < (len(tablero)):
            ubicacionJugador[1] = ubicacionJugador[1] + 1
    elif movimiento=='w' or movimiento=='W':
        if ubicacionJugador[0]-1 >= 0:
            ubicacionJugador[0] = ubicacionJugador[0] -1
    elif movimiento=='s' or movimiento=='S':
        if ubicacionJugador[0]+1 < (len(tablero)):
            ubicacionJugador[0] = ubicacionJugador[0] + 1

    elif movimiento=='m' or movimiento=='M':
        tableroBanderas[ubicacionJugador[0]][ubicacionJugador[1]]="%"
    elif movimiento=='c' or movimiento=='C':
        tableroBanderas[ubicacionJugador[0]][ubicacionJugador[1]]="0"

    elif movimiento=='e' or movimiento=='E':
        if tablero[ubicacionJugador[0]][ubicacionJugador[1]]==" ":
            return False
    return True


def comprobarFin(tableroDeBanderas,tableroDeMinasNoVisibles):
    """Recibe un tablero de banderas y un tablero de minas no visibles, y si en
    una posición hay bandera y no hay bomba, devuelve False porque el juego no
    termimó, y si hay bomba y no está marcada, tampoco termina"""
    for i in range(len(tableroDeBanderas)):
        for j in range(len(tableroDeBanderas[i])):
            if not(tableroDeBanderas[i][j]=="%" and tableroDeMinasNoVisibles[i][j]==" "):
                return False
    return True


##inicio_juego()

################################################################################


# Escribe una función que tome por parámetro una lista de enteros y devuelva la
# cantidad de números naturales pares que hay en ella. Supón que la función
# siempre recibe valores válidos. Si quieres un reto adicional, define la
# función de modo que la lista pueda contener datos de cualesquiera tipos.
def cantidad_numeros_enteros_pares_lista(lista):
    """ Recibe una lista y retorna el número de números naturales pares que hay
    en ella """
    cont = 0
    for x in lista:
        if(type(x) == type(0)):
            if((x >= 0) and ((x % 2) == 0)):
                cont = cont + 1
    return cont


##lista_ejemplo_1 = [-2, 6, -6, 7, 1, 0, 4, 12]
##print(cantidad_numeros_enteros_pares_lista(lista_ejemplo_1))


################################################################################################################################################################

# Escriba un programa que pida palabras por teclado. El programa finalizará
# cuando se introduzca la cadena vacía y en ese momento mostrará como resultado
# el número de veces que se ha introducido una palabra idéntica a la anterior.
# No se pueden emplear listas.

# Ejemplo: con la entrada de "esto", "es", "una", "prueba", "es" el programa
# debe mostrar un 1 como resultado puesto que "es" se repite una vez de forma
# consecutiva.
##n = str(input("Dame palabra. Dame la vacía para finalizar: "))
##cad = ''
##cont = 0
##while(0 < 1):
##    if(n == ''):
##        break
##    if(cad in n):
##        cont = cont + 1
##    cad = cad + n
##    n = str(input("Dame palabra. Dame la vacía para finalizar: "))
##print("Número de palabras repetidas:", cont)


# Dadas dos listas de palabras, se desea filtrar en la primera las palabras
# que cumplan unas determinadas condiciones.

# Se pide escribir la función filtrar(A,B,v) que recibe como parámetros dos
# listas de palabras (A y B) y un valor booleano.

# Si el valor es True, la función debe eliminar de A las palabras que están
# contenidas en B. En caso contrario debe eliminar de A las palabras que no
# están en B.

# En ambos casos se eliminarán también las palabras que tengan tres o menos
# caracteres. Observe que la función no debe devolver ningún valor sino
# modificar la lista A eliminando los elementos mencionados.

def filtrar_ejercicio(A,B,v):
    """ Hace lo del enunciado """
    eliminar_de_A_las_palabras_de_menos_de_tres_caracteres(A)
    if(v):
        eliminar_de_A_lo_que_hay_en_B(A,B)
    else:
        eliminar_de_A_lo_que_no_hay_en_B(A,B)

def eliminar_de_A_las_palabras_de_menos_de_tres_caracteres(A):
    for x in A:
        if(len(str(x)) < 3):
            A.pop(A.index(x))


def eliminar_de_A_lo_que_hay_en_B(A,B):
    for x in A[::]:
        if(x in B):
            A.pop(A.index(x))


def eliminar_de_A_lo_que_no_hay_en_B(A,B):
    for x in A[::]:
        if(x not in B):
            A.pop(A.index(x))


##lista_A = ["hola","adios","buenas"]
##lista_B = ["tal","hello","hola"]

##print("Lista A antes de ejecución:", lista_A)

##filtrar_ejercicio(lista_A,lista_B,True) ## Deberia de quedar lista_A = ["adios","buenas"]
##filtrar_ejercicio(lista_A,lista_B,False) ## Deberia de quedar lista_A = ["hola"]

##print("Lista A después de ejecución:", lista_A)


# Un fichero contiene en cada línea los tres vértices de un triángulo siendo el
# formato:

    # (x1,y1) (x2,y2) (x3,y3)

# donde (x1,y1) (x2,y2) (x3,y3) son las coordenadas cartesianas de los vértices.
# Haga un programa que calcule la suma de las áreas de todos los triángulos
# empleando la siguiente fórmula del área donde a, b y c son los tres lados del
# triángulo:

    # s = (a + b + c) / 2

    # area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Utilice a modo de ejemplo el siguiente contenido para el fichero. En este caso
# debe obtenerse un 4 como suma total de los tres triángulos. Nótese que puede
# haber espacios sobrantes.

def suma_total_areas_triangulos_fichero_ejercicio(nombre):
    """ Recibe el nombre de un fichero de texto el cuál tiene en cada línea de
    texto las coordenadas cartesianas de los tres puntos de un triángulo.
    Retorna la suma total de las áreas de todos los triángulos que hay en el
    fichero, hay un tríangulo por línea de fichero """
    f1 = open(nombre, 'r')
    s = 0
    for x in f1:
        s = s + area_triangulo_fichero(saca_lados_triangulo_fichero(saca_coordenadas_triangulo_fichero(procesa_linea_triangulo_fichero(x.strip('\n')))))
    f1.close()
    return s


def area_triangulo_fichero(lados):
    """ Recibe una lista de longitudes de los lados de un triángulo y retorna
    el área de dicho triángulo """
    s = (lados[0] + lados[1] + lados[2]) / 2
    return round((s * (s - lados[0]) * (s - lados[1]) * (s - lados[2])) ** 0.5, 1)


def saca_lados_triangulo_fichero(coordenadas):
    """ Recibe una lista de coordenadas de puntos cartesianos de un tríangulo
    y retorna una lista en la que cada elemento que la compone es la longitud de
    cada lado de dicho triángulo """
    punto1_x = coordenadas[0][0]
    punto1_y = coordenadas[0][1]

    punto2_x = coordenadas[1][0]
    punto2_y = coordenadas[1][1]

    punto3_x = coordenadas[2][0]
    punto3_y = coordenadas[2][1]


    lado_A = round((((punto2_x - punto1_x) ** 2) + ((punto2_y - punto1_y) ** 2)) ** 0.5, 1) ## lado 1-2
    lado_B = round((((punto3_x - punto2_x) ** 2) + ((punto3_y - punto2_y) ** 2)) ** 0.5, 1) ## lado 2-3
    lado_C = round((((punto3_x - punto1_x) ** 2) + ((punto3_y - punto1_y) ** 2)) ** 0.5, 1) ## lado 1-3

    return [lado_A,lado_B,lado_C]


def saca_coordenadas_triangulo_fichero(linea):
    """ Recibe una linea procesada de un fichero de texto el cuál tiene en cada
    linea las coordenadas de los tres puntos de un triángulo. Retorna una lista
    de listas en la que cada una de estas segundas tendrán la coordenada 'x' y
    la coordenada 'y' de cada punto del triángulo """
    aux1 = linea.split(')(')
    lsal = []
    for x in aux1:
        coordenadas = x.split(',')

        coordenada_x = float(coordenadas[0])
        coordenada_y = float(coordenadas[1])

        lsal.append([coordenada_x,coordenada_y])
    return lsal


def procesa_linea_triangulo_fichero(linea):
    """ Recibe una línea de un fichero de texto el cuál tiene en cada línea las
    coordenadas cartesianas de los tres puntos de un tríangulo. Esta función
    dejará dichas cada línea de dicho fichero en un formato determinado para
    procesar en otras funciones. Retorna la línea procesada final con el formato
    determinado"""
    line = linea.lstrip('(').rstrip(')')
    aux1 = []
    for x in line:
        aux1.append(x)
    for x in aux1:
        if(x == '\t' or x == ''):
            aux1.pop(aux1.index(x))
    cadf = ''.join(aux1)
    return cadf



##print("Resultado final:", suma_total_areas_triangulos_fichero_ejercicio("puntos triangulos.txt"))


################################################################################################################################################################


# Crea la lista "a" que valga [0,1,2,3,4,5]
##a = [i for i in range(6)]
##print(a)

# Crea una lista "b" que contenga los inversos de las raíces cuadradas de los
# números del 1 al 100
##b = [1/(i ** 0.5) for i in range(1,101,1)]
##print(b)

# Crea una lista con las cinco primeras potencias del número complejo 1+1j
##c = [(1+1j)**n for n in range(5)]
##print(c)

# Realiza el producto escalar de dos vectores v1 y v2.
##d = sum([a * b for a,b in zip(v1,v2)])
##print(d)

# Asigna a menores una lista con el menor de los elementos de dos listas
##menores = [min(a,b) for a,b in zip(v1,v2)]
##print(menores)

# Retorna la lista con los caracteres iniciales de cada cadena de caracteres
##v1 = ["esto","es","una","prueba"]
##iniciales = [x[0] for x in v1]
##print(iniciales)

# Retorna la lista con los caracteres finales de cada cadena de caracteres
##v1 = ["esto","es","una","prueba"]
##finales = [x[-1] for x in v1]
##print(finales)

# Realiza la suma de cada elemento de las tres listas
##lista_1=[1,2,3,4]
##lista_2=[10,20,30,40]
##lista_3=[100,200,300,400]
##suma = [a+b+c for a,b,c in zip(lista_1,lista_2,lista_3)]
##print(suma)

# Imprime la lista por la salida estándar dos veces y, tras eso, elimina todos
# los elementos de la lista
##lista=[50,-22,10,60,30,-18]
##[print("Número (primera salida por consola):",x) for x in lista]
##[print("Número (segunda salida por consola):",lista[i]) for i in range(len(lista))]
##[lista.pop() for j in range(len(lista))]

# Sea "matriz" una lista de listas: matriz=[[1,2,3,4],[5,6,7,8],[9,10,11,12]],
# Haz un programa que guarde en una lista la suma de todos los elementos de la
# dicha matriz
##matriz=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
##suma = sum([sum(matriz[i]) for i in range(len(matriz))])
##print(suma)

# Supongamos que en numeros tenemos el resultado de leer un fichero, crea un
# código que intente convertir cada elemento leído a flotante
##numeros = ["123\n","68.5\n","-4.1\n","9.9\n"]
##numeros = [float(x) for x in numeros]
##print(numeros)

# Haz un programa que cree una lista con solo los números negativos de la
# siguiente lista:
##lista = [50,-22,10,60,30,-18]
##negativos = [x for x in lista if x < 0]
##print(negativos)

# Haz un programa que cree una lista con solo los números positivos de la
# siguiente lista:
##lista = [50,-22,10,60,30,-18]
##positivos = [x for x in lista if x >= 0]
##print(positivos)

# Haz un programa que cree una lista con solo los números pares de la siguiente
# lista:
##lista = [50,-22,10,60,30,-18]
##pares = [x for x in lista if x % 2 == 0]
##print(pares)

# Haz un programa que cree una lista con solo los números impares de la
# siguiente lista:
##lista = [50,-22,10,60,30,-18]
##impares = [x for x in lista if x % 2 != 0]
##print(impares)

# Haz un programa que cuente la cantidad de números negativos que hay en la
# siguiente lista:
##lista = [50,-22,10,60,30,-18]
##numero_negativos = sum([1 for x in lista if x < 0])
##print(numero_negativos)

# Haz un programa que cuente la cantidad de números positivos que hay en la
# siguiente lista:
##lista = [50,-22,10,60,30,-18]
##numero_positivos = sum([1 for x in lista if x >= 0])
##print(numero_positivos)

# Haz un programa que cuente la cantidad de números pares que hay en la
# siguiente lista:
##lista = [50,-22,10,60,30,-18]
##numero_pares = sum([1 for x in lista if x % 2 == 0])
##print(numero_pares)

# Haz un programa que cuente la cantidad de números impares que hay en la
# siguiente lista:
##lista = [50,-22,10,60,30,-18]
##numero_impares = sum([1 for x in lista if x % 2 != 0])
##print(numero_impares)

# Haz un programa que almacene en una lista llamada "numeros" los elementos de
# "lista" que cumplan la condición de ser enteros o reales
##lista = ["hola",12,6.7,[],True,1.5,-1]
##numeros = [x for x in lista if type(x) == type(0) or type(x) == type(0.0)]
##print(numeros)

# Haz un programa que almacene en una lista llamada "cadenas" los elementos de
# "lista" que cumplan la condición de ser cadenas de texto
##lista = ["hola",12,6.7,[],True,1.5,-1]
##cadenas = [x for x in lista if type(x) == type("")]
##print(cadenas)

# Haz un programa que almacene en una lista llamada "listas" los elementos de
# "lista" que cumplan la condición de ser listas
##lista = ["hola",12,6.7,[],True,1.5,-1]
##listas = [x for x in lista if type(x) == type([])]
##print(listas)

# Haz un programa que almacene en una lista llamada "booleanos" los elementos de
# "lista" que cumplan la condición de ser booleanos
##lista = ["hola",12,6.7,[],True,1.5,-1]
##booleanos = [x for x in lista if type(x) == type(True)]
##print(booleanos)

# Haz un programa que almacene en una lista llamada "enteros" los elementos de
# "lista" que cumplan la condición de ser enteros
##lista = ["hola",12,6.7,[],True,1.5,-1]
##enteros = [x for x in lista if type(x) == type(0)]
##print(enteros)

# Haz un programa que almacene en una lista llamada "reales" los elementos de
# "lista" que cumplan la condición de ser reales
##lista = ["hola",12,6.7,[],True,1.5,-1]
##reales = [x for x in lista if type(x) == type(0.0)]
##print(reales)

# Haz un programa que almacene en una lista llamada "enteros_positivos" los
# elementos de "lista" que cumplan la condición de ser enteros positivos
##lista = ["hola",12,6.7,[],True,1.5,-1]
##enteros_positivos = [x for x in lista if((type(x) == type(0)) and (x >= 0))]
##print(enteros_positivos)

# Haz un programa que almacene en una lista llamada "enteros_negativos" los
# elementos de "lista" que cumplan la condición de ser enteros negativos
##lista = ["hola",12,6.7,[],True,1.5,-1]
##enteros_negativos = [x for x in lista if((type(x) == type(0)) and (x < 0))]
##print(enteros_negativos)

# Haz un programa que almacene en una lista llamada "reales_positivos" los
# elementos de "lista" que cumplan la condición de ser reales positivos
##lista = ["hola",12,6.7,[],True,1.5,-1]
##reales_positivos = [x for x in lista if type(x) == type(0.0) and x >= 0.0]
##print(reales_positivos)

# Haz un programa que almacene en una lista llamada "reales_negativos" los
# elementos de "lista" que cumplan la condición de ser reales negativos
##lista = ["hola",12,6.7,[],True,1.5,-1]
##reales_negativos = [x for x in lista if type(x) == type(0.0) and x < 0.0]
##print(reales_negativos)

# Haz un programa que almacene en una lista llamada "enteros_pares" los
# elementos de "lista" que cumplan la condición de ser enteros pares
##lista = ["hola",12,6.7,[],True,1.5,-1]
##enteros_pares = [x for x in lista if type(x) == type(0) and x % 2 == 0]
##print(enteros_pares)

# Haz un programa que almacene en una lista llamada "enteros_impares" los
# elementos de "lista" que cumplan la condición de ser enteros impares
##lista = ["hola",12,6.7,[],True,1.5,-1]
##enteros_impares = [x for x in lista if type(x) == type(0) and x % 2 != 0]
##print(enteros_impares)

# Haz un programa que almacene en una lista llamada "reales_pares" los
# elementos de "lista" que cumplan la condición de ser reales pares
##lista = ["hola",12,6.7,[],True,1.5,-1]
##reales_pares = [x for x in lista if type(x) == type(0.0) and x % 2 == 0]
##print(reales_pares)

# Haz un programa que almacene en una lista llamada "reales_impares" los
# elementos de "lista" que cumplan la condición de ser reales impares
##lista = ["hola",12,6.7,[],True,1.5,-1]
##reales_impares = [x for x in lista if type(x) == type(0.0) and x % 2 != 0]
##print(reales_impares)

################################################################################

# Escriba una función que reciba como parámetros dos listas de cualquier tipo y
# que devuelva la distancia entre ambas.
# Esta distancia entre listas quedará definida como la suma de la diferencia
# entre longitudes de cada lista y el número de elementos distintos en cada
# posición.
# De esta manera tenemos que la distancia entre [1.9,1.4,1.2,0,1.7] y
# [1.7,1.4,0.1,0,1.7] es 2.

# Entre [1.5,0.4,1.3,0] y [0.2,0.4,1.3,0] es 1.
# Entre [1.9,1.7,0,1.9,1.4] y [1.2,2,0.4,1.1,0] es 5.
# Entre [0.2,0,0.1,0,1.1,0.6,0,1.7] y [0.2,0,0.1,0,1.1,1.1,1.4] es 3.

# Haga un pequeño programa para verificar su correcto funcionamiento.

def distancia_entre_listas(l1,l2):
    """ Recibe dos listas de cualquier tipo y retorna la distancia entre ambas.
    Esta distancia entre listas quedará definida como la suma de la diferencia
    entre longitudes de cada lista y el número de elementos distintos en cada
    posición """
    diff_longitudes = abs(len(l1) - len(l2))
    numero_distintos = numero_elementos_distintos_listas(l1,l2)
    return diff_longitudes + numero_distintos


def numero_elementos_distintos_listas(l1,l2):
    """ Recibe dos listas de cualquier tipo y retorna el número de elementos
    distintos que hay entre ellas en cada posición"""
    cont = 0
    if(len(l1) < len(l2)):
        for x in range(len(l1)):
            if(l1[x] != l2[x]):
                cont = cont + 1
    else:
        for x in range(len(l2)):
            if(l2[x] != l1[x]):
                cont = cont + 1
    return cont

##l1 = [0.2,0,0.1,0,1.1,0.6,0,1.7]
##l2 = [0.2,0,0.1,0,1.1,1.1,1.4]
##print(distancia_entre_listas(l1,l2))


# Haga una función llamada extrae_negativos que reciba como parámetro una lista
# de números y extraiga de esa lista pasada como parámetro los números negativos
# y los devuelva en otra lista como resultado.

# Además debe eliminar estos números negativos de la lista original.

# Ejemplo, si la lista antes de la llamada es [10,11,-7,4.5,-2,-2,6.3,8,-1],
# después de la llamada debe ser [10,11,4.5,6.3,8] y además la función debe
# devolver [-7,-2,-2,-1].

# Haga un pequeño programa de prueba con estos datos para comprobar su correcto
# funcionamiento.

def extrae_negativos(lista):
    """ Recibe una lista de números y extrae de ésta los números negativos y los
    deja en otra lista que será retornada """
    negat = []
    for x in lista[:]:
        if(x < 0):
            negat.append(lista.pop(lista.index(x)))
    return negat

##lista = [10,11,-7,4.5,-2,-2,6.3,8,-1]
##print("Lista antes de la llamada:", lista)
##res = extrae_negativos(lista)
##print("Lista despues de la llamada:", lista)
##print("Lista retornada tras la llamada:", res)


# Sin usar la función sorted, escriba una función booleana llamada ordenada, que
# reciba una lista homogénea de cualquier tipo y devuelva True si está ordenada
# crecientemente o False en caso contrario. Haga un pequeño programa de prueba.

# Ejemplos de uso:

    # - Llamada con la lista [9,11,10,20], debe devolver False
    # - Llamada con la lista ["Ana","Juan","Teresa"] debe devolver True

def ordenada(lista):
    """ Recibe una lista homogénea de cualquier tipo y retorna True si está
    ordenada crecientemente o False en caso contrario """
    for i in range(len(lista)-1):
        if(lista[i] > lista[i+1]):
            return False
    return True

##print("Llamada con la lista [9,11,10,20]:", ordenada([9,11,10,20]))
##print("Llamada con la lista [Ana,Juan,Teresa]:", ordenada(["Ana","Juan","Teresa"]))


# Haga una función llamada inserta_ceros, que reciba como parámetro una lista de
# números, y modifique esa lista insertando un cero delante de cada número
# negativo. La función no debe devolver nada.

# Ejemplo, si la lista antes de la llamada es [10,11,-7,4.5,-2,-2,6.3,8,-1],
# después de la llamada debe ser [10,11,0,-7,4.5,0,-2,0,-2,6.3,8,0,-1].

# Haga un pequeño programa de prueba con estos datos para comprobar su correcto
# funcionamiento.

def inserta_ceros(lista):
    """ Recibe una lista de números y modifica dicha lista insertando un cero
    delante de cada número negativo """
    for x in range(len(lista)-1,-1,-1):
        if(lista[x] < 0):
            lista.insert(x,0)

##lista = [10,11,-7,4.5,-2,-2,6.3,8,-1]
##print("Lista antes de la llamada:", lista)
##inserta_ceros(lista)
##print("Lista después de la llamada:", lista)

