def format_variable(variable: float) -> str:
    """Formats float by either rounding to 1 decimal place if decimal, or 0 decimal places if whole number, returns variable as a string

    Args:
        variable (float): Float to be formatted

    Returns:
        str: Formatted variable as string, with either 1 decimal place, or 0 decimal places
    """
    # Convert variable to float
    variable = float(variable)

    # Round float to 1 decimal place
    variable = round(variable, 1)

    # If the float is a whole number, convert it to an integer
    if variable % 1 == 0:
        variable = int(variable)

    # Convert variable into string for output
    variable = str(variable)

    return variable
