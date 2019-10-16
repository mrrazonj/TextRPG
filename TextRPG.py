import random
from datetime import datetime

import menus
import world_db
import classes


if __name__ == '__main__':
    random.seed(datetime.now())

    menus.main_menu()
    main_menu_input = menus.get_int_input()

    menus.clear()
    if main_menu_input == 1:
        menus.opening_scene()

        character_data = menus.character_creation()
        player = classes.Player(character_data[0], character_data[1], *world_db.dict_normal_race[character_data[2]],
                                *world_db.dict_normal_job[character_data[3]])
        player.show_stats()

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

        player_location = world_db.dict_place["Cainta"]
        while True:
            is_correct_world_input = False
            while not is_correct_world_input:
                menus.clear()
                print(f"You are now in the {player_location[1]} of {player_location[0]}")

                if player_location[1] == "town":
                    for world_key, world_value in enumerate(list_town_selection):
                        print(world_key + 1, world_value)
                    world_selection = menus.get_int_input()

                    if world_selection == 1:
                        is_correct_world_input = True
                        menus.character_menu(player)

                    elif world_selection == 2:
                        is_correct_world_input = True
                        # TODO shop menu

                    elif world_selection == 3:
                        player_location = world_db.dict_place[menus.travel_menu(player_location[0],
                                                                                player_location[2])]
                        is_correct_world_input = True

                else:
                    for world_key, world_value in enumerate(list_dungeon_selection):
                        print(world_key + 1, world_value)
                    world_selection = menus.get_int_input()

                    if world_selection == 1:
                        is_correct_world_input = True
                        enemy = classes.Enemy(*menus.spawn_boss(player_location[3]))
                        enemy.show_stats()
                        menus.battle_menu(player, enemy)

                    elif world_selection == 2:
                        is_correct_world_input = True
                        enemy = classes.Enemy(*menus.spawn_monster(player_location[3]))
                        enemy.show_stats()
                        menus.battle_menu(player, enemy)

                    elif world_selection == 3:
                        player_location = world_db.dict_place[menus.travel_menu(player_location[0],
                                                                                player_location[2])]
                        is_correct_world_input = True

    elif main_menu_input == 2:
        pass
    else:
        pass
