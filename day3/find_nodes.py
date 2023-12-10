from typing import List
from  classes import NumberNode, SymbolNode, Edge

empty_set = {'.'}

digits = {'1','2','3','4','5','6','7','8','9','0'}



# Read the text from the file
with open('./day3/input.txt', 'r') as file:
    content = file.read()

# Split the content into lines
lines = content.split('\n')

# Format it into a list
input_matrix = [line.strip() for line in lines if line.strip()]

# input_matrix = [
#     "467..114..",
#     "...*......",
#     "..35..633.",
#     "......#...",
#     "617*......",
#     ".....+.58.",
#     "..592.....",
#     "......755.",
#     "...$.*....",
#     ".664.598..",
# ]

def find_nodes(input_matrix: List[str]) -> (List[NumberNode], List[SymbolNode]):

    symbol_nodes = []
    number_nodes = []
    for row, string in enumerate(input_matrix):
        print(string)
        start_index = -1
        end_index = -1
        for col, char in enumerate(string):
            # symbol found
            if char != '.' and char not in digits:
                symbol_nodes.append(SymbolNode(row, col))

            if col == 0 and row == 4:
                print("Debug")
            
            # Find start and end of number
            if ( char in digits and col == 0) or( string[col-1]  not in digits and char in digits):
                # start of number found
                start_index = col
                pass

            # check if at last index
            if ( col + 1 < len(string) and string[col+1] not in digits or char == string[-1]) and char in digits :
                # end of number found
                end_index = col
                number = int(string[start_index:end_index+1])
                if number == 6:
                    print("Debug")
                number_nodes.append(NumberNode(start_index, end_index, row, number))
                pass

    return (number_nodes, symbol_nodes)



def create_edges(number_nodes: List[NumberNode], symbol_nodes: List[SymbolNode]) -> List[Edge]:
    edges = []
    for number_node in number_nodes:
        for symbol_node in symbol_nodes:
            # Check if adjacent
            if (
                abs(symbol_node.row - number_node.row) <= 1
                and symbol_node.col >= number_node.start_index - 1
                and symbol_node.col <= number_node.end_index + 1
            ):
                edges.append(Edge(symbol_node, number_node))
    return edges


(number_nodes, symbol_nodes) = find_nodes(input_matrix)

for number_node in number_nodes:
    # print(number_node)
    pass

for symbol_node in symbol_nodes:
    pass
    # print(symbol_node)

edges = create_edges(number_nodes, symbol_nodes)
sum = 0

# Tvítelja ekki tölur
M = {}
for edge in edges:

    # print(f"{edge.numberNode} adjacent to {edge.symbolNode}")

    key = (edge.numberNode.start_index, edge.numberNode.row)
    if key not in M:
        sum += edge.numberNode.number
    M[key] = True
print(sum)
