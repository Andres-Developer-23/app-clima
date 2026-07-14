# app-clima

Aplicación web del clima construida con Django. Consulta el clima actual de cualquier ciudad usando la API de OpenWeatherMap.

## Stack

- **Backend:** Django 6.0 (Python 3.12)
- **API:** OpenWeatherMap
- **Frontend:** Django Templates + CSS vanilla
- **Base de datos:** SQLite (desarrollo) / PostgreSQL (producción)

## Deploy

### Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

1. Forkear el repo y conectarlo a Render como Web Service
2. Configurar las variables de entorno en Render:

| Variable | Descripción |
|---|---|
| `DJANGO_SECRET_KEY` | Secret key de Django (generar en [djecrety.ir](https://djecrety.ir)) |
| `OPENWEATHER_API_KEY` | API key de OpenWeatherMap |
| `ALLOWED_HOSTS` | `.onrender.com,localhost,127.0.0.1` |
| `DEBUG` | `False` |

3. Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
4. Start Command: `gunicorn app_clima.wsgi --bind 0.0.0.0:$PORT`

## Desarrollo local

```bash
git clone https://github.com/Andres-Developer-23/app-clima.git
cd app-clima
pip install -r requirements.txt
cp .env.example .env  # Configurar OPENWEATHER_API_KEY
python manage.py runserver
```

## Licencia

MIT
