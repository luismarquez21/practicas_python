# IF con Python - Expresiones y Operadores Booleanos: Curso de Programación con Python #3
"""
Sistemas de orientacion vocacional

artes --> Teatro
deportes -> Medicina deportiva
matematicas -> Ingenieria 

"""

"""
artes = True
deportes = True 
matematicas = False


if artes and not matematicas: 
    print("Estudiar arquitectura")

"""

"""
Club juvenil deportivo
"""
edad = int(input("Introduce tu edad:  "))
if edad >= 10 and edad <= 14:
    print("Equipo Juvenil A")
elif edad > 14 and edad <= 17:
    print("Equipo juvenil B")
elif edad == 18: 
    print("Equipo profesional")   
else: 
    print("Eres demasiado pequeño o demasiado grande") 


