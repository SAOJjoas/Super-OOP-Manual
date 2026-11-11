class Combate:
    def __init__(self, player, inimigo):
        self.player = player
        self.inimigo = inimigo
        self.turno = 1

    @property
    def combate_ativo(self):
        return self.player.atributos.esta_vivo and self.inimigo.atributos.esta_vivo

    def calcular_dano(self, atacante, defensor):
        dano_bruto = atacante.atributos.ataque_total - defensor.atributos.defesa_total
        return max(1, dano_bruto)

    def atacar(self, atacante, defensor):
        if not atacante.atributos.esta_vivo:
            return f"{atacante.nome} não pode mais atacar!"

        dano = self.calcular_dano(atacante, defensor)
        defensor.atributos.receber_dano(dano)

        mensagem = f"{atacante.nome} atacou {defensor.nome}\nDano: {dano}"

        if not defensor.atributos.esta_vivo:
            mensagem += f"\n{defensor.nome} foi derrotado!"

        return mensagem

    def executar_rodada(self):
        if not self.combate_ativo:
            return ["Fim da luta!"]

        eventos = [f"--- Turno {self.turno} ---"]

        eventos.append(self.atacar(self.player, self.inimigo))

        if self.inimigo.atributos.esta_vivo:
            eventos.append(self.atacar(self.inimigo, self.player))

        self.turno += 1
        return eventos
