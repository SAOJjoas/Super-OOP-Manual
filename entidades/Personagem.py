class Personagem:
    def __init__(self, nome, vida, nivel):
        self.nome = nome
        self.vida = vida
        self.nivel = nivel


class Player(Personagem):
    def __init__(self, nome, vida, controle, nivel):
        self.controle = controle
        super().__init__(nome, vida, nivel)

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, recompensa):
        super().__init__(nome, vida, nivel)

        self.recompensa = recompensa

