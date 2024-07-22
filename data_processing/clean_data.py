def clean_variable(variable: str) -> float:
    """Cleans up the variable by removing degree symbols (°), percentage signs (%), and spaces ( )

    Args:
        variable (str): Variable to be cleaned

    Returns:
        variable (float): Cleaned variable as a float
    """
    # Convert variable to string
    variable = str(variable)

    # Remove any degree symbols, percentage signs, or spaces
    variable = variable.strip("°% ")

    # Convert into float
    variable = float(variable)

    return variable
