from collections import defaultdict

dict_item_id = defaultdict(lambda: [0, 0, 0, 0, 0, 0, "none", 0, 0])
dict_item_id.update({
    # TODO Finish up to 40 item dict
    # HP, AP, Spd, Atk, Def, ID, Name, Type, Rarity
    0: [0, 0, 0, 0, 0, 0, "none", 0, 0],
    1: [0, 1, 4, 25, 0, 1, "Rusty Axe", 0, 0],
    2: [0, 0, 2, 40, 15, 2, "Chipped Sword", 0, 0],
    3: [0, 2, 6, 15, 10, 3, "Crude Bow", 0, 0],
    4: [0, 0, 2, 75, 0, 4, "Mundane Staff", 0, 0],
    5: [0, 1, 3, 35, 5, 5, "Broken Rod", 0, 0],
    6: [150, 0, 2, 0, 20, 6, "Torn Fur Armor", 1, 0],
    7: [250, 0, 0, 0, 35, 7, "Tarnished Copper Armor", 1, 0],
    8: [100, 1, 4, 0, 15, 8, "Old Leather Armor", 1, 0],
    9: [50, 0, 3, 0, 12, 9, "Unremarkable Robe", 1, 0],
    10: [100, 0, 3, 0, 18, 10, "Unblessed Vestments", 1, 0]
})

dict_rare_item_id = defaultdict(lambda: [0, 0, 0, 0, 0, 0, "none", 0, 0])
dict_rare_item_id.update({
    # TODO Finish up to 40 rare item dict
    # HP, AP, Spd, Atk, Def, ID, Name, Type, Rarity
    0: [0, 0, 0, 0, 0, 0, "none", 0, 0],
    1: [0, 1, 6, 40, 10, 11, "Executioner's Axe", 0, 1],
    2: [100, 1, 3, 50, 20, 12, "Knight's Broadsword", 0, 1],
    3: [0, 3, 12, 20, 12, 13, "Elven Bow", 0, 1],
    4: [0, 1, 6, 125, 9, 14, "Purification Staff", 0, 1],
    5: [120, 1, 5, 60, 15, 15, "Exorcism Rod", 0, 1],
    6: [250, 1, 4, 30, 35, 16, "Chieftain's Fur Armor", 1, 1],
    7: [600, 0, 0, 20, 60, 17, "Crusader's Copper Armor", 1, 1],
    8: [180, 2, 6, 10, 25, 18, "Elven Leather Armor", 1, 1],
    9: [80, 1, 5, 40, 15, 19, "Mystical Robe", 1, 1],
    10: [150, 1, 6, 20, 30, 20, "Priest's Vestments", 1, 1]
})

dict_boss_item_id = defaultdict(lambda: [0, 0, 0, 0, 0, 0, "none", 0, 0])
dict_boss_item_id.update({
    # HP, AP, Spd, Atk, Def, ID, Name, Type, Rarity
    0: [200, 2, 5, 55, 15, 21, "Excalipoor", 0, 1],
    1: [400, 1, 4, 15, 45, 22, "Avalawn", 1, 1]
})

dict_normal_race = {
    # Name, Str, Dex, Con, Int, Luk
    "Human": ["Human", 125, 3, 8, 6, 5],
    "Elf": ["Elf", 100, 4, 12, 5, 3],
    "Orc": ["Orc", 200, 2, 6, 9, 7],
    "Troll": ["Troll", 250, 1, 2, 15, 10],
    "Dwarf": ["Dwarf", 150, 3, 7, 8, 8],
    "Kobold": ["Kobold", 70, 3, 9, 4, 2]
}

dict_normal_job = {
    # Name, Str, Dex, Con, Int, Luk
    "Warrior": ["Warrior", 20, 14, 12, 8, 12],
    "Knight": ["Knight", 16, 7, 20, 10, 13],
    "Mage": ["Mage", 9, 12, 8, 26, 11],
    "Ranger": ["Ranger", 11, 18, 10, 12, 15],
    "Priest": ["Priest", 11, 13, 16, 14, 12]
}

dict_boss_race = {
    "Human": ["Human", 250, 5, 16, 12, 10],
    "Elf": ["Elf", 200, 6, 21, 10, 8],
    "Orc": ["Orc", 500, 3, 14, 24, 15],
    "Troll": ["Troll", 700, 2, 7, 30, 20],
    "Dwarf": ["Dwarf", 300, 4, 15, 15, 15],
    "Kobold": ["Kobold", 150, 4, 14, 9, 6],
    "Centaur": ["Centaur", 550, 4, 18, 22, 15],
    "Undead": ["Undead", 250, 4, 13, 15, 15],
    "Lamia": ["Lamia", 350, 5, 20, 10, 10],
    "Sahuagin": ["Sahuagin", 400, 3, 15, 16, 12],
    "Minotaur": ["Minotaur", 550, 3, 12, 25, 18],
    "Giant": ["Giant", 1200, 1, 5, 80, 40]
}

list_race_choices = []
for key in dict_boss_race:
    list_race_choices.append(key)

dict_boss_job = {
    "Warrior": ["Warrior", 35, 22, 20, 15, 12],
    "Knight": ["Knight", 30, 14, 40, 18, 13],
    "Mage": ["Mage", 12, 20, 12, 64, 11],
    "Ranger": ["Ranger", 26, 31, 15, 20, 15],
    "Priest": ["Priest", 24, 25, 28, 32, 12],
    "Berserker": ["Berserker", 42, 24, 10, 10, 8],
    "Warlock": ["Warlock", 15, 15, 16, 57, 15]
}

list_job_choices = []
for key in dict_boss_job:
    list_job_choices.append(key)

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
