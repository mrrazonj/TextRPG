import menus
import world_db


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
        menus.clear()
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
        menus.pause()

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
            self.loot_dropped = world_db.dict_rare_item_id[loot]
        else:
            self.loot_dropped = world_db.dict_item_id[loot]

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
        menus.clear()
        print(f"Monster is carrying {self.loot_dropped[-1]}!")
        menus.pause()


class Player(Entity):
    def __init__(self, level, desc_name, desc_race, base_hp, base_ap, base_spd, base_atk, base_def,
                 desc_job, stat_str, stat_dex, stat_con, stat_int, stat_luk):
        super().__init__(level, desc_name, desc_race, base_hp, base_ap, base_spd, base_atk, base_def,
                         desc_job, stat_str, stat_dex, stat_con, stat_int, stat_luk)

        self.experience = 0
        self.inventory = []
        self.equipped_skills = []
        self.learned_skills = []

        self.unallocated_stat = 0
        self.unallocated_skill = 2

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
