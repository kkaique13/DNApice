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

        elif distanciaPercorrida >= chegada:
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
            print(f"O organismo {organismo.nome} ficou muito desidratado e morreu...")
            vitimas.append(organismo.nome)
            organismos.remove(organismo)
            time.sleep(1.5)
            break

        #Vendo se o organismo está com a energia muito baixa
        if organismo.energia <= 40:
            print(f"O organismo {organismo.nome} está com a energia muito baixa! Descanse um pouco!")
            print(f"A taxa de desidratação do organismo {organismo.nome} aumentou!\n")
            organismo.taxaDesidratacao += 0.2
        
        #Vendo se o organismo tá muito quente ou frio
        if organismo.temperatura > 42:
            os.system('cls')
            print(f"O organismo {organismo.nome} ficou muito quente e morreu...")
            vitimas.append(organismo.nome)
            organismos.remove(organismo)
            time.sleep(1.5)
            break
        
        elif organismo.temperatura > 40:
            print(f"O organismo {organismo.nome} está com insolação!")
            print("Fique na sombra o máximo possível pra diminuir a sua temperatura!\n")
            organismo.taxaDesidratacao += 0.3
            
        elif organismo.temperatura < 30:
            os.system('cls')
            print(f"O organismo {organismo.nome} ficou muito frio e morreu...")
            vitimas.append(organismo.nome)
            organismos.remove(organismo)
            time.sleep(1.5)
            break
        
        elif organismo.temperatura < 34:
            print(f"O organismo {organismo.nome} está com hipotermia!")
            print("Fique na sol o máximo possível pra aumentar a sua temperatura!\n")
            organismo.taxaDesidratacao += 0.3
            
        #Menu
        print("1- Fazer o organismo correr")
        print("2- Fazer o organismo andar")
        print("3- Beber água do cantil")
        print("4- Ficar no sol")
        print("5- Ficar na sombra")
        print("6- Encher cantil")
        print("7- Desistir")
        try:
            es = int(input("\nEscolha uma das opções: \n"))

            match es:
                
                #Correr
                case 1:
                    os.system('cls')
                    if organismo.energia - 20 <= 0:
                        print(f"O organismo {organismo.nome} está com a energia muito baixa! Descanse um pouco!\n")
                    else:
                        organismo.correr()
                        distanciaPercorrida += 10

                #Andar
                case 2:
                    os.system('cls')
                    if organismo.energia - 10 <= 0:
                        print(f"O organismo {organismo.nome} está com a energia muito baixa! Descanse um pouco!\n")
                    else:
                        organismo.andar()
                        distanciaPercorrida += 5

                #Beber água
                case 3:
                    os.system('cls')
                    if organismo.hidratacao >= 100:
                        os.system('cls')
                        print("Hidratação está máximizada!\n")
                    else:
                        organismo.beberAgua()

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
                    if organismo.cantil >= 100:
                        os.system('cls')
                        print("O cantil está cheio!")
                    else:
                        if distanciaPercorrida % 25 == 0:
                            os.system('cls')
                            organismo.encherCantil()
                        else:
                            os.system('cls')
                            print("Não há nenhuma fonte de água por perto, faça o organismo correr um pouco mais!")

                #Desistir
                case 7:
                    vida = input("Tem certeza? (s/n)\n")
                    if vida.lower() == 's':
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
                
                case _:
                    os.system('cls')
                    print("Opção inválida!")
        except ValueError:
            os.system('cls')
            print("Opção inválida!")