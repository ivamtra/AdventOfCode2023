from read_input import read_game_data
from typing import List



capacities = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

game_data = read_game_data(file_path="./day2/input.txt")

def check_if_valid(game : List[List[tuple]]) -> bool:
    for round in game:
        for tup in round:
            (count, color) = tup
            if count > capacities[color]:
                return False
    return True



result_set = list(map(check_if_valid, game_data.values()))


# calculate result
sum = 0

for i, b in enumerate(result_set):
    if b:
        sum += i+1
print(sum)


