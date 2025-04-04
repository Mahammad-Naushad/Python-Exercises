"""
Given a 2D matrix, transpose it

while transposing,
if the number is even, double it
if the number is odd, halve it
"""


def matrix_transpose(my_matrix):
    transpose_matrix = [[0 for _ in range(len(my_matrix))] for _ in range(len(my_matrix[0]))]

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            transpose_matrix[column][row] = matrix[row][column]

    return transpose_matrix


# Taking hardcoded values as input
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix_transpose(matrix))