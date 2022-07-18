# Continuar un bucle
"""Hay situaciones en las que, en vez de romper un bucle, nos interesa saltar 
adelante hacia la siguiente repetición. Para ello Python nos ofrece la sentencia continue 
que hace precisamente eso, descartar el resto del código del bucle y saltar a la siguiente iteración."""

# Veamos un ejemplo en el que usaremos esta estrategia para mostrar todos los números en el rango [1,20] 
# ignorando aquellos que sean múltiplos de 3:
numy = 21 

while numy >= 1:
    numy -=1 
    if numy % 3 == 0:
        continue
    print(numy, end=',') # Evitar salto de linea
