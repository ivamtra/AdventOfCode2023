class NumberNode:
    def __init__(self, start_index, end_index, row, number):
        self.start_index = start_index
        self.end_index = end_index
        self.row = row
        self.number = number

    def __str__(self):
        return f"NumberNode({self.number}) - Row: {self.row}, Start Index: {self.start_index}, End Index: {self.end_index}"

    def __hash__(self):
        return hash((self.start_index, self.end_index, self.row, self.number))


class SymbolNode:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col

    def __str__(self):
        return f"SymbolNode - Row: {self.row}, Column: {self.col}"

    def __hash__(self):
        return hash((self.row, self.col))


class Edge:
    def __init__(self, symbolNode, numberNode) -> None:
        self.symbolNode = symbolNode
        self.numberNode = numberNode

    def __str__(self):
        return f"Edge - SymbolNode: {self.symbolNode}, NumberNode: {self.numberNode}"

    def __hash__(self):
        return hash((self.symbolNode, self.numberNode))
