from typing import List
import math
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

current_nodes: List[str] = []


# find starting nodes
for point in Graph.keys():
    if point[-1] == "A":
        current_nodes.append(point)

max_steps = 0

def stepsToFinish(node: str):
    steps = 0
    while True:
        if node[-1] == 'Z':
            break
        for char in LR_instructions:
            if char == 'L':
                node = Graph[node][0]
            else:
                node = Graph[node][1]
            steps += 1
    return steps

steps_per_node = list(map(stepsToFinish, current_nodes))
print(steps_per_node)
print(current_nodes)
print(max_steps)
print(math.lcm(*steps_per_node))