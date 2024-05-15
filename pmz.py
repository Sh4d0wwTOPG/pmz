graph = {
    'A': [('B', 1, False)],
    'B': [('C', 3, False), ('D', 2, True), ('E', 4, True)],
    'C': [('B', 3, False)],
    'D': [('G', 2, True)],
    'E': [('F', 2, False)],
    'F': [('E', 2, False), ('I', 3, True)],
    'G': [('H', 3, True)],
    'H': [('G', 3, True), ('I', 2, False)],
    'I': [('H', 2, False)]
}
