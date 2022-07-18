#metodo constructor


class Persona: 
    pass
    def __init__(self, nombre, año):
        self.nombre = nombre 
        self.año = año
    def descripcion(self):
        return '{} tiene {} años'.format(self.nombre, self.año)
    
    def comentario(self, frase): 
        return '{} dice: {}'.format(self.nombre, frase)

doctor = Persona('JOSE', 28)
print(doctor.nombre)
print(doctor.descripcion())
print(doctor.comentario('hola que tal'))


