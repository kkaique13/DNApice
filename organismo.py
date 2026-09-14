from coracao import Coracao
from pulmao import Pulmao

class Organismo:
    def __init__(self) -> None:
        self.hidratacao = 100
        self.temperatura = 36.5
        self.coracao = Coracao()
        self.pulmao = Pulmao()

    def correr(self) -> None:
        print("O organismo começou a correr!")
        self.coracao.acelerar()
        self.pulmao.respirarMaisRapido()
    
    def ficarNoSol(self) -> None:
        print("O organismo está exposto ao calor!")
        self.hidratacao -= 15
        self.temperatura += 6.5

    def beberAgua(self) -> None:
        print("O organismo bebeu água!")
        self.hidratacao += 20
    
    def mostrarStatus(self) -> None:
        print("\n ==== STATUS DO ORGANISMO ====")
        print(f"Hidratação: {self.hidratacao}")
        print(f"Temperatura: {self.temperatura}ºC")
        self.coracao.mostrarStatus()
        self.pulmao.mostrarStatus()
