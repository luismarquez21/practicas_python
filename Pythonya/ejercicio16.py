# Se ingresa por teclado un valor entero, 
# mostrar una leyenda que indique si el número es positivo, 
# negativo o nulo (es decir cero)

num = int(input("Ingrese un numero: "))
if num > 0:
    print("El numero es positivo")
else:
    if num == 0:
        print("Nuemro es nulo es 0")
    else:
        print("El numero es negativo")