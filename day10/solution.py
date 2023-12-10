from typing import List, Tuple
from math import ceil
import sys 

sys.setrecursionlimit(10**6) 

filename = "./day10/input.txt"  # Replace with the actual filename

# Read the file and create a list of lists (2D matrix)
with open(filename, 'r') as file:
    matrix = [list(line.strip()) for line in file]


def find_S(matrix : List[List[chr]]) -> Tuple[int, int]:
    for i, row in enumerate(matrix):
        for j, x in enumerate(row):
            if x == 'S':
                return (i,j)
    return (-1,-1)


pipes = {'|', '-', 'F', ' L', 'J', '7'}

# Up, down, left, right
directions = {'U', 'D', 'L', 'R'}

(start_i, start_j) = find_S(matrix)

M = {}

def traverse(i, j, previous_direction, depth=0):
    char = matrix[i][j]
    if char == '.':
        return
    
    if char == 'S' and (i,j) in M:
        print('S found again!')
        print(f'Depth = {depth}')
        print(f'Midpoint = {ceil(depth/2)}')
        return
    
    # Starting at S
    if char == 'S' and (i,j) not in M:
        M[(i,j)] = char
        # check up
        next_char = matrix[i-1][j]
        if i != 0 and  (next_char == '|' or next_char == 'F' or next_char == '7'):
            traverse(i-1, j, 'U', depth+1)
        # check down
        next_char = matrix[i+1][j]
        if i != len(matrix)-1 and (next_char == '|' or next_char == 'J' or next_char == 'L'):
            traverse(i+1, j, 'D', depth+1)
        # check right
        next_char = matrix[i][j+1]
        if j != len(matrix[i])-1 and (next_char == '-' or next_char == 'J' or next_char == '7'):
            traverse(i, j+1, 'R', depth+1)
        # check left
        next_char = matrix[i][j-1]
        if j != 0 and (next_char == '-' or next_char == 'L' or next_char == 'F'):
            traverse(i, j-1, 'L', depth+1)

    # Pipe

    M[(i,j)] = char
    match previous_direction:
        case 'U':
            if char == '|':
                traverse(i-1, j, 'U', depth+1)
            elif char == 'F':
                traverse(i, j+1, 'R', depth+1)
            elif char == '7':
                traverse(i, j-1, 'L', depth+1)
        case 'D':
            if char == '|':
                traverse(i+1, j, 'D', depth+1)
            elif char == 'L':
                traverse(i, j+1, 'R', depth+1)
            elif char == 'J':
                traverse(i, j-1, 'L', depth+1)
        case 'L':
            if char == '-':
                traverse(i, j-1, 'L', depth+1)
            elif char == 'F':
                traverse(i+1, j, 'D', depth+1)
            elif char == 'L':
                traverse(i-1, j, 'U', depth+1)
        case 'R':
            if char == '-':
                traverse(i, j+1, 'R', depth+1)
            elif char == '7':
                traverse(i+1, j, 'D', depth+1)
            elif char == 'J':
                traverse(i-1, j, 'U', depth+1)


    # Finding s again

traverse(start_i, start_j, '0')


# Part 2

enclosed = []
def count_enclosed(matrix) -> int:
    count = 0
    for i, row in enumerate(matrix):
        for j, tile in enumerate(row):
            # Ray casting algorithm

            # If (i,j) not in main loop
            if (i,j) not in M and j != 0:
                intersections_count = 0
                # check number of intersections with main loop by
                # checking upwards
                for x in range(j):
                    if (i,x) in M and (M[(i,x)] == '|' or M[(i,x)] == 'J' or M[(i,x)] == 'L'):
                        intersections_count += 1
                
                if intersections_count % 2 == 1:
                    print(i,j)
                    print(tile)
                    print()
                    count +=1 
    return count

count = count_enclosed(matrix)
print(f"count,", count)

# 18 punktar
"""
...........
.F--S---7..
.|......|..
.|......|..
.|......|..
.L------J..
...........
"""