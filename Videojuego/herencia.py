class Personaje:
    

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre 
        self.fuerza = fuerza 
        self.inteligencia = inteligencia 
        self.defensa = defensa 
        self.vida = vida 
    # funcion del estado del objeto o el valor de sus atributos
    def atributos(self):
        print(self.nombre, ":", sep="")
        print(".Fuerza:", self.fuerza)
        print(".Inteligencia:", self.inteligencia)
        print(".Defensa:", self.defensa)
        print(".Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa 

    def esta_vivo(self):
        return self.vida > 0 

    def morir(self):
        self.vida = 0
        print(self.nombre, "Ha muerto")
    
    def daño(self, enemigo): 
        return self.fuerza - enemigo.defensa 

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño 
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("La vida de", enemigo.nombre, "es", enemigo.vida)
        else: 
            enemigo.morir()

    
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada): 
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10  "))
        if opcion == 1: 
            self.espada = 8 
        elif opcion == 2:
            self.espada = 10
        else: 
            print("Numero de arma incorrecto")
    
    def atributos(self): 
        super().atributos()
        print(".Espada:", self.espada)
    
    def daño(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa 

class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro): 
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
    
    def atributos(self): 
        super().atributos()
        print(".Libro:", self.libro)
    
    def daño(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa 


        
goku = Personaje("Goku", 20, 15, 10, 100)
guts = Guerrero("Guts", 20, 15, 10, 100, 5)
vanessa = Mago("Vanessa",20, 15, 10, 100, 5)
goku.atacar(guts)
guts.atacar(vanessa)
vanessa.atacar(goku)
goku.atributos()
guts.atributos()
vanessa.atributos()





