# 9 - Estructura repetitiva while
""" 
La sintaxis del bucle while es la siguiente:
while condicion:
    cuerpo del bucle 
"""
x = 0 
while x <= 10: 
    print(x)
    x=x+1 
print("Programa terminado")
# el siguiente programa escribe los números del 1 al 3:
# Ejemplo de bucle while 1
i = 1 
while i <= 3:
    print(i)
    i += 1 
print("Programa terminado")
""" 
El ejemplo anterior se podría haber programado con un bucle for. 
La ventaja de un bucle while es que la variable de control se puede modificar 
con mayor flexibilidad, como en el ejemplo siguiente:
"""
# Ejemplo de bucle while 2
i = 1
while i <= 50:
    print(i)
    i = 3 * i + 1 
print("Programa terminado")

""" 
Otra ventaja del bucle while es que el número de iteraciones no está definida antes de empezar el bucle, 
por ejemplo porque los datos los proporciona el usuario. Por ejemplo, el siguiente ejemplo pide un número 
positivo al usuario una y otra vez hasta que el usuario lo haga correctamente:
"""
# Ejemplo de bucle while 3
numero = int(input("Escriba un número positivo: "))
while numero < 0: 
    print("¡Ha escrito un numero negativo! Intentelo de nuevo")
    numero = int(input("Escriba un número positivo: "))
print("Gracias por su colaboracion")

