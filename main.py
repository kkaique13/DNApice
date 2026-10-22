import time
from organismo import Organismo
from bioma import Bioma
from jogo import game
from utils import limpar

def nomeEmUso(nome: str, *listas) -> bool:
    return any(nome.lower() == n.lower() for lista in listas for n in lista)

if __name__ == "__main__":
    # Variáveis e listas
    organismos = []
    vitimas = []
    vencedores = []
    ambiente = Bioma("Caatinga", 30.0)

    while True:
        # Menu
        print("\nCAATINGA: NÃO SE DESIDRATE!")
        print("1- Jogar")
        print("2- Criar organismo")
        print("3- Mostrar organismos vivos")
        print("4- Mostrar organismos mortos")
        print("5- Mostrar organismos vencedores")
        print("6- Sair")
        try:
            es = int(input("Escolha sua opção: \n"))
        except ValueError:
            limpar()
            print("Opção inválida!")
            continue

        match es:
            # Jogar
            case 1:
                if len(organismos) < 1:
                    limpar()
                    print("Nenhum organismo para selecionar! Crie um organismo para jogar!\n")
                    continue

                for avatar in organismos:
                    print(f"{avatar.nome}")

                av = input("\nEscolha o organismo pro experimento: \n").strip()
                escolhido = next((o for o in organismos if o.nome.lower() == av.lower()), None)

                if escolhido is None:
                    limpar()
                    print("Organismo inválido!")
                else:
                    print("O jogo vai começar! Boa sorte!")
                    time.sleep(1)
                    game(escolhido, organismos, vitimas, vencedores)
                    limpar()

            # Criar organismo
            case 2:
                nome = input("\nDigite o nome do organismo: \n").strip()
                limpar()
                if not nome:
                    print("Nome inválido!")
                elif nomeEmUso(nome, vitimas):
                    print("Não dá para reviver os mortos.")
                elif nomeEmUso(nome, [o.nome for o in organismos], vencedores):
                    print("Já existe um organismo com esse nome!")
                else:
                    avatar = Organismo(nome, ambiente)
                    organismos.append(avatar)
                    print(f"\nOrganismo {avatar.nome} criado!")

            # Ver vivos
            case 3:
                limpar()
                if len(organismos) == 0:
                    print("\nNenhum organismo criado!")
                else:
                    for avatar in organismos:
                        print(f"\n{avatar.nome}")

            # Ver mortos
            case 4:
                limpar()
                if len(vitimas) == 0:
                    print("\nNenhum organismo foi morto! (por enquanto)")
                else:
                    for vitima in vitimas:
                        print(f"\n{vitima}")

            # Ver vencedores
            case 5:
                limpar()
                if len(vencedores) == 0:
                    print("\nNenhum organismo venceu ainda!")
                else:
                    for vencedor in vencedores:
                        print(f"\n{vencedor}")

            # Sair
            case 6:
                print("Obrigado por jogar!\n")
                break

            case _:
                limpar()
                print("Opção inválida!")