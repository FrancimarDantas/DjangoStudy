"""
 O polimorfismo é a capacidade de uma função tratar objetos de diferentes classes de maneira uniforme.
Isso é possível porque diferentes classes podem ter métodos com o mesmo nome, mas implementações distintas.
"""

class Passaro:
    def falar(self):
        print("Piu")

class Gato:
    def falar(self):
        print("Miau")

def som_animal(animal):
    animal.falar()

passaro = Passaro()
gato = Gato()

som_animal(passaro)
som_animal(gato)