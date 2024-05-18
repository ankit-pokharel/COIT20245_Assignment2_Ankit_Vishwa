from nominatim import gps_coordinate
from wildlife import get_species_list, get_surveys_by_species

RADIUS = 100000  # 100 km

def display_menu():
    print("Help")
    print("====")
    print("The following commands are recognized:")
    print("Display help            wildlife> help")
    print("Search species           wildlife> species <city>")
    print("Display venomous species wildlife> species <city> venomous")
    print("Display animal sightings wildlife> sightings <city> <taxonid>")
    print("Exit the application    wildlife> exit")

def gps(city):
    """
    Returns the GPS coordinate for a given city.
    """
    return gps_coordinate(city)

def search_species(city):
    """
    Searches for species in a given city and returns a list of species dictionaries.
    """
    coordinate = gps(city)
    if coordinate:
        species_list = get_species_list(coordinate, RADIUS)
        return species_list
    else:
        print(f"Error: Could not find GPS coordinates for '{city}'. Please try a different city name.")
        return []

def display_species(species_list):
    for species in species_list:
        name = species["Species"]["AcceptedCommonName"] if "AcceptedCommonName" in species["Species"] else "Unknown"
        status = species["Species"]["PestStatus"] if "PestStatus" in species["Species"] else "Nil"
        print(f"Species: {name}, Pest Status: {status}")

def search_sightings(taxonid, city):
    """
    Searches for sightings of a particular species in a given city.

    Args:
        taxonid (int): The TaxonID of the species to search for.
        city (str): The name of the city to search around.

    Returns:
        list: A list of dictionaries, where each dictionary represents a sighting.
    """
    coordinate = gps(city)
    if coordinate:
        surveys = get_surveys_by_species(coordinate, RADIUS, taxonid)
        sightings = [survey for survey in surveys if survey["properties"]["SiteCode"] == "INCIDENTAL"]
        return sightings
    else:
        print(f"Error: Could not find GPS coordinates for '{city}'")
        return []

def earliest(sightings):
    """
    Returns the sighting with the minimum start date.

    Args:
        sightings (list): A list of dictionaries representing sightings.

    Returns:
        dict: The sighting dictionary with the minimum start date, or None if the list is empty.
    """
    if not sightings:
        return None

    earliest_sighting = min(sightings, key=lambda s: s["properties"]["StartDate"])
    return earliest_sighting

def sort_by_date(sightings):
    """
    Sorts the list of sightings by date in ascending order.

    Args:
        sightings (list): A list of dictionaries representing sightings.

    Returns:
        list: A new list of sightings sorted by date in ascending order.
    """
    sorted_sightings = sorted(sightings, key=lambda s: s["properties"]["StartDate"])
    return sorted_sightings

def display_sightings(sightings):
    if sightings:
        sorted_sightings = sort_by_date(sightings)
        for sighting in sorted_sightings:
            start_date = sighting["properties"]["StartDate"]
            locality = sighting["properties"]["LocalityDetails"]
            print(f"Sighting: {locality} ({start_date})")
    else:
        print("No sightings found.")

def filter_venomous(species_list):
    """
    Filters the list of species and returns only the venomous ones.
    """
    venomous_species = [species for species in species_list if species["Species"]["PestStatus"] == "Venomous"]
    return venomous_species

def test_filter_venomous():
    """
    Tests the filter_venomous function.
    """
    species_list = [
        {"Species": {"AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
        {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}}
    ]
    expected_output = [
        {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}}
    ]
    assert filter_venomous(species_list) == expected_output

def main():
    display_menu()
    while True:
        command = input("wildlife> ")
        if command == "help":
            display_menu()
        elif command == "exit":
            print("Exiting the application.")
            break
        elif command.startswith("species "):
            parts = command.split(" ")
            city = parts[1]
            if len(parts) > 2 and parts[2] == "venomous":
                species_list = search_species(city)
                venomous_species = filter_venomous(species_list)
                display_species(venomous_species)
            else:
                species_list = search_species(city)
                display_species(species_list)
        elif command.startswith("sightings "):
            parts = command.split(" ")
            city = parts[1]
            taxonid = int(parts[2])
            sightings = search_sightings(taxonid, city)
            display_sightings(sightings)
        else:
            print("Error: Unrecognized command. Please try again.")

if __name__ == "__main__":
    test_filter_venomous()
    # Test the search_sightings function
    # sightings = search_sightings(860, "Cairns")
    # assert len(sightings) > 0
    # print(sightings)
    main()
