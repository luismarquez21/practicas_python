#Implementar una función recursiva que imprima en forma descendente de 5 a 1 de uno en uno

def imprimir(x):
    if x>2: 
        print(x)
        imprimir(x-1)

imprimir(10)