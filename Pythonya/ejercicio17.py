"""
Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras
 y muestre un mensaje indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si
  el número de cifras es mayor.
"""
num = int(input("Ingrese un numero: "))
if num <10:
    print("tiene una cifra")
else: 
    if num<100:
        print("Tiene 2 digitos")
    else: 
        if num<1000: 
            print("tienes 3 digitos")
        else: 
            print("Error de entrada de datos")
print("fin del programa")