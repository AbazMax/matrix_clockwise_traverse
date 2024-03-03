from django.urls import path
from ninja import NinjaAPI
from . import views

from django.urls import path

api = NinjaAPI()

@api.get('/get_matrix/')
async def get_matrix(request, url: str):
    result = await views.get_matrix(request, url)
    return result

urlpatterns = [
    path('api/', api.urls),
]
