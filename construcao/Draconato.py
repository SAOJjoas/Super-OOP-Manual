from construcao.Raca import Raca

class Draconato (Raca):
    def __init__(self, vitalidade = 60, defesa = 20, forca = 20):
        super().__init__(forca, vitalidade, defesa)