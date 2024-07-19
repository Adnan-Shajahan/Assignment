from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Restaurant

# Create your views here.

@api_view(['GET'])

def get_restaurants(request):
    address = request.GET.get('address')
    has_table_booking = request.GET.get('table_booking')
    has_online_delivery = request.GET.get('online_delivery')
    cuisines = request.GET.get('cuisines')

    restaurants = Restaurant.objects.all()

    if has_table_booking is not None:
        restaurants = restaurants.filter(has_table_booking=has_table_booking.lower() in ['true', '1'])
    if has_online_delivery is not None:
        restaurants = restaurants.filter(has_online_delivery=has_online_delivery.lower() in ['true', '1'])
    if cuisines:
        restaurants = restaurants.filter(cuisines__icontains=cuisines)

    restaurants = restaurants.order_by('-aggregate_rating')