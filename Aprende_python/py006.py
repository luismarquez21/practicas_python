#La setencia For 
"""Python permite recorrer aquellos tipos de datos que sean iterables, es decir, que admitan iterar 2 sobre ellos. 
Algunos ejemplos de tipos y estructuras de datos que permiten ser iteradas (recorridas) 
son: cadenas de texto, listas, diccionarios, ficheros, etc. La sentencia for nos permite realizar esta acción."""
#La sintaxis de un bucle for es la siguiente:
"""
for variable in elemento iterable (lista, cadena, range, etc.):
    cuerpo del bucle
"""

word = 'Python_es_lo_mejor'

for letter in word: 
    print(letter, end='')

# Python for y la clase range
for i in range(11):
    print(i)