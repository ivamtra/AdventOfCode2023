from typing import List

# Read input from file
with open('./day6/input.txt', 'r') as file:
    lines = file.readlines()

# Create lists for time and distance
time_list = [int(value) for value in lines[0].split()[1:]]
distance_list = [int(value) for value in lines[1].split()[1:]]

# Print the lists
print("Time:", time_list)
print("Distance:", distance_list)

ways_to_win_list: List[int] = []
for race_time, distance_to_beat in zip(time_list, distance_list):
    count = 0
    for time_pressed in range(1,race_time):
        time_left = race_time-time_pressed
        distance = time_pressed*time_left
        if distance > distance_to_beat:
            count += 1
    ways_to_win_list.append(count)

print(ways_to_win_list)

prod = 1
for x in ways_to_win_list:
    prod*=x

print(prod)