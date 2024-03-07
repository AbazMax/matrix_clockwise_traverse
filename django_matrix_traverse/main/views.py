import httpx
from django.http import HttpResponse
from ninja import Router
from asgiref.sync import sync_to_async
from .models import Matrix

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

def save_input_matrix(input_matrix):
    """Save input matrix"""
    new_matrix = Matrix(input_matrix=input_matrix)
    new_matrix.save()


router = Router()

# Declare a route handler for GET requests
@router.get('/get_matrix')
async def get_matrix(request, url: str = None):
    """Get matrix from the URL and format it to list of values"""
    if not url:
        return HttpResponse('URL parameter is missing', status=400)
    try:
        # Execute a GET request for the given URL and check the status of the response code.
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            # process the obtained matrix
            if response.status_code == 200:
                await sync_to_async(save_input_matrix)(response.text)
                reformat_matrix = parse_matrix(response.text)
                traverse_result = clockwise_matrix_traverse(reformat_matrix)
                return HttpResponse(traverse_result)
            # Handling server errors
            else:
                return HttpResponse(f'Server error: {response.status_code}', status=response.status_code)
    # Handling of HTTP errors of status 4xx and 5xx
    except httpx.HTTPStatusError as e:
        return HttpResponse(f'HTTP status error: {e}')
    # Handling network errors (Connection Timeout, Connection Refused, etc.)
    except httpx.NetworkError as e:
        return HttpResponse(f'Network error: {e}')