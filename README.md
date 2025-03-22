# jobs_project

A containerized Scrapy pipeline for parsing job data from JSON files and storing it in MongoDB. Designed for modularity, reusability, and ease of use.

## Project Structure

```
canaria_project/
├── docker-compose.yaml
├── Dockerfile
├── .env
├── jobs_project/
│   ├── __init__.py
│   ├── items.py
│   ├── pipelines.py
│   ├── query.py
│   ├── settings.py
│   ├── spiders/
│   │   ├── __init__.py
│   │   └── json_spider.py
├── infra/
│   ├── __init__.py
│   └── mongodb_connector.py
├── data/
│   ├── s01.json
│   └── s02.json
└── final_jobs.csv
```

## Setup Instructions

### 1. Prerequisites
- Docker & Docker Compose installed
- Python 3.12 (for running local utilities like `query.py`)
- VS Code with Dev Containers support (optional but helpful)

### 2. Environment Variables
Create a `.env` file at the root of the project:

```ini
MONGO_URI=mongodb://mongodb:27017
MONGO_DATABASE=scrapy_db
```

Or ensure `docker-compose.yaml` sets these variables.

### 3. Build & Run the Containers
```bash
docker-compose up --build
```

This will:
- Start MongoDB
- Start the Scrapy spider container that processes `s01.json` and `s02.json`
- Store job data in the `scrapy_db.items` collection

## Run Spider Manually
If you want to run the spider from within the container:

```bash
docker exec -it jobs_spider_container bash
scrapy crawl json_spider
```

## Export Data to CSV
To extract all jobs into a CSV file:

```bash
# Activate virtual environment
source .venv/bin/activate
python3 jobs_project/query.py
```

Output: `final_jobs.csv`

## Notes
- JSON files should live in `jobs_project/data/`
- All job entries are under the `jobs` key in each JSON file
- The `MongoDBPipeline` handles deduplication and insertion
- MongoDB database: `scrapy_db`, collection: `items`

## Features
- Reads local JSON files and parses job data
- Stores structured items in MongoDB
- Exports stored data to a CSV file
- Easily extendable to support Redis deduplication
- Organized codebase for maintainability



