import time
from organismo import (Organismo, DISTANCIA_CORRER, DISTANCIA_ANDAR, LIMITE_ENERGIA_BAIXA,)
from utils import limpar

CHEGADA = 100        # Km
INTERVALO_AGUA = 25  # Km entre fontes de água

def _morrer(organismo: Organismo, organismos: list, vitimas: list, motivo: str) -> None:
    limpar()
    print(f"O organismo {organismo.nome} {motivo}")
    vitimas.append(organismo.nome)
    organismos.remove(organismo)
    time.sleep(1.5)

def _mostrarAlertas(organismo: Organismo) -> None:
    if organismo.energia <= LIMITE_ENERGIA_BAIXA:
        print(f"O organismo {organismo.nome} está com a energia muito baixa! Descanse um pouco!")
        print("Enquanto estiver cansado, a taxa de desidratação aumenta a cada ação!\n")
    if 40 < organismo.temperatura <= 42:
        print(f"O organismo {organismo.nome} está com insolação!")
        print("Fique na sombra o máximo possível pra diminuir a sua temperatura!\n")
    elif 30 <= organismo.temperatura < 34:
        print(f"O organismo {organismo.nome} está com hipotermia!")
        print("Fique no sol o máximo possível pra aumentar a sua temperatura!\n")

def game(organismo: Organismo, organismos: list, vitimas: list, vencedores: list) -> None:
    limpar()
    distanciaPercorrida = 0

    while True:
        # Status
        organismo.mostrarStatus()

        # Distância
        print(f"Percorra {CHEGADA}Km (andando ou correndo) para ganhar o jogo!")
        print(f"Fontes de água a cada {INTERVALO_AGUA}Km")
        print(f"Km percorridos: {distanciaPercorrida}")

        if distanciaPercorrida >= CHEGADA:
            limpar()
            print("Km faltando: 0")
            print("Parabéns! Você ganhou!")
            print("Voltando ao menu principal...")
            organismos.remove(organismo)
            vencedores.append(organismo.nome)
            time.sleep(1.5)
            break
        
        print(f"Km faltando: {CHEGADA - distanciaPercorrida}\n")

        # Mortes
        if organismo.hidratacao <= 0:
            _morrer(organismo, organismos, vitimas, "ficou muito desidratado e morreu...")
            break

        if organismo.temperatura > 42:
            _morrer(organismo, organismos, vitimas, "ficou muito quente e morreu...")
            break

        if organismo.temperatura < 30:
            _morrer(organismo, organismos, vitimas, "ficou muito frio e morreu...")
            break

        # Alertas (não alteram nada, só avisam)
        _mostrarAlertas(organismo)

        # Menu
        print("1- Fazer o organismo correr")
        print("2- Fazer o organismo andar")
        print("3- Beber água do cantil")
        print("4- Ficar no sol")
        print("5- Ficar na sombra")
        print("6- Encher cantil")
        print("7- Desistir")

        try:
            es = int(input("\nEscolha uma das opções: \n"))
        except ValueError:
            limpar()
            print("Opção inválida!")
            continue

        acaoValida = False  # só ações válidas gastam turno e geram penalidades

        match es:
            # Correr
            case 1:
                limpar()
                if not organismo.podeCorrer():
                    print(f"O organismo {organismo.nome} está com a energia muito baixa! Descanse um pouco!\n")
                else:
                    organismo.correr()
                    distanciaPercorrida += DISTANCIA_CORRER
                    acaoValida = True

            # Andar
            case 2:
                limpar()
                if not organismo.podeAndar():
                    print(f"O organismo {organismo.nome} está com a energia muito baixa! Descanse um pouco!\n")
                else:
                    organismo.andar()
                    distanciaPercorrida += DISTANCIA_ANDAR
                    acaoValida = True

            # Beber água
            case 3:
                limpar()
                if organismo.hidratacao >= 100:
                    print("Hidratação está maximizada!\n")
                else:
                    acaoValida = organismo.beberAgua()

            # Ficar no sol
            case 4:
                limpar()
                organismo.ficarNoSol()
                acaoValida = True

            # Ficar na sombra
            case 5:
                limpar()
                organismo.ficarNaSombra()
                acaoValida = True

            # Encher o cantil
            case 6:
                limpar()
                if organismo.cantil >= 100:
                    print("O cantil está cheio!\n")
                elif distanciaPercorrida % INTERVALO_AGUA == 0:
                    organismo.encherCantil()
                    acaoValida = True
                else:
                    proxima = (distanciaPercorrida // INTERVALO_AGUA + 1) * INTERVALO_AGUA
                    print("Não há nenhuma fonte de água por perto!")
                    print(f"A próxima fonte fica no Km {proxima}.\n")

            # Desistir
            case 7:
                vida = input("Tem certeza? (s/n)\n")
                if vida.strip().lower() == 's':
                    limpar()
                    vitimas.append(organismo.nome)
                    organismos.remove(organismo)
                    print("O organismo não aguentou a pressão e desistiu de continuar...")
                    time.sleep(1.5)
                    break
                print("Não desista ainda! Tenha determinação!")
                time.sleep(1)
                limpar()

            case _:
                limpar()
                print("Opção inválida!")

        if acaoValida:
            organismo.aplicarPenalidades()