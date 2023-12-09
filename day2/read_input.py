# Input
"""
Game 1: 7 green, 4 blue, 3 red; 4 blue, 10 red, 1 green; 1 blue, 9 red
Game 2: 2 red, 4 blue, 3 green; 5 green, 3 red, 1 blue; 3 green, 5 blue, 3 red
Game 3: 12 red, 1 blue; 6 red, 2 green, 3 blue; 2 blue, 5 red, 3 green
"""

# Output
{
    1: [[(7, 'green'), (4, 'blue'), (3, 'red')], [(4, 'blue'), (10, 'red'), (1, 'green')], [(1, 'blue'), (9, 'red')]],
    2: [[(2, 'red'), (4, 'blue'), (3, 'green')], [(5, 'green'), (3, 'red'), (1, 'blue')], [(3, 'green'), (5, 'blue'), (3, 'red')]],
    3: [[(12, 'red'), (1, 'blue')], [(6, 'red'), (2, 'green'), (3, 'blue')], [(2, 'blue'), (5, 'red'), (3, 'green')]],
}


def read_game_data(file_path):
    games_data = {}

    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into game number and rounds data
            game_info, rounds_info = line.strip().split(": ")
            
            # Extract game number
            game_number = int(game_info.split()[1])

            # Split rounds using ';' as a separator
            rounds_data = rounds_info.split('; ')

            # Process each round to create the desired format
            game_data = []
            for round_info in rounds_data:
                round_data = []
                items = round_info.split(', ')
                for item in items:
                    quantity, color = item.split()
                    round_data.append((int(quantity), color.lower()))
                game_data.append(round_data)

            # Store the data in the dictionary
            games_data[game_number] = game_data

    return games_data

