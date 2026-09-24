from organismo import Organismo
import os
import time

def game(organismo:Organismo, organismos:list, vitimas:list) -> None:
    os.system('cls')
    distanciaPercorrida = 0
    chegada = 100
    while True:
        #Mostra os status do organismo
        organismo.mostrarStatus()

        #Conferindo a distância percorrida e a que falta
        print(f"Corra {chegada}Km para ganhar o jogo!")
        print(f"Km percorridos: {distanciaPercorrida}")
        if distanciaPercorrida < chegada:
            print(f"Km faltando: {chegada - distanciaPercorrida}")

        elif distanciaPercorrida == chegada:
            os.system('cls')
            print("Km faltando: 0")
            print("Parabéns! Você ganhou!")
            print("Voltando ao menu principal...")
            time.sleep(1.5)
            break

        else:
            print(f"Km faltando: {chegada - distanciaPercorrida}")

        #Vendo se o organismo está muito desidratado
        if organismo.hidratacao <= 0:
            os.system('cls')
            print("O organismo ficou muito desidratado e morreu...")
            vitimas.append(organismo.nome)
            organismos.remove(organismo)
            time.sleep(1.5)
            break
        
        #Menu
        print("1- Fazer o organismo correr")
        print("2- Fazer o organismo andar")
        print("3- Beber água do cantil")
        print("4- Ficar no sol")
        print("5- Ficar na sombra")
        print("6- Encher cantil")
        print("7- Desistir")
        es = int(input("\nEscolha uma das opções: \n"))

        match es:
            
            #Correr
            case 1:
                os.system('cls')
                if organismo.energia - 20 <= 0:
                    print("O organismo está com a energia muito baixa! Descanse um pouco!")
                else:
                    organismo.correr()
                    distanciaPercorrida += 10

            #Andar
            case 2:
                os.system('cls')
                if organismo.energia - 10 <= 0:
                    print("O organismo está com a energia muito baixa! Descanse um pouco!")
                else:
                    organismo.andar()
                    distanciaPercorrida += 5

            #Beber água
            case 3:
                os.system('cls')
                if organismo.cantil > 0:
                    organismo.beberAgua()
                else:
                    os.system('cls')
                    print("O cantil está com muita pouca água! Encha-o para conseguir beber água")

            #Ficar no sol
            case 4:
                os.system('cls')
                organismo.ficarNoSol()

            #Ficar na sombra
            case 5:
                os.system('cls')
                organismo.ficarNaSombra()

            #Encher o cantil
            case 6:
                if distanciaPercorrida % 25 == 0:
                    os.system('cls')
                    organismo.encherCantil()
                else:
                    os.system('cls')
                    print("Não há nenhuma fonte de água por perto, faça o organismo correr um pouco mais!")

            #Desistir
            case 7:
                vida = input("Tem certeza? (s/n)\n")
                if vida == 's':
                    os.system('cls')
                    vitimas.append(organismo.nome)
                    organismos.remove(organismo)
                    print("O organismo não aguentou a pressão e desistiu de continuar...")
                    time.sleep(1.5)
                    break
                else:
                    print("Não desista ainda! Tenha determinação!")
                    time.sleep(1)
                    os.system('cls')