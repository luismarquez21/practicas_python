#Ejemplo 2 de un metodo constructor

class Persona:
    nombre = ""
    apellidos = ""
    ntelefono = ""
    nID = ""
    sexo = ""


    def saludar(self): 
        saludo = "Hola, mi nombre es: " + self.nombre
        return saludo

p1 = Persona()
print (p1.saludar())