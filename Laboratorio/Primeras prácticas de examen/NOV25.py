### ESTE ES EL MÓDULO  NOV25 (Clase Teoría del Jueves 25/NOV)

###  listas-Cadenas (ap.2.6 en páginas 69..103 apuntes)


### CADENAS  o STRINGS

#c1=""
#c2=" "
#c3="ÁLVAREZ,GONZÁLEZ;LUCIA"
#print(c3,len(c3),type(c3))




### CADENAS Y LISTAS TIENEN LOS MISMOS ÍNDICES POSITIVOS Y NEGATIVOS

#print(len(c3),c3[0],c3[len(c3)-1],c3[-2],c3[-20])

#print(c3[-30],c3[25])  # da error por fuera de índice



### RECORRIDO DE CADENAS, IGUAL QUE LAS LISTAS:
### * por posición: for i in range(inicio,fin,paso):
### * por elemento: for x in cadena:



### Los STRINGS en PYTHON son "NO MUTABLES"
### Las LISTAS son "MUTABLES"

#c3="ÁLVAREZ,GONZÁLEZ;LUCIA"
#c3[20]="Í"    #da error por no ser mutable

### HABRÁ QUE SORTEAR ESO, GENERANDO UNA
### NUEVA CADENA CON EL CONTENIDO QUE QUERAMOS




### OPERADOR "in" en CADENAS
### es diferente su funcionamiento a con las listas
### la sintaxis es cad1 in cad2 ( cad1 y cad2 con ctes.,
### vbles. o expr, de tipo str
### Devuelve:
### True si cad1 está dentro (de forma consecutiva) de cad2
### False en caso contrario

#cad1="ABEL"
#cad2="cascabeles"
#cad3="CACABELES"
#print(cad1 in cad2)
#print(cad1.lower())   #letras minúsculas
#print(cad1.upper())   #letras mayúsculas
#print(cad1.upper() in cad2.upper())
#print(cad3 in cad3)




### CONVERSIÓN DE CADENAS A LISTAS (split)


#c3="ÁLVAREZ,GONZÁLEZ;LUCÍA"
#l1=c3.split(";")
#print(l1)
#l2=l1[0].split(",")
#print(l2)
#nombrec=l1[1]+"**"+l2[0]+"**"+l2[1]
#print(nombrec)


#c4="En un lugar     de la Mancha"
#l3=c4.split()     # por omisión es split(" ")
#print(l3)
#print(len(l3))




### CONVERSIÓN DE LISTAS  A CADENAS (join)
### La lista a juntar tiene que ser de elementos
### de tipo str

#lista1=[3,6,7,3,2,48,5,9]
#print(lista1)
#cad1="/".join(lista1)  # da error por no str los elementos
###Vamos a convertirla a lista de elementos str
#lista2=[]
#for x in lista1:
#    lista2.append(str(x))
#print(lista2)
#cad1="/".join(lista2)
#print(cad1)
#print(len(cad1),type(cad1))

### Vamos a hacer la operación inversa
#lista2=cad1.split("/")
#print(lista2)
### Vamos a convertirla a lista de enteros
### para acabar como al principio
#lista1=[]
#for x in lista2:
#    lista1.append(int(x))
#print(lista1)







#### FUNCIONES strip, rstrip, lstrip
#### strip: quita los carácteres iguales al dado por ambos extremos,
#### rstrip: los quita por la derecha (right)
#### lstrip: los quita por la izquierda (left)

#### SON EJEMPLO DE LAS MUCHAS FUNCIONES QUE CUALQUIER
#### LENGUAJE EN GENERAL, Y PYTHON EN PARTICULAR; TIENE
#### PARA TRABAJAR MÁS FÁCIL CON EL TIPO String (str)

#n1="****APELLIDO1, APELLIDO2 ,  NOMBRE*******"
#print(n1)
#n1=n1.strip("*")
#print(n1)


#n1="****APELLIDO1, APELLIDO2 ,  NOMBRE*******"
#print(n1)
#n1=n1.rstrip("*")
#print(n1)


#n1="****APELLIDO1, APELLIDO2 ,  NOMBRE*******"
#print(n1)
#n1=n1.lstrip("*")
#print(n1)


#n1="     APELLIDO1,  APELLIDO2 ,  NOMBRE    "
######Vamos a quitar todos los blancos
#print(n1)
#n1=n1.strip()  #por defecto es strip(" ")
#print (n1)
#l=n1.split(",")
#print(l)
#for i in range(len(l)):
#    l[i]=l[i].strip()
#print(l)
#n1=";".join(l)
#print(n1)



#### EJERCICIOS PROPUESTOS

def nuestra_strip(cad,x):
    """que devuelva otra cadena que sea cad, pero
    quitando el caracter x por ambos extremos"""
    #programarlo
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
    """que devuelva otra cadena que sea cad, pero
    quitando el caracter x por el extremo derecha"""
    #programarlo
    res=[]
    y=str(x)
    for linea in cad:
        res.append(linea)
    while len(res)!=0 and res[len(res)-1]==y: ## el elemento situado en len(res)-1 sea == y
        res.pop(len(res)-1)
    cadf=''.join(res)
    return cadf


def nuestra_lstrip(cad,x):
    """que devuelva otra cadena que sea cad, pero
    quitando el caracter x por el extremo izquierdo"""
    #programarlo
    res=[]
    y=str(x)
    for linea in cad:
        res.append(linea)
    while len(res)!=0 and res[0]==y:
        res.pop(0)
    cadf=''.join(res)
    return cadf



n2="*****HOLA *Y* ADIOS**"
print(nuestra_strip(n2,"*"))
print(nuestra_rstrip(n2,"*"))
print(nuestra_lstrip(n2,"*"))




#### OPERADORES DE CORTE CON CADENAS
#### Funcionan del mismo modo con listas


#c1="kY0rT5yC6hQ7sW9eZ0bW7"
#minus=c1[::3]
#mayus=c1[1::3]
#digit=c1[2::3]
#print(minus+"/"+mayus+"/"+digit)
#reves=c1[::-2]
#print(reves)
#reves=c1[len(c1)-2::-2]
#print(reves)



#### EJERCICIO 1

def contarVocales (texto):
    """recibe una cadena texto y devuelve el número
    de vocales que contiene el texto"""
    cont=0
    for x in texto:
        if x in "AEIOUaeiouÁÉÍÓÚáéíóú":
            cont=cont+1
    return cont

#t="aytrtbEeéÉÚi"
#print(contarVocales(t)) # devolverá 7



#### EJERCICIO 2

def cambiarVocales(texto,sustituto ):
    """recibe una cadena texto y un carácter sustituto
    y devuelve  una cadena igual a texto, excepto cada vocal
    minúscula sin acentuar, que es cambiada por el sustituto"""
    sal=""  # al ser inmutables lo hacemos sobre otra cadena
    for i in range (len(texto)):
        if texto[i] in "aeiou":
            sal=sal+sustituto
        else:
            sal=sal+texto[i]
    return sal

#t="aytrtbEeéÉÚi"
#t=cambiarVocales(t,"*")
#t=cambiarVocales(t,"HOLA")
#print(t)



#### EJERCICIO 3

### NÚMERO ENTEROS CAPICUAS (tienen el mismo valor en ambos sentidos)
### TEXTOS PALÍNDROMOS (se leen igual en ambos sentidos)
def capicua1(n):
    """recibe un entero o string n y dice True (si es capicúa
    o palíndromo) y False en caso contrario"""
    m=str(n)
    return m==m[::-1]

def capicua2(n):
    """hace lo mismo  """
    m=str(n)
    for i in range(len(m)//2+1):
        if m[i]!=m[len(m)-1-i]:
            return False
    return True

def capicua3(n):
    """hace lo mismo  """
    m=str(n)
    l=[]
    for x in m:
        l.append(x)
    return l==l[::-1]

####### def capicua4,5,6 .... se podría hacer de bastantes formas

#n1=23432
#print(capicua1(n1),capicua2(n1),capicua3(n1))
#n2=22332
#print(capicua1(n2),capicua2(n2),capicua3(n2))
#t1="dabalearrozalazorraelabad"
#print(capicua1(t1),capicua2(t1),capicua3(t1))
#t2="larutanosaportootropasonatural"
#print(capicua1(t2),capicua2(t2),capicua3(t2))
#t3="poco palindromo es esto"
#print(capicua1(t3),capicua2(t3),capicua3(t3))



#### EJERCICIO 4

### Queremos listar qué numeros enteros en el rango[0..100000] son
### automórficos, es decir su cuadrado acaba en las mismas cifras que él.
### P.e. 25 es automorfico, ya que 625 es su cuadrado y ...
### P.e. 100 no es automórfico, ya que 10000 es su cuadrado y ...

def automorfico(n):
    """dice si n es automórfico o no.
    Vamos a utilizar la potencialidad de tipo str.
    Haciéndolo con tipo int es más engorroso, puede
    pensar cómo sería"""
    x=str(n)
    y=str(n*n)
    termy=y[len(y)-len(x)::]
    if x==termy:
        return True
    return False

def listadoAutomorficos(n):
    """lista automórficos en el rango [0..n]"""
    for i in range(n+1):
        if automorfico(i):
            print(i,"*",i**2,end="/////")

#listadoAutomorficos(100000)




