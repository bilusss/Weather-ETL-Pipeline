# Weather-ETL-Pipeline

Create .env file in main directory and 
insert api keys from openweather website
example:
```
OPENWEATHER_API=XXXXX
DB_URL=postgresql://admin:admin@localhost:5432/weather_db
```


then run those commands:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
docker compose up -d
python src/pipeline.py
```

