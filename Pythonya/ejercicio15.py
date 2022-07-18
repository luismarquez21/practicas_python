# Se cargan por teclado tres números distintos. 
# Mostrar por pantalla el mayor de ellos.
num1 = int(input("Ingrese primer numero 1:"))
num2 = int(input("Ingrese segunda numero 2:"))
num3 = int(input("Ingrese tercer numero 3:"))
if num1>num2: 
    if num1>num3:
        print(num1)
    else:
        print(num3)

else: 
    if num2>num3:
        print(num2)
    else:
        print(num3)


""" 
if num1 > num2 and num1 > num3:
    print("El mayor es el numero 1:" , num1)
else:
    if num2 > num1 and num2 > num3:
        print("El mayor es el numero 2:" , num2)
    else: 
         print("El mayor es el numero 3:" , num3)
"""