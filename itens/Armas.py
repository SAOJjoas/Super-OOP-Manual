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
