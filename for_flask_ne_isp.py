from flask import Flask
import requests

app = Flask(__name__)

def get_weather():
    params = {"access_key": "86a3fe972756lk34a6a042bll348b1e3", "query": "Moscow"}
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    return f"Сейчас в Москве {api_response['current']['temperature']} градусов"

@app.route("/hello")
def hello():
    weather = get_weather()
    print(weather)
    return "Hello World!"
if __name__ == "__main__":
    app.run()