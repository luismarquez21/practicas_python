#Metodos
#Class nombre de la clase:
# DEF nombre del metodo (SELF):
#SELF.nombre de la variable = ALGORITMO

class Matematicas: 
    def suma(self): 
        self.n1 = 2 
        self.n2 = 3 

s = Matematicas()
s.suma()
print(s.n1 + s.n2)