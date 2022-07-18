#Se ingresa por teclado un número positivo de uno o dos dígitos (1..99)
#mostrar un mensaje indicando si el número tiene uno o dos dígitos.
#(Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)

digito = int(input("ingrese un numero positivo de uno o dos digitos (1..99): "))
if digito <= 9: 
    print("El numero tiene un digito")
else:
    print("El numero tiene 2 digitos")