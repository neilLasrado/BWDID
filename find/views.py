from django.shortcuts import render
from find.services import *


def index_page(request):
    return render(request, 'find/index.html')


def get_food(request, location):
    coordinates = location.split(',')
    latitude = coordinates[0]
    longitude = coordinates[1]
    bars_list = get_bars(latitude, longitude, '')
    return render(request, 'find/bars.html', {'bars_list': bars_list,
                                                     'lat': latitude,
                                                     'longi': longitude})


def get_cafes(request, location):
    coordinates = location.split(',')
    latitude = coordinates[0]
    longitude = coordinates[1]
    cafe_id = 1
    cafe_list = get_bars(latitude, longitude, cafe_id)
    return render(request, 'find/cafe.html', {'cafe_list': cafe_list,
                                              'lat': latitude,
                                              'longi': longitude})



def wrong_location(request):
    return render(request, 'find/wrongLocation.html')
