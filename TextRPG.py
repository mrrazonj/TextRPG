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

        self.combat_hp = base_hp + (stat_str * 30) + (stat_con * 55)
        self.combat_ap = int(base_ap + (stat_dex * 0.03))
        self.combat_spd = base_spd + (stat_dex * 1)
        if self.stat_str * 5 > self.stat_int * 3:
            self.combat_atk = base_atk + (stat_str * 5)
        else:
            self.combat_atk = base_atk + (stat_int * 3)
        self.combat_def = base_def + (stat_con * 4)

        self.desc_name = desc_name
        self.desc_race = desc_race
        self.desc_job = desc_job
        self.level = level

    def show_stats(self):
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


class Enemy(Entity):
    def __init__(self, level, desc_name, desc_race, base_hp, base_ap, base_spd, base_atk, base_def,
                 desc_job, stat_str, stat_dex, stat_con, stat_int, stat_luk, loot1, loot2, loot3, loot4, loot5):
        super().__init__(level, desc_name, desc_race, base_hp, base_ap, base_spd, base_atk, base_def,
                         desc_job, stat_str, stat_dex, stat_con, stat_int, stat_luk)

        self.loot_id = [loot1, loot2, loot3, loot4, loot5]

    def get_loot(self, select_item):
        return self.loot_id[select_item]


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
    print("▄▄▄█████▓▓█████  ██▀███   ███▄ ▄███▓ ██▓ ███▄    █  ▄▄▄       ██▓        ██▀███  ▓█████ ██▒   █▓▓█████  ██▀███   ██▓▓█████ ")
    print("▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▒████▄    ▓██▒       ▓██ ▒ ██▒▓█   ▀▓██░   █▒▓█   ▀ ▓██ ▒ ██▒▓██▒▓█   ▀ ")
    print("▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒▓██    ▓██░▒██▒▓██  ▀█ ██▒▒██  ▀█▄  ▒██░       ▓██ ░▄█ ▒▒███   ▓██  █▒░▒███   ▓██ ░▄█ ▒▒██▒▒███   ")
    print("░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  ▒██    ▒██ ░██░▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██░       ▒██▀▀█▄  ▒▓█  ▄  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  ░██░▒▓█  ▄ ")
    print("  ▒██▒ ░ ░▒████▒░██▓ ▒██▒▒██▒   ░██▒░██░▒██░   ▓██░ ▓█   ▓██▒░██████▒   ░██▓ ▒██▒░▒████▒  ▒▀█░  ░▒████▒░██▓ ▒██▒░██░░▒████▒")
    print("  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░▓  ░   ░ ▒▓ ░▒▓░░░ ▒░ ░  ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░░▓  ░░ ▒░ ░")
    print("    ░     ░ ░  ░  ░▒ ░ ▒░░  ░      ░ ▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░░ ░ ▒  ░     ░▒ ░ ▒░ ░ ░  ░  ░ ░░   ░ ░  ░  ░▒ ░ ▒░ ▒ ░ ░ ░  ░")
    print("  ░         ░     ░░   ░ ░      ░    ▒ ░   ░   ░ ░   ░   ▒     ░ ░        ░░   ░    ░       ░░     ░     ░░   ░  ▒ ░   ░   ")
    print("            ░  ░   ░            ░    ░           ░       ░  ░    ░  ░      ░        ░  ░     ░     ░  ░   ░      ░     ░  ░")
    print("                                                                                            ░                              ")
    print("1. New Game\t\t2.Continue")
    print("3. Quit")


def opening_scene():
    pass


def character_creation():

    player_race_dict = {1: "Human",
                        2: "Elf",
                        3: "Orc",
                        4: "Dwarf"
                        }

    player_job_dict = {1: "Warrior",
                       2: "Knight",
                       3: "Ranger",
                       4: "Mage",
                       5: "Priest"
                       }

    is_name_final = False
    while not is_name_final:
        desc_name = input("Enter your name> ")
        print("You will be known as", desc_name, "throughout the realm.")

        name_finalization_input = input("You cannot change your name beyond this point, continue? (y/n) > ")
        if name_finalization_input == 'y':
            is_name_final = True

    is_race_final = False
    while not is_race_final:
        print("Now, you must choose your race:")
        for i in player_race_dict:
            print(i, player_race_dict[i])

        race_selected = int(input("> "))
        if race_selected > len(player_race_dict) or race_selected < 1:
            print("You have entered an invalid number, please try again")
            continue
        else:
            desc_race = player_race_dict[race_selected]

        print("You have selected", desc_race, "as your race.")
        race_finalization_input = input("You cannot change your race beyond this point, continue? (y/n) > ")
        if race_finalization_input == 'y':
            is_race_final = True

    is_job_final = False
    while not is_job_final:
        print("Finally, you must choose your job:")
        for i in player_job_dict:
            print(i, player_job_dict[i])

        job_selected = int(input("> "))
        if job_selected > len(player_job_dict) or job_selected < 1:
            print("You have entered an invalid number, please try again")
            continue
        else:
            desc_job = player_job_dict[job_selected]

        print("You have selected", desc_job, "as your race.")
        job_finalization_input = input("You cannot change your job beyond this point, continue? (y/n) > ")
        if job_finalization_input == 'y':
            is_job_final = True

    character_creation_data = [1, desc_name, desc_race, desc_job]
    return character_creation_data


if __name__ == '__main__':
    dict_race = {"Human": ["Human", 125, 3, 8, 6, 5],
                 "Elf": ["Elf", 100, 4, 12, 5, 3],
                 "Orc": ["Orc", 200, 2, 6, 9, 7],
                 "Troll": ["Troll", 250, 1, 2, 15, 10],
                 "Dwarf": ["Dwarf", 150, 3, 7, 8, 8],
                 "Kobold": ["Kobold", 70, 3, 9, 4, 2]
                 }

    dict_job = {"Warrior": ["Warrior", 20, 14, 12, 8, 12],
                "Knight": ["Knight", 16, 7, 20, 10, 13],
                "Mage": ["Mage", 9, 12, 8, 26, 11],
                "Ranger": ["Ranger", 11, 18, 10, 12, 15],
                "Priest": ["Priest", 11, 13, 16, 14, 12]
                }

    main_menu()
    main_menu_input = int(input("> "))

    if main_menu_input == 1:
        opening_scene()

        character_data = character_creation()
        player = Player(character_data[0], character_data[1], *dict_race[character_data[2]],
                        *dict_job[character_data[3]])
        player.show_stats()
    elif main_menu_input == 2:
        pass
    else:
        pass
