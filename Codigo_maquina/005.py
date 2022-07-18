#funciones en python
# Funciones en Python: Curso de Programación con Python #8
def suma_dos_numeros(a, b): 
    suma = a+b 
    return suma 

def suma_muchos_numeros(*numeros):
    suma = 0
    for numero in numeros: 
        suma = suma + numero
    return suma 

print("Suma: ", suma_muchos_numeros(1,2,3,4,5))

print("El resultado de 3 + 4", suma_dos_numeros(3, 4))
print("El resultado de 13 + 4", suma_dos_numeros(13, 4))

print("__________________________________________________")
def formatea_nombre(nombre, paterno, materno):
    formato = nombre.upper()+ " " + paterno.capitalize()+ " " + materno.capitalize()
    return formato

print(formatea_nombre("JUAn", "Hernandez", "JIMenez"))


print("__________________________________________________")

def crea_clave(nombre, fecha_nacimiento):
    clave = ""
    for vocablo in nombre.split(): 
        clave = clave + vocablo[0]
    fecha_nacimiento = str(fecha_nacimiento)
    return clave+fecha_nacimiento[-2:]

print(crea_clave("JUAN HERNANDEZ JIMENEZ", 1980))



