class Personaje:
    

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre 
        self.__fuerza = fuerza 
        self.__inteligencia = inteligencia 
        self.__defensa = defensa 
        self.__vida = vida 
    # funcion del estado del objeto o el valor de sus atributos
    def atriburtos(self):
        print(self.__nombre, ":", sep="")
        print(".Fuerza:", self.__fuerza)
        print(".Inteligencia:", self.__inteligencia)
        print(".Defensa:", self.__defensa)
        print(".Vida:", self.__vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa 

    def esta_vivo(self):
        return self.__vida > 0 

    def morir(self):
        self.__vida = 0
        print(self.nombre, "Ha muerto")
    
    def daño(self, enemigo): 
        return self.__fuerza - enemigo.__defensa 

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.__vida = enemigo.__vida - daño 
        print(self.__nombre, "ha realizado", daño, "puntos de daño a", enemigo.__nombre)
        if enemigo.esta_vivo():
            print("La vida de", enemigo.__nombre, "es", enemigo.__vida)
        else: 
            enemigo.__morir()

    def get_fuerza(self):
        return self.__fuerza
    
    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print("Error, has introducido un valor negativo")
        else:
            self.__fuerza = fuerza


mi_personaje = Personaje("BitBoss", 10, 1, 5, 0)
mi_enemigo = Personaje("Enemigo Stando", 8, 5, 3, 5)

mi_personaje.set_fuerza(5)
mi_personaje.atriburtos()



