#Clases y Objetos ejemplo
class Perro:
    # Variable clase
    animal = "perro"

    def __init__(self, raza, edad, color):
        #Variable de instancia
        self.raza = raza 
        self.edad = edad 
        self.color = color
        self.hambre = 10
    
    def ladrar(self): 
        print("woofff woofff woofff")
    
    def comer(self, comida): 
        print("comiendo", comida, "...")

mi_perro = Perro("Labrador", 2, "Cafe")
mi_otro_perro = Perro("Pug", 5, "negro")

mi_perro.ladrar