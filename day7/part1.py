class Hand:
    def __init__(self, hand: str, bet: int) -> None:
        self.hand = hand
        self.bet = bet
    def __str__(self) -> str:
        return f"Hand: {self.hand}, Bet: {self.bet}"

# Read input from file
with open('./day7/test.txt', 'r') as file:
    lines = file.readlines()

# Create a list of Hand objects
hands_list = [Hand(line.split()[0], int(line.split()[1])) for line in lines]

# Print the hands list
for hand in hands_list:
    print(f"Hand: {hand.hand}, Bet: {hand.bet}")
