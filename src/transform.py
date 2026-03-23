import pandas as pd
from logger import get_logger

logger = get_logger("transform")

def transform(raw_data: dict[str, dict]) -> pd.DataFrame:
  records = []
  logger.info(f"Starting transforming raw data for {len(raw_data)} cities")
  for city, item in raw_data.items():
    try:
      logger.debug(f"Transforming {city}")
      records.append({
        "city": item["name"],
        "country": item["sys"]["country"],
        "temperature": item["main"]["temp"],
        "feels_like": item["main"]["feels_like"],
        "temp_min": item["main"]["temp_min"],
        "temp_max": item["main"]["temp_max"],
        "pressure": item["main"]["pressure"],
        "humidity": item["main"]["humidity"],
        "weather": item["weather"][0]["main"],
        "weather_description": item["weather"][0]["description"],
        "wind_speed": item["wind"]["speed"],
        "fetched_at": item["dt"]
      })
    except Exception as e:
      logger.exception(f"Failed transforming data for {city} - {e}")
    
  df = pd.DataFrame(records)
  df["temperature"] = df["temperature"].round(1)
  df["wind_speed"] = df["wind_speed"].round(1)
  print(df)
  return df