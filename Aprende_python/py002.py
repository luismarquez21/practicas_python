#Romper un bucle while
# Python ofrece la posibilidad de romper o finalizar un bucle antes de que se cumpla la condición de parada. 
# Supongamos un ejemplo en el que estamos buscando el primer número múltiplo de 3 yendo desde 20 hasta 1:
print("##### Romper un bucle while con break #####")
num = 15

while num >=1:
    if num % 3 == 0:
        print(num)
        break
    num -=1

#COMPROBAR LA ROTURA (si break entro)
#Python nos ofrece la posibilidad de detectar si el bucle ha acabado de forma ordinaria
# Para ello podemos hacer uso de la sentencia else como parte del propio bucle.
print("##### Romper un bucle while con break si break entro poner else #####")
numx = 7

while numx >= 1:
    if numx % 9 == 0:
        print(f'{numx} is a multiple of 9!')
        break
    numx -= 1
else:
    print(f'{numx} No multiples of 9 found!')

print("##### Fin del programa #####")