# Listas en Python

empty_list = []

languages = ['Python', 'Ruby', 'Javascript']

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13]

data = ['Tenerife', {'cielo' : 'limpio', 'temp' : 24}, 3718, (28.2933947, -16.5226597)]

print(languages)

# conversión desde una cadena de texto
list('Python')

# obtener elementos de una lista
shopping = ['Agua', 'Huevos', 'Aceite']
shopping[0]

# CREANDO DESDE VACÍO
even_numbers = []

for i in range(21):
    if i % 2 == 0:
        even_numbers.append(i)

print(even_numbers)

#Combinar listas
shopping = ['Agua', 'Huevos', 'Aceite']
fruitshop = ['Naranja', 'Manzana', 'Piña']

shopping + fruitshop 
