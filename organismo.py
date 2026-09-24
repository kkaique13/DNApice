from coracao import Coracao
from pulmao import Pulmao
from bioma import Bioma
from random import randint

class Organismo:
    def __init__(self, nome:str, bioma:Bioma) -> None:
        self.nome = nome
        self.tempoSol = 0
        self.hidratacao = 100
        self.temperatura = 36.5
        self.taxaDesidratacao = 1
        self.energia = 100
        self.cantil = 100
        self.bioma = bioma
        self.coracao = Coracao()
        self.pulmao = Pulmao()

    def suar(self) -> None:
        self.hidratacao -= 5 * self.taxaDesidratacao
        self.temperatura -= 0.5

    def correr(self) -> None:
        print("O organismo começou a correr!\n")
        self.coracao.acelerar()

        print(f"O batimento cardíaco do organismo {self.nome} aumentou!\n")
        self.pulmao.respirarMaisRapido()

        print(f"O organismo {self.nome} está respirando mais rápido!\n")
        self.hidratacao -= 25 * self.taxaDesidratacao
        self.energia -= 20

    def andar(self) -> None:
        print("O organismo começou a andar!\n")

        self.hidratacao -= 10 * self.taxaDesidratacao
        self.energia -= 10
    
    def ficarNoSol(self) -> None:
        print("O organismo está exposto ao calor!")

        if self.tempoSol >= 5 and self.hidratacao < 50:
            print("Atenção! O organismo ficou muito tempo no sol, o suor não é suficiente! Beba água!\n")
            self.temperatura += 0.5
            self.hidratacao -= 15 * self.taxaDesidratacao

        else:
            self.tempoSol += 1
            self.hidratacao -= 15  * self.taxaDesidratacao
            self.temperatura += 0.5
            self.taxaDesidratacao -= 0.1
            self.suar()
            print("O organismo suou pra manter a temperatura estável!\n")

    def ficarNaSombra(self) -> None:
        print("O organismo está descansando na sombra!")
        self.temperatura -= 0.5
        self.energia += 10

    def encherCantil(self) -> None:
        quantidadeEnchida = randint(10, 50)
        print(f"O organismo encheu o cantil com {quantidadeEnchida} de água!")
        self.cantil += quantidadeEnchida

    def beberAgua(self) -> None:
        print("O organismo bebeu água!\n")

        self.cantil -= 25
        self.hidratacao += 20
        self.temperatura -= 1
    
    def mostrarStatus(self) -> None:
        print("==== STATUS DO ORGANISMO ====")
        print(f"Nome: {self.nome}")
        print(f"Bioma atual: {self.bioma.nome}")
        print(f"Hidratação: {self.hidratacao}%")
        print(f"Quantidade de água no cantil: {self.cantil}")
        print(f"Temperatura: {self.temperatura}ºC")
        print(f"Energia atual: {self.energia}")
        print(f"Taxa de desidratação: {self.taxaDesidratacao * 100}%")
        self.coracao.mostrarStatus()
        self.pulmao.mostrarStatus()
