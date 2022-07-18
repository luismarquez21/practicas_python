#La sentencia For
"""La sentencia for
Python permite recorrer aquellos tipos de datos que sean iterables, es decir, 
que admitan iterar 2 sobre ellos. Algunos ejemplos de tipos y estructuras de datos 
que permiten ser iteradas (recorridas) son: cadenas de texto, listas, diccionarios, 
ficheros, etc. La sentencia for nos permite realizar esta acción."""

lista = list((2,1,0))
tupla = tuple((2,1,0))
conjunto = set((2,1,0))
diccionario = dict(((2,"dos"), (1,"uno"), (0,"cero")))

for iterador in diccionario:
    print(iterador)

print("###Otro Ejemplo de for###")
word = 'Python'
for letter in word:
    print(letter)


print("###Otro Ejemplo de for con range y len ###")
#len se usa para obtner el numero de elementos
#range una secuencia de indices 
lista = ["Vamos", "a", "acceder", "a", "esta", "lista", "por", "indices"]
for indice in range(len(lista)):
    print("Indice:", indice, "Elemento:", lista[indice])
