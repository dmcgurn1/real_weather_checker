from flask import Flask, render_template, request
import time
from main import get_results

# Flask website
app = Flask(__name__)

# Home
@app.route('/')
def home():

    return render_template('home.html')

# Results
@app.route('/', methods=['POST'])

def results():

    town = request.form['townName']
    country_code = request.form['countryCode']

    time.sleep(0.1)

    # main.py
    weather_data = get_results(town, country_code)

    # Render results page
    return render_template('/results.html', output_data=weather_data)


if __name__ == '__main__':
    app.run(debug=True)
