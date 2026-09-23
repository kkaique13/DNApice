from organismo import Organismo
from bioma import Bioma
from jogo import Game
import os
import time
if __name__ == "__main__":
    organismos = []
    vitimas = []
    ambiente = Bioma("Caatinga", 30.0)
    
    while True:
        print("\nCAATINGA: NÃO SE DESIDRATE!")
        print("1- Jogar")
        print("2- Criar organismo")
        print("3- Mostrar organismos vivos")
        print("4- Mostrar organismos mortos")
        print("5- Sair")
        es = int(input("Escolha sua opção: \n"))

        match es:
            case 1:
                if len(organismos) < 1:
                    print("Nenhum organismo para selecionar! Crie um organismo para jogar!\n")

                for avatar in organismos:
                    print(f"{avatar.nome}")

                av = input("Escolha o organismo pro experimento: \n")
                encontrado = False
                for avatar in organismos:
                    if avatar.nome == av:
                        encontrado = True
                        print("O jogo vai começar! Boa sorte!")
                        time.sleep(1)
                        game(avatar, organismos, vitimas)
                        os.system('cls')

                if encontrado == False:
                    print("Organismo inválido!")
            
            case 2:
                nome = input("\nDigite o nome do organismo: \n")
                morto = False
                for vitima in vitimas:
                    if nome.lower() == vitima.lower():
                        morto = True
                        os.system('cls')
                        print("Não dá para reviver os mortos.")
                if morto == False:
                    avatar = Organismo(nome, ambiente)
                    organismos.append(avatar)
                    os.system('cls')
                    print(f"\nOrganismo {avatar.nome} criado!")

            case 3:
                if len(organismos) == 0:
                    os.system('cls')
                    print("\nNenhum organismo criado!")
                else:
                    os.system('cls')
                    for avatar in organismos:
                        print(f"\n{avatar.nome}")

            case 4:
                if len(vitimas) == 0:
                    os.system('cls')
                    print("\nNenhum organismo foi morto! (por enquanto)")
                else:
                    os.system('cls')
                    for vitima in vitimas:
                        print(f"\n{vitima}")

            case 5:
                print("Obrigado por jogar!\n")
                break
