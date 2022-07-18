# Programación de Funciones Recursivas con Python
"""
CASO BASE: El caso mas simple o el ultimo caso.

CASO RECURSIVO: La funcion se llama a si misma, pero resolviendo un problema menor.

"""

"""
Imprimir del 5 al 0

Imprimir 5 + Imprimir del 4 al 0
Imprimir 4 + Imprimir del 3 al 0
Imprimir 3 + Imprimir del 2 al 0
Imprimir 2 + Imprimir del 1 al 0
Imprimir 1 + Imprimir el 0

"""

def recursiva(n):
    if n == 0:  # caso base
        print(n)
    else: 
        print(n)
        recursiva(n-1)

recursiva(5) 

print("_________________________________________________")

#Factorial
"""
0! =                    = 1
1! = 1                  = 1
2! = 1 * 2              = 2
3! = 1 * 2 * 3          = 6
4! = 1 * 2 * 3 * 4      = 24
5! = 1 * 2 * 3 * 4 * 5  = 120    

"""

def factorial_iteractivo(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n+1):
        resultado *= i
    return resultado

def factorial_recursivo(n):
    if n == 0 or n == 1: # Caso Base
        return 1
    return n*factorial_recursivo(n-1) # Caso recursivo

for i in range(6):
    print(i, factorial_iteractivo(i), factorial_recursivo(i))

 
