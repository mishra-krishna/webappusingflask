from flask import Flask, render_template, request
from weather import get_weather_by_city as weather_main
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    data = None
    if request.method == 'POST':
        city = request.form['cityInput']
        state = request.form['stateInput']
        country = request.form['countryInput']
        print(f"Received form data: {city}, {state}, {country}")

        data = weather_main(city, state, country, api_key)
        print(f"Weather data: {data}")

    return render_template('index.html',data=data)



if __name__ == '__main__':
    app.run(debug=True)
