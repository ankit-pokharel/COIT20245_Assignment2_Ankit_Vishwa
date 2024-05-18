# nominatim.py
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

CAIRNS_COORDINATES = {"latitude": -16.9186, "longitude": 145.7781}

def gps_coordinate(city):
    """
    Returns the GPS coordinate for a given city.

    Args:
        city (str): The name of the city.

    Returns:
        dict: A dictionary containing the latitude and longitude of the city, or None if the city is not found.
    """
    city_lower = city.lower()
    if city_lower == "cairns":
        logging.info(f"GPS coordinates for '{city}': {CAIRNS_COORDINATES['latitude']}, {CAIRNS_COORDINATES['longitude']}")
        return CAIRNS_COORDINATES
    else:
        logging.warning(f"No GPS coordinates found for '{city}'")
        return None

