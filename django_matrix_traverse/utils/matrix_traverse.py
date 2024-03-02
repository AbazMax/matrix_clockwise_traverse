import httpx
import asyncio

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
    

async def get_matrix(url: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            if response.status_code == 200:
                reformat_matrix = parse_matrix(response.text)
                traverse_result = clockwise_matrix_traverse(reformat_matrix)
                return traverse_result
            else:
                # Handling server errors
                print(f"Server error: {response.status_code}")
                return None
    except httpx.HTTPStatusError as e:
        # Handling of HTTP errors of status 4xx and 5xx
        print(f"HTTP status error: {e}")
        return None
    except httpx.NetworkError as e:
        # Handling network errors (Connection Timeout, Connection Refused, etc.)
        print(f"Network error: {e}")
        return None

# SOURCE_URL = 'https://raw.githubusercontent.com/Real-Estate-THE-Capital/python-assignment/main/matrix.txt'
# TRAVERSAL = [
#     10, 50, 90, 130,
#     140, 150, 160, 120,
#     80, 40, 30, 20,
#     60, 100, 110, 70,
# ]

# print(asyncio.run(get_matrix(SOURCE_URL)))

