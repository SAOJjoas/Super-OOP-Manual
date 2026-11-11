from core.Atributos import Atributos

class Personagem:
    def __init__(self, nome, vida, nivel, forca, vitalidade, defesa):
        self.nome = nome
        self.vida = vida
        self.nivel = nivel

        self.atributos = Atributos(forca, vitalidade, defesa)

    def vida(self):
        return self.atributos.vida_atual