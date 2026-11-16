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

    def obter_equipamentos(self, entidade):
        """Retorna lista com todos os itens equipados (arma, armadura, etc.)."""
        if hasattr(entidade, "inventario"):
            return [item for item in entidade.inventario.equipados.values() if item is not None]
        return [
            item for item in (
                getattr(entidade, "arma_equipada", None),
                getattr(entidade, "armadura_equipada", None)
            )
            if item is not None
        ]

    def _processar_inicio_turno(self, entidade, eventos):
        for item in self.obter_equipamentos(entidade):
            if hasattr(item, "ao_iniciar_turno"):
                efeito = item.ao_iniciar_turno(entidade)
                if efeito:
                    eventos.append(efeito)

    def atacar(self, atacante, defensor):
        if not atacante.atributos.esta_vivo:
            return f"{atacante.nome} não pode mais atacar!"

        dano = self.calcular_dano(atacante, defensor)
        defensor.atributos.receber_dano(dano)

        mensagem = f"{atacante.nome} atacou {defensor.nome}\nDano: {dano}"

        for item in self.obter_equipamentos(atacante):
            if hasattr(item, "ao_causar_dano"):
                efeito = item.ao_causar_dano(atacante, defensor, dano)
                if efeito:
                    mensagem += f"\n{efeito}"

        for item in self.obter_equipamentos(defensor):
            if hasattr(item, "ao_receber_dano"):
                efeito = item.ao_receber_dano(defensor, atacante, dano)
                if efeito:
                    mensagem += f"\n{efeito}"

        if not defensor.atributos.esta_vivo:
            mensagem += f"\n{defensor.nome} foi derrotado!"
        if not atacante.atributos.esta_vivo:
            mensagem += f"\n{atacante.nome} foi derrotado pelos próprios ferimentos!"

        return mensagem

    def executar_rodada(self):
        if not self.combate_ativo:
            return ["Fim da luta!"]

        eventos = [f"--- Turno {self.turno} ---"]

        self._processar_inicio_turno(self.player, eventos)
        if not self.combate_ativo:
            if not self.inimigo.atributos.esta_vivo:
                eventos.append(f"{self.inimigo.nome} foi derrotado!")
            if not self.player.atributos.esta_vivo:
                eventos.append(f"{self.player.nome} foi derrotado!")
            return eventos

        eventos.append(self.atacar(self.player, self.inimigo))

        if self.combate_ativo:
            self._processar_inicio_turno(self.inimigo, eventos)
            if self.combate_ativo:
                eventos.append(self.atacar(self.inimigo, self.player))
            else:
                if not self.player.atributos.esta_vivo:
                    eventos.append(f"{self.player.nome} foi derrotado!")
                if not self.inimigo.atributos.esta_vivo:
                    eventos.append(f"{self.inimigo.nome} foi derrotado!")

        self.turno += 1
        return eventos