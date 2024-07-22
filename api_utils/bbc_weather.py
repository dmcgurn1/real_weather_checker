from api_utils.beautiful_soup_html_parser import html_parser

def fetch_bbc_weather_data(location_id):

    base_url = 'https://bbc.co.uk/weather/'

    forecast_url = f'{base_url}{location_id}'

    # Using helper function
    soup = html_parser(forecast_url)

    # Temperature:
    temperature = soup.find("div", {"class": "wr-time-slot-primary__temperature"}).get_text()
    temperature = temperature[0:2]

    # Feels like:
    feels_like = soup.find("span", {"class": "wr-time-slot-secondary__feels-like-temperature-value gel-long-primer-bold wr-value--temperature--c"}).get_text()

    # Wind speed:
    wind_speed = soup.find("div", {"class": "wr-time-slot-primary__wind-speed"}).get_text().strip('Wind speed mph').split()[0]

    # Wind description:
    wind_desc = soup.find("div", {"class": "wr-time-slot-secondary__wind-direction wr-time-slot-secondary__bottom-section gel-long-primer"}).get_text()

    # Rain chance:
    rain_chance = soup.find("div", {"class": "wr-u-font-weight-500"}).get_text()
    rain_chance = rain_chance.replace('chance of precipitation', '')

    # Sunrise:
    sunrise = soup.find("span", {"class": "wr-c-astro-data__sunrise gel-pica-bold gs-u-pl-"}).get_text()
    sunrise = sunrise.strip('Sunrise')

    # Sunset:
    sunset = soup.find("span", {"class": "wr-c-astro-data__sunset gel-pica gs-u-pl-"}).get_text()
    sunset = sunset.strip('Sunset')

    # Humidity:
    humidity = soup.find("dd", {"class": "wr-time-slot-secondary__value gel-long-primer-bold"}).get_text()

    # BBC Weather data
    bbc_weather_data = {
        'temperature': temperature,
        'feels_like': feels_like,
        'wind_speed': wind_speed,
        'wind_desc': wind_desc,
        'rain_chance': rain_chance,
        'humidity': humidity,
        'sunrise': sunrise,
        'sunset': sunset
    }

    return bbc_weather_data