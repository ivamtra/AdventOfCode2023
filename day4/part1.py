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


print(card_dict[1])
scores = []

for (winning_numbers, your_numbers)in card_dict.values():
    numbers_won = list(filter(lambda x: x in winning_numbers, your_numbers))
    score = int(2**(len(numbers_won)-1))
    scores.append(score)

print(sum(scores))