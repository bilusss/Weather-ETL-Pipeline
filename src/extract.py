import requests
import os
from dotenv import load_dotenv
from logger import get_logger

load_dotenv()

CITIES = ["Krakow", "Warsaw", "Poznan", "Wroclaw", "Gdansk", "Lublin"]
API_KEY = os.getenv("OPENWEATHER_API")

def fetch_weather(city: str) -> dict:
  """metric = Celsius"""
  url = "https://api.openweathermap.org/data/2.5/weather"
  params = {"q": city, "appid": API_KEY, "units": "metric"}
  response = requests.get(url, params=params, timeout=10)
  response.raise_for_status()
  return response.json()

def extract_all() -> list[dict]:
  results = []
  for city in CITIES:
    try:
      data = fetch_weather(city)
      results.append(data)
      print(f"Fetched correctly {city}")
    except Exception as e:
      print(f"Failed fetching {city} - {e}")
  return results