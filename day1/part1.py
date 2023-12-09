
values = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
]

# find first digit

def find_number(s: str) -> int:
    first_number = -1
    second_number = -1

    for c in s:
        try:
            first_number = int(c)
            break
        except:
            pass
    for c in reversed(s):
        try:
            second_number = int(c)
            break
        except:
            pass
    return first_number*10 + second_number

# read file

# Specify the path to your file
file_path = "input.txt"

# Read the content of the file
with open(file_path, 'r') as file:
    file_content = file.read()

# Split the content into a list of strings based on newline character
values = file_content.strip().split('\n')

print(sum(map(find_number, values)))