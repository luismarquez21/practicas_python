class NinjaPrincipal:
    HP = 100
    resistencia = 50
    XP = 1
    vidas = 3
    def game_over(self): 
        print("Game Over") 

ninja = NinjaPrincipal()
print(ninja.HP)

ninja_enemigo = NinjaPrincipal()
ninja_enemigo.HP = 25
ninja_enemigo.resistencia = 10
ninja_enemigo.vidas = 1  
print(ninja_enemigo.HP, ninja_enemigo.resistencia, ninja_enemigo.vidas)
