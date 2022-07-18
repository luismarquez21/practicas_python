# Parámetros y argumentos 
def sqrt(value):
    return value ** (1/2)

monaco = sqrt(4)
print(monaco)

"""
Cuando llamamos a una función con argumentos, 
los valores de estos argumentos se copian en los correspondientes 
parámetros dentro de la función:
"""
def my_pretty_function(value_a, value_b, value_c):
    pass
my_pretty_function('Hola', 3.14, {1,2,3})
