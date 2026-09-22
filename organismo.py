from coracao import Coracao
from pulmao import Pulmao
from bioma import Bioma

class Organismo:
    def __init__(self, nome:str, bioma:Bioma) -> None:
        self.nome = nome
        self.tempoSol = 0
        self.hidratacao = 100
        self.temperatura = 36.5
        self.bioma = bioma
        self.coracao = Coracao()
        self.pulmao = Pulmao()

    def suar(self) -> None:
        self.hidratacao -= 5
        self.temperatura -= 0.5

    def correr(self) -> None:
        print("O organismo começou a correr!\n")
        self.coracao.acelerar()
        self.pulmao.respirarMaisRapido()
    
    def ficarNoSol(self) -> None:
        print("O organismo está exposto ao calor!")
        if self.tempoSol >= 5 and self.hidratacao < 50:
            print("Atenção! O organismo ficou muito tempo no sol, o suor não é suficiente! Beba água!\n")
            self.temperatura += 0.5
        else:
            self.tempoSol += 1
            self.hidratacao -= 15
            self.temperatura += 0.5
            self.suar()
            print("O organismo suou pra manter a temperatura estável!\n")
            

    def beberAgua(self) -> None:
        print("O organismo bebeu água!\n")
        self.hidratacao += 20
        self.temperatura -= 1
    
    def mostrarStatus(self) -> None:
        print("==== STATUS DO ORGANISMO ====")
        print(f"Nome: {self.nome}")
        print(f"Bioma atual: {self.bioma.nome}")
        print(f"Hidratação: {self.hidratacao}%")
        print(f"Temperatura: {self.temperatura}ºC")
        self.coracao.mostrarStatus()
        self.pulmao.mostrarStatus()
