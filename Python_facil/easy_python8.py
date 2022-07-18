intentos = 3 
while intentos > 0: 
    if input(">>> Escriba la contraseña:") == "BitBoss": 
        print("¡Correcta!")
        break 
    intentos = intentos -1 
    print("Contraseña incorrecta")
else: 
    print("Se te acaron los intentos :( ")    