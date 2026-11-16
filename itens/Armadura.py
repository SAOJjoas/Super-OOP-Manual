import random
from itens.Equipamento import Equipamento

class TunicaAcolchoada(Equipamento):
    def __init__(self):
        super().__init__(
            nome="Túnica Acolchoada",
            descricao="Armadura comum. Camadas grossas de tecido que amortecem golpes leves.",
            raridade="Comum",
            slot="armadura",
            bonus_forca=0,
            bonus_defesa=5
        )

class CotaDeMalhaEnferrujada(Equipamento):
    def __init__(self):
        super().__init__(
            nome="Cota de Malha Enferrujada",
            descricao="Armadura incomum. Boa proteção física, mas tem 20% de chance de beliscar o portador ao atacar (-2 HP).",
            raridade="Incomum",
            slot="armadura",
            bonus_forca=0,
            bonus_defesa=11
        )

    def ao_causar_dano(self, portador, alvo, dano_causado):
        if random.randint(1, 5) == 1:
            portador.atributos.receber_dano(2)
            return f"Os elos da {self.nome} beliscaram {portador.nome} durante o golpe (-2 de vida)!"
        return None

class CouracaDeCarvalhoVivo(Equipamento):
    def __init__(self):
        super().__init__(
            nome="Couraça de Carvalho Vivo",
            descricao="Armadura incomum. Regenera 3 de vida no início de cada turno.",
            raridade="Incomum",
            slot="armadura",
            bonus_forca=0,
            bonus_defesa=9
        )

    def ao_iniciar_turno(self, portador):
        if portador.atributos.vida_atual < portador.atributos.vida_maxima:
            cura = 3
            portador.atributos.vida_atual = min(
                portador.atributos.vida_maxima,
                portador.atributos.vida_atual + cura
            )
            return f"A {self.nome} floresceu, regenerando +{cura} de vida em {portador.nome}!"
        return None

class ArmaduraEspinhosDeFerro(Equipamento):
    def __init__(self):
        super().__init__(
            nome="Armadura de Espinhos de Ferro",
            descricao="Armadura rara. Devolve 5 de dano perfurante sempre que o portador recebe um ataque.",
            raridade="Raro",
            slot="armadura",
            bonus_forca=2,
            bonus_defesa=15
        )

    def ao_receber_dano(self, portador, atacante, dano_recebido):
        if atacante is not None and dano_recebido > 0:
            dano_espinhos = 5
            atacante.atributos.receber_dano(dano_espinhos)
            return f"Os espinhos da {self.nome} perfuraram {atacante.nome} de volta ({dano_espinhos} de dano)!"
        return None

class PlacasDeVapor(Equipamento):
    def __init__(self):
        super().__init__(
            nome="Placas de Vapor",
            descricao="Armadura rara. Converte 30% do dano recebido em pressão, liberando-a como dano no início do próximo turno.",
            raridade="Raro",
            slot="armadura",
            bonus_forca=0,
            bonus_defesa=17
        )
        self.pressao_acumulada = 0
        self.ultimo_atacante = None

    def ao_receber_dano(self, portador, atacante, dano_recebido):
        carga = int(dano_recebido * 0.3)
        if carga > 0:
            self.pressao_acumulada += carga
            self.ultimo_atacante = atacante
            return f"As {self.nome} absorveram o impacto (+{carga} de pressão acumulada)."
        return None

    def ao_iniciar_turno(self, portador):
        if self.pressao_acumulada > 0 and self.ultimo_atacante is not None:
            dano = self.pressao_acumulada
            alvo = self.ultimo_atacante
            self.pressao_acumulada = 0
            alvo.atributos.receber_dano(dano)
            return f"VÁLVULA ABERTA! As {self.nome} escaldaram {alvo.nome} em {dano} de dano!"
        return None

class MantoDeSangueSombrio(Equipamento):
    def __init__(self):
        super().__init__(
            nome="Manto de Sangue Sombrio",
            descricao="Armadura épica. Drena 4 de vida por turno para fortalecer os ataques do portador com +8 de dano sombrio.",
            raridade="Épico",
            slot="armadura",
            bonus_forca=8,
            bonus_defesa=19
        )

    def ao_iniciar_turno(self, portador):
        custo = 4
        portador.atributos.receber_dano(custo)
        return f"O {self.nome} alimentou-se de {portador.nome} (-{custo} HP) para manter sua aura sombria!"

    def ao_causar_dano(self, portador, alvo, dano_causado):
        dano_sombrio = 8
        alvo.atributos.receber_dano(dano_sombrio)
        return f"A aura do {self.nome} consumiu {alvo.nome} (+{dano_sombrio} de dano sombrio)!"

class EgideDeCristalRunico(Equipamento):
    def __init__(self):
        super().__init__(
            nome="Égide de Cristal Rúnico",
            descricao="Armadura épica. Gera uma barreira a cada 2 turnos que bloqueia 10 de dano e reflete 6 ao atacante.",
            raridade="Épico",
            slot="armadura",
            bonus_forca=0,
            bonus_defesa=22
        )
        self.barreira_ativa = True
        self.recarga = 0

    def ao_iniciar_turno(self, portador):
        if not self.barreira_ativa:
            self.recarga += 1
            if self.recarga >= 2:
                self.barreira_ativa = True
                self.recarga = 0
                return f"As runas da {self.nome} brilharam: Barreira de Cristal restaurada!"
        return None

    def ao_receber_dano(self, portador, atacante, dano_recebido):
        if self.barreira_ativa and dano_recebido > 0:
            self.barreira_ativa = False
            cura_bloqueio = min(dano_recebido, 10)
            portador.atributos.vida_atual = min(
                portador.atributos.vida_maxima,
                portador.atributos.vida_atual + cura_bloqueio
            )
            msg = f"A Barreira da {self.nome} absorveu {cura_bloqueio} de dano e se estilhaçou"
            if atacante is not None:
                atacante.atributos.receber_dano(6)
                msg += f", ferindo {atacante.nome} em 6!"
            else:
                msg += "!"
            return msg
        return None

class ArmaduraColossoDeMagma(Equipamento):
    def __init__(self):
        super().__init__(
            nome="Armadura do Colosso de Magma",
            descricao="Armadura lendária. Converte 50% do dano recebido em calor. Ao atingir 20 de calor, explode causando dano em área no atacante.",
            raridade="Lendário",
            slot="armadura",
            bonus_forca=5,
            bonus_defesa=30
        )
        self.calor = 0

    def ao_receber_dano(self, portador, atacante, dano_recebido):
        self.calor += int(dano_recebido * 0.5)
        if self.calor >= 20 and atacante is not None:
            explosao = self.calor
            self.calor = 0
            atacante.atributos.receber_dano(explosao)
            return f"ERUPÇÃO VULCÂNICA! A {self.nome} atingiu massa crítica e incinerou {atacante.nome} em {explosao} de dano!"
        return f"Núcleo da {self.nome} aquecendo ({self.calor}/20 de calor)..."