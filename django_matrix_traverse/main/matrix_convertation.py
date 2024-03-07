def parse_matrix(inpput_matrix):
    """Parse the matrix and reformat it to a standard view"""
    matrix = []
    for row in inpput_matrix.split('\n'):
        # Delete all formating symbols and add values to a new formated matrix
        if row.startswith('|'):
            row = row.replace('|', '').replace('-', '')
            row = [int(num) for num in row.split()]
            matrix.append(row)
    return matrix

def clockwise_matrix_traverse(matrix):
    """Traverse matrix clockwise"""
    if not matrix:
        return []

    result = []
    rows, cols = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, rows - 1, 0, cols - 1

    while top <= bottom and left <= right:
        # Traverse from top to bottom
        for row in range(top, bottom + 1):
            result.append(matrix[row][left])
        left += 1

        # Traverse from left to right
        for col in range(left, right + 1):
            result.append(matrix[bottom][col])
        bottom -= 1

        # Check if left has not crossed the right
        if left <= right:
            # Traverse from bottom to top
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][right])
            right -= 1

        # Check if top has not crossed the bottom
        if top <= bottom:
            # Traverse from right to left
            for col in range(right, left - 1, -1):
                result.append(matrix[top][col])
            top += 1

    return result

def get_values(matrix):
    reformat_matrix = parse_matrix(matrix)
    list_of_values = clockwise_matrix_traverse(reformat_matrix)
    return list_of_values