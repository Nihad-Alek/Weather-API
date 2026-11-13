# Weather API

A REST API built with FastAPI that provides current weather information and weather forecasts using the OpenWeather API.

## Features

- Get current weather by city name.
- Retrieve weather forecasts.
- Get forecast information for different time periods.
- Handle invalid city names.
- Handle HTTP request errors.
- Return structured JSON responses.

## Technologies 

- Python
- FastAPI
- HTTPX
- OpenWeather API
- python-dotenv

## Standard Library:
- datetime — Used for working with dates and times, such as determining the day of the week.
- os — Used for interacting with environment variables and the operating system.

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