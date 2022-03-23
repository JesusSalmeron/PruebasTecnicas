# Args

"""

def maximo(*args):
    maximo= args[0]
    for numero in args[1]:
        if numero > maximo:
            maximo = numero
    return maximo

print(maximo(3,5,7,3,43,87,23,27))


def maximo_dos(lista):
    maximo = (lista)
    for numero in lista[1:]:
        if numero > maximo:
            maximo_dos = numero
    return maximo

print(maximo_dos(34,24,87))
"""


def formato_descarga(tipo,*args):
    tipo = tipo.upper()
    numArgs = len(args)
    if tipo == "VIDEO":
        if numArgs == 0:
            print(f"El formato seleccionado: \n-Tipo de archivo: {tipo}")
        elif numArgs == 1:
            print(f"El formato seleccionado: \n-Tipo de archivo: {tipo}\n-Resolución: {args[0]}")
        elif numArgs == 2:
            print(f"El formato seleccionado: \n-Tipo de archivo: {tipo}\n-Resolución: {args[0]}\n-FPS: {args[1]}")
    elif tipo == "AUDIO": 
        print(f"El formato seleccionado: \n-Tipo de archivo: {tipo}")
    else:
        print("El formato seleccionado no es correcto.")

formato_descarga("video",1080,60) 


# Keyword Arbitrary Arguments

def printKwargs(**kwargs):
    print("\n")
    print("Los atributos del personaje son: ")
    for clave, valor in kwargs.items():
        print(f"{clave} ---> {valor}")

print(printKwargs(nombre = "Leonidas", clase = "Guerrero", raza = "humano"))
