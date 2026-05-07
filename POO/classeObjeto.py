"""
Uma classe define atributos (Características) e métodos (Ações) que os objetos criados a partir dela terão. 
Já um objeto é uma instância de uma classe, ou seja, é uma entidade concreta que possui as características 
e comportamentos definidos pela classe.
"""

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
 

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}")
    
"Criação de Objetos"

meu_carro = Carro("Toyota", "Corolla")
meu_carro.exibir_informacoes()