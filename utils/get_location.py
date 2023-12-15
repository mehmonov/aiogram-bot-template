from geopy.geocoders import Nominatim

def get_location_details(latitude, longitude):
    geolocator = Nominatim(user_agent="http")
    location = geolocator.reverse(f"{latitude}, {longitude}")

   
    return {
        'full_address': location.address,
    }
