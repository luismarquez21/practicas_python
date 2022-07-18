#Bucles anidados
#Como ya vimos en las sentencias condicionales, 
# el anidamiento es una técnica por la que incluimos distintos niveles de encapsulamiento de sentencias,
#  unas dentro de otras, con mayor nivel de profundidad. En el caso de los bucles también es posible 
# hacer anidamiento.

#Veamos un ejemplo de 2 bucles anidados en el que generamos todas las tablas de multiplicar:

for i in range(1,10):
    for j in range(1, 10):
        result = i * j 
        print(f'{i} * {j} = {result}')

