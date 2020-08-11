from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='allanportfolio')
def get_coordinates(address):
    location = geolocator.geocode(address)
    try:
        return location.latitude, location.longitude
    except:
        return None
