#funciones para atributos 

class Persona: 
    edad = 27 
    nombre = 'victor'
    pais = 'brazil'

doctor = Persona()

print('la edad del doctor es:', doctor.edad ,'años')
print('la edad del doctor es:', getattr(doctor, 'edad') ,'años')
print('el doctor tiene una edad?', hasattr(doctor, 'apellido') ) 

doctor1 = Persona()
print('antes era: ', doctor1.nombre)
setattr(doctor1, 'nombre', 'hector')
print('ahora se llama: ', doctor1.nombre)

doctor2 = Persona()
delattr(Persona, 'pais')
print(doctor.nombre)
print(doctor.edad)
print(doctor.pais)
