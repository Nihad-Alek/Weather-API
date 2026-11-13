from fastapi import HTTPException
import httpx
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

api_key = os.getenv('OPENWEATHER_API_KEY')

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
BASE_URL_forecast = 'https://api.openweathermap.org/data/2.5/forecast'

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
        if error.response.status_code == 404:
            raise HTTPException(status_code=404, detail=f"City '{city}' not found")
        raise HTTPException(status_code=500, detail='Error from server')
    except httpx.RequestError:
        raise HTTPException(status_code=500 , detail=f"Error fetching weather data")
    
def get_weather_data_forecast(city: str):
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    if not api_key:
        raise HTTPException(status_code=500 , detail='API key not found')
    try:
        response = httpx.get(BASE_URL_forecast , params=params , timeout=10)
        response.raise_for_status()
        data = response.json()
        weekday_and_temp = {}
        for item in data['list']:
            dt = datetime.datetime.strptime(item['dt_txt'], "%Y-%m-%d %H:%M:%S")
            weekday_dt = dt.strftime("%A")
            temp = item['main']['temp']
            icon = item['weather'][0]['icon']
            description = item['weather'][0]['description']
    
            if weekday_dt not in weekday_and_temp:
                weekday_and_temp[weekday_dt] = {
                    'temperature': [],
                    'icon' : [],
                    'description': []
                }
    
            weekday_and_temp[weekday_dt]['temperature'].append(temp)
            weekday_and_temp[weekday_dt]['icon'].append(icon)
            weekday_and_temp[weekday_dt]['description'].append(description)
        forecast = []

        for day , values in weekday_and_temp.items():
            min_temp = min(values['temperature'])
            max_temp = max(values['temperature'])
            forecast.append({
                'day_name': day,
                'min_temp': min_temp,
                'max_temp': max_temp,
                'icon': values['icon'][0],
                'description': values['description'][0]
            })
        
        return {
            'success': True,
            'data': forecast,
            'message': 'OK'
            }
    except httpx.HTTPStatusError as error:
        if error.response.status_code == 404:
            raise HTTPException(status_code=404, detail=f"City '{city}' not found")
        raise HTTPException(status_code=500, detail='Error from server')
    except httpx.RequestError:
        raise HTTPException(status_code=500 , detail=f"Error fetching weather data")
    
def get_weather_rain_probability(city: str):
    params = {
        'q' : city,
        'appid' : api_key,
        'units' : 'metric'
    }
    if not api_key:
        raise HTTPException(status_code=500 , detail='API key not found')
    try:
        response = httpx.get('https://api.openweathermap.org/data/2.5/forecast' , params=params , timeout=10)
        response.raise_for_status()
        data = response.json()
        now = datetime.datetime.now()
        end_time = now + datetime.timedelta(hours=18)
        time_rain = {}
        for item in data['list']:
            forecast_time = datetime.datetime.fromtimestamp(item["dt"])
            if now < forecast_time <= end_time:
                time_rain[forecast_time.strftime('%I%p').lstrip('0')] = {
                    'probability': item['pop'] * 100,
                    'condition': item['weather'][0]['main']
                    }
        rain_probability = []
        
        for day, values in time_rain.items():
                rain_probability.append({
                    'time_label' : day,
                    'probability': values['probability'],
                    'condition': values['condition']
                })

        return {
            'success' : True,
            'data' : rain_probability,
            'message' : 'OK'
        }
    except httpx.HTTPStatusError as error:
        if error.response.status_code == 404:
            raise HTTPException(status_code=404, detail=f"City '{city}' not found")
        raise HTTPException(status_code=500, detail='Error from server')
    except httpx.RequestError:
        raise HTTPException(status_code=500 , detail=f"Error fetching weather data")