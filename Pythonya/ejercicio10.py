# ESTRUCTURA CONDICIONAL COMPUESTA
"""
Se hace la entrada de num1 y num2 por teclado. Para saber cual variable tiene un valor mayor preguntamos si el contenido de num1 es mayor (>) que el contenido de num2, si la respuesta es verdadera vamos por la rama de la derecha e imprimimos num1, en caso que la condición sea falsa vamos por la rama de la izquierda (Falsa) e imprimimos num2.
Como podemos observar nunca se imprimen num1 y num2 simultáneamente.
"""

num1 = int(input("Ingrese primer valor: "))
num2 = int(input("ingrese el segundo valor: ")) 
print("El valor mayor es")
if num1>num2: 
    print(num1)
else: 
    print(num2)