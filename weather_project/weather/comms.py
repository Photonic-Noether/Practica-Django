import requests
from django.conf import settings

def llamar_api(ciudad: str):
    api_key = settings.KEY
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad.upper()}&appid={api_key}&units=metric"
    respuesta = requests.get(url)
    return respuesta