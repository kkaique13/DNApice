from random import randint
from coracao import Coracao
from pulmao import Pulmao
from bioma import Bioma

#Constantes
TEMPERATURA_NORMAL = 36.5
LIMITE_ENERGIA_BAIXA = 40

CUSTO_ENERGIA_CORRER = 20
CUSTO_HIDRATACAO_CORRER = 25
DISTANCIA_CORRER = 10  # Km

CUSTO_ENERGIA_ANDAR = 10
CUSTO_HIDRATACAO_ANDAR = 10
DISTANCIA_ANDAR = 5  # Km

AGUA_POR_GOLE = 25         # quanto sai do cantil
HIDRATACAO_POR_GOLE = 25   # quanto o organismo recupera
LIMITE_TEMPO_SOL = 5

class Organismo:
    def __init__(self, nome: str, bioma: Bioma) -> None:
        self.nome = nome
        self.tempoSol = 0
        self.hidratacao = 100
        self.temperatura = TEMPERATURA_NORMAL
        self.taxaDesidratacao = 1
        self.energia = 100
        self.cantil = 100
        self.bioma = bioma
        self.coracao = Coracao()
        self.pulmao = Pulmao()

    #Auxiliares
    def _perderHidratacao(self, base: float) -> None:
        self.hidratacao = round(self.hidratacao - base * self.taxaDesidratacao, 1)

    def _ajustarTaxa(self, valor: float) -> None:
        self.taxaDesidratacao = max(0.5, round(self.taxaDesidratacao + valor, 2))

    def podeCorrer(self) -> bool:
        return self.energia - CUSTO_ENERGIA_CORRER >= 0

    def podeAndar(self) -> bool:
        return self.energia - CUSTO_ENERGIA_ANDAR >= 0

    #Ações
    def suar(self) -> None:
        self._perderHidratacao(5)
        self.temperatura -= 0.5

    def correr(self) -> None:
        print("O organismo começou a correr!")
        self.coracao.acelerar()
        print(f"O batimento cardíaco do organismo {self.nome} aumentou!")

        if self.pulmao.respirarMaisRapido():
            print(f"O organismo {self.nome} está respirando mais rápido!\n")
        else:
            print("Oxigenação está maximizada!\n")

        self._perderHidratacao(CUSTO_HIDRATACAO_CORRER)
        self.energia -= CUSTO_ENERGIA_CORRER

    def andar(self) -> None:
        print("O organismo começou a andar!\n")
        self.coracao.acelerar(5)
        self._perderHidratacao(CUSTO_HIDRATACAO_ANDAR)
        self.energia -= CUSTO_ENERGIA_ANDAR

    def ficarNoSol(self) -> None:
        print("O organismo está exposto ao calor!")

        if self.tempoSol >= LIMITE_TEMPO_SOL or self.hidratacao < 50:
            print("Atenção! O organismo ficou muito tempo no sol, o suor não é suficiente! Fique na sombra!\n")
            self.temperatura += 0.5
            self._perderHidratacao(15)
        else:
            self.tempoSol += 1
            self._perderHidratacao(15)
            self.temperatura += 0.5
            self._ajustarTaxa(-0.1)
            self.suar()
            print(f"O organismo {self.nome} suou pra manter a temperatura estável!\n")

    def ficarNaSombra(self) -> None:
        energiaAnterior = self.energia
        self.energia = min(100, self.energia + 10)
        self.temperatura = max(TEMPERATURA_NORMAL, self.temperatura - 0.5)
        self.coracao.desacelerar()
        self.pulmao.respirarNormalmente()
        self.tempoSol = max(0, self.tempoSol - 1)

        print(f"A frequência cardíaca do organismo {self.nome} diminuiu!")
        if self.energia > energiaAnterior:
            print(f"A energia do organismo {self.nome} aumentou!")
        print(f"O organismo {self.nome} está descansando na sombra!\n")

    def encherCantil(self) -> None:
        antes = self.cantil
        self.cantil = min(100, self.cantil + randint(10, 50))
        print(f"O organismo {self.nome} encheu o cantil com {self.cantil - antes} de água!\n")

    def beberAgua(self) -> bool:
        if self.cantil < AGUA_POR_GOLE:
            print(f"O cantil está vazio ou com pouca água! O organismo {self.nome} não consegue beber água!\n")
            return False

        self.cantil -= AGUA_POR_GOLE
        self.hidratacao = min(100, self.hidratacao + HIDRATACAO_POR_GOLE)
        self.temperatura = max(TEMPERATURA_NORMAL, self.temperatura - 1)
        self.coracao.desacelerar()
        print(f"O organismo {self.nome} bebeu água!")
        print(f"A temperatura do organismo {self.nome} diminuiu!")
        print(f"A frequência cardíaca do organismo {self.nome} diminuiu!\n")
        return True

    def aplicarPenalidades(self) -> None:
        houve = False

        if self.energia <= LIMITE_ENERGIA_BAIXA:
            self._ajustarTaxa(0.2)
            print(f"A taxa de desidratação do organismo {self.nome} aumentou (cansaço)!")
            houve = True

        if 40 < self.temperatura <= 42 or 30 <= self.temperatura < 34:
            self._ajustarTaxa(0.3)
            print(f"A taxa de desidratação do organismo {self.nome} aumentou (temperatura)!")
            houve = True

        if houve:
            print()

    def mostrarStatus(self) -> None:
        print("==== STATUS DO ORGANISMO ====")
        print(f"Nome: {self.nome}")
        print(f"Bioma atual: {self.bioma.nome}")
        print(f"Hidratação: {self.hidratacao:g}%")
        print(f"Quantidade de água no cantil: {self.cantil}")
        print(f"Temperatura: {self.temperatura}°C")
        print(f"Energia atual: {self.energia}")
        print(f"Taxa de desidratação: {self.taxaDesidratacao * 100:.0f}%\n")
        self.coracao.mostrarStatus()
        self.pulmao.mostrarStatus()