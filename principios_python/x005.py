# ¿Qué es args y kwargs en python?
#*args
""" 
def unafuncion(arg1, arg2,arg3, arg4):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)

unafuncion("hola", "i", "o", "y")
"""

def unafuncion(*args):
    print(args)
unafuncion("hola", "i", "o", "y", "maradona", "basura", "petroleo")

def total(*args):
    total = sum(args)
    print(total)

total(300, 500, 433, 423424, 324)

#**kargs

def empleado(**kwargs):
   for key, value in  kwargs.items():
        print(f"{key} : {value}") 

empleado(nombre="carlos", puesto="programador", lenguaje="java")
#keyword arguments 

# Clases 

class Carro:
    def __init__(self, color, marca):
        self.color = color
        self.marca = marca

class Tesla(Carro):

    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.marca = "Tesla"

