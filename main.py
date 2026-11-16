import random
from entidades.Player import Player
from entidades.Inimigo import Inimigo
from core.Combate import Combate

from itens.Armas import (
    AdagaEnferrujada,
    MarteloDePolvora,
    BrasasDaForja,
    EspadaDeEngrenagens,
    LaminaDeObsidiana,
    CajadoDoEcoRunico,
    CeifadoraDeCristal,
    BaiacuTita,
)
from itens.Armadura import (
    TunicaAcolchoada,
    CouracaDeCarvalhoVivo,
    CotaDeMalhaEnferrujada,
    ArmaduraEspinhosDeFerro,
    PlacasDeVapor,
    MantoDeSangueSombrio,
    EgideDeCristalRunico,
    ArmaduraColossoDeMagma,
)


def pool_itens():
    return [
        AdagaEnferrujada,
        MarteloDePolvora,
        BrasasDaForja,
        EspadaDeEngrenagens,
        LaminaDeObsidiana,
        CajadoDoEcoRunico,
        CeifadoraDeCristal,
        BaiacuTita,
        TunicaAcolchoada,
        CouracaDeCarvalhoVivo,
        CotaDeMalhaEnferrujada,
        ArmaduraEspinhosDeFerro,
        PlacasDeVapor,
        MantoDeSangueSombrio,
        EgideDeCristalRunico,
        ArmaduraColossoDeMagma,
    ]


def gerar_loot(nivel_inimigo):
    pesos_por_raridade = {
        "Comum": max(10, 50 - nivel_inimigo * 5),
        "Incomum": 30,
        "Raro": 15 + nivel_inimigo * 2,
        "Épico": 4 + nivel_inimigo * 2,
        "Lendário": 1 + nivel_inimigo,
    }
    instancias = [cls() for cls in pool_itens()]
    pesos = [pesos_por_raridade.get(item.raridade, 10) for item in instancias]
    return random.choices(instancias, weights=pesos, k=1)[0]


def criar_inimigo(onda):
    catalogo = [
        ("Rato de Esgoto", 1, 3, 5, 1, "15 moedas"),
        ("Goblin Saqueador", 2, 5, 7, 2, "30 moedas"),
        ("Esqueleto Enferrujado", 3, 7, 9, 4, "50 moedas"),
        ("Autômato a Vapor", 4, 9, 12, 6, "85 moedas"),
        ("Cavaleiro Sombrio", 5, 12, 15, 9, "140 moedas"),
        ("Colosso de Magma", 6, 16, 20, 12, "300 moedas"),
    ]
    indice = min(onda - 1, len(catalogo) - 1)
    nome, nivel_base, forca, vitalidade, defesa, recompensa = catalogo[indice]
    escala = max(0, onda - len(catalogo))

    inimigo = Inimigo(
        nome=f"{nome}" if escala == 0 else f"{nome} +{escala}",
        vida=(vitalidade + escala * 3) * 10,
        nivel=nivel_base + escala,
        recompensa=recompensa,
        forca=forca + escala * 2,
        vitalidade=vitalidade + escala * 3,
        defesa=defesa + escala * 2,
    )

    # Inimigos de ondas mais altas também podem vir equipados
    if onda == 3:
        inimigo.arma_equipada = AdagaEnferrujada()
    elif onda == 4:
        inimigo.armadura_equipada = PlacasDeVapor()
    elif onda == 5:
        inimigo.arma_equipada = CeifadoraDeCristal()
        inimigo.armadura_equipada = MantoDeSangueSombrio()
    elif onda >= 6:
        inimigo.arma_equipada = BaiacuTita()
        inimigo.armadura_equipada = ArmaduraColossoDeMagma()

    return inimigo


def exibir_status(player):
    atr = player.atributos
    arma = player.inventario.equipados["arma"]
    armadura = player.inventario.equipados["armadura"]

    print("\n" + "=" * 50)
    print(f"HERÓI: {player.nome} | Nível {player.nivel}")
    print(f"HP: {atr.vida_atual}/{atr.vida_maxima}")
    print(
        f"Força: {atr.forca} (Ataque Total: {atr.ataque_total}) | "
        f"Defesa: {atr.defesa} (Defesa Total: {atr.defesa_total})"
    )
    print(f"Arma equipada:     {arma.nome if arma else 'Nenhuma'}")
    print(f"Armadura equipada: {armadura.nome if armadura else 'Nenhuma'}")
    print("=" * 50)


def gerenciar_inventario(player):
    inv = player.inventario
    while True:
        print("\n--- INVENTÁRIO ---")
        print(f"Arma equipada:     {inv.equipados['arma'].nome if inv.equipados['arma'] else 'Nenhuma'}")
        print(f"Armadura equipada: {inv.equipados['armadura'].nome if inv.equipados['armadura'] else 'Nenhuma'}")
        print(f"\nMochila ({len(inv.mochila)}/{inv.capacidade_mochila}):")

        if not inv.mochila:
            print("  (vazia)")
        else:
            for idx, item in enumerate(inv.mochila, start=1):
                print(
                    f"  [{idx}] {item.nome} ({item.raridade} | {item.slot}) "
                    f"[+Força: {item.bonus_forca}, +Def: {item.bonus_defesa}] - {item.descricao}"
                )

        print("\nOpções:")
        print("  [Número] Equipar item da mochila")
        print("  [A] Desequipar arma")
        print("  [D] Desequipar armadura")
        print("  [0] Voltar")

        escolha = input("> ").strip().lower()
        if escolha == "0":
            break
        elif escolha == "a":
            print(inv.desequipar("arma"))
        elif escolha == "d":
            print(inv.desequipar("armadura"))
        elif escolha.isdigit():
            indice = int(escolha) - 1
            if 0 <= indice < len(inv.mochila):
                print(inv.equipar(inv.mochila[indice]))
            else:
                print("Índice inválido.")
        else:
            print("Opção inválida.")


def iniciar_batalha(player, inimigo):
    combate = Combate(player, inimigo)
    print(f"\n>>> UM INIMIGO APARECEU: {inimigo.nome} (Nível {inimigo.nivel}) <<<")
    print(
        f"HP Inimigo: {inimigo.atributos.vida_atual}/{inimigo.atributos.vida_maxima} | "
        f"Ataque: {inimigo.atributos.ataque_total} | Defesa: {inimigo.atributos.defesa_total}"
    )

    while combate.combate_ativo:
        print(
            f"\n[{player.nome}: {player.atributos.vida_atual}/{player.atributos.vida_maxima} HP] "
            f"VS [{inimigo.nome}: {inimigo.atributos.vida_atual}/{inimigo.atributos.vida_maxima} HP]"
        )
        print("1 - Lutar (executar rodada)")
        print("2 - Abrir inventário e trocar equipamento")
        print("3 - Fugir")

        acao = input("> ").strip()
        if acao == "1":
            eventos = combate.executar_rodada()
            print()
            for linha in eventos:
                print(linha)
        elif acao == "2":
            gerenciar_inventario(player)
        elif acao == "3":
            print(f"{player.nome} recuou da batalha!")
            return "fugiu"
        else:
            print("Comando inválido.")

    if player.atributos.esta_vivo:
        print(f"\nVITÓRIA! Você derrotou {inimigo.nome} e recebeu {inimigo.recompensa}!")
        player.nivel += 1
        player.atributos.forca += 1
        player.atributos.vitalidade += 1
        player.atributos.defesa += 1
        player.atributos.vida_maxima = player.atributos.vitalidade * 10
        player.atributos.curar(25)
        print("Você subiu de nível (+1 em todos os atributos) e recuperou 25 de HP!")

        loot = gerar_loot(inimigo.nivel)
        print(f"Item encontrado: {loot.nome} ({loot.raridade}) - {loot.descricao}")
        print(player.inventario.adicionar_item(loot))
        return "vitoria"

    print(f"\nDERROTA... {player.nome} caiu em combate.")
    return "derrota"


def main():
    print("=== ARENA RPG ===")
    nome = input("Digite o nome do seu personagem: ").strip() or "Aventureiro"

    player = Player(
        nome=nome,
        vida=120,
        controle="teclado",
        nivel=1,
        forca=6,
        vitalidade=12,
        defesa=3,
    )

    # Equipamentos iniciais
    arma_inicial = AdagaEnferrujada()
    armadura_inicial = TunicaAcolchoada()
    player.inventario.adicionar_item(arma_inicial)
    player.inventario.adicionar_item(armadura_inicial)
    player.inventario.equipar(arma_inicial)
    player.inventario.equipar(armadura_inicial)

    onda = 1
    while player.atributos.esta_vivo:
        exibir_status(player)
        print(f"\nPróximo desafio: Onda {onda}")
        print("1 - Entrar em combate")
        print("2 - Gerenciar inventário")
        print("3 - Descansar (+15 HP)")
        print("0 - Sair do jogo")

        opcao = input("> ").strip()
        if opcao == "1":
            inimigo = criar_inimigo(onda)
            resultado = iniciar_batalha(player, inimigo)
            if resultado == "vitoria":
                onda += 1
            elif resultado == "derrota":
                break
        elif opcao == "2":
            gerenciar_inventario(player)
        elif opcao == "3":
            antes = player.atributos.vida_atual
            player.atributos.curar(15)
            print(f"Você descansou e recuperou {player.atributos.vida_atual - antes} HP.")
        elif opcao == "0":
            print("Encerrando o jogo. Até a próxima!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()