#Funciones recursivas 

def decrementar(n):
    if (n == 0): 
        print("Finalizo el conteo!")
    else: 
        n -= 1 
        print("El decremeto va en el #", n)
        decrementar(n)

decrementar(8)