from entidades.Personagem import Personagem


class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, recompensa, forca=4, vitalidade=8, defesa=2):
        super().__init__(nome, vida, nivel, forca, vitalidade, defesa)
        self.recompensa = recompensa