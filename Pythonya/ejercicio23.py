# Se ingresan por teclado tres números, si al menos uno de los valores ingresados es menor a 10,
#  imprimir en pantalla la leyenda "Alguno de los números es menor a diez".

val1=int(input("Ingrese valor 1: "))
val2=int(input("Ingrese valor 2:"))
val3=int(input("Ingrese valor 3: "))

if val1 < 10 or val2 < 10 or val3 < 10:
    print("Alguno de los números es menor a diez")