import random
from itens.Equipamento import Equipamento

class BaiacuTita(Equipamento):
    def __init__(self):
        super().__init__(
            nome="Baiacu Titã",
            descricao="Arma lendária. Tem 1/3 de chance de inflar e causar dano extra, mas devolve 1/3 do dano total no turno seguinte.",
            raridade="Lendário",
            slot="arma",
            bonus_forca=35,
            bonus_defesa=0
        )
        self.dano_recuo = 0

    def ao_causar_dano(self, portador, alvo, dano_causado):
        mensagens = []
        dano_final_turno = dano_causado

        if random.randint(1, 3) == 1:
            dano_extra = int(dano_causado * 0.5)
            alvo.atributos.receber_dano(dano_extra)
            dano_final_turno += dano_extra
            mensagens.append(f"O {self.nome} INFLOU e causou +{dano_extra} de dano EXTRA!")

        self.dano_recuo = int(dano_final_turno / 3)
        if self.dano_recuo > 0:
            mensagens.append(f"Os espinhos do {self.nome} vibram... ({self.dano_recuo} de dano de recuo no próximo turno)")

        return "\n".join(mensagens) if mensagens else None

    def ao_iniciar_turno(self, portador):
        if self.dano_recuo > 0:
            dano_recuo = self.dano_recuo
            self.dano_recuo = 0
            portador.atributos.receber_dano(dano_recuo)
            return f"O {self.nome} espetou {portador.nome}, devolvendo {dano_recuo} de dano do turno anterior!"
        return None

class AdagaEnferrujada(Equipamento):
    def __init__(self):
        super().__init__(
            nome="Adaga Enferrujada",
            descricao="Arma comum. Tem 20% de chance de abrir um corte profundo e causar +3 de dano fixo.",
            raridade="Comum",
            slot="arma",
            bonus_forca=6,
            bonus_defesa=0
        )

    def ao_causar_dano(self, portador, alvo, dano_causado):
        if random.randint(1, 5) == 1:
            dano_extra = 3
            alvo.atributos.receber_dano(dano_extra)
            return f"A {self.nome} abriu um corte sujo em {alvo.nome} (+{dano_extra} de dano)!"
        return None

class MarteloDePolvora(Equipamento):
    def __init__(self):
        super().__init__(
            nome="Martelo de Pólvora",
            descricao="Arma incomum. 25% de chance de detonar ao impacto (+6 de dano no alvo, 2 de dano no portador).",
            raridade="Incomum",
            slot="arma",
            bonus_forca=13,
            bonus_defesa=0
        )

    def ao_causar_dano(self, portador, alvo, dano_causado):
        if random.randint(1, 4) == 1:
            alvo.atributos.receber_dano(6)
            portador.atributos.receber_dano(2)
            return f"BUM! A carga do {self.nome} detonou! (+6 no alvo, -2 em {portador.nome})"
        return None

class LaminaDeObsidiana(Equipamento):
    def __init__(self):
        super().__init__(
            nome="Lâmina de Obsidiana",
            descricao="Arma rara. Muito afiada, mas estilhaça se o golpe causar mais de 20 de dano, ferindo o portador em 4.",
            raridade="Raro",
            slot="arma",
            bonus_forca=21,
            bonus_defesa=0
        )

    def ao_causar_dano(self, portador, alvo, dano_causado):
        if dano_causado > 20:
            portador.atributos.receber_dano(4)
            return f"A {self.nome} estilhaçou com a força do impacto, cortando {portador.nome} (-4 de vida)!"
        return None

class BrasasDaForja(Equipamento):
    def __init__(self):
        super().__init__(
            nome="Brasas da Forja",
            descricao="Arma incomum. Aquece o alvo ao bater, causando 4 de dano de queimadura no início do próximo turno.",
            raridade="Incomum",
            slot="arma",
            bonus_forca=11,
            bonus_defesa=1
        )
        self.alvo_queimando = None

    def ao_causar_dano(self, portador, alvo, dano_causado):
        self.alvo_queimando = alvo
        return f"{alvo.nome} está em chamas pelas {self.nome}!"

    def ao_iniciar_turno(self, portador):
        if self.alvo_queimando is not None:
            alvo = self.alvo_queimando
            self.alvo_queimando = None
            alvo.atributos.receber_dano(4)
            return f"As brasas queimaram {alvo.nome} em 4 de dano!"
        return None

class EspadaDeEngrenagens(Equipamento):
    def __init__(self):
        super().__init__(
            nome="Espada de Engrenagens",
            descricao="Arma rara. Acelera a cada golpe seguido, causando +3 de dano acumulado por ataque (máx. +12).",
            raridade="Raro",
            slot="arma",
            bonus_forca=17,
            bonus_defesa=2
        )
        self.rotacao = 0

    def ao_causar_dano(self, portador, alvo, dano_causado):
        if self.rotacao < 4:
            self.rotacao += 1
        bonus = self.rotacao * 3
        alvo.atributos.receber_dano(bonus)
        return f"Engrenagens girando (Nível {self.rotacao}/4): +{bonus} de dano mecânico!"

class CajadoDoEcoRunico(Equipamento):
    def __init__(self):
        super().__init__(
            nome="Cajado do Eco Rúnico",
            descricao="Arma épica. 30% de chance de armazenar o golpe e repetir metade do dano no início do próximo turno.",
            raridade="Épico",
            slot="arma",
            bonus_forca=24,
            bonus_defesa=3
        )
        self.alvo_eco = None
        self.dano_eco = 0

    def ao_causar_dano(self, portador, alvo, dano_causado):
        if random.randint(1, 10) <= 3:
            self.alvo_eco = alvo
            self.dano_eco = int(dano_causado * 0.5)
            return f"Uma runa brilhante marcou {alvo.nome} para ecoar {self.dano_eco} de dano!"
        return None

    def ao_iniciar_turno(self, portador):
        if self.dano_eco > 0 and self.alvo_eco is not None:
            dano = self.dano_eco
            alvo = self.alvo_eco
            self.dano_eco = 0
            self.alvo_eco = None
            alvo.atributos.receber_dano(dano)
            return f"O ECO RÚNICO disparou, atingindo {alvo.nome} em {dano} de dano!"
        return None

class CeifadoraDeCristal(Equipamento):
    def __init__(self):
        super().__init__(
            nome="Ceifadora de Cristal",
            descricao="Arma épica. Causa +40% de dano extra se o alvo estiver com menos de 50% da vida máxima.",
            raridade="Épico",
            slot="arma",
            bonus_forca=26,
            bonus_defesa=0
        )

    def ao_causar_dano(self, portador, alvo, dano_causado):
        if alvo.atributos.vida_atual < (alvo.atributos.vida_maxima * 0.5):
            dano_extra = int(dano_causado * 0.4)
            if dano_extra > 0:
                alvo.atributos.receber_dano(dano_extra)
                return f"O cristal ressoou com a fraqueza de {alvo.nome}, causando +{dano_extra} de dano de execução!"
        return None