class Atributos:
    def __init__(self, forca, vitalidade, defesa):
        self.forca = forca
        self.vitalidade = vitalidade
        self.defesa = defesa

        self.bonus_ataque = 0
        self.bonus_defesa = 0

        self.vida_maxima = self.vitalidade * 10
        self.vida_atual = self.vida_maxima

    @property
    def ataque_total(self):
        return (self.forca * 2) + self.bonus_ataque

    @property
    def defesa_total(self):
        return self.defesa + self.bonus_defesa

    @property
    def esta_vivo(self):
        return self.vida_atual > 0

    def receber_dano(self, quantidade):
        self.vida_atual = max(0, self.vida_atual - quantidade)

    def curar(self, quantidade):
        self.vida_atual = max(self.vida_maxima, self.vida_atual + quantidade)