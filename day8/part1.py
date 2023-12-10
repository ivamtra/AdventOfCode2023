# Read input from file
file_path = 'day8/input.txt'  # Replace with the actual file path
with open(file_path, 'r') as file:
    lines = file.readlines()

# Extracting the first line as a string
LR_instructions = lines[0].strip()

# Creating a dictionary with strings as keys and tuples as values
Graph = {}
for line in lines[2:]:  # Skip the empty line at index 1
    key, value_str = map(str.strip, line.split('='))
    # Assuming tuples are in the format (value1, value2)
    values = tuple(map(str.strip, value_str[1:-1].split(',')))
    Graph[key] = values

# Print the extracted data
print("Dictionary:")
for key, values in Graph.items():
    print(f"{key} = {values}")


G = {}

# BFS algo

current_node: str = "AAA"

steps = 0

# go one step
while True:
    if current_node == "ZZZ":
        break
    for char in LR_instructions:
        if char == 'L':
            current_node = Graph[current_node][0]
        else:
            current_node = Graph[current_node][1]
        steps += 1


print(current_node)
print(steps)