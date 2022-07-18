# Bucles infinitos
#El programador ha olvidado modificar la variable de control dentro del bucle 
# y el programa imprimirá números 1 indefinidamente:
i = 1
while i <= 10: 
    print(i, end="")
    i = i + 1 #Variable control del bucle que no tiene para para el bucle 

# El programador ha escrito una condición que se cumplirá siempre y 
# el programa imprimirá números consecutivos indefinidamente:
i = 1 
while i > 0: # condición que siempre se cumplirá
    print(i, end=" ")
    i += 1  
print("Fin del programa")

# Se aconseja expresar las condiciones como desigualdades en vez de comparar valores.
#  En el ejemplo siguiente, el programador ha escrito una condición que se cumplirá siempre
#  y el programa imprimirá números consecutivos indefinidamente:
i = 1
while i != 100: # <=100 deberia ser. condición que se cumplirá siempre y no para el ciclo
    print(i, end="")
    i += 2 
print("Fin del programa")