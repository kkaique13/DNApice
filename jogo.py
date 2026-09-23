from organismo import Organismo
import os
import time
def Game(organismo:Organismo):
    os.system('cls')
    distanciaPercorrida = 75
    chegada = 100
    while True:
        organismo.mostrarStatus()
        print(f"Corra {chegada}Km para ganhar o jogo!")
        print(f"Km percorridos: {distanciaPercorrida}")
        if distanciaPercorrida < chegada:
            print(f"Km faltando: {chegada - distanciaPercorrida}")
        elif distanciaPercorrida == chegada:
            print(f"Km faltando: {distanciaPercorrida}")
        else:
            print(f"Km faltando: {chegada - distanciaPercorrida}")
        print("1- Fazer o organismo correr")
        print("2- Beber água do cantil")
        print("3- Ficar no sol") #Como benefício, vai diminuir a taxa de desidratação do organismo por ele estar se acostumando com o sol, mas ele ainda vai desidratar mais de imediato
        print("4- Ficar na sombra")
        print("5- Desistir")
        es = int(input("\nEscolha uma das opções: \n"))
        match es:
            case 1:
                os.system('cls')
                organismo.correr()
            case 2:
                os.system('cls')
                organismo.beberAgua()
            case 3:
                os.system('cls')
                organismo.ficarNoSol()
            #case 4:
                #os.system('cls')
                #organismo.ficarNaSombra()
            case 5:
                vida = input("Tem certeza? (s/n)")
                if vida == 's':
                    break
                else:
                    print("Não desista ainda! Tenha determinação!")
                    time.sleep(1)
                    os.system('cls')