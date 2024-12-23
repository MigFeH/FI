
# Escriba una función cuenta_vocales(nombre, letra, veces) que a partir del nombre del
# fichero que se pasa como parámetro, escriba un fichero con la frecuencia de aparición
# de cada una de las vocales:
# a 24
# e 41
# i 16
# o 23
# u 8

def cuenta_vocales(nombre):
    """A partir del nombre del fichero que se pasa como parámetro, escriba un fichero con la frecuencia de aparición
    de cada una de las vocales"""
    f1=open(nombre,'r')
    f2=open('NumeroVocales.txt','w')
    vocales=["a","e","i","o","u"]
    lres=[]
    vecesA=0
    vecesE=0
    vecesI=0
    vecesO=0
    vecesU=0
    for linea in f1:
        for x in linea.lower():
            if x!="\n" and x!="\t":
                lres=linea.split(" ")
            if x==vocales[0]:
                vecesA=vecesA+1
            if x==vocales[1]:
                vecesE=vecesE+1
            if x==vocales[2]:
                vecesI=vecesI+1
            if x==vocales[3]:
                vecesO=vecesO+1
            if x==vocales[4]:
                vecesU=vecesU+1
    TotalA="a" + " " + str(vecesA) + "\n"
    TotalE="e" + " " + str(vecesE) + "\n"
    TotalI="i" + " " + str(vecesI) + "\n"
    TotalO="o" + " " + str(vecesO) + "\n"
    TotalU="u" + " " + str(vecesU) + "\n"
    f2.write(TotalA)
    f2.write(TotalE)
    f2.write(TotalI)
    f2.write(TotalO)
    f2.write(TotalU)

    f1.close
    f2.close

nombre=input("NOMBRE FICHERO SIN EXTENSIÓN: ")
cuenta_vocales(nombre+".txt")



















