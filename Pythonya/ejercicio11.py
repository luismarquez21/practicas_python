# Realizar un programa que solicite la carga por teclado de dos números, 
# si el primero es mayor al segundo informar su suma y diferencia,
#  en caso contrario informar el producto  y la división del primero respecto al segundo.

num1 = int(input("Ingrese primer valor: "))
num2 = int(input("ingrese el segundo valor: ")) 
if num1>num2: 
    print("Suma de los 2 numeros", num1 + num2, "Diferencia de los 2 numeros", num1 - num2)
else: 
    print("Producto de los 2 numeros:", num1 * num2 , "Division de los 2 numeros:", num1 / num2)

