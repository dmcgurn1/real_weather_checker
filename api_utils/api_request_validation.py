def validate_geonames_request(town: str, country_code: str) -> bool:
    """Checks if submitted town and country code are correct lengths, returns True or False

    Args:
        town (str): Submitted town
        country_code (str): Submitted country code

    Returns:
        bool: True or False
    """    

    # Convert to strings
    town = str(town)
    country_code = str(country_code)

    # Remove spaces from fields
    town = town.replace(" ", "")
    country_code = country_code.replace(" ", "")

    # Check:
    # town is longer than 1 character and shorter than 31 characters
    # country_code is 2 characters long

    if 1 < len(town) <= 30 and len(country_code) == 2:
        return True
    
    else:
        return False
    