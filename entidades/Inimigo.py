from entidades.Personagem import Personagem


class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, recompensa):
        super().__init__(nome, vida, nivel)

        self.recompensa = recompensa
