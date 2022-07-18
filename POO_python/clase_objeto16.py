#clase y estatico 
import math
class Pastel: 
    def __init__(self, ingredientes,tamaño):
        self.ingredientes = ingredientes 
        self.tamaño = tamaño 
    def __repr__(self):
        return (f'Pastel({self.ingredientes}, 'f'{self.tamaño})')
    
    def area(self):
        return self.tamaño_area(self.tamaño)
    
    @staticmethod
    def tamaño_area(A):
        return A ** 2 * math.pi

nuevo_pastel = Pastel(['harina', 'azucar', 'leche', 'crema'], 4)
print(nuevo_pastel.tamaño_area(12))


