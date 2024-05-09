from random import randint

lista_npcs = []

player = {
    "name": 'Matias',
    "level": 1,
    "exp": 0,
    "exp_max": 7,
    "hp": 100,
    "hp_max": 100,
    "dano": 25,
}

def criar_npc(level):

    novo_npc = {
        "name": f'Monstro #{level}',
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level,
        "hp_max": 100 * level,
        "exp": 7 * level
        
    }


    return novo_npc

def exibir_npcs():
    for npc in lista_npcs:
        print(
            f"Nome: {npc['name']} // Level: {npc['level']} // Dano: {npc['dano']} // HP: {npc['hp']} // EXP: {npc['exp']}"
        )

def exibir_npc(npc):
    print(
        f"Nome: {npc['name']} // Level: {npc['level']} // Dano: {npc['dano']} // HP: {npc['hp']} // EXP: {npc['exp']}"
    )

def exibir_player():
    print(
        f"Nome: {player['name']} // Level: {player['level']} // Dano: {player['dano']} // HP: {player['hp']}/{player['hp_max']} // EXP: {player['exp']}/{player['exp_max']}"
    )

def reset_player():
    player['hp'] = player['hp_max']

def reset_npc(npc):
    npc['hp'] = npc['hp_max']

def level_up():
    if player['exp'] >= player['exp_max']:
        player['level'] += 1
        player['exp_max'] *= player['level']
        player['exp'] = 0
        player['hp_max'] += 20
        player['dano'] += 30

def iniciar_batalha(npc):
    while player['hp'] > 0 and npc['hp'] > 0:
        atacar_npc(npc)
        atacar_player(npc)
        exibir_info_batalha(npc)

    if player['hp'] > 0:
        print(f"O player {player['name']} venceu e ganhou {npc['exp']} de EXP!")
        player['exp'] += npc['exp']
        exibir_player()
    else:
        print('Game over, you died')
        exibir_npcs(npc)
    level_up()
    reset_player()
    reset_npc(npc)

def atacar_npc(npc):
    npc["hp"] -= player["dano"]

def atacar_player(npc):
    player["hp"] -= npc["dano"]

def exibir_info_batalha(npc):
    print(f"Player HP: {player['hp']}/{player['hp_max']}")
    print(f"NPC: {npc['name']}: {npc['hp']}/{npc['hp_max']}")
    print('--------------------------\n ')

def gerar_npcs(n_npcs):
    for x in range(n_npcs):
        novo_npc = criar_npc(x+1)
        lista_npcs.append(novo_npc)
        
gerar_npcs(5)
exibir_npcs()
for npc in lista_npcs:
    iniciar_batalha(npc)
