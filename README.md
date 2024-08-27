# real-weather-checker-app
Quick, accurate spot-check forecast for the current time, based on averaged weather data.

The weather data is collected and averaged in numpy arrays.

The output is either an average of the weather variables, if available, or a singular element from one of the sources -> (e.g. current temperature comes from all 4 sources and then averaged, rain chance comes from 2 sources and then averaged, but gust speed is only present on the MetOffice API so it is not an average)

IMPORTANT: You will require your own API key for OpenWeather, as well as your own API 'id' and 'secret' for MetOffice

Weather data sources: OpenWeather API, MetOffice Weather API, BBC Weather, and YrNo Weather
Moon data source: Moon Phases

Fill out values in .env file

Activate virtual environment: 

1. Go to root directory in terminal (...\real-weather-checker-app) -> i.e. "cd {path}"
2. python -m venv venv
3. .\venv\Scripts\activate
4. python -m pip install -r requirements.txt
5. pip install -e .
