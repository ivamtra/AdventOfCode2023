from typing import List, Tuple

# Initialize an empty dictionary to store the results
card_dict = {}

# Open the file in read mode
with open('./day4/input.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Split the line into two parts using '|'
        parts = line.strip().split('|')

        # Extract values from the two parts and create lists
        card_index = int(parts[0].split(':')[0].split()[-1])
        winning_numbers = list(map(int, parts[0].split(':')[1].split()))
        your_numbers = list(map(int, parts[1].split()))

        # Store the lists in the dictionary with the card index as the key
        card_dict[card_index] = (winning_numbers, your_numbers)

# print(card_dict)

count = [0]
def count_cards(key: int):

    if key not in card_dict:
        return
    
    count[0] += 1
    
    card = card_dict[key]
    print(key)
    (winning_numbers, your_numbers) = card
    cards_won = len(list(filter(lambda x: x in winning_numbers, your_numbers)))
    for i in range(cards_won):
        count_cards(key + (i+1))
    pass


for index in card_dict.keys():
    count_cards(index)

print(count)