class Bioma:
    def __init__(self, nome:str, temperatura:float) -> None:
        self.nome = nome
        self.temperatura = temperatura

    def mostrarStatus(self) -> None:
        print("\n==== STATUS DO BIOMA ====")
        print(f"Nome: {self.nome} ({self.temperatura}ºC)\n")