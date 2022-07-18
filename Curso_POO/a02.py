#Los atributos son las propiedades de un objeto

class NinjaPrincipal:
    HP = 100
    resistencia = 50
    XP = 1
    vidas = 3
    def game_over(self): 
        print("Game Over") 

ninja = NinjaPrincipal()
print(ninja.HP)

ninja.HP = 0 
if ninja.HP == 0 and ninja.vidas == 0: 
    ninja.game_over()
