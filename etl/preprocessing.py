from geopy.geocoders import Nominatim 

def get_address(latitude,longitude):
    """Get neighbourhood of geographic point
    Args:
        latitude (float): vehicle's latitude
        longitude (float): vehicle's longitude
    Returns:
        The neighborhood where the vehicle is located
    """
        
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(str(latitude)+","+str(longitude))
    if location is None:
        return None
    else:
        address = location.raw['address']
        neighbourhood = address.get('neighbourhood', '')
        return neighbourhood
