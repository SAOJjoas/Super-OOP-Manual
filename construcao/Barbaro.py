from construcao.Raca import Raca

class Barbaro(Raca):
    def __init__(self, forca = 15, vitaliade = 120, defesa = 40):
        super().__init__(forca, vitaliade, defesa)