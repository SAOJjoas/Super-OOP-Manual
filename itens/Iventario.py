class Inventario:
    def __init__(self, atributos, capacidade_mochila=20):
        self.atributos = atributos
        self.capacidade_mochila = capacidade_mochila
        self.mochila = []
        self.equipados = {
            "arma": None,
            "armadura": None
        }

    def _atualizar_atributos(self):
        """Recalcula e aplica os bônus dos itens equipados diretamente em Atributos."""
        total_ataque = 0
        total_defesa = 0

        for item in self.equipados.values():
            if item is not None:
                # Lê bonus_forca (padrão das armas/armaduras criadas) ou bonus_ataque
                total_ataque += getattr(item, "bonus_forca", 0)
                total_defesa += getattr(item, "bonus_defesa", 0)

        self.atributos.bonus_ataque = total_ataque
        self.atributos.bonus_defesa = total_defesa

    def adicionar_item(self, item):
        if len(self.mochila) >= self.capacidade_mochila:
            return f"Mochila cheia! Não foi possível guardar {item.nome}."
        self.mochila.append(item)
        return f"{item.nome} foi adicionado à mochila."

    def equipar(self, item):
        slot = getattr(item, "slot", None)
        if slot not in self.equipados:
            return f"{item.nome} não pode ser equipado (slot inválido: {slot})."

        if item in self.mochila:
            self.mochila.remove(item)

        item_anterior = self.equipados[slot]
        if item_anterior is not None:
            self.mochila.append(item_anterior)

        self.equipados[slot] = item
        self._atualizar_atributos()

        if item_anterior:
            return f"Você desequipou {item_anterior.nome} e equipou {item.nome}!"
        return f"Você equipou {item.nome} no slot de {slot}!"

    def desequipar(self, slot):
        if slot not in self.equipados:
            return f"Slot '{slot}' não existe."

        item = self.equipados[slot]
        if item is None:
            return f"Não há nada equipado no slot de {slot}."

        if len(self.mochila) >= self.capacidade_mochila:
            return f"Mochila cheia! Não há espaço para guardar {item.nome}."

        self.equipados[slot] = None
        self.mochila.append(item)
        self._atualizar_atributos()
        return f"Você desequipou {item.nome} e guardou na mochila."