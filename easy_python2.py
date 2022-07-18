# a(b) => c
def decoradora(func):
    def nueva_funcion():
        print("Primero hago algo")
        func()
        print("hago otra cosa")
    return nueva_funcion

@decoradora
def saludame():
    print("Hola mundo!")

saludame() 