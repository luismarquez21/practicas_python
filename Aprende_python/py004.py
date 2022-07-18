#Bucle infinito
"""Si no establecemos correctamente la condición de parada o bien el valor de alguna 
variable está fuera de control, es posible que lleguemos a una situación de bucle infinito, 
del que nunca podamos salir. Veamos un ejemplo de esto:"""

num = 1 

while num != 10: 
    num += 2 