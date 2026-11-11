# Weather API

A simple REST API built with FastAPI that provides current weather information using OpenWeather API.

## Features

- Get current weather by city name
- Handle invalid city names and return appropriate error responses.
- Handle HTTP requests error

## Technologies 

- Python
- FastAPI
- HTTPX
- OpenWeather API 

## Installation 

1. Clone the repository:

   git clone YOUR_REPOSITORY_URL

2. Navigate to the project directory:

   cd weather-api

3. Create a virtual environment:

   python -m venv venv

4. Activate the virtual environment:

   source venv/bin/activate

5. Install dependencies:

   pip install -r requirements.txt

## Environment Virtual 

Create a `.env` file in the root directory of the project.

Add your OpenWeather API key:

OPENWEATHER_API_KEY=your_api_key

## Running 
Run the following comand:

fastapi dev main.py

The API will be available at:

http://127.0.0.1:8000

## API Documentation

Interactive API documentation is available at:

http://127.0.0.1:8000/docs