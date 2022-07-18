# ciclo For

filosofos = ["Marx", "Mileto", "Platon", "Socrates"]


#for filosofo in filosofos:
#    print(filosofo)


for filosofo in filosofos:
    if filosofo == 'Platon':
        print(f'{filosofo} - es el mejor.')
        break
    else: 
        print(filosofo)
