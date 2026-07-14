from django.shortcuts import render, redirect
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def ciudad(request):
    return render(request, 'ciudad.html')

def obtener_clima(request):
    datos = {}

    if request.method == 'POST':
        nombre_ciudad = request.POST.get('ciudad')
        API_KEY = '8f97891dd4b3303bb98f870997f24661'
        url = "https://api.openweathermap.org/data/2.5/weather"

        parametros = {
            "q": nombre_ciudad,
            "units": "metric",
            "lang": "es",
            "appid": API_KEY
        }

        try:
            respons = requests.get(url, params=parametros, timeout=3.0)
            respons.raise_for_status()
            datos = respons.json()

        except requests.exceptions.RequestException:
            # Control de errores si la ciudad no existe o falla la conexión
            datos = {"error": f"No se encontraron resultados para '{nombre}'"}

        return render(request, 'ciudad.html', {
            'datos': datos
        })
    else:
        return render(request, 'index.html')