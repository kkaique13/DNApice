# from coracao.py import coracao

class Pulmao:
    def __init__(self) -> None:
        self.oxigenacao = 90 # %
    
    def respirarMaisRapido(self) -> None:
        if self.oxigenacao < 100:
            self.oxigenacao += 1
        else:
            print("Oxigenação está maximizada!")
            
    def mostrarStatus(self) -> None:
        print(f"Oxigenação: {self.oxigenacao}")