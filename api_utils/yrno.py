from api_utils.beautiful_soup_html_parser import html_parser
from data_processing.conversions import meters_per_second_to_mph

def fetch_yrno_data(location_id):

    base_url = 'https://www.yr.no/en/forecast/daily-table/2-'

    forecast_url = f'{base_url}{location_id}'

    # Using helper function
    soup = html_parser(forecast_url)

    # Temperature - temperature can be warm or cold:
    try:
        temperature = soup.find("span", {"class": "temperature temperature--warm-primary"}).get_text()
    except:
        temperature = soup.find("span", {"class": "temperature temperature--cold-primary"}).get_text()

    temperature = temperature.split('Temperature')[1]

    # Feels like:
    feels_like = soup.find("div", {"class": "feels-like-text"}).get_text()
    feels_like = feels_like.split('Feels like ')[1]
    feels_like = feels_like[-3:]

    # Wind speed:
    wind_speed = soup.find("span", {"class": "wind__value now-hero__next-hour-wind-value"}).get_text()
    wind_speed = float(wind_speed)
    wind_speed = meters_per_second_to_mph(wind_speed)

    # Rainfall:
    rain_amount = soup.find("span", {"class": "now-hero__next-hour-precipitation-value"}).get_text()

    # YrNo weather data
    yrno_data = {
        'temperature': temperature,
        'feels_like': feels_like,
        'wind_speed': wind_speed,
        'rain_amount': rain_amount
    }

    return yrno_data