#clase y estatico

class Pastel: 
    def __init__(self,ingredientes):
        self.ingredientes = ingredientes

    def __repr__(self):
        return f'pastel({self.ingredientes !r})'

    @classmethod
    def Pastel_chocolate(cls):
        return cls(['harina', 'leche', 'chocolate'])

    @classmethod
    def Pastel_vainilla(cls):
        return cls(['harina', 'leche', 'vainilla'])

print(Pastel.Pastel_chocolate())

    
