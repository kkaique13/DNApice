from organismo import Organismo
from bioma import Bioma
from jogo import Game
import os
import time

if __name__ == "__main__":
    organismos = []
    ambiente = Bioma("Caatinga", 30.0)
    while True:
        print("\nCAATINGA: NÃO SE DESIDRATE!")
        print("1- Jogar")
        print("2- Criar organismo")
        print("3- Mostrar organismos")
        print("4- Sair")
        es = int(input("Escolha sua opção: \n"))
        match es:
            case 1:
                if len(organismos) < 1:
                    es = print("Nenhum organismo para selecionar! Crie um organismo para jogar!\n")
                    break

                for avatar in organismos:
                    print(f"{avatar.nome}\n")

                av = input("Escolha o organismo pro experimento: \n")
                encontrado = False

                for avatares in organismos:
                    if avatares.nome == av:
                        encontrado = True
                        print("O jogo vai começar! Boa sorte!")
                        time.sleep(1)
                        Game(avatar)

                if encontrado == False:
                    print("Organismo inválido!")
            
            case 2:
                nome = input("\nDigite o nome do organismo: \n")
                avatar = Organismo(nome, ambiente)
                organismos.append(avatar)
                print(f"\nOrganismo {avatar.nome} criado!")

            case 3:
                if len(organismos) == 0:
                    print("\nNenhum organismo criado!")
                for avatar in organismos:
                    print(f"\n{avatar.nome}")

            case 4:
                print("Obrigado por jogar!\n")
                break
