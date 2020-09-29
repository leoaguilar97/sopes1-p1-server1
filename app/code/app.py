from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return 'App Works!'

@app.route('/<string:city>/<string:country>/')
def weather_by_city(country, city):
    url = 'https://samples.openweathermap.org/data/2.5/weather'
    params = dict(
        q=city + "," + country,
        appid= "d5dc476be1debbd6890ae64bfdbb5b11",
    )
    response = requests.get(url=url, params=params)
    data = response.json()
    return data

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)