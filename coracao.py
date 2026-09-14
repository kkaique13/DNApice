class Coracao:
    def __init__(self) -> None:
        self.frequenciaCardiaca = 70 #bpm
    
    def acelerar(self) -> None:
        self.frequenciaCardiaca += 20
    
    def desacelerar(self) -> None:
        self.frequenciaCardiaca -= 10

    def mostrarStatus(self) -> None:
        print(f"Frequência cardíaca: {self.frequenciaCardiaca}")