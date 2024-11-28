from django.http import JsonResponse
from django.apps import apps
from django.shortcuts import render
from geopy.distance import geodesic
import requests 

def index(request):
    Park = apps.get_model('Twendesafari', 'Park')  # Get the Park model
    parks = list(Park.objects.values('latitude', 'longitude')[:65])
    context = {'parks': parks}
    return render(request, 'index.html', context)


def nearest_park(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    user_location = latitude, longitude
    park_distances={}
    for park in park.objects.all()[:65]:
        park_location = park.latitude,park.longitude
        
        distance = geodesic(user_location,park_location).km
        park_distances[distance] = park_location
        
    min_distance = min(park_distances)
    park_coords = park_distances[min_distance]
    
    
    return JsonResponse({
        'coordinates': park_coords,
        'distance': min_distance
    })
def weather(request):
    # Get user's location (replace with your geolocation logic)
    user_lat = 0.023
    user_longitude = 37.90

    # Fetch weather data
    api_key = 'c4f8ed272caa68e2d07059803591e452'  # Replace with your actual OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={user_lat}&lon={user_longitude}&appid={api_key}&units=metric"
    response = requests.get(url)

    # Check for successful response
    if response.status_code == 200:
        data = response.json()

        # Extract weather information
        temperature = data['main']['temp']
        description = data['weather'][0]['description']

        # Pass weather data to the template
        context = {
            'temperature': temperature,
            'description': description
        }
        return render(request, 'weather.html', context)
    else:
        # Handle error (optional)
        print(f"Error fetching weather data: {response.status_code}")
        context = {'error_message': "Couldn't retrieve weather data."}
        return render(request, 'weather.html', context)
