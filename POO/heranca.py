"""
A herança permite que uma classe herde características de outra classe.
"""

class Veiculo:
    def __init__(self, rodas):
        self.rodas =rodas

class Carro(Veiculo):
    def __init__(self, rodas, marca):
        super().__init__(rodas)
        self.marca = marca