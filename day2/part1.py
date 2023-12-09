from read_input import read_game_data
from typing import List

# Input
"""
Game 1: 7 green, 4 blue, 3 red; 4 blue, 10 red, 1 green; 1 blue, 9 red
Game 2: 2 red, 4 blue, 3 green; 5 green, 3 red, 1 blue; 3 green, 5 blue, 3 red
Game 3: 12 red, 1 blue; 6 red, 2 green, 3 blue; 2 blue, 5 red, 3 green
"""

# Output
"""
{
    [[(7, 'green'), (4, 'blue'), (3, 'red')], [(4, 'blue'), (10, 'red'), (1, 'green')], [(1, 'blue'), (9, 'red')]]
    [[(2, 'red'), (4, 'blue'), (3, 'green')], [(5, 'green'), (3, 'red'), (1, 'blue')], [(3, 'green'), (5, 'blue'), (3, 'red')]]
    [[(12, 'red'), (1, 'blue')], [(6, 'red'), (2, 'green'), (3, 'blue')], [(2, 'blue'), (5, 'red'), (3, 'green')]]
}
"""

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


