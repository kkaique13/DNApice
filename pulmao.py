OXIGENACAO_BASE = 90    # %
OXIGENACAO_MAXIMA = 100  # %

class Pulmao:
    def __init__(self) -> None:
        self.oxigenacao = OXIGENACAO_BASE  # %

    def respirarMaisRapido(self) -> bool:
        if self.oxigenacao < OXIGENACAO_MAXIMA:
            self.oxigenacao += 1
            return True
        return False

    def respirarNormalmente(self) -> None:
        self.oxigenacao = max(OXIGENACAO_BASE, self.oxigenacao - 2)

    def mostrarStatus(self) -> None:
        print(f"Oxigenação: {self.oxigenacao}%\n")