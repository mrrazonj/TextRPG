from os import system, name
import sys

import random
import world_db


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def pause():
    if name == "nt":
        _ = system("pause")
    else:
        _ = input()


def travel_menu(place_name, place_id):
    dict_place_selection = {}
    for i, key in enumerate(world_db.dict_place):
        dict_place_selection[i + 1] = key

    is_correct_input = False
    while not is_correct_input:
        clear()
        print(f"You are currently in {place_name}, Where would you like to go?")
        for i in range(place_id - 1, place_id + 2):
            if place_id - 1 < 1:
                print("1 Cainta")
                print("2 Cainta Prairie")
                break
            elif place_id + 1 > len(world_db.dict_place):
                print("9 Binangonan")
                print("10 Binangonan Ruins")
                break
            else:
                print(i, dict_place_selection[i])
        selection = int(input("> "))
        if selection > place_id + 1 or selection < place_id - 1:
            print("You have entered an invalid number, please try again.")
            pause()
        else:
            selected = dict_place_selection[selection]
            is_correct_input = True
            return selected


def character_menu(player):
    list_character_menu = [
        "Manage Inventory",
        "View Stats",
        "View Skills",
        "Save",
        "Exit Menu",
        "Quit"
    ]

    is_correct_input = False
    while not is_correct_input:
        clear()
        print(f"What would you like to do, {player.desc_name}?")
        for i, value in enumerate(list_character_menu):
            print(i + 1, value)
        selection = int(input("> "))
        if selection == 1:
            is_correct_input = True
        elif selection == 2:
            is_correct_input = True
        elif selection == 3:
            skill_menu(player)
            is_correct_input = True
        elif selection == 4:
            is_correct_input = True
        elif selection == 5:
            is_correct_input = True
        elif selection == 6:
            sys.exit(0)


def main_menu():
    print("▄▄▄█████▓█████ ██▀███  ███▄ ▄███▓██▓███▄    █ ▄▄▄      ██▓    ")
    print("▓  ██▒ ▓▓█   ▀▓██ ▒ ██▓██▒▀█▀ ██▓██▒██ ▀█   █▒████▄   ▓██▒    ")
    print("▒ ▓██░ ▒▒███  ▓██ ░▄█ ▓██    ▓██▒██▓██  ▀█ ██▒██  ▀█▄ ▒██░    ")
    print("░ ▓██▓ ░▒▓█  ▄▒██▀▀█▄ ▒██    ▒██░██▓██▒  ▐▌██░██▄▄▄▄██▒██░    ")
    print("  ▒██▒ ░░▒████░██▓ ▒██▒██▒   ░██░██▒██░   ▓██░▓█   ▓██░██████▒")
    print("  ▒ ░░  ░░ ▒░ ░ ▒▓ ░▒▓░ ▒░   ░  ░▓ ░ ▒░   ▒ ▒ ▒▒   ▓▒█░ ▒░▓  ░")
    print("    ░    ░ ░  ░ ░▒ ░ ▒░  ░      ░▒ ░ ░░   ░ ▒░ ▒   ▒▒ ░ ░ ▒  ░")
    print("  ░        ░    ░░   ░░      ░   ▒ ░  ░   ░ ░  ░   ▒    ░ ░   ")
    print("    ██▀███ ▓███████▒   █▓█████ ██▀███  ██▓█████    ░  ░   ░  ░")
    print("   ▓██ ▒ ██▓█   ▓██░   █▓█   ▀▓██ ▒ ██▓██▓█   ▀               ")
    print("   ▓██ ░▄█ ▒███  ▓██  █▒▒███  ▓██ ░▄█ ▒██▒███                 ")
    print("   ▒██▀▀█▄ ▒▓█  ▄ ▒██ █░▒▓█  ▄▒██▀▀█▄ ░██▒▓█  ▄               ")
    print("   ░██▓ ▒██░▒████▒ ▒▀█░ ░▒████░██▓ ▒██░██░▒████▒              ")
    print("   ░ ▒▓ ░▒▓░░ ▒░ ░ ░ ▐░ ░░ ▒░ ░ ▒▓ ░▒▓░▓ ░░ ▒░ ░              ")
    print("     ░▒ ░ ▒░░ ░  ░ ░ ░░  ░ ░  ░ ░▒ ░ ▒░▒ ░░ ░  ░              ")
    print("     ░░   ░   ░      ░░    ░    ░░   ░ ▒ ░  ░                 ")
    print("      ░       ░  ░    ░    ░  ░  ░     ░    ░  ░              ")
    print("                     ░                                        ")
    print("1. New Game\t\t2.Continue")
    print("3. Quit")


def opening_scene():
    pass


def character_creation():
    dict_race_selection = {}
    for i, key in enumerate(world_db.dict_race):
        dict_race_selection[i + 1] = key

    dict_job_selection = {}
    for i, key in enumerate(world_db.dict_job):
        dict_job_selection[i + 1] = key

    is_name_final = False
    desc_name = ''
    while not is_name_final:
        clear()
        desc_name = input("Enter your name> ")
        clear()
        print("You will be known as", desc_name, "throughout the realm.")

        name_finalization_input = input("You cannot change your name beyond this point, continue? (y/n) > ")
        is_name_final = True if name_finalization_input == 'y' else False

    specs_2d = [['race', dict_race_selection], ['job', dict_job_selection]]
    specs_list = []
    for spec, spec_dict in specs_2d:
        is_desc_final = False
        while not is_desc_final:
            clear()
            print(f"Now you must choose your {spec}")
            for i in spec_dict:
                print(i, spec_dict[i])
            spec_selected = int(input("> "))
            clear()
            if spec_selected > len(spec_dict) or spec_selected < 1:
                print("You have entered an invalid number, please try again.")
                continue
            else:
                print(f"You have selected {spec_dict[spec_selected]} as your {spec}.")
                finalization_input = input(f"You cannot change your {spec} beyond this point, continue? (y/n) >")
                if finalization_input == 'y':
                    is_desc_final = True
                    specs_list.append(spec_dict[spec_selected])

    return [1, desc_name, *specs_list]


def player_turn(player, enemy, player_hp, enemy_hp, player_ap, is_in_battle):
    # Turn initialization
    list_combat_selection = ["Technique", "Magic", "Check loot", "Items", "Flee"]
    player_ap += player.combat_ap

    clear()
    print(f"{player.desc_name}'s turn!")
    pause()

    while enemy_hp > 0 and player_hp > 0 and player_ap > 0 and is_in_battle:
        clear()
        print(f"{player.desc_name}'s HP: {player_hp}\t\t", f"{enemy.desc_name}'s HP: {enemy_hp}")
        print(f"Remaining AP: {player_ap}")
        print("What would you like to do?")
        for i, command in enumerate(list_combat_selection):
            print(i + 1, command)
        selection = int(input("> "))
        if selection == 1:
            pass
        elif selection == 2:
            pass
        elif selection == 3:
            enemy.show_loot()
            player_ap -= 1
        elif selection == 4:
            pass
        elif selection == 5:
            flee_probability = random.random()
            if flee_probability >= 0.33:
                clear()
                print(f"{player.desc_name} has successfully escaped the battle!")
                pause()
                is_in_battle = False
            else:
                clear()
                print(f"{player.desc_name} failed to escape!")
                pause()
                player_ap = 0

    return player_hp, enemy_hp, player_ap, is_in_battle


def enemy_turn(player, enemy, player_hp, enemy_hp, enemy_ap, enemy_heal_charges, is_enemy_spec_used):
    # Turn initialization
    enemy_ap += enemy.combat_ap
    # Turn flags
    has_enemy_healed = False

    clear()
    print("Enemy's Turn!")
    pause()

    while enemy_hp > 0 and player_hp > 0 and enemy_ap > 0:
        clear()
        if enemy_hp > enemy.combat_hp * 0.80:
            if int((enemy.combat_atk * 0.50) - player.combat_def) > 0:
                player_hp -= int((enemy.combat_atk * 0.50) - player.combat_def)
                print(f"Enemy attacked {player.desc_name} for {int((enemy.combat_atk * 0.50) - player.combat_def)}"
                      " damage!")
            else:
                print("Enemy did no damage!")
            enemy_ap -= 2
            pause()
        elif enemy_hp > enemy.combat_hp * 0.50:
            if int((enemy.combat_atk * 0.80) - player.combat_def) > 0:
                player_hp -= int((enemy.combat_atk * 0.80) - player.combat_def)
                print(f"Enemy viciously attacked {player.desc_name} for "
                      f"{int((enemy.combat_atk * 0.80) - player.combat_def)} damage!")
            else:
                print("Enemy did no damage!")
            enemy_ap -= 3
            pause()
        elif enemy_hp > enemy.combat_hp * 0.25:
            if enemy_heal_charges > 0 and not has_enemy_healed:
                enemy_hp += int(enemy.combat_hp * 0.15)
                enemy_heal_charges -= 1
                enemy_ap -= 2
                has_enemy_healed = True
                print(f"Enemy used a potion to heal for {int(enemy.combat_hp * 0.15)} damage!")
                pause()
            else:
                if enemy.combat_atk - player.combat_def > 0:
                    player_hp -= enemy.combat_atk - player.combat_def
                    print(f"Enemy furiously attacked {player.desc_name} "
                          f"for {enemy.combat_atk - player.combat_def} damage!")
                else:
                    print("Enemy did no damage!")
                enemy_ap -= 3
                pause()
        elif enemy_hp > enemy.combat_hp * 0.10:
            if not is_enemy_spec_used:
                player_hp -= enemy.combat_atk * 2.0
                enemy_hp += enemy.combat_atk
                enemy_ap -= 4
                is_enemy_spec_used = True
                print(f"Enemy dealt {enemy.combat_atk * 2.0} absolute damage,"
                      f" while healing for half the amount!")
                pause()
            else:
                player_hp -= enemy.combat_atk
                enemy_ap -= 3
                print(f"Enemy desperately attacked {player.desc_name} for {enemy.combat_atk} absolute damage!")
                pause()

    return player_hp, enemy_hp, enemy_ap, enemy_heal_charges, is_enemy_spec_used


def battle_menu(player, enemy):
    # ==========Initialize Stats===========
    player_hp = player.combat_hp
    enemy_hp = enemy.combat_hp
    player_ap = 0
    enemy_ap = 0
    # ===========Battle Flags==============
    is_in_battle = True
    enemy_heal_charges = 2
    is_enemy_spec_used = False

    if player.combat_spd > enemy.combat_spd:
        while enemy_hp > 0 and player_hp > 0 and is_in_battle:
            turn_computations = player_turn(player, enemy, player_hp, enemy_hp, player_ap, is_in_battle)
            player_hp, enemy_hp, player_ap, is_in_battle = turn_computations
            if not is_in_battle:
                break
            clear()
            turn_computations = enemy_turn(player, enemy, player_hp, enemy_hp, enemy_ap, enemy_heal_charges,
                                           is_enemy_spec_used)
            player_hp, enemy_hp, enemy_ap, enemy_heal_charges, is_enemy_spec_used = turn_computations
    else:
        while enemy_hp > 0 and player_hp > 0 and is_in_battle:
            turn_computations = enemy_turn(player, enemy, player_hp, enemy_hp, enemy_ap, enemy_heal_charges,
                                           is_enemy_spec_used)
            player_hp, enemy_hp, enemy_ap, enemy_heal_charges, is_enemy_spec_used = turn_computations
            clear()
            turn_computations = player_turn(player, enemy, player_hp, enemy_hp, player_ap, is_in_battle)
            player_hp, enemy_hp, player_ap, is_in_battle = turn_computations


def spawn_monster(place_level):
    list_monster_name = ["Alfred", "Eugene", "Vincent", "Dennis", "Jericho", "Jeremiah"]

    monster_race = world_db.dict_race[random.choice(list(world_db.dict_race))]
    monster_job = world_db.dict_job[random.choice(list(world_db.dict_job))]
    monster_name = random.choice(list(list_monster_name))
    monster_level = random.randint(place_level - 2, place_level + 5)
    if monster_level < 1:
        monster_level = 1
    if monster_level > 40:
        monster_level = 40

    loot_probability = random.random()
    if loot_probability > 0.90:
        monster_loot_id = random.randint(place_level, place_level + 10)
        has_rare = True
    elif loot_probability >= 0.66:
        monster_loot_id = random.randint(place_level, place_level + 10)
        has_rare = False
    else:
        monster_loot_id = 0
        has_rare = False

    return [monster_level, monster_name, *monster_race, *monster_job, monster_loot_id, has_rare]


def skill_menu(player):
    list_menu_selection = [
        "Learn Techniques",
        "Equip Techniques",
        "View Techniques"
    ]

    list_learnable_skills = world_db.dict_skills[player.desc_job]

    clear()
    print("What would you like to do?")
    for i, value in enumerate(list_menu_selection):
        print(i + 1, value)
    selection = input("> ")

    if selection == '1':
        clear()
        print("Which technique would you like to learn?")
        print(f"Remaining skillpoints: {player.unallocated_skill}")
        for i, key in enumerate(list_learnable_skills):
            print(i + 1, key[0])
        learn_selection = int(input("> "))
        if 1 > learn_selection > len(list_learnable_skills):
            clear()
            print("Invalid selection!")
            pause()
        elif list_learnable_skills[learn_selection - 1][0] in player.learned_skills:
            clear()
            print("You already know this technique!")
            pause()
        elif list_learnable_skills[learn_selection - 1][1] > player.level:
            clear()
            print(f"You need to be level {list_learnable_skills[learn_selection - 1][1]} to learn this technique!")
            pause()
        elif player.unallocated_skill < list_learnable_skills[learn_selection - 1][2]:
            clear()
            print("You don't have enough skill points!")
            pause()
        else:
            clear()
            player.learned_skills.append(list_learnable_skills[learn_selection - 1][0])
            player.unallocated_skill -= list_learnable_skills[learn_selection - 1][2]
            print(f"You have successfully learned {list_learnable_skills[learn_selection - 1][0]}!")
            pause()

    elif selection == '2':
        print("You have the following techniques currently equipped: ")
        for i, value in enumerate(player.equipped_skills):
            print(i + 1, value)
        print("============================================================")
        print("Which technique would you like to equip?")
        for i, value in enumerate(player.learned_skills):
            print(i + 1, value)
        equip_selection = int(input("> "))
        if player.learned_skills[equip_selection - 1] in player.equipped_skills:
            clear()
            print("You already have this technique equipped!")
            pause()
        else:
            if len(player.equipped_skills) >= 5:
                clear()
                print("You can only equip a maximum of 5 techniques!")
                print("Select a technique to unequip:")
                for i, value in enumerate(player.equipped_skills):
                    print(i + 1, value)
                unequip_selection = int(input("> "))
                if 1 > unequip_selection > len(player.equipped_skills):
                    clear()
                    print("Invalid selection!")
                    pause()
                else:
                    clear()
                    print(f"Successfully unequipped {player.equipped_skills[unequip_selection - 1]}")
                    del player.equipped_skills[unequip_selection - 1]
                    pause()

            clear()
            player.equipped_skills.append(player.learned_skills[equip_selection - 1])
            print(f"Successfully equipped {player.learned_skills[equip_selection - 1]}")
            pause()

    elif selection == '3':
        clear()
        print("Equipped techniques:")
        for i, value in enumerate(player.equipped_skills):
            print(i + 1, value)
        print("============================================================")
        print("Learned techniques:")
        for i in player.learned_skills:
            print(i)
        pause()