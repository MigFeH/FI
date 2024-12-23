#### ESTE ES EL MÓDULO  NOV23 (Clase Teoría del Martes 23/NOV)

####  listas  (ap. 2.6 en páginas 69..103 apuntes)

####LISTA DE LISTAS (listas Bidimensionales)
####  2  9  6  2
####  3 -2  6  9
####  6  8 -1  3

lBid=[[2,9,6,2],[3,-2,6,9],[6,8,-1,3]]
print(lBid)
#print(lBid[1])
#print(lBid[1][3])
#print(len(lBid))
#print(len(lBid[0]))


##### FORMAS DE RECORRER UNA LISTA BIDIMENSIONAL

#####FORMA 1:para escribirla
#for i in range(len(lBid)):
#    print (lBid[i])

######FORMA 1:para sumar sus elementos
#s=0
#for i in range(len(lBid)):
#    s=s+sum(lBid[i])
#print("LA SUMA ES=",s)

######FORMA 2:para escribirla
#for i in range(len(lBid)):
#    for j in range(len(lBid[i])):
#        print(lBid[i][j],end="*")
#    print()

######FORMA 2:para sumar sus elementos
#s=0
#for i in range(len(lBid)):
#    for j in range(len(lBid[i])):
#        s=s+lBid[i][j]
#print("LA SUMA ES=",s)


######FORMA 3:para escribirla
#for x in lBid:
#    print (x)

######FORMA 3:para sumar sus elementos
#s=0
#for x in lBid:
#    s=s+sum(x)
#print("LA SUMA ES=",s)


######FORMA4:para escribirla
#for x in lBid:
#    for y in x:
#        print(y,end="/")
#    print()

######FORMA4:para sumar sus elementos
#s=0
#for x in lBid:
#    for y in x:
#      s=s+y
#print("LA SUMA ES=",s)


#### ESCRIBIR UNA FUNCIÓN sumaFilas a la que se le pasa una lista
#### de listas l con elementos numéricos y retorna una lista con la
#### suma de sus filas
def sumaFilas(l):
    """ hace lo pedido antes"""
    lres=[]
    for x in l:   # p.e por la FORMA 4
        lres.append(sum(x))
    return lres

#print(sumaFilas(lBid))
#print(sum(sumaFilas(lBid)))



#### ESCRIBIR UNA FUNCIÓN sumaColumnas a la que se le pasa una lista
#### de listas l con elementos numéricos y retorna una lista con la
#### suma de sus columnas
def sumaColumnas(l):
    """hace lo pedido antes"""
    lres=[]
    fil=len(l)
    col=len(l[0])
    for j in range(col):   #por la FORMA 2
        s=0
        for i in range (fil):
            s=s+l[i][j]
        lres.append(s)
    return lres

#print(sumaColumnas(lBid))
#print(sum(sumaFilas(lBid)))



#### ESCRIBIR UNA FUNCIÓN mayorLdeL a la que se le
#### pasa una lista de listas con valores numéricos y y retorna
#### dos valores:el índice de la fila y el índice de la columna
#### en las que se encuentra el elemento mayor.
#### En caso de empate, vale cualquiera
def mayorLdeL(l):
    """ESCRIBIR UNA FUNCIÓN mayorLdeL a la que se le
    pasa una lista de listas l con valores numéricos o str y retorna
    dos valores:el índice de la fila y el índice de la columna
    en las que se encuentra el elemento mayor. En caso de empate
    vale cualquiera"""
    ma=l[0][0]
    filma=0
    colma=0
    for i in range(len(l)):
        for j in range (len(l[0])):
            if l[i][j]>ma: # > es FIFO ; >= es LIFO
                ma=l[i][j]
                filma=i
                colma=j
    return filma,colma

######debe devolver (0,1) o (1,3), porque es donde está el 9
#print(mayorLdeL(lBid))

