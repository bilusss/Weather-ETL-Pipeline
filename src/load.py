from sqlalchemy import create_engine, text
import pandas as pd
import os
from dotenv import load_dotenv
from logger import get_logger

logger = get_logger("load")
load_dotenv()

