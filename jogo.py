from organismo import Organismo
import os
import time

def game(organismo:Organismo, organismos:list, vitimas:list) -> None:
    os.system('cls')
    distanciaPercorrida = 0
    chegada = 100
    cantil = 100

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
        print("3- Ficar no sol")
        print("4- Ficar na sombra")
        print("5- Desistir")
        es = int(input("\nEscolha uma das opções: \n"))

        match es:
            case 1:
                os.system('cls')
                organismo.correr()

            case 2:
                os.system('cls')
                if cantil > 0:
                    organismo.beberAgua()
                else:
                    print("O cantil está com muita pouca água! Encha-o para conseguir beber água")

            case 3:
                os.system('cls')
                organismo.ficarNoSol()

            case 4:
                os.system('cls')
                organismo.ficarNaSombra()

            case 5:
                vida = input("Tem certeza? (s/n)\n")
                if vida == 's':
                    vitimas.append(organismo.nome)
                    organismos.remove(organismo)
                    break
                else:
                    print("Não desista ainda! Tenha determinação!")
                    time.sleep(1)
                    os.system('cls')