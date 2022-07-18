#Decorador una funcion que crea funciones
def decorador(func): #A,B
    def nueva_funcion():
        print("Vamos a ejecutar la funcion")
        func()
        print("Se ejecuto la funcion")
    return nueva_funcion #C


@decorador 
def saluda(): 
    print("Hola mundo")

#A, B, C son funciones 
#A recibe como parametro B para poder crear C
saluda()

