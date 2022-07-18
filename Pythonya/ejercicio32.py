# Problema 1:
#Realizar un programa que imprima en pantalla los números del 0 al 100. 
# Este problema lo podemos resolver perfectamente con el ciclo while pero en esta 
# situación lo resolveremos empleando el for.
print("Programa resuelto con for - numeros del 0 al 100")
for x in range(11): # x es nombre de la variable que almacenará en cada vuelta del for
    """ La función range retorna la primera vez el valor 0 y se almacena en x, 
    luego el 1 y así sucesivamente hasta que retorna el valor que le pasamos 
    a range menos uno (-1 a 100) (es decir en nuestro ejemplo al final retorna un 100)"""
    print("Numero con for:", x)

print("________________________________________")
print("Fin del programa de for")
print("________________________________________")

print("Programa resuelto con while - numeros del 0 al 100")

y = 0 
while y < 11: 
    print("Numero con while:", y)
    y = y+1 



print("________________________________________")
print("Fin del programa con while")
print("________________________________________")

