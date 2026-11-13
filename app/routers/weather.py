from fastapi import APIRouter, HTTPException
from app.service.weather_service import get_weather_data , get_weather_data_forecast , get_weather_rain_probability
import httpx 

router = APIRouter(
    prefix='/api/weather',
    tags=['weather']
)

@router.get('/current')
def get_weather(city: str | None = None):
    if not city:
        raise HTTPException(status_code=400, detail='City parameter is required')
    try:
        weather_data = get_weather_data(city)
        return weather_data
    except HTTPException as error:
        if error.status_code == 404:
            raise HTTPException(status_code=404, detail=f"City '{city}' not found")
        
        raise HTTPException(status_code=500, detail='Error from server')
    except httpx.RequestError as error:
        raise HTTPException(status_code=500, detail='Error fetching weather data')
    
@router.get('/forecast')
def get_forecast(city: str | None = None):
    if not city:
        raise HTTPException(status_code=400, detail='City parameter is not written')
    try:
        weather_forecast_data = get_weather_data_forecast(city)
        return weather_forecast_data
    except HTTPException as error:
        if error.status_code == 404:
            raise HTTPException(status_code=404, detail=f"City '{city}' not found")
        
        raise HTTPException(status_code=500, detail='Error from server')
    except httpx.RequestError as error:
        raise HTTPException(status_code=500, detail='Error fetching weather data')
    
@router.get('/rain_probability')
def get_rain_probability(city: str | None = None):
    if not city:
        raise HTTPException(status_code=400, detail='City parameter is not written')
    try:
        weather_rain_probability_data = get_weather_rain_probability(city)
        return weather_rain_probability_data
    except HTTPException as error:
        if error.status_code == 404:
            raise HTTPException(status_code=404, detail=f"City '{city}' not found")
        
        raise HTTPException(status_code=500, detail='Error from server')
    except httpx.RequestError as error:
        raise HTTPException(status_code=500, detail='Error fetching weather data')