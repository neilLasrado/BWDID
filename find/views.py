from django.shortcuts import render
from find.services import *
import random

def index_page(request):
    return render(request, 'find/index.html')


def get_drunk(request, location):
    coordinates = location.split(',')
    latitude = coordinates[0]
    longitude = coordinates[1]
    establishment_type_list = [7,5,6,8]
    establishment_type = random.choice(establishment_type_list)
    bars_list = get_restaurants(latitude, longitude, establishment_type)
    return render(request, 'find/bars.html', {'bars_list': bars_list,
                                              'lat': latitude,
                                              'longi': longitude})


def get_cafes(request, location):
    coordinates = location.split(',')
    latitude = coordinates[0]
    longitude = coordinates[1]
    cafe_id = 1
    cafe_list = get_restaurants(latitude, longitude, cafe_id)
    return render(request, 'find/cafe.html', {'cafe_list': cafe_list,
                                              'lat': latitude,
                                              'longi': longitude})

# TODO Actually look for parties.
def get_parties(request, location):
    coordinates = location.split(',')
    latitude = coordinates[0]
    longitude = coordinates[1]
    establishment_type_list = [7,5,6,8]
    establishment_type = random.choice(establishment_type_list)
    parties_list = get_restaurants(latitude, longitude, establishment_type)
    return render(request, 'find/party.html', {'parties_list': parties_list,
                                               'lat': latitude,
                                               'longi': longitude})


def wrong_location(request):
    return render(request, 'find/wrongLocation.html')
