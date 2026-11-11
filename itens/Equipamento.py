from itens.Item import Item


class Equipamento(Item):
    def __init__(self, nome, descricao, raridade, slot, bonus_forca = 0, bonus_defesa = 0):
        super().__init__(nome, descricao, raridade)
        self.slot= slot
        self.bonus_forca = bonus_forca
        self.bonus_defesa = bonus_defesa

    def ao_causar_dano(self, portador, alvo, dano_causado):

        return None
