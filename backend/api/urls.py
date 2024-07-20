from django.urls import path
from .views import get_name, get_degree


urlpatterns = [
    path('name/', get_name),
    path('degree/', get_degree),
]
