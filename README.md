# Weather ETL Pipeline

An automated ETL pipeline that collects weather data for selected Polish cities from the OpenWeatherMap API and stores it in PostgreSQL.

## Project Goal

The pipeline runs on a schedule and performs a full ETL cycle:

1. **Extract** weather data from OpenWeatherMap
2. **Transform** JSON responses into a clean tabular format
3. **Load** results into a PostgreSQL table

## Architecture

### Diagram (placeholder)

> Leave this section for your future architecture image.
>
> Suggested path: `docs/architecture-diagram.png`

<!-- Insert architecture diagram here in the future, e.g.:
![Weather ETL Architecture](docs/architecture-diagram.png)
-->

### Components

- **OpenWeatherMap API** – external weather data source
- **`src/extract.py`** – fetches API data for configured cities
- **`src/transform.py`** – converts raw JSON into a pandas DataFrame and rounds numeric values
- **`src/load.py`** – creates the SQL table (if needed) and inserts rows into PostgreSQL
- **`src/pipeline.py`** – orchestrates the ETL flow and runs it on an APScheduler interval
- **`src/logger.py`** – centralized logging to console and daily log files (`logs/etl_YYYYMMDD.log`)
- **PostgreSQL 17 (Docker)** – persistent storage layer

### Cities

- Krakow
- Warsaw
- Poznan
- Wroclaw
- Gdansk
- Lublin

## Tech Stack

- Python
- pandas
- requests
- SQLAlchemy
- psycopg2
- APScheduler
- python-dotenv
- Docker / Docker Compose
- PostgreSQL

## How to Run

### Requirements

- Python 3.10+
- Docker and Docker Compose
- OpenWeatherMap API key

### 1) Create `.env` in the project root

```env
OPENWEATHER_API=your_api_key
DB_URL=postgresql://admin:admin@localhost:5432/weather_db
```

### 2) Install dependencies and start services

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
docker compose up -d
```

### 3) Run the pipeline

```bash
python src/pipeline.py
```

## SQL Table: `weather_readings`

| Column | Type | Description |
|---|---|---|
| `id` | `SERIAL PRIMARY KEY` | Unique record identifier |
| `city` | `VARCHAR(100)` | City name (e.g., `Krakow`) |
| `country` | `VARCHAR(2)` | ISO country code (e.g., `PL`) |
| `temperature` | `NUMERIC(4,1)` | Current temperature in °C |
| `feels_like` | `NUMERIC(4,1)` | Perceived temperature in °C |
| `temp_min` | `NUMERIC(4,1)` | Minimum temperature in °C |
| `temp_max` | `NUMERIC(4,1)` | Maximum temperature in °C |
| `pressure` | `SMALLINT` | Atmospheric pressure in hPa |
| `humidity` | `SMALLINT` | Relative humidity in % |
| `weather` | `VARCHAR(50)` | Main weather category (e.g., `Clouds`) |
| `weather_description` | `VARCHAR(255)` | Detailed weather description |
| `wind_speed` | `REAL` | Wind speed in m/s |
| `fetched_at` | `TIMESTAMP` | API fetch timestamp |

## Logs

- Console: `INFO` and above
- File logs: `DEBUG` and above
- Daily files: `logs/etl_YYYYMMDD.log`
