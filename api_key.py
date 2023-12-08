import requests

def get_weather(city):
    api_key = "56737f1535cdd9099a084540fa3e1a21"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] == 200:
        weather_info = {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "icon": data["weather"][0]["icon"]
        }
        return weather_info
    else:
        return None