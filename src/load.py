from sqlalchemy import create_engine, text
import pandas as pd
import os
from dotenv import load_dotenv
from logger import get_logger

logger = get_logger("load")
load_dotenv()

DB_URL = os.getenv("DB_URL", "postgresql://admin:admin@localhost:5432/weather_db")

def load(df: pd.DataFrame):
  