from entidades.Personagem import Personagem
from itens.Iventario import Inventario


class Player(Personagem):
    def __init__(self, nome, vida, controle, nivel, forca=5, vitalidade=10, defesa=3):
        self.controle = controle
        super().__init__(nome, vida, nivel, forca, vitalidade, defesa)
        self.inventario = Inventario(self.atributos)