import random
import menus


def normal_attack(player, enemy, player_hp, player_ap, enemy_hp, enemy_ap, order):
    end_turn = False
    menus.clear()
    if order == 1:
        enemy_hp -= int((player.combat_atk * 0.75) - enemy.combat_def)
        print(f"{player.desc_name} attacked for {int((player.combat_atk * 0.75) - enemy.combat_def)} damage!")
        menus.pause()
        return player, enemy, player_hp, player_ap, enemy_hp, enemy_ap, end_turn
    elif order == 2:
        player_ap -= 1
        enemy_hp -= int((player.combat_atk * 0.95) - enemy.combat_def)
        print(f"{player.desc_name} attacked for {int((player.combat_atk * 0.95) - enemy.combat_def)} damage!")
        menus.pause()
        return player, enemy, player_hp, player_ap, enemy_hp, enemy_ap, end_turn
    elif order == 3:
        player_ap -= 2
        enemy_hp -= int((player.combat_atk * 1.20) - enemy.combat_def)
        print(f"{player.desc_name} attacked for {int((player.combat_atk * 1.20) - enemy.combat_def)} damage!")
        menus.pause()
        return player, enemy, player_hp, player_ap, enemy_hp, enemy_ap, end_turn


def bide(player, enemy, player_hp, player_ap, enemy_hp, enemy_ap, order):
    end_turn = True
    menus.clear()
    if order == 1:
        player_ap += 4
        print(f"{player.desc_name} opts to bide their time, gaining 4 bonus AP!")
        menus.pause()
        return player, enemy, player_hp, player_ap, enemy_hp, enemy_ap, end_turn
    elif order == 2:
        player_ap += 2
        print(f"{player.desc_name} opts to bide their time, gaining 2 bonus AP!")
        menus.pause()
        return player, enemy, player_hp, player_ap, enemy_hp, enemy_ap, end_turn
    elif order == 3:
        print(f"{player.desc_name} opts to bide their time!")
        menus.pause()
        return player, enemy, player_hp, player_ap, enemy_hp, enemy_ap, end_turn


def bash(player, enemy, player_hp, player_ap, enemy_hp, enemy_ap, order):
    end_turn = False
    menus.clear()
    if order == 1:
        player_ap -= 1
        enemy_hp -= int((player.combat_atk * 0.8) - enemy.combat_def)
        def_reduction = int(enemy.combat_def * (.30 + random.uniform(0, 0.20)))
        enemy.combat_def -= def_reduction
        print(f"{player.desc_name} bashed {enemy.desc_name}'s armor in, dealing "
              f"{int((player.combat_atk * 0.8) - enemy.combat_def)} damage and reducing its defense by {def_reduction}")
        menus.pause()
        return player, enemy, player_hp, player_ap, enemy_hp, enemy_ap, end_turn
    elif order == 2:
        player_ap -= 2
        enemy_ap -= int(((player.combat_atk * 1.25) - enemy.combat_def) / 80)
        enemy_hp -= int((player.combat_atk * 1.25) - enemy.combat_def)
        print(f"{player.desc_name} bashed {enemy.desc_name}'s head in, dealing "
              f"{int((player.combat_atk * 1.25) - enemy.combat_def)} damage and reducing its AP by "
              f"{int(((player.combat_atk * 1.25) - enemy.combat_def) / 80)}!")
        menus.pause()
        return player, enemy, player_hp, player_ap, enemy_hp, enemy_ap, end_turn
    elif order == 3:
        player_ap -= 4
        nullify_probability = random.random() * 100
        if nullify_probability <= (2 + (player.stat_str * 0.20)):
            enemy_ap -= enemy.combat_ap
            print("Enemy next turn AP income is nullified!")
        enemy_hp -= int((player.combat_atk * 1.50) - enemy.combat_def)
        print(f"{player.desc_name} bashed {enemy.desc_name} face in, dealing "
              f"{int((player.combat_atk * 1.50) - enemy.combat_def)} damage!")
        menus.pause()
        return player, enemy, player_hp, player_ap, enemy_hp, enemy_ap, end_turn


dict_common_skills = {
    "Normal Attack": ["Normal Attack", 1, 0, normal_attack],
    "Bide": ["Bide", 1, 1, bide],
}

dict_skills = {
    "Warrior": [["Bash", 1, 1, bash],
                ["Rush", 11, 3],
                ["Execute", 21, 5],
                ["Reckless Onslaught", 31, 5],
                ["Chaotic Drive", 40, 7]]
}