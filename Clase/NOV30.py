#### ESTE ES EL MÓDULO  NOV30 (Clase Teoría Martes 30/NOV)

#### FICHEROS (ap.2.7 en páginas 103..109 apuntes)



### ABRIR FICHEROS

### CASO 1
### f=open(nombre,"r")    # r de read
###    para leerlo y procesarlo,
###    si no existe da error

### CASO 2
### f=open(nombre,"w")    # w de write
###    para creerlo desde cero,
###    si existe previamente, se pierde eso

### CASO 3
### f=open(nombre,"a")    # a de append
###    para seguir añadiendo por el final,
###    si no existe previamente, desde cero


### CERRAR FICHEROS

### Cuando se acaba de leer, escribir o añadir
### en un fichero f, hay que cerrar con:
### f.close()



from NOV23pr import *



def crearFichero(nombre):
    """crea un fichero de nombre nombre, línea a línea
    hasta teclear fin o FIN,
    Si ya existe un fichero con ese nombre, se elimina y
    crea uno nuevo """
    f=open(nombre,"w")
    linea=input("linea, fin para acabar")
    while linea.lower()!="fin":
       f.write(linea+"\n")
       linea=input("linea siguiente, fin para acabar")
    f.close()

##nom=input("NOMBRE FICHERO")
##crearFichero(nom+".txt")




def crecerFichero(nombre):
    """crece por el final un fichero de nombre nombre,
    línea a línea hasta teclear fin,
    Si no existe un fichero con ese nombre, lo va
    creando desde la nada"""
    f=open(nombre,"a")
    linea=input("linea, fin para acabar")
    while linea.upper()!="FIN":
        f.write(linea+"\n")
        linea=input("linea siguiente, fin para acabar")
    f.close()


##nom=input("NOMBRE FICHERO a EXTENDER")
##crecerFichero(nom+".txt")





def volcarFichero(nombre):
    """recibe un fichero y lo escribe (print)"""
    f=open(nombre,"r")
    #hay muchas formas de leer un fichero
    #aquí lo vamos hacer línea a línea
    for linea in f:
        linea=linea[0:len(linea)-1:1]  #quita el FL
        #linea=linea.strip()
        #print(len(linea))
        print(linea)
    f.close()

##fich=input("NOMBRE FICHERO")
##volcarFichero(fich+".txt")





def ficheroALista1(nombre):
    """devuelve una lista de enteros con todos los valores
    numéricos del fichero de entrada nombre.
    El fichero ha de tener un número entero por linea"""
    f=open(nombre,"r")
    lsal=[]
    for linea in f:
        linea=linea.strip("\n")#linea[:len(linea)-1:]
        lsal.append(int(linea)) #se convierte a entero
    f.close()
    return lsal

##l=ficheroALista1("znumeros1.txt")
##print(l)
##print(media(l),varianza(l),desvTipica(l),moda(l),modaMultiple(l),mediana(l))





def ficheroALista2(nombre):
    """devuelve una lista de enteros con todos los valores
    numéricos del fichero de entrada nombre.
    El fichero puede tener un número entero o más por línea,
    separados por ; """
    f=open(nombre,"r")
    lsal=[]
    for linea in f:
        linea=linea.strip("\n")#linea[:len(linea)-1:]
        lista=linea.split(";")
        for x in lista:
            lsal.append(int(x))
    f.close()
    return lsal

##l=ficheroALista2("znumeros2.txt")
##print(l)
##print(media(l),varianza(l),desvTipica(l),moda(l),modaMultiple(l),mediana(l))






def listaAFichero(l,nombre):
    """crea un fichero nombre con el contenido de una lista
    de números enteros.
    El fichero creado tendrá un número por línea"""
    f=open(nombre,"w")
    for numero in l:
        f.write(str(numero)+"\n")  #hay que convertir a str
    f.close()

##l=ficheroALista1("znumeros1.txt")+ficheroALista2("znumeros2.txt")
##print(l)
##print(media(l),varianza(l),desvTipica(l),moda(l),modaMultiple(l),mediana(l))
##listaAFichero(l,"zanimales3.txt")
##volcarFichero("zanimales3.txt")






