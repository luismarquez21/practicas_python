# Se ingresan tres notas de un alumno, 
# si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado"
nota1 = int(input("Ingresa nota 1:"))
print(nota1)
nota2 = int(input("Ingresa nota 1:"))
print(nota2)
nota3 = int(input("Ingresa nota 1:"))
print(nota3)
promedio = (nota1 + nota2 + nota3)/3
print("Promedio:", promedio)
if promedio >= 7: 
    print("Promocionado")
else:
    print("No promocionado")



