#La sentencia if
print('#####Ejemplo if #######')
temperature = 40 

if temperature > 35:
    print('Aviso por alta temperatura')

#La setencia else 
print('#####Ejemplo else #######')
temperature2 = 20

if temperature2 > 35:
    print("Aviso por la temperatura")
else: 
    print("Parametros normales")

#condiciones anidadas 
print('#####Condiciones anidadas #######')
temperature3 = 9 

if temperature3 < 20:
    if temperature3 <10:
        print('Nivel azul')
    else: 
        print('Nivel verde')
else: 
    if temperature3 < 30: 
        print('Nivel naranja')
    else: 
        print('Nivel rojo')

#sentencia elif 
print('#####Sentencia elif #######')
nota = float(input("Introduzca su nota:  "))
if 0 <= nota and nota < 5:
    print("Estas en suspenso, F")
elif 5 <= nota and nota < 7:
    print('Aprobado')
elif 7 <= nota and nota < 9:
    print('Notable') 
elif 9 <= nota and nota <= 10:
    print('Sobresaliente')
else: 
    print("Nota fuera de rango")