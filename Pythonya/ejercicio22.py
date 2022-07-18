# Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10,
#  imprimir en pantalla la leyenda "Todos los números son menores a diez".

val1=int(input("Ingrese valor 1: "))
val2=int(input("Ingrese valor 2:"))
val3=int(input("Ingrese valor 3: "))

if val1 < 10 and val2 < 10 and val3 < 10:
    print("Todos los números son menores a diez")