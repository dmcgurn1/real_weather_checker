import requests
from data_processing.conversions import meters_per_second_to_mph

def fetch_open_weather_data(latitude, longitude, fetch_open_weather_data_api_key):

    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    query_url = f"{base_url}?lat={latitude}&lon={longitude}&units=metric&APPID={fetch_open_weather_data_api_key}"

    # Request
    fetch_open_weather_data_response = requests.get(query_url)

    # Check if the request is ok (HTTP status code within 200-299)
    if fetch_open_weather_data_response.ok is False:
        raise Exception("OpenWeather API received a bad request.")

    # Data
    data = fetch_open_weather_data_response.json()

    # Temperature
    temperature = data['main']['temp']

    # Feels like
    feels_like = data['main']['feels_like']
    
    # Wind speed
    wind_speed = data['wind']['speed']
    wind_speed = meters_per_second_to_mph(wind_speed)

    # Weather description
    weather_desc = data['weather'][0]['description']

    # Humidity
    humidity = data['main']['humidity']

    # Open Weather data
    fetch_open_weather_data_data = {
        'temperature': temperature,
        'feels_like': feels_like,
        'wind_speed': wind_speed,
        'weather_desc': weather_desc,
        'humidity': humidity
    }

    return fetch_open_weather_data_data