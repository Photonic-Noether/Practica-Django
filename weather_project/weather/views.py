from django.shortcuts import render
import datetime
from weather.comms import llamar_api
from weather.forms import CityForm
from weather.models import Person

def widget_tiempo(request):
    data = None
    respuesta = None
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            ciudad = form.cleaned_data["city"]
            respuesta = llamar_api(ciudad)
            data = respuesta.json()
        if respuesta.status_code == 200:
            context = {
                "location": data["name"],
                "temperature": f"{data['main']["temp"]} ºC",
                "max_temp": f"{data["main"]["temp_max"]} ºC",
                "min_temp": f"{data["main"]["temp_min"]} ºC",
                "condition": data["weather"][0]["description"],
                "date": datetime.datetime.now()  # La fecha de ahora
            }
        else:
            context = {
                "location": "N/A",
                "temperature": "N/A",
                "condition": "N/A",
                "max_temp": "N/A",
                "min_temp": "N/A",
                "date": datetime.datetime.now()  # La fecha de ahora
            }
    else:
        form = CityForm()
        context = {
                "location": "N/A",
                "temperature": "N/A",
                "condition": "N/A",
                "max_temp": "N/A",
                "min_temp": "N/A",
                "date": datetime.datetime.now()  # La fecha de ahora
            }
    return render(request, "vista_tiempo.html", {"form": form, "context": context})

def ver_personas(request):
    mi_persona = Person.objects.get(id=3)
    return render(request, "test.html", {"nombre_persona": mi_persona})