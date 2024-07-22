import requests
from datetime import datetime
from data_processing.conversions import knots_per_hour_to_mph
import json

def fetch_met_office_weather_data(latitude, longitude, met_office_api_key):

    base_url = 'https://data.hub.api.metoffice.gov.uk/sitespecific/v0/point/'

    # Met Office weather parameters
    requestHeaders = {"apikey": f'{met_office_api_key}'}
    headers = {'accept': "application/json"}
    headers.update(requestHeaders)
    params = {
        'excludeParameterMetadata': False,
        'includeLocationName': True,
        'latitude': latitude,
        'longitude': longitude
    }

    timesteps = 'hourly'

    url = base_url + timesteps

    met_office_response = requests.get(url, headers=headers, params=params)

    # Check if the request is ok (HTTP status code within 200-299)
    if met_office_response.ok is False:
        raise Exception("MetOffice Weather API received a bad request")

    # Convert current time into a string that will match in the json data
    current_time = str(datetime.date(datetime.now())) + str('T') + str(datetime.time(datetime.now()))[0:3] + str('00Z')

    # Retrieve data
    json_key = met_office_response.json()['features'][0]['properties']['timeSeries']

    # 24 hours in a day
    for i in range(25):

        # Check for current date and time in data
        if json_key[i]['time'] == current_time:

            # Temperature
            temperature = json_key[i]['screenTemperature']

            # Feels like
            feels_like = json_key[i]['feelsLikeTemperature']

            # Wind speed
            wind_speed = json_key[i]['windSpeed10m']

            # Gust speed
            gust_speed = json_key[i]['windGustSpeed10m']
            gust_speed = knots_per_hour_to_mph(gust_speed)

            # Rain chance
            rain_chance = json_key[i]['probOfPrecipitation']

            # Snow

            # Snow condition flag: 0 = Not going to snow, 1 = Forecasted to snow
            snow_condition_flag = 0

            # Snow amount - doesn't always exist in the json data
            try:
                snow_amount = json_key[i]['totalSnowAmount']
            except:
                snow_amount = 0

            # Set snow condition flag equal to 1 if snow is forecasted
            if snow_amount > 0:
                snow_condition_flag = 1

            # Significant weather code
            weather_code = json_key[i]['significantWeatherCode']
            weather_code = str(weather_code)

            # Reading json file containing Met Office significant weather codes
            weather_codes_json_path = r"data\met_office_weather_codes.json"

            with open(weather_codes_json_path, 'r') as significant_weather_codes_json:

                significant_weather_codes = json.load(significant_weather_codes_json)

                # Retrieving weather description from wignificant weather code key in json file
                weather_desc = significant_weather_codes[weather_code]

            # UV index
            uv_index_code_json_path = "data\met_office_uv_index_codes.json"

            with open(uv_index_code_json_path, 'r') as uv_index_codes_json:

                uv_index_codes = json.load(uv_index_codes_json)

                uv_index_code = json_key[i]['uvIndex']

            # If UV Index > 11 display the highest warning
            if int(uv_index_code) > 11:
                uv_index_desc = "Extreme. Avoid being outside during midday hours. Shirt, sunscreen and hat essential."

            # Otherwise display the corresponding description for the index number
            else:
                uv_index_desc = str(uv_index_code)
                uv_index_desc = uv_index_codes[uv_index_desc]

            # Humidity
            humidity = json_key[i]['screenRelativeHumidity']

            # Met Office weather data
            met_office_data = {
                'temperature': temperature,
                'feels_like': feels_like,
                'wind_speed': wind_speed,
                'gust_speed': gust_speed,
                'weather_desc': weather_desc,
                'rain_chance': rain_chance,
                'snow_condition_flag': snow_condition_flag,
                'snow_amount': snow_amount,
                'uv_index_code': uv_index_code,
                'uv_index_desc': uv_index_desc,
                'humidity': humidity
            }

            return met_office_data