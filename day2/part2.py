from read_input import read_game_data
from typing import List

game_data = read_game_data(file_path="./day2/input.txt")


def check_if_valid(game : List[List[tuple]]) -> dict:
    # Max values of each color
    max_values = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for round in game:
        for tup in round:
            (count, color) = tup
            max_values[color] = count if count > max_values[color] else max_values[color]
    return max_values

# Calculate sum
sum = 0
for key, value in game_data.items():
    power = 1
    result = check_if_valid(value)
    for item in result.values():
        power*= item
    sum += power

print(sum)