# Una función que tome una lista y devuelva el número mas grande.

lista = [1,2,3,7,5,3,9,12]

def maximo (lista):
    return max(lista)


print("El número mas alto es:" , maximo(lista))

def max_dos (lista):
    inicio = 0
    for i in lista:
        if i > inicio:
            inicio = i
    return inicio

print(max_dos(lista))

#Escribir una lista de palabras y que una funcion devuelva la mas larga.


lista_palabras = ["hola", "Mañana", "Camioneta","sol"]

def mas_larga (lista_palabras):
   mas_larga = ""
   for i in lista_palabras:
       if len(i)>len(mas_larga):
           mas_larga = i
   return mas_larga

print("La palabras mas larga es: ", mas_larga(lista_palabras))


