#Polimorfismo
""""
class Auto:
    rueda = 4
    def despazamiento(self):
        print('el auto se desplaza sobre 4 ruedas')


class Moto:
    rueda = 2
    def despazamiento(self):
        print('La moto se desplaza sobre 2 ruedas')
"""

class Animales:
    def __init__(self,nombre):
        self.nombre = nombre
    def tipo_animal(self):
        print('animal')
        pass
    
class Leon(Animales):
    def tipo_animal(self):
        print('animal salvaje')

class Perro(Animales):
    def tipo_animal(self):
        print('animal domestico')

nuevo_animal = Leon('SIMBA')
nuevo_animal.tipo_animal()

nuevo_animal2 = Perro('REX')
nuevo_animal2.tipo_animal()



