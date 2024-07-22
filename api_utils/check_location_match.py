def location_match_checker(town, country_code, geonames_town, geonames_country_code) -> bool:
    """Checks town and country code against GeoNames API response town and country code. Returns True if they match, or False if they don't

    Args:
        town (str): Inputted town to check against town from GeoNames API response
        country_code (str): Inputted country code to check against country code from GeoNames API response
        geonames_town (str): Town from GeoNames API response
        geonames_country_code (str): Country code from GeoNames API response

    Returns:
        bool: True or False depending on whether inputted town and country code match town and country code from GeoNames API response
    """    

    # Convert towns and country codes to lowercase 
    town = town.lower()
    geonames_town = geonames_town.lower()

    country_code = country_code.lower()
    geonames_country_code = geonames_country_code.lower()

    # Check if they match and return True or False depending on result
    if town != geonames_town and country_code != geonames_country_code:
        return False
    
    else:
        return True
    