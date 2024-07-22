import requests
from api_utils.api_request_validation import validate_geonames_request
from api_utils.check_location_match import location_match_checker

def fetch_geonames_data(town: str, country_code: str, geonames_username: str) -> dict:
    """Converts town and country code to dictionary of location data (name, country code, longitude, latitude, and location ID)

    Args:
        town (str): Town to search for
        country_code (str): Country to search for
        geonames_username (str): GeoNames API username (should be stored in .env file)

    Raises:
        ValueError: If lengths of town and/or country code are invalid
        Exception: If bad request, or no results found, or inputted town/country code doesn't match GeoNames API response

    Returns:
        location_data: Dictionary of location data containing name, country code, longitude, latitude, and location ID
    """    

    # Construct GeoNames API request, uses fuzziness parameter (default = 60%) to look for approximate matches to improve searching
    fuzziness = 0.6
    api_search_url = f'http://api.geonames.org/searchJSON?q={town}&country={country_code}&featureClass=P&continentCode=&fuzzy={fuzziness}&username={geonames_username}'

    # Validate submitted fields for API request (using "validate_api_request" helper function to check lengths)
    is_valid_location = validate_geonames_request(town, country_code)

    # Raise ValueError if town and/or country code are incorrect lengths
    if is_valid_location is False:
        raise ValueError("Invalid location")
    
    # Query GeoNames API
    geonames_response = requests.get(api_search_url)

    # Raise Exception if bad request or no locations found
    if geonames_response.status_code == 401:
        raise Exception("Bad request")
    
    if geonames_response.json()['totalResultsCount'] == 0:
        raise Exception("Location not found")
    
    # Store GeoNames API reponse
    geonames_town = geonames_response.json()['geonames'][0]['name']
    geonames_country_code = geonames_response.json()['geonames'][0]['countryCode']
    latitude = geonames_response.json()['geonames'][0]['lat']
    longitude = geonames_response.json()['geonames'][0]['lng']
    location_id = geonames_response.json()['geonames'][0]['geonameId']

    # Check if town and country code match what was inputted, using "check_location_match" helper function
    location_match_result = location_match_checker(town, country_code, geonames_town, geonames_country_code)
    
    # If doesn't match, increase fuzziness to 80% and attempt to search again 
    if location_match_result is False:

        fuzziness = 0.8
        api_search_url = f'http://api.geonames.org/searchJSON?q={town}&country={country_code}&featureClass=P&continentCode=&fuzzy={fuzziness}&username={geonames_username}'
        geonames_response = requests.get(api_search_url)

        geonames_town = geonames_response.json()['geonames'][0]['name']
        geonames_country_code = geonames_response.json()['geonames'][0]['countryCode']

        location_match_result = location_match_checker(town, country_code, geonames_town, geonames_country_code)
    
        # Raise Exception if location not found on second loop (location doesn't match after increasing fuzziness and searching again)
        if location_match_checker is False:
            raise Exception("Location not found")

    # Store and return location data from GeoNames API request
    location_data = {
        'town': geonames_town,
        'country_code': geonames_country_code,
        'latitude': latitude,
        'longitude': longitude,
        'location_id': location_id
    }

    return location_data
