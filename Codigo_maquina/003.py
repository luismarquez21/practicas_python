#Ciclos While & For en Python (Estructuras Cíclicas): Curso de Programación con Python #7
0<10 #true
1<10 #true
2<10 #true
9<10 #true
10<10 #False

contador = 1
while contador > -1:
    print("Iteracion ", contador)
    #contador+=1 # contador = contador + 1 // acumulador
    contador = contador -1 # contador en decremento

print("Termina Ejecucion")

total = 0# acumulador  que guardara la suma 
num_sumas = 5 
contador = 0

while contador < num_sumas: 
    num = int(input("Ingresa un numero: "))
    total = total + num 
    contador += 1
print("El total de la suma ",total)

print("Termina Ejecucion 2")
#contraseña 
autorizacion = False
while autorizacion == False: 
    contrasena = input("Ingresa tu contrseña: ")
    if contrasena == "123456":
        autorizacion = True
    else: 
        print("Acceso denegado")
print("Ingrese al sistema exitosamente")

print("Termina Ejecucion 3")
