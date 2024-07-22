import requests
from bs4 import BeautifulSoup

def html_parser(url: str) -> BeautifulSoup:
    """Parses webpage using Beautiful Soup

    Args:
        url (str): URL of webpage to parse

    Returns:
        soup: BeautifulSoup object representing parsed HTML webpage
    """    
    # Make request to URL
    response = requests.get(url)

    # Parse webpage with Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")

    # Return parsed webpage
    return soup
