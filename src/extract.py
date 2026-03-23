import requests
import os
from dotenv import load_dotenv
from logger import get_logger

load_dotenv()
logger = get_logger("extract")

CITIES = ["Krakow", "Warsaw", "Poznan", "Wroclaw", "Gdansk", "Lublin"]
API_KEY = os.getenv("OPENWEATHER_API")

def fetch_weather(city: str) -> dict:
  """metric = Celsius"""
  url = "https://api.openweathermap.org/data/2.5/weather"
  params = {"q": city, "appid": API_KEY, "units": "metric"}
  logger.debug(f"Sending request for {city}")
  response = requests.get(url, params=params, timeout=10)
  response.raise_for_status()
  return response.json()

def extract_all() -> dict[str, dict]:
  logger.info(f"Starting extracting for {len(CITIES)} cities")
  results = {}
  for city in CITIES:
    try:
      data = fetch_weather(city)
      results[city] = data
      logger.info(f"{city} - {data['main']['temp']} °C")
    except requests.exceptions.Timeout:
      logger.warning(f"Timeout for {city} - skipping")
    except requests.exceptions.HTTPError as e:
      logger.error(f"HTTP error for {city}: {e.response.status_code}")
    except Exception as e:
      logger.exception(f"Unexpected error when fetching {city} - {e}")
    
    logger.info(f"Extraction done: {len(results)}/{len(CITIES)} successful")
  return results