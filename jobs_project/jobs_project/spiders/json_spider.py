import scrapy
import json
import os
from jobs_project.items import JobsProjectItem


class JsonSpider(scrapy.Spider):
    name = "json_spider"

    def start_requests(self):
        # Define the data directory
        base_path = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.normpath(os.path.join(base_path, "..", "data"))
        
        # JSON files to read
        filenames = ["s01.json", "s02.json"]

        # Yield a Scrapy request for each file
        for filename in filenames:
            file_path = os.path.join(data_dir, filename)
            if os.path.exists(file_path):
                self.logger.info(f"Reading file: {file_path}")
                yield scrapy.Request(
                    url=f"file://{file_path}",
                    callback=self.parse,
                    dont_filter=True
                )
            else:
                self.logger.warning(f"File not found: {file_path}")

    def parse(self, response):
        try:
            data = json.loads(response.body)
        except json.JSONDecodeError:
            self.logger.error(f"Failed to decode JSON from {response.url}")
            return

        jobs = data.get("jobs", [])

        for job in jobs:
            item = JobsProjectItem()
            item.update(job)  # Will dynamically assign all fields
            yield item
