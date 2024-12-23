
# Escribe una función que tome por parámetro una cadena de caracteres que se asumirá siguiendo el formato de cada línea del fichero anterior,
# y devuelva una lista en la que:
    # el primer elemento sea el nombre de provincia (cadena de caracteres)
    # el segundo elemento sea el número de hombres (valor numérico)
    # el tercer elemento sea el número de mujeres (valor numérico)

# Escribe un programa principal que lea línea por línea el fichero y transforme sus campos empleando
# para ello la función anterior

def funcion1(texto):
    """Hace lo del enunciado"""
    f1=open(texto,'r')
    lsal=[]
    for linea in f1:
        lsal=linea.strip("\n").split(",")
        print(lsal)
    f1.close
    return lsal

##funcion1('zprovincias.txt')



# Modifica el programa anterior para almacenar en una lista el nombre de las provincias en las que el
# número de mujeres es superior al de hombres. Tras ello, muestra sus elementos por pantalla

















