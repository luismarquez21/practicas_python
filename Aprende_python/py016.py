#Funciones 
"""
El concepto de función es básico en prácticamente cualquier lenguaje de programación. 
Se trata de una estructura que nos permite agrupar código. Persigue dos objetivos claros:

1. No repetir trozos de código durante nuestro programa.

2. Reutilizar el código para distintas situaciones.
"""

def say_hello():
    print('Hello!')

say_hello()

# Retornar un valor 
print('Retornar valor en una funcion')
def one(): 
    return 6 

if one() == 1: 
    print('It works!')
else: 
    print('Something is broken')

