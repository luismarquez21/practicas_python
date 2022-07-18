#propiedades()
class Empleado: 
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario
    def getnombre(self):
        return self.__nombre 
    def getsalario(self): 
        return self.__salario 
    def setnombre(self,nombre):
        self.__nombre = nombre 
    def setsalario(self,salario):
        self.__salario = salario 
    def delnombre(self):
        del self.__nombre 
    def delsalario(self):
        del self.__salario 

empleado_uno = Empleado('victor', 2000)
print(empleado_uno.getnombre(),',',empleado_uno.getsalario())
empleado_uno.setnombre('raul')
print(empleado_uno.getnombre(),',',empleado_uno.getsalario())
