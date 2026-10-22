FREQUENCIA_MINIMA = 60   # bpm
FREQUENCIA_MAXIMA = 200  # bpm

class Coracao:
    def __init__(self) -> None:
        self.frequenciaCardiaca = 70  # bpm

    def acelerar(self, valor: int = 20) -> None:
        self.frequenciaCardiaca = min(FREQUENCIA_MAXIMA, self.frequenciaCardiaca + valor)

    def desacelerar(self, valor: int = 10) -> None:
        self.frequenciaCardiaca = max(FREQUENCIA_MINIMA, self.frequenciaCardiaca - valor)

    def mostrarStatus(self) -> None:
        print(f"Frequência cardíaca: {self.frequenciaCardiaca} bpm\n")