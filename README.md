# jobs_project

A containerized Scrapy pipeline for parsing job data from JSON files and storing it in MongoDB. 

## Setup Instructions

### 1. Prerequisites
- Docker & Docker Compose installed
- Python 3.12

### 3. Build & Run the Containers
```bash
docker-compose up --build
```

## Run Spider Manually
# run the spider from within the container:

```bash
docker exec -it scrapy_container bash # enter scrapy container
cd jobs_project
scrapy crawl json_spider
```

## Export Data to CSV
To extract all jobs into a CSV file:

```bash
docker exec -it scrapy_container bash
cd jobs_project
python3 jobs_project/query.py
```

Output: `final_jobs.csv`



