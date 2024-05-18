import requests

def get_species_list(coordinate, radius):
    """
    Fetches the list of species from the Queensland wildlife data API within a specified radius of a given coordinate.

    Args:
        coordinate (dict): A dictionary containing the latitude and longitude of the center point.
        radius (int): The radius in meters to search for species around the center point.

    Returns:
        list: A list of dictionaries, where each dictionary represents a species.
    """
    lat, lon = coordinate["latitude"], coordinate["longitude"]
    url = f"https://apps.des.qld.gov.au/species/?op=getspecieslist&kingdom=animals&circle={lat},{lon},{radius}"
    response = requests.get(url).json()

    if "SpeciesSightingSummary" in response["SpeciesSightingSummariesContainer"]:
        return response["SpeciesSightingSummariesContainer"]["SpeciesSightingSummary"]
    else:
        return []

def get_surveys_by_species(coordinate, radius, taxonid):
    """
    Fetches the list of surveys for a particular species within a specified radius of a given coordinate.

    Args:
        coordinate (dict): A dictionary containing the latitude and longitude of the center point.
        radius (int): The radius in meters to search for surveys around the center point.
        taxonid (int): The TaxonID of the species to search for.

    Returns:
        list: A list of dictionaries, where each dictionary represents a survey.
    """
    lat, lon = coordinate["latitude"], coordinate["longitude"]
    url = f"https://apps.des.qld.gov.au/species/?op=getsurveysbyspecies&taxonid={taxonid}&circle={lat},{lon},{radius}"
    response = requests.get(url).json()

    if "features" in response:
        return response["features"]
    else:
        return []

