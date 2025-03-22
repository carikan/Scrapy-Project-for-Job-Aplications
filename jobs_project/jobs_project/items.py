import scrapy

class JobsProjectItem(scrapy.Item):
    # Accept all dynamic fields
    def __setitem__(self, key, value):
        self.fields.setdefault(key, scrapy.Field())
        super().__setitem__(key, value)

