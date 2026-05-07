"""
Usa métodos e variáveis privadas, que não podem ser acessados diretamente fora da classe.
Isso protege os dados e permite que a classe matanha controle total sobre o que é exposto.
"""

class ContaBancaria:
    def __init__(self,saldo):
        self.__saldo  = saldo # Atributo provado
    
    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("valor inválido")
    
    def ver_saldo(self):
        return self.__saldo