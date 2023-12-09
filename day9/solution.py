# check if list only has 0 values, returns true if that is case
def null_check(history: list[int]):
    for item in history:
        if item != 0:
            return False
    return True


def extrapolate_next(history : list[int]):

    history_matrix = [history]

    row_index = 0

    ## Create history triangle to extrapolate

    # while row has non null values
    while True:
        # check current row
        if null_check(history_matrix[row_index]):
            break

        # create new row

        new_row = []
        
        for i in range(len(history_matrix[row_index]) - 1):
            difference = history_matrix[row_index][i+1] \
                        - history_matrix[row_index][i]
            new_row.append(difference)
        
        # add to history matrix
        history_matrix.append(new_row)
        # update row index
        row_index += 1
        


    ## Extrapolate new value

    # add 0 to last row
    history_matrix[len(history_matrix)-1].append(0)

    # loop in reverse order to exrapolate values
    for i in range(len(history_matrix) - 2, -1, -1):
        current_row = history_matrix[i]
        last_row = history_matrix[i+1]
        # extrapolate
        current_row.append(current_row[-1] + last_row[-1])

    extrapolated_value = history_matrix[0][-1]
    return extrapolated_value


# Read in input

file_path = 'input.txt'

# Read the file and convert to 2D array
with open(file_path, 'r') as file:
    lines = file.read().splitlines()

histories = [list(map(int, line.split())) for line in lines]


# Answer part 1
print(sum(map(extrapolate_next, histories)))


# Answer part 2
print(sum(map(extrapolate_next, map(lambda x: list(reversed(x)),histories))))
