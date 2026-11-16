from construcao.Raca import Raca

class Anao(Raca):
    def __init__(self, forca = 7, vitalidade = 80, defesa = 50):
        super().__init__(forca, vitalidade, defesa)