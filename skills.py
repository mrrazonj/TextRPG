import random
import menus


def compute_resistance(damage_dealt, entity_defense):
    if damage_dealt - entity_defense < 0:
        return 0
    else:
        return int(damage_dealt - entity_defense)


def tick_buff_duration(atk_buff_duration, def_buff_duration):
    if atk_buff_duration > 0:
        atk_buff_duration -= 1
    if def_buff_duration > 0:
        def_buff_duration -= 1
    return atk_buff_duration, def_buff_duration


def remove_buff(player, player_atk, player_def, atk_buff_duration, def_buff_duration):
    if atk_buff_duration == 0:
        player_atk = player.combat_atk
    if def_buff_duration == 0:
        player_def = player.combat_def
    return player_atk, player_def


def normal_attack(player, enemy, player_hp, player_atk, player_def, player_ap, enemy_hp, enemy_atk, enemy_def,
                  enemy_ap, order):
    end_turn = False
    menus.clear()

    if order == 1:
        damage_dealt = compute_resistance(player.combat_atk * 0.75, enemy.combat_def)
        enemy_hp -= damage_dealt
        print(f"{player.desc_name} attacked for {damage_dealt} damage!")
        menus.pause()
        return player, enemy, player_hp, player_atk, player_def, player_ap, enemy_hp, enemy_atk, enemy_def, enemy_ap, \
            end_turn

    elif order == 2:
        player_ap -= 1
        damage_dealt = compute_resistance(player.combat_atk * 0.95, enemy.combat_def)
        enemy_hp -= damage_dealt
        print(f"{player.desc_name} attacked for {damage_dealt} damage!")
        menus.pause()
        return player, enemy, player_hp, player_atk, player_def, player_ap, enemy_hp, enemy_atk, enemy_def, enemy_ap, \
            end_turn

    elif order == 3:
        player_ap -= 2
        damage_dealt = compute_resistance(player.combat_atk * 1.20, enemy.combat_def)
        enemy_hp -= damage_dealt
        print(f"{player.desc_name} attacked for {damage_dealt} damage!")
        menus.pause()
        return player, enemy, player_hp, player_atk, player_def, player_ap, enemy_hp, enemy_atk, enemy_def, enemy_ap, \
            end_turn


def bide(player, enemy, player_hp, player_atk, player_def, player_ap, enemy_hp, enemy_atk, enemy_def, enemy_ap, order):
    end_turn = True
    menus.clear()

    if order == 1:
        player_ap += 4
        print(f"{player.desc_name} opts to bide their time, gaining 4 bonus AP!")
        menus.pause()
        return player, enemy, player_hp, player_atk, player_def, player_ap, enemy_hp, enemy_atk, enemy_def, enemy_ap, \
            end_turn

    elif order == 2:
        player_ap += 2
        print(f"{player.desc_name} opts to bide their time, gaining 2 bonus AP!")
        menus.pause()
        return player, enemy, player_hp, player_atk, player_def, player_ap, enemy_hp, enemy_atk, enemy_def, enemy_ap, \
            end_turn

    elif order == 3:
        print(f"{player.desc_name} opts to bide their time!")
        menus.pause()
        return player, enemy, player_hp, player_atk, player_def, player_ap, enemy_hp, enemy_atk, enemy_def, enemy_ap, \
            end_turn


def bash(player, enemy, player_hp, player_atk, player_def, player_ap, enemy_hp, enemy_atk, enemy_def, enemy_ap, order):
    end_turn = False
    menus.clear()

    if order == 1:
        player_ap -= 1
        damage_dealt = compute_resistance(player.combat_atk * 0.8, enemy.combat_def)
        def_reduction = int(enemy.combat_def * (.30 + random.uniform(0, 0.20)))
        enemy_hp -= damage_dealt
        enemy.combat_def -= def_reduction
        print(f"{player.desc_name} bashed {enemy.desc_name}'s armor in, dealing {damage_dealt} damage "
              f"and reducing its defense by {def_reduction}")
        menus.pause()
        return player, enemy, player_hp, player_atk, player_def, player_ap, enemy_hp, enemy_atk, enemy_def, enemy_ap, \
            end_turn

    elif order == 2:
        player_ap -= 2
        damage_dealt = compute_resistance(player.combat_atk * 1.25, enemy.combat_def)
        ap_reduction = int(round(damage_dealt / 80))
        enemy_hp -= damage_dealt
        enemy_ap -= ap_reduction
        print(f"{player.desc_name} bashed {enemy.desc_name}'s head in, dealing {damage_dealt} damage and "
              f"reducing its AP by {ap_reduction}!")
        menus.pause()
        return player, enemy, player_hp, player_atk, player_def, player_ap, enemy_hp, enemy_atk, enemy_def, enemy_ap, \
            end_turn

    elif order == 3:
        player_ap -= 4
        damage_dealt = compute_resistance(player.combat_atk * 1.50, enemy.combat_def)
        nullify_probability = random.random() * 100
        if nullify_probability <= (10 + int(player.stat_str * 0.20)):
            enemy_ap -= enemy.combat_ap
            print("Enemy next turn AP income is nullified!")
        enemy_hp -= damage_dealt
        print(f"{player.desc_name} bashed {enemy.desc_name} face in, dealing {damage_dealt} damage!")
        menus.pause()
        return player, enemy, player_hp, player_atk, player_def, player_ap, enemy_hp, enemy_atk, enemy_def, enemy_ap, \
            end_turn


def rush(player, enemy, player_hp, player_atk, player_def, player_ap, enemy_hp, enemy_atk, enemy_def, enemy_ap, order):
    end_turn = False
    menus.clear()

    if order == 1:
        player_ap -= 1
        damage_dealt = compute_resistance(player.combat_atk * 0.50, enemy.combat_def)
        enemy_hp -= damage_dealt * 2
        print(f"{player.desc_name} attacked twice for {damage_dealt} each!")
        bonus_atk_probability = random.random() * 100
        if bonus_atk_probability <= (30 + player.stat_dex):
            damage_dealt = compute_resistance(player.combat_atk * 0.75, enemy.combat_def)
            enemy_hp -= damage_dealt
            print(f"{player.desc_name} found an opening and attacked once more for {damage_dealt}!")
        menus.pause()

    elif order == 2:
        player_ap -= 3
        damage_dealt = compute_resistance(player.combat_atk * 0.70, enemy.combat_def)
        enemy_hp -= damage_dealt * 2
        print(f"{player.desc_name} attacked twice for {damage_dealt} each!")
        bonus_atk_probability = random.random() * 100
        if bonus_atk_probability <= (45 + player.stat_dex):
            damage_dealt = compute_resistance(player.combat_atk * 0.85, enemy.combat_def)
            enemy_hp -= damage_dealt
            print(f"{player.desc_name} found an opening and attacked once more for {damage_dealt}!")
            bonus_atk_probability = random.random() * 100
            if bonus_atk_probability <= (20 + player.stat_dex):
                damage_dealt = compute_resistance(player.combat_atk * 0.75, enemy.combat_def)
                enemy_hp -= damage_dealt
                print(f"{player.desc_name} took advantage of the dazed enemy to attack again for {damage_dealt}!")
        menus.pause()

    elif order == 3:
        player_ap -= 5
        damage_dealt = int(player.combat_atk * 3.20)
        enemy_hp -= damage_dealt
        print(f"{player.desc_name} dealt {damage_dealt} absolute damage by attacking "
              f"the enemy's weak point four times!")
        menus.pause()

    return player, enemy, player_hp, player_atk, player_def, player_ap, enemy_hp, enemy_atk, enemy_def, enemy_ap, \
        end_turn


def execute(player, enemy, player_hp, player_atk, player_def, player_ap, enemy_hp, enemy_atk, enemy_def, enemy_ap,
            order):
    end_turn = True
    menus.clear()

    if order == 1:
        player_ap -= 3
        damage_dealt = compute_resistance(player.combat_atk * 1.20, enemy.combat_def)
        enemy_hp -= damage_dealt
        absolute_health_damage = int((enemy.combat_hp - enemy_hp) * 0.30)
        if enemy.is_boss:
            absolute_health_damage /= 2
            int(absolute_health_damage)
        enemy_hp -= absolute_health_damage
        print(f"{player.desc_name} tried to strike {enemy.desc_name} vital organs, dealing "
              f"{damage_dealt + absolute_health_damage} damage!")
        menus.pause()

    elif order == 2:
        player_ap -= 6
        damage_dealt = compute_resistance(player.combat_atk * 1.80, enemy.combat_def)
        enemy_hp -= damage_dealt
        absolute_health_damage = int((enemy.combat_hp - enemy_hp) * 0.50)
        if enemy.is_boss:
            absolute_health_damage /= 2
            int(absolute_health_damage)
        enemy_hp -= absolute_health_damage
        print(f"{player.desc_name} tried to strike {enemy.desc_name}'s heart, dealing "
              f"{damage_dealt + absolute_health_damage} damage!")
        menus.pause()

    elif order == 3:
        player_ap -= 10
        damage_dealt = compute_resistance(player.combat_atk * 2.40, enemy.combat_def)
        enemy_hp -= damage_dealt
        absolute_health_damage = int(enemy.combat_hp - enemy_hp)
        if enemy.is_boss:
            absolute_health_damage /= 2
            int(absolute_health_damage)
        enemy_hp -= absolute_health_damage
        print(f"{player.desc_name} tried to decapitate {enemy.desc_name}, dealing "
              f"{damage_dealt + absolute_health_damage} damage!")
        menus.pause()

    return player, enemy, player_hp, player_atk, player_def, player_ap, enemy_hp, enemy_atk, enemy_def, enemy_ap, \
        end_turn


def reckless_onslaught(player, enemy, player_hp, player_atk, player_def, player_ap, enemy_hp, enemy_atk, enemy_def,
                       enemy_ap, order):
    end_turn = False
    menus.clear()

    if order == 1:
        player_ap -= 2
        damage_dealt = compute_resistance(player_atk * 2, enemy_def)
        self_damage = int(round(damage_dealt / 2))
        enemy_hp -= damage_dealt
        player_hp -= self_damage
        if player.has_permanent_atk_buff and player.attack_buff_remaining_turns > 0:
            player_atk = player.combat_atk * 3
            int(round(player_atk))
            player.attack_buff_remaining_turns = 1
        elif player.attack_buff_remaining_turns > 0:
            player_atk = player.combat_atk * 1.50
            int(round(player_atk))
            player.attack_buff_remaining_turns = 1
        else:
            player_atk *= 1.50
            int(round(player_atk))
            player.attack_buff_remaining_turns = 1
        print(f"{player.desc_name} daringly charged {enemy.desc_name} for {damage_dealt} damage, and half of that "
              f"as self damage, {player.desc_name} also empowered his follow-up!")
        menus.pause()

    elif order == 2:
        player_ap -= 5
        damage_dealt = compute_resistance(player_atk * 3.5, enemy_def)
        self_damage = int(round(damage_dealt / 2))
        enemy_hp -= damage_dealt
        player_hp -= self_damage
        if player.has_permanent_atk_buff and player.attack_buff_remaining_turns > 0:
            player_atk = player.combat_atk * 4
            int(round(player_atk))
            player.attack_buff_remaining_turns = 1
        elif player.attack_buff_remaining_turns > 0:
            player_atk = player.combat_atk * 2
            int(round(player_atk))
            player.attack_buff_remaining_turns = 1
        else:
            player_atk *= 2
            int(round(player_atk))
            player.attack_buff_remaining_turns = 1
        print(f"{player.desc_name} rashly assailed {enemy. desc_name} for {damage_dealt} damage, and half of that "
              f"as self damage, {player.desc_name} also empowered his finishing move!")
        menus.pause()

    elif order == 3:
        player_ap -= 8
        damage_dealt = compute_resistance(player_atk * 5, enemy_def)
        self_damage = int(round(damage_dealt / 2))
        enemy_hp -= damage_dealt
        player_hp -= self_damage
        if not player.has_permanent_atk_buff:
            player_atk *= 2
            int(round(player_atk))
            player.has_permanent_atk_buff = True

        print(f"{player.desc_name} recklessly demolished {enemy.desc_name} for {damage_dealt} damage, and half of that "
              f"as self damage, {player.desc_name} also empowered all his moves!")
        menus.pause()

    return player, enemy, player_hp, player_atk, player_def, player_ap, enemy_hp, enemy_atk, enemy_def, enemy_ap, \
        end_turn


def chaotic_drive(player, enemy, player_hp, player_atk, player_def, player_ap, enemy_hp, enemy_atk, enemy_def,
                  enemy_ap, order):
    # TODO opening, follow-up, finishing
    end_turn = False
    menus.clear()

    if order == 1:
        # TODO
        pass

    return player, enemy, player_hp, player_atk, player_def, player_ap, enemy_hp, enemy_atk, enemy_def, enemy_ap, \
        end_turn


dict_common_skills = {
    "Normal Attack": ["Normal Attack", 1, 0, normal_attack],
    "Bide": ["Bide", 1, 1, bide],
}

dict_skills = {
    "Warrior": [["Bash", 1, 1, bash],
                ["Rush", 11, 3, rush],
                ["Execute", 21, 5, execute],
                ["Reckless Onslaught", 31, 5, reckless_onslaught],
                ["Chaotic Drive", 40, 7, chaotic_drive]]
}
