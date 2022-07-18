#Escriba un programa que calcule la distancia hamming entre dos cadenas de texto de la misma longitud.

#Ejemplo
#Entrada: 0001010011101 y 0000110010001

#Salida: 4

str1 = '000101001110101'
str2 = '000011001000110'

i = 0
distance = 0

while i < len(str1):
    if str1[i] != str2[i]:
        distance += 1
    i += 1

print(distance)

