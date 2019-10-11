from collections import defaultdict

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

dict_skills = {
    "Warrior": ["Bash", "Rush", "Execute", "Reckless Onslaught", "Chaotic Drive"]
}

list_common_skills = [
    "Normal Attack",
    "Bide",
]

list_warrior_skills = [
    "Bash",
    "Rush",
    "Execute",
    "Reckless Onslaught",
    "Chaotic Drive"
]