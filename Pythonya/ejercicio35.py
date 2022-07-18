# Problema 4:
#Desarrollar un programa que permita la carga de 10 valores por teclado y 
# nos muestre posteriormente la suma de los valores ingresados y su promedio. 
# Este problema ya lo desarrollamos, lo resolveremos empleando la estructura for 
# para repetir la carga de los diez valores por teclado.
suma = 0 
for f in range(10): 
    valor = int (input("Ingrese valor:  "))
    suma2 = suma + valor 
print("La suma es")
print(suma2)
promedio = suma2 / 10 
print("El promedio es:")
print(promedio)

"""Como vemos la variable f del for solo sirve para iterar(repetir) 
las diez veces el bloque contenido en el for.
El resultado hubiese sido el mismo si llamamos a 
la funcion range con los valores: range(1,11)"""