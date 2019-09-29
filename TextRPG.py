class Entity:
    def __init__(self, base_hp, base_ap, base_spd, base_atk, base_def,
                 stat_str, stat_dex, stat_con, stat_int, stat_luk,
                 desc_name, desc_race, desc_job, level):
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
        self.combat_ap = base_ap + (stat_dex * 0.03)
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
        print(self.combat_atk, end='')
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

    def get_hp(self):
        return self.combat_hp

    def get_ap(self):
        return self.combat_ap

    def get_spd(self):
        return self.combat_spd

    def get_atk(self):
        return self.combat_atk

    def get_def(self):
        return self.combat_def

    def set_hp(self, value):
        self.combat_hp += value

    def set_ap(self, value):
        self.combat_ap += value

    def set_spd(self, value):
        self.combat_spd += value

    def set_atk(self, value):
        self.combat_atk += value

    def set_def(self, value):
        self.combat_def += value


class Enemy(Entity):
    def __init__(self, base_hp, base_ap, base_spd, base_atk, base_def,
                 stat_str, stat_dex, stat_con, stat_int, stat_luk,
                 desc_name, desc_race, desc_job, level, item_id1, item_id2, item_id3, item_id4, item_id5):
        super().__init__(base_hp, base_ap, base_spd, base_atk, base_def,
                         stat_str, stat_dex, stat_con, stat_int, stat_luk,
                         desc_name, desc_race, desc_job, level)

        self.loot_id = [item_id1, item_id2, item_id3, item_id4, item_id5]

    def get_loot(self, select_item):
        return self.loot_id[select_item]


class Player(Entity):
    def __init__(self, base_hp, base_ap, base_spd, base_atk, base_def,
                 stat_str, stat_dex, stat_con, stat_int, stat_luk,
                 desc_name, desc_race, desc_job, level):
        super().__init__(base_hp, base_ap, base_spd, base_atk, base_def,
                         stat_str, stat_dex, stat_con, stat_int, stat_luk,
                         desc_name, desc_race, desc_job, level)

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


if __name__ == '__main__':
    pass
