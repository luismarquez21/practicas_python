# Los operadores son símbolos que le indican al intérprete que realice una operación 
# específica, como aritmética, comparación, lógica, etc.
# Estos son los diferentes tipos de operadores en Python:
# e{{ee{eee{{{{{{ee{{\\\^^}}}}}}}}}}}

# 1. Operadores aritméticos
""" +	Realiza Adición entre los operandos """
suma = 12 + 3 # 15
print("La suma es:", suma)
""" - Realiza Substracción entre los operandos """
resta = 12 - 3 #9 
print("La resta es:", resta)
""" *	Realiza Multiplicación entre los operandos """
multipicador = 12 * 3 # 36 
print("La Multiplicación es: ", multipicador)
""" / Realiza División entre los operandos	"""
division = 12 / 3 # 4
print("La division es:" , division)
"""  %	Realiza un módulo entre los operandos """ 
modulo = 16 % 3 # 1
print("Realiza un modulo entre los operandos: ", modulo)
""" ** Realiza la potencia de los operandos """
potencia = 12**3 # 1728 
""" //  Realiza la división con resultado de número entero	 """
division_entero = 18//5 #3 

# Nota: Para obtener el resultado en tipo flotante,
#  uno de los operandos también debe ser de tipo flotante.

print("__________________________________________________________________")
print("##################################################################")
print("__________________________________________________________________")
# 2. Operadores relacionales 
# Un operador relacional se emplea para comparar y establecer la relación entre ellos. 
# Devuelve un valor booleano (true o false) basado en la condición.
""" >	Devuelve True si el operador de la izquierda es mayor que el operador de la derecha"""
# Mayor que: 3 > 2 True (verdadero)
# Mayor que: 3 > 5 False (False)
Mayor_que = 12 > 3
print("12 > 3: ", Mayor_que) #12 > 3 devuelve True
Mayor_que2 = 2 > 3
print("2 > 3: ", Mayor_que2)#2 > 3 devuelve False
""" <	Devuelve True si el operador de la derecha es mayor que el operador de la izquierda	12  """
Menor_que = 12 < 3 
print("12 < 3: ", Menor_que) #12 < 3 devuelve False

Menor_que2 = 2 < 3 
print("2 < 3: ", Menor_que2) #2 < 3 devuelve True

""" ==	Devuelve True si ambos operandos son iguales """
igual = 12 == 3
print("12 == 3:", igual)#12 == 3 devuelve False

igual = 12 == 12
print("12 == 12:", igual) #12 == 3 devuelve False

""">=	Devuelve True si el operador de la izquierda es mayor o igual que el operador de la derecha"""
Mayor_igual = 12 >= 3 
print("12 >= 3:", Mayor_igual)# 12 >= 3 devuelve True

Mayor_igual2 = 1 >= 3 
print("1 >= 3:", Mayor_igual2)# 12 >= 3 devuelve False

"""<=	Devuelve True si el operador de la derecha es mayor o igual que el operador de la izquierda	12 <= 3 devuelve False"""
Menor_igual = 12 >= 3 
print("12 <= 3:", Mayor_igual)# 12 >= 3 devuelve True

Menor_igual2 = 1 >= 3 
print("1 <= 3:", Mayor_igual2)# 1 >= 3 devuelve False
"""!=	Devuelve True si ambos operandos no son iguales	12 != 3 devuelve True""" 
No_igual = 12 != 3
print("12 != 3", No_igual) #12 != 3 devuelve True

No_igual2 = 3 != 3
print("3 != 3", No_igual2) #12 != 3 devuelve False


# 3.  Operadores Bit a Bit
# 4. Operadores de asignación
# 5. Operadores lógicos
# 6. Operadores de pertenencia
# 7. Operadores de identidad