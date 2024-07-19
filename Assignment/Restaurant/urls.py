from django.urls import path
from .views import get_restaurants

urlpatterns = [
    path('api/restaurants/',get_restaurants)
]