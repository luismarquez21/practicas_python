"""
Problema:
Confeccionar un programa que pida por teclado tres notas de un alumno, 
calcule el promedio e imprima alguno de estos mensajes:
Si el promedio es >=7 mostrar "Promocionado".
Si el promedio es >=4 y <7 mostrar "Regular".
Si el promedio es <4 mostrar "Reprobado".
"""
nota1 = int(input("Ingrese primer nota:"))
nota2 = int(input("Ingrese segunda nota:"))
nota3 = int(input("Ingrese tercer nota:"))
prom=(nota1+nota2+nota3)/3
print("Promedio:", prom)
if prom>=7:
    print("Promocionado")
else: 
    if prom>=4: 
        print("Regular")
    else: 
        print("Reprobado")



