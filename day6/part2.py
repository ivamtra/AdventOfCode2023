# Read input from file
with open('./day6/input.txt', 'r') as file:
    lines = file.readlines()

# Extract and concatenate time and distance as single numbers
time_str = ''.join(lines[0].split()[1:])
distance_str = ''.join(lines[1].split()[1:])

# Convert the concatenated strings to integers
race_time = int(time_str)
distance_to_beat = int(distance_str)

count = 0
for time_pressed in range(1,race_time):
    time_left = race_time-time_pressed
    distance = time_pressed*time_left
    if distance > distance_to_beat:
        count += 1

print(count)