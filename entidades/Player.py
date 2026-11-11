from entidades import Personagem


class Player(Personagem):
    def __init__(self, nome, vida, controle, nivel):
        self.controle = controle
        super().__init__(nome, vida, nivel)