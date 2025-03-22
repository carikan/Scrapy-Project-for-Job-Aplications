# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class JobsProjectItem(scrapy.Item):
    # Accept all dynamic fields
    def __setitem__(self, key, value):
        self.fields.setdefault(key, scrapy.Field())
        super().__setitem__(key, value)

