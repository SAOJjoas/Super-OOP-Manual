from entidades import Personagem
from itens.Iventario import Inventario


class Player(Personagem):
    def __init__(self, nome, vida, controle, nivel):
        self.controle = controle
        super().__init__(nome, vida, nivel)
        self.inventario = Inventario(self.atributos)