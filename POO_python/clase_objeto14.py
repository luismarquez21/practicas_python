#f-strings

class Estudiante: 
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __repr__ (self): 
        return f" hola que tal soy {self.nombre} {self.apellido} {self.edad}"

nuevo_estudiante = Estudiante('victor', 'cruz', 17)
print(f"{nuevo_estudiante !r}")


