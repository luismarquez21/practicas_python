# Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero con el segundo y 
# a este resultado se lo multiplica por el tercero.

val1=int(input("Ingrese valor 1: "))
val2=int(input("Ingrese valor 2: "))
val3=int(input("Ingrese valor 3: "))

if val1 == val2 and val2  == val3:
    suma = val1 + val2 
    print("Suma del primero con el segundo valor: ")
    print(suma)
    multiplicacion_valor = suma * val3
    print("Resultado de la suma de los 2 primeros + la multiplicacion del 3")
    print(multiplicacion_valor)