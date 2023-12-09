from typing import List

number_digits = [1,2,3,4,5,6,7,8,9]

string_digits = {
     "one": 1,
     "two": 2,
     "three": 3,
     "four": 4,
     "five": 5,
     "six": 6,
     "seven": 7,
     "eight": 8,
     "nine": 9,
}


def find_digits(string: str) -> List[int]:
    # digit: [first_index_found, last_index_found]
    candidate_first_digits = {}
    # Find all possible digits and indices by first position found
    for string_digit in string_digits.keys():
        candidate_first_digits[string_digit] = string.find(string_digit)
    for number_digit in number_digits:
        candidate_first_digits[number_digit] = string.find(str(number_digit))
    
    # Find all possible digits and indices by last position found
    candidate_second_digits = {}
    for string_digit in string_digits.keys():
        candidate_second_digits[string_digit] = string.rfind(string_digit)
    for number_digit in number_digits:
        candidate_second_digits[number_digit] = string.rfind(str(number_digit))

    # Filter non found digits
    candidate_first_digits = {key: value for key, value in candidate_first_digits.items() if value != -1}
    candidate_second_digits = {key: value for key, value in candidate_second_digits.items() if value != -1}


    # Here digits are either a number or a string

    # Find the first digit
    first_digit = min(candidate_first_digits, key=lambda k: candidate_first_digits[k])

    # Find the second digit
    second_digit = max(candidate_second_digits, key=lambda k: candidate_second_digits[k])

    # print(first_digit, second_digit)
    # convert to numbers if applicable
    first_digit = string_digits[first_digit] if first_digit in string_digits else first_digit
    second_digit = string_digits[second_digit] if second_digit in string_digits else second_digit
    # return the number
    return first_digit*10 + second_digit

# Specify the path to your file
file_path = "input.txt"

# Read the content of the file
with open(file_path, 'r') as file:
    file_content = file.read()

# Split the content into a list of strings based on newline character
values = file_content.strip().split('\n')

# Answer
digits = [find_digits(value) for value in values]
print(sum(digits))