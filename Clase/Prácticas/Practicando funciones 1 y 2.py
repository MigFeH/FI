# Ejercicios de funciones 1



# Ejercicio 1.- Definir dos funciones:

# 1. La función lee_entero() que retorna un número entero leído por teclado.
# 2. Una función que retorne el mayor de dos números enteros dados. A esta función la denotaremos como mayor.

# Utilizar las funciones definidas previamente para escribir un programa que solicite dos números enteros
# y muestre en pantalla el mayor de ellos.

def lee_entero(n):
    """Retorna un número entero n leído por teclado"""
    return n

def mayor(m,n):
    """Retorna el mayor de dos números enteros m,n dados"""
    if m<n:
        return n
    else:
        return m

    # solicita 2 numeros enteros
##num1=int(input("Dame primer entero: "))
##num2=int(input("Dame segundo entero: "))
##
##print(mayor(num1,num2))



# Ejercicio 2.- Mediante el uso de docstrings documenta las funciones del ejercicio
# anterior.
## hecho previamente en el ejercicio anterior



# Ejercicio 3.- Utilizando las funciones del ejercicio 1 ¿podrías calcular el mayor de 3
# números dados? Escribe un programa que así lo permita.
## no se podría usar la función mayor ya que está construida para devolver el mayor de
## solo dos enteros, no de tres

def mayor_de_tres(a,b,c):
    """Retorna el mayor de tres números enteros a,b,c dados"""
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c



# Ejercicio 4.- Define una función que retorne cierto si un año dado es bisiesto y falso en
# caso contrario.

# A continuación, escribe un programa que solicite por teclado un año
# (entero positivo) y muestre en pantalla si éste es o no bisiesto, haciendo uso de la función
# ya definida.

# Se supondrá que el año se introduce correctamente y para describir la función se puede
# utilizar la definición de año bisiesto dada en la Wikipedia.
# Ejemplo de resultado (para el año en curso) -> El año 2014 no es bisiesto.

## Año bisiesto es el divisible entre 4, salvo que sea año secular, terminado en «00»-,
## en cuyo caso también ha de ser divisible entre 400.

def bisiesto(m):
    """Retorna si un año m es bisiesto o no"""
    if m%4==0:
        return m,"Es bisiesto"
    elif m%100==0:
        if m%400==0:
            return m,"Es bisiesto"
        else:
            return m,"No es bisiesto"
    else:
        return m,"No es bisiesto"

##print(bisiesto(2000))



# Ejercicio 6.- Define una función que proporcione el estado nutricional de una persona.
# Esto es; la clasificación de su índice de masa corporal (IMC), según la tabla
# proporcionada. La función recibirá el peso (en kilos) y la talla de una persona (en metros),
# datos a partir de los cuales se puede calcular el IMC cómo:

def IMC(p,h):
    """Calcula el IMC de una persona y retorna su estado corporal a partir del peso p y altura h dada"""
    IMC=p/h*h
    if IMC < 18.50:
        return "Bajo peso"
    elif IMC >= 18.50 and IMC < 25.00:
        return "Normal"
    elif IMC >= 25.00:
        return "Sobrepeso"
    elif IMC >= 30.00:
        return "Obesidad"






# Ejercicios de funciones 2:


# Ejercicio 1.- Define una función que retorne el factorial de un número entero no negativo
# dado y escribe un programa que solicite un número entero no negativo y muestre en
# pantalla éste y su factorial.

def factorial(n):
    """Retorna el factorial de un número entero no negativo n"""
    p=1
    for i in range(1,n+1):
        p=p*i
    return p

##n=int(input("Dame entero no negativo: "))
##while n<0:
##    n=int(input("Dame entero no negativo: "))
##
##print(n,factorial(n))



# Ejercicio 2.- Define una función que retorne la suma de todos los divisores propios
# positivos de un número dado, sin incluirse él mismo. Utiliza ésta para escribir un
# programa que solicite por teclado un número entero positivo mayor que uno y muestre en
# la pantalla si éste es o no perfecto.

# Nota. Un número entero positivo es perfecto cuando es igual a la suma de todos sus
# divisores propios positivos.

def sumaDivisores(n):
    """Retorna la suma de todos los divisores propios positivos de un número n dado, sin incluirse él mismo"""
    div=0
    for i in range(1,n+1):
        if n%i==0:
            div=div+i

def esPerfecto(n):
    """Muestra por pantalla si un número n dado es perfecto o no lo es"""
    if sumaDivisores(n)==n:
        print(n,"es perfecto")
    else:
        print(n,"no es perfecto")



# Ejercicio 3.- Utilizando la función definida en el ejercicio anterior, escribe un programa
# que muestre en pantalla la secuencia de números perfectos comprendidos entre 2 y un
# número entero positivo umbral que se solicitará por teclado.

# Salida esperada para umbral = 10000 -> 6 28 496 8128

##def secuenciaPerfectos(n):
##    """Muestra por pantalla la secuencia de números comprendidos entre el 2 y
##    un número positivo umbral"""
##    for i in range(2,n+1):
##        for j in range(2,i+1):
##            if i%j==0:
##                print(i)

##print(secuenciaPerfectos(10000))


