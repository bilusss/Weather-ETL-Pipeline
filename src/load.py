from sqlalchemy import create_engine, text
import pandas as pd
import os
from dotenv import load_dotenv
from logger import get_logger

logger = get_logger("load")
load_dotenv()

DB_URL = os.getenv("DB_URL", "postgresql://admin:admin@localhost:5432/weather_db")

def create_table_if_not_exists(engine):
  logger.debug(f"Trying to connect with DB")
  with engine.connect() as conn:
    conn.execute(text("""
      CREATE TABLE IF NOT EXISTS weather_readings(
        id SERIAL PRIMARY KEY,
        city VARCHAR(100),
        country VARCHAR(2),
        temperature NUMERIC(4,1),
        feels_like NUMERIC(4,1),
        temp_min NUMERIC(4,1),
        temp_max NUMERIC(4,1),
        pressure SMALLINT,
        humidity SMALLINT,
        weather VARCHAR(50),
        weather_description VARCHAR(255),
        wind_speed REAL,
        fetched_at TIMESTAMP
      )
    """))
    conn.commit()
    logger.debug(f"Made sure table is created")

def load(df: pd.DataFrame):
  engine = create_engine(DB_URL)
  create_table_if_not_exists(engine)
  df.to_sql("weather_readings", engine, if_exists="append", index=False)
  logger.info(f"Loaded {len(df)} rows to database")