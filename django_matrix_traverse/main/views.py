import httpx
from django.http import HttpResponse
from ninja import Router
from asgiref.sync import sync_to_async
from .models import Matrix
from .matrix_convertation import get_values



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
                list_of_values = get_values(response.text)
                return HttpResponse(list_of_values)
            # Handling server errors
            else:
                return HttpResponse(f'Server error: {response.status_code}', status=response.status_code)
    # Handling of HTTP errors of status 4xx and 5xx
    except httpx.HTTPStatusError as e:
        return HttpResponse(f'HTTP status error: {e}')
    # Handling network errors (Connection Timeout, Connection Refused, etc.)
    except httpx.NetworkError as e:
        return HttpResponse(f'Network error: {e}')