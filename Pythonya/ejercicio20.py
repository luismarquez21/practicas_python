# 8 - Condiciones compuestas con operadores lógicos
# Operador and
num1=int(input("Ingrese primer valor:"))
num2=int(input("Ingrese segundo valor:"))
num3=int(input("Ingrese tercer valor:"))

print("El mayor de los tres valores es:")
if num1 > num2 and num1 > num3:
    print(num1)
else: 
    if num2 > num3:
        print(num2)
    else: 
        print(num3)
print("__________________________________________________________________")
print("##################################################################")
print("__________________________________________________________________")

# Operador or
dia=int(input("Ingrese nro de dia: "))
mes=int(input("Ingrese nro de mes:"))
año=int(input("Ingrese nro de año:"))

if mes==1 or mes==2 or mes==3:
    print("Corresponde al primer trimestre")

