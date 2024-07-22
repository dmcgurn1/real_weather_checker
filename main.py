# Import libraries
from dotenv import load_dotenv
import os
# import requests
import numpy as np
from datetime import datetime
from dataclasses import dataclass

# Import functions from modules
from api_utils import fetch_geonames_data, validate_geonames_request, location_match_checker, fetch_open_weather_data, fetch_met_office_weather_data, fetch_bbc_weather_data, fetch_yrno_data, fetch_moon_phase_data
from data_processing import clean_variable, format_variable
from emojis import weather_emoji_picker

# Import API Keys from '.env'
load_dotenv()
geonames_username = os.getenv('GeoNamesUsername')
open_weather_api_key = os.getenv('OpenWeatherAPIKey')
met_office_api_key = os.getenv('MetOfficeAPIKey')

# Initialise data class for output
@dataclass
class AppData:
    current_date: str
    current_time: str
    latitude: str
    longitude: str
    location_name: str
    location_id: str
    temperature: str
    feels_like: str
    weather_desc: str
    wind_speed: str
    gust_speed: str
    wind_desc: str
    rain_chance: str
    rain_amount: str
    snow_condition_flag: int
    snow_amount: str
    uv_index_code: str
    uv_index_desc: str
    humidity: str
    sunrise: str
    sunset: str
    moon_phase: str
    moon_emoji: str
    moon_percent: str
    weather_emoji: str

# Main logic:

# Get weather information from:
# 1. OpenWeather
# 2. Met Office
# 3. BBC Weather (+Sunrise/Sunset)
# 4. Yr.No

# Additional:
# TimeandDate.com - 'timeanddate.com/moon/phases' (Moon Phase)

def get_results(town, country_code):

    # Initialise weather_data variable
    weather_data = None

    # Create empty numpy arrays to put variables in, to average afterwards
    all_temperatures = np.array([])
    all_feels_like = np.array([])
    all_wind_speeds = np.array([])
    all_rain_chance = np.array([])
    all_humidity = np.array([])

    # Geocoding information

    # Get town and country code from html form submission - commented out for time being
    # MOVED TO app.py

    # TEMP - Get town and country code from user input
    # town = input("Town: ")
    # country_code = input("Country code: ")

    # Store location info from geo_coder function in variable
    geonames_data = fetch_geonames_data(town, country_code, geonames_username)

    # Get location info using geo_coder function
    latitude = geonames_data['latitude']
    longitude = geonames_data['longitude']
    location_id = geonames_data['location_id']

    # Getting weather information...

    # Get weather data
    open_weather_data = fetch_open_weather_data(latitude, longitude, open_weather_api_key)
    met_office_data = fetch_met_office_weather_data(latitude, longitude, met_office_api_key)
    bbc_weather_data = fetch_bbc_weather_data(location_id)
    yrno_data = fetch_yrno_data(location_id)
    moon_phase_data = fetch_moon_phase_data(location_id)

    # Print weather data:
    # print('OpenWeather Data:', open_weather_data)
    # print('MetOffice Data:', met_office_data)
    # print('BBC Data:', bbc_weather_data)
    # print('YrNo Data:', yrno_data)
    # print('Moon Phase Data:', moon_phase_data)

    # Clean / store variables for averaging
    all_temperatures = np.append(all_temperatures, [
        clean_variable(open_weather_data['temperature']),
        clean_variable(met_office_data['temperature']),
        clean_variable(bbc_weather_data['temperature']),
        clean_variable(yrno_data['temperature']),
    ])

    all_feels_like = np.append(all_feels_like, [
        clean_variable(open_weather_data['feels_like']),
        clean_variable(met_office_data['feels_like']),
        clean_variable(bbc_weather_data['feels_like']),
        clean_variable(yrno_data['feels_like']),
    ])

    all_wind_speeds = np.append(all_wind_speeds, [
        clean_variable(open_weather_data['wind_speed']),
        clean_variable(met_office_data['wind_speed']),
        clean_variable(bbc_weather_data['wind_speed']),
        clean_variable(yrno_data['wind_speed']),
    ])

    all_rain_chance = np.append(all_rain_chance, [
        clean_variable(met_office_data['rain_chance']),
        clean_variable(bbc_weather_data['rain_chance']),
    ])

    all_humidity = np.append(all_humidity, [
        clean_variable(open_weather_data['humidity']),
        clean_variable(met_office_data['humidity']),
        clean_variable(bbc_weather_data['humidity'])
    ])

    # Print arrays
    # print("All temperatures:", all_temperatures)
    # print("All feels like:", all_feels_like)
    # print("All wind speeds:", all_wind_speeds)
    # print("All rain chance:", all_rain_chance)
    # print("All humidity:", all_humidity)

    # Get average values from arrays
    average_temperature = np.average(all_temperatures)
    average_feels_like = np.average(all_feels_like)
    average_wind_speed = np.average(all_wind_speeds)
    average_rain_chance = np.average(all_rain_chance)
    average_humidity = np.average(all_humidity)

    # Format averages
    average_temperature = format_variable(average_temperature)
    average_feels_like = format_variable(average_feels_like)
    average_wind_speed = format_variable(average_wind_speed)
    average_rain_chance = format_variable(average_rain_chance)
    average_humidity = format_variable(average_humidity)

    # Store other variables
    weather_desc = met_office_data['weather_desc']
    gust_speed = met_office_data['gust_speed']
    wind_desc = bbc_weather_data['wind_desc']
    rain_amount = yrno_data['rain_amount']
    snow_condition_flag = met_office_data['snow_condition_flag']
    snow_amount = met_office_data['snow_amount']
    uv_index_code = met_office_data['uv_index_code']
    uv_index_desc = met_office_data['uv_index_desc']
    sunrise = bbc_weather_data['sunrise']
    sunset = bbc_weather_data['sunset']
    moon_phase = moon_phase_data['moon_phase']
    moon_percent = moon_phase_data['moon_percent']

    # Format other variables where necessary
    location_id = str(location_id)
    gust_speed = format_variable(gust_speed)
    snow_amount = format_variable(snow_amount)
    uv_index_code = format_variable(uv_index_code)
    moon_percent = format_variable(clean_variable(moon_percent))

    # Extras:

    # Retrieve town and country code as shown in GeoNames API request, then format to create location_name string
    town = geonames_data['town']
    country_code = geonames_data['country_code']

    location_name = f'{town}, {country_code}'

    # Get date and time for current run
    current_date_str = f'{str(datetime.now())[8:10]}/{str(datetime.now())[5:7]}/{str(datetime.now())[0:4]}'
    current_time_str = f'{str(datetime.now())[11:16]}'

    # Weather emoji
    weather_emoji = weather_emoji_picker(weather_desc)

    # Moon emoji
    moon_emoji = moon_phase_data['moon_emoji']

    # Put output variable in AppData dataclass as 'weather_data'
    weather_data = AppData(
        current_date=current_date_str,
        current_time=current_time_str,
        latitude=latitude,
        longitude=longitude,
        location_name=location_name,
        location_id=location_id,
        temperature=average_temperature,
        feels_like=average_feels_like,
        weather_desc=weather_desc,
        wind_speed=average_wind_speed,
        gust_speed=gust_speed,
        wind_desc=wind_desc,
        rain_chance=average_rain_chance,
        rain_amount=rain_amount,
        snow_condition_flag=snow_condition_flag,
        snow_amount=snow_amount,
        uv_index_code=uv_index_code,
        uv_index_desc=uv_index_desc,
        humidity=average_humidity,
        sunrise=sunrise,
        sunset=sunset,
        moon_phase=moon_phase,
        moon_emoji=moon_emoji,
        moon_percent=moon_percent,
        weather_emoji=weather_emoji
    )

    # (Contains 23 variables)

    # Print weather_data, putting a new line after bracket/comma
    print("Print weather results: \n")
    print(str(weather_data).replace('(', '(\n').replace("',", ",\n"))

    return weather_data

# TEMP - Run function (testing)
# get_results()