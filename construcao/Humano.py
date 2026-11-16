from construcao.Raca import Raca

class Humano(Raca):
    def __init__(self, forca = 10, vitalidade = 100, defesa = 20):
        super().__init__(forca, vitalidade, defesa)