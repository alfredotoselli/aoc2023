with open("inputs/2.txt") as file:
    games_list = file.readlines()

game_map = {}
for game in games_list:
    parts = game.strip().split(": ")
    game_map[int(parts[0].replace("Game ", ""))] = parts[1]

sum_game = 0
min_power_game = 0
for game_id in game_map.keys():
    game_sets = game_map[game_id].split("; ")
    minimum_red = 0
    minimum_green = 0
    minimum_blue = 0
    invalid_set = False
    for game_set in game_sets:
        cubes = game_set.split(", ")
        for cube in cubes:
            if "red" in cube:
                val = int(cube.replace(" red", ""))
                if val > minimum_red:
                    minimum_red = val
                if val > 12:
                    invalid_set = True
            if "green" in cube:
                val = int(cube.replace(" green", ""))
                if val > minimum_green:
                    minimum_green = val
                if val > 13:
                    invalid_set = True
            if "blue" in cube:
                val = int(cube.replace(" blue", ""))
                if val > minimum_blue:
                    minimum_blue = val
                if val > 14:
                    invalid_set = True

    min_power_game += minimum_red * minimum_green * minimum_blue
    if invalid_set:
        continue
    else:
        sum_game += game_id


print(sum_game)
print(min_power_game)
