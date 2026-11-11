from fastapi import APIRouter, HTTPException
from app.service.weather_service import get_weather_data
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
    