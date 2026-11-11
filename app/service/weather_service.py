from fastapi import HTTPException
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENWEATHER_API_KEY')

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather_data(city: str):
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    if not api_key:
        raise HTTPException(status_code=500 , detail='API key not found')
    try:
        response = httpx.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {'success' : True,
            'data' : {
                'city_name' : data['name'],
                'temp' : data['main']['temp'],
                'feels_like' : data['main']['feels_like'],
                'wind_speed' : data['wind']['speed'],
                'wind_direction' : data['wind']['deg'],
                'pressure' : data['main']['pressure'],
                'humidity' : data['main']['humidity'],
                'sunrise' : data['sys']['sunrise'],
                'sunset' : data['sys']['sunset'],
                'icon' : data['weather'][0]['icon'],
                'description' : data['weather'][0]['description'],
                'datetime' : data['dt']
            },
            'message': 'OK'
            }
    except httpx.HTTPStatusError as error:
        raise HTTPException(status_code=404, detail=f"City '{city}' not found")
    
    except httpx.RequestError as error:
        raise HTTPException(status_code=500, detail=f"Error fetching weather data")
    