# Problema 3:
# Desarrollar un programa que permita la carga de 10 valores por teclado y 
# nos muestre posteriormente la suma de los valores ingresados y su promedio.

"""
En este problema, a semejanza de los anteriores, tenemos un CONTADOR llamado x que nos sirve para contar las vueltas que debe repetir el while.
También aparece el concepto de ACUMULADOR (un acumulador es un tipo especial de variable que se incrementa o disminuye con valores variables durante la ejecución del programa)

Hemos dado el nombre de suma a nuestro acumulador. Cada ciclo que se repita la estructura repetitiva, la variable suma se incrementa con el contenido ingresado en la variable valor.

La prueba del diagrama se realiza dándole valores a las variables:
"""
x = 1 # CONTADOR llamado x que nos sirve para contar las vueltas que debe repetir el while
suma = 0 # ACUMULADOR (un acumulador es un tipo especial de variable que se incrementa o disminuye con valores variables durante la ejecución del programa)
while x <= 10: 
    valor = int(input("Ingrese un valor:  "))
    suma = suma + valor
    x= x+1
promedio = suma/10 
print("La suma de los 10 valores es: ")
print(suma)
print("El promedio es: ")
print(promedio)
