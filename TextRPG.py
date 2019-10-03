import sys
from os import system, name
from collections import defaultdict
import random
from datetime import datetime


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


class Entity:
    def __init__(self, level, desc_name, desc_race, base_hp, base_ap, base_spd, base_atk, base_def,
                 desc_job, stat_str, stat_dex, stat_con, stat_int, stat_luk):
        self.base_hp = base_hp
        self.base_ap = base_ap
        self.base_spd = base_spd
        self.base_atk = base_atk
        self.base_def = base_def

        self.stat_str = stat_str
        self.stat_dex = stat_dex
        self.stat_con = stat_con
        self.stat_int = stat_int
        self.stat_luk = stat_luk

        self.init_stats()

        self.desc_name = desc_name
        self.desc_race = desc_race
        self.desc_job = desc_job
        self.level = level

    def show_stats(self):
        clear()
        print("========================================")
        print(self.desc_name)
        print("Lv", end='')
        print(self.level, end=' ')
        print(self.desc_race, end=' ')
        print(self.desc_job)
        print("========================================")
        print("HP: ", end='')
        print(self.combat_hp)
        print("AP: ", end='')
        print(self.combat_ap)
        print("Spd: ", end='')
        print(self.combat_spd)
        print("Atk: ", end='')
        print(self.combat_atk)
        print("Def: ", end='')
        print(self.combat_def)
        print("========================================")
        print("Str: ", end='')
        print(self.stat_str)
        print("Dex: ", end='')
        print(self.stat_dex)
        print("Con: ", end='')
        print(self.stat_con)
        print("Int: ", end='')
        print(self.stat_int)
        print("Luk: ", end='')
        print(self.stat_luk)
        print("========================================")
        pause()

    def init_stats(self):
        self.combat_hp = self.base_hp + (self.stat_str * 30) + (self.stat_con * 55)
        self.combat_ap = self.base_ap + int(self.stat_dex * 0.03)
        self.combat_spd = self.base_spd + (self.stat_dex * 1)
        if self.stat_str * 5 > self.stat_int * 3:
            self.combat_atk = self.base_atk + (self.stat_str * 5)
        else:
            self.combat_atk = self.base_atk + (self.stat_int * 3)
        self.combat_def = self.base_def + (self.stat_con * 4)


class Enemy(Entity):
    def __init__(self, level, desc_name, desc_race, base_hp, base_ap, base_spd, base_atk, base_def,
                 desc_job, stat_str, stat_dex, stat_con, stat_int, stat_luk, loot, has_rare):
        super().__init__(level, desc_name, desc_race, base_hp, base_ap, base_spd, base_atk, base_def,
                         desc_job, stat_str, stat_dex, stat_con, stat_int, stat_luk)

        self.update_stats()

        self.has_rare = has_rare
        if self.has_rare:
            self.loot_dropped = dict_rare_item_id[loot]
        else:
            self.loot_dropped = dict_item_id[loot]

    def update_stats(self):
        dict_job_level_modifiers = {
            # Str, Dex, Con, Int, Luk
            "Warrior": [4, 3, 1, 1, 1],
            "Knight": [2, 1, 5, 1, 1],
            "Ranger": [1, 5, 1, 1, 2],
            "Mage": [1, 1, 1, 6, 1],
            "Priest": [2, 2, 2, 2, 2]
        }

        list_attributes = [self.stat_str, self.stat_dex, self.stat_con, self.stat_int, self.stat_luk]

        for i, value in enumerate(dict_job_level_modifiers[self.desc_job]):
            list_attributes[i] += value * self.level
        self.stat_str = list_attributes[0]
        self.stat_dex = list_attributes[1]
        self.stat_con = list_attributes[2]
        self.stat_int = list_attributes[3]
        self.stat_luk = list_attributes[4]

        self.init_stats()

    def show_loot(self):
        print(f"Monster is carrying {self.loot_dropped[-1]}!")


class Player(Entity):
    def __init__(self, level, desc_name, desc_race, base_hp, base_ap, base_spd, base_atk, base_def,
                 desc_job, stat_str, stat_dex, stat_con, stat_int, stat_luk):
        super().__init__(level, desc_name, desc_race, base_hp, base_ap, base_spd, base_atk, base_def,
                         desc_job, stat_str, stat_dex, stat_con, stat_int, stat_luk)

        self.experience = 0
        self.inventory = []
        self.skill = []

        self.unallocated_stat = 0
        self.unallocated_skill = 0

        self.has_weapon_equipped = False
        self.has_armor_equipped = False
        self.equipped_weapon = ""
        self.equipped_armor = ""
        self.armor_slot = 0
        self.weapon_slot = 0

    def level_up(self):
        self.experience = 0
        self.unallocated_stat += 11
        self.unallocated_skill += 1

    def add_str(self):
        self.stat_str += 1
        self.unallocated_stat -= 1

    def add_dex(self):
        self.stat_dex += 1
        self.unallocated_stat -= 1

    def add_con(self):
        self.stat_con += 1
        self.unallocated_stat -= 1

    def add_int(self):
        self.stat_int += 1
        self.unallocated_stat -= 1

    def add_luk(self):
        self.stat_luk += 1
        self.unallocated_stat -= 1

    def show_inventory(self):
        pass

    def equip_weapon(self, hp_bonus, ap_bonus, spd_bonus, atk_bonus,
                     def_bonus, item_id, item_name):
        self.has_weapon_equipped = True
        self.equipped_weapon = item_name
        self.weapon_slot = item_id
        self.combat_hp += hp_bonus
        self.combat_ap += ap_bonus
        self.combat_spd += spd_bonus
        self.combat_atk += atk_bonus
        self.combat_def += def_bonus

    def equip_armor(self, hp_bonus, ap_bonus, spd_bonus, atk_bonus,
                    def_bonus, item_id, item_name):
        self.has_armor_equipped = True
        self.equipped_armor = item_name
        self.armor_slot = item_id
        self.combat_hp += hp_bonus
        self.combat_ap += ap_bonus
        self.combat_spd += spd_bonus
        self.combat_atk += atk_bonus
        self.combat_def += def_bonus

    def unequip_weapon(self, hp_bonus, ap_bonus, spd_bonus, atk_bonus,
                       def_bonus, item_id, item_name):
        self.has_weapon_equipped = False
        self.equipped_weapon = ""
        self.weapon_slot = 0
        self.combat_hp -= hp_bonus
        self.combat_ap -= ap_bonus
        self.combat_spd -= spd_bonus
        self.combat_atk -= atk_bonus
        self.combat_def -= def_bonus

    def unequip_armor(self, hp_bonus, ap_bonus, spd_bonus, atk_bonus,
                      def_bonus, item_id, item_name):
        self.has_armor_equipped = False
        self.equipped_armor = ""
        self.armor_slot = 0
        self.combat_hp -= hp_bonus
        self.combat_ap -= ap_bonus
        self.combat_spd -= spd_bonus
        self.combat_atk -= atk_bonus
        self.combat_def -= def_bonus


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
    for i, key in enumerate(dict_race):
        dict_race_selection[i+1] = key

    dict_job_selection = {}
    for i, key in enumerate(dict_job):
        dict_job_selection[i+1] = key

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


def spawn_monster(place_level):
    list_monster_name = ["Alfred", "Eugene", "Vincent", "Dennis", "Jericho", "Jeremiah"]

    monster_race = random.choice(list(dict_race))
    monster_job = random.choice(list(dict_job))
    monster_name = random.choice(list(list_monster_name))
    monster_level = random.randint(place_level-2, place_level+5)
    if monster_level < 1:
        monster_level = 1
    if monster_level > 40:
        monster_level = 40

    loot_probability = random.random()
    if loot_probability > 0.90:
        monster_loot_id = random.randint(place_level, place_level+10)
        has_rare = True
    elif loot_probability >= 0.66:
        monster_loot_id = random.randint(place_level, place_level+10)
        has_rare = False
    else:
        monster_loot_id = 0
        has_rare = False

    return [monster_level, monster_name, *monster_race, *monster_job, monster_loot_id, has_rare]


def travel(place_name, place_id):
    dict_place_selection = {}
    for i, key in enumerate(dict_place):
        dict_place_selection[i+1] = key

    is_correct_input = False
    while not is_correct_input:
        print(f"You are currently in {place_name}, Where would you like to go?")
        for i in range(place_id-1, place_id+2):
            if place_id-1 < 1:
                print("1 Cainta")
                print("2 Cainta Prairie")
                break
            elif place_id+1 > len(dict_place):
                print("9 Binangonan")
                print("10 Binangonan Ruins")
                break
            else:
                print(i, dict_place_selection[i])
        selection = int(input("> "))
        if selection > place_id+1 or selection < place_id-1:
            print("You have entered an invalid number, please try again.")
        else:
            is_correct_input = True
            world_menu(*dict_place[dict_place_selection[selection]])


def character_menu(place_name):
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
            print(i+1, value)
        selection = int(input("> "))
        if selection == 1:
            is_correct_input = True
        elif selection == 2:
            is_correct_input = True
        elif selection == 3:
            is_correct_input = True
        elif selection == 4:
            is_correct_input = True
        elif selection == 5:
            is_correct_input = True
            world_menu(*dict_place[place_name])
        elif selection == 6:
            sys.exit(0)


def world_menu(place_name, place_type, place_id, place_level):
    list_town_selection = [
        "Manage character",
        "Go to shop",
        "Travel"
    ]

    list_dungeon_selection = [
        "Hunt Boss Monster",
        "Hunt Normal Monsters",
        "Travel"
    ]

    is_correct_input = False
    while not is_correct_input:
        clear()
        print(f"You are now in the {place_type} of {place_name}")

        if place_type == "town":
            for i, value in enumerate(list_town_selection):
                print(i+1, value)
            selection = int(input("> "))
            if selection == 1:
                is_correct_input = True
                character_menu(place_name)
            elif selection == 2:
                is_correct_input = True
            elif selection == 3:
                is_correct_input = True
                travel(place_name, place_id)

        else:
            for i, value in enumerate(list_dungeon_selection):
                print(i+1, value)
            selection = int(input("> "))
            if selection == 1:
                is_correct_input = True
            elif selection == 2:
                is_correct_input = True
                enemy = Enemy(*spawn_monster(place_level))
                enemy.show_stats()
            elif selection == 3:
                is_correct_input = True
                travel(place_name, place_id)


if __name__ == '__main__':
    random.seed(datetime.now())

    dict_race = {
        # Name, Str, Dex, Con, Int, Luk
        "Human": ["Human", 125, 3, 8, 6, 5],
        "Elf": ["Elf", 100, 4, 12, 5, 3],
        "Orc": ["Orc", 200, 2, 6, 9, 7],
        "Troll": ["Troll", 250, 1, 2, 15, 10],
        "Dwarf": ["Dwarf", 150, 3, 7, 8, 8],
        "Kobold": ["Kobold", 70, 3, 9, 4, 2]
    }

    dict_job = {
        # Name, Str, Dex, Con, Int, Luk
        "Warrior": ["Warrior", 20, 14, 12, 8, 12],
        "Knight": ["Knight", 16, 7, 20, 10, 13],
        "Mage": ["Mage", 9, 12, 8, 26, 11],
        "Ranger": ["Ranger", 11, 18, 10, 12, 15],
        "Priest": ["Priest", 11, 13, 16, 14, 12]
    }

    dict_place = {
        # Name, Type, ID, Level
        "Cainta": ["Cainta", "town", 1, 1],
        "Cainta Prairie": ["Cainta Prairie", "dungeon", 2, 1],
        "Taytay": ["Taytay", "town", 3, 11],
        "Taytay Caverns": ["Taytay Caverns", "dungeon", 4, 11],
        "Antipolo": ["Antipolo", "town", 5, 21],
        "Antipolo Peaks": ["Antipolo Peaks", "dungeon", 6, 21],
        "Angono": ["Angono", "town", 7, 31],
        "Angono Sanctuary": ["Angono Sanctuary", "dungeon", 8, 31],
        "Binangonan": ["Binangonan", "town", 9, 40],
        "Binangonan Ruins": ["Binangonan Ruins", "dungeon", 10, 40]
    }

    dict_item_id = defaultdict(lambda: [0, 0, 0, 0, 0, 0, "none"])
    dict_item_id.update({
        # HP, AP, Spd, Atk, Def, ID, Name
        0: [0, 0, 0, 0, 0, 0, "none"],
        1: [0, 1, 4, 25, 0, 1, "Rusty Axe"],
        2: [0, 0, 2, 40, 15, 2, "Chipped Sword"],
        3: [0, 2, 6, 15, 10, 3, "Crude Bow"],
        4: [0, 0, 2, 75, 0, 4, "Mundane Staff"],
        5: [0, 1, 3, 35, 5, 5, "Broken Rod"],
        6: [150, 0, 2, 0, 20, 6, "Torn Fur Armor"],
        7: [250, 0, 0, 0, 35, 7, "Tarnished Copper Armor"],
        8: [100, 1, 4, 0, 15, 8, "Old Leather Armor"],
        9: [50, 0, 3, 0, 12, 9, "Unremarkable Robe"],
        10: [100, 0, 3, 0, 18, 10, "Unblessed Vestments"]
    })

    dict_rare_item_id = defaultdict(lambda: [0, 0, 0, 0, 0, 0, "none"])
    dict_item_id.update({
        # HP, AP, Spd, Atk, Def, ID, Name
        0: [0, 0, 0, 0, 0, 0, "none"],
        1: [0, 1, 6, 40, 10, 11, "Executioner's Axe"],
        2: [200, 0, 2, 40, 18, 12, "Inquisitor's Sword"],
        3: [0, 3, 12, 20, 12, 13, "Elven Bow"],
        4: [0, 1, 6, 125, 9, 14, "Purification Staff"],
        5: [120, 1, 5, 60, 15, 15, "Exorcism Rod"],
        6: [250, 1, 4, 30, 35, 16, "Chieftain's Fur Armor"],
        7: [600, 0, 0, 20, 60, 17, "Crusader's Copper Armor"],
        8: [180, 2, 6, 10, 25, 18, "Elven Leather Armor"],
        9: [80, 1, 5, 40, 15, 19, "Mystical Robe"],
        10: [150, 1, 6, 20, 30, 20, "Priest's Vestments"]
    })

    main_menu()
    main_menu_input = int(input("> "))
    clear()

    if main_menu_input == 1:
        opening_scene()

        character_data = character_creation()
        player = Player(character_data[0], character_data[1], *dict_race[character_data[2]],
                        *dict_job[character_data[3]])
        player.show_stats()
        world_menu(*dict_place["Cainta"])

    elif main_menu_input == 2:
        pass
    else:
        pass
