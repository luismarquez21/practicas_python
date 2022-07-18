#Parámetros por Referencia y Valor en Funciones: Curso de Programación con Python #9

def doblar(referencia, valor):
    referencia *= 2
    valor *= 2
    print ("DURANTE", referencia, valor)

estructura = ["a", "b", "c"]
primitiva = "abc"

print("Antes", estructura, primitiva)
doblar(estructura, primitiva)
print("DESPUES", estructura, primitiva)

print("_________________________________________")
#Veamos un ejemplo de paso por valor. 
x = 10 
def funcion(entradar): 
    entradar = 0 

funcion(x) #entro de la función se crea una copia local de x, por lo que la variable original no es modificada.
print(x) # 10

print("_________________________________________")
y = [10, 20, 30]
def funcion_x(entrada):
    entrada.append(40)

funcion_x(y)
print(y)


print("_________________________________________")
# por valor
def test(n): # parametros
    print("Valor inicial", n)
    n *= 10
    print("Valor modificado", n)

n = 10
test(n) # argumentos
print("Valor ene el cuerpo ppal.", n)


print("_________________________________________")

print("_________________________________________")
# por referencia 
def test(n): # parametros
    print("Valor inicial", n)
    for i in range(len(n)):
        n[i] *= 2
    print("Valor modificado", n)

n = [1, 10, 100]
test(n) # argumentos
print("Valor ene el cuerpo ppal.", n)