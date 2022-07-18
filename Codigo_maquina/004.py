# For en Python (Estructuras Cíclicas): Curso de Programación con Python #7 

for numero in [0,1,2,3,4,5,6,7,8,9]:
    print("Iteracion: ", numero)

print("----------------------------")

for numero in [6,7,8,9,10]:
    print("Iteracion: ", numero)

print("----------------------------")
#Tienda colores 
colores = ["rojo", "verde", "amarillo", "azul"]

for color in colores: 
    print("Hay pintura color:", color)

print("----------------------------")
indice = 0 
while indice < len(colores):
    print("Hay pintura color:", colores [indice])
    indice += 1

print("----------------------------")
#range en for
for numero in range (5,10):
    print("Iteracion", numero)


