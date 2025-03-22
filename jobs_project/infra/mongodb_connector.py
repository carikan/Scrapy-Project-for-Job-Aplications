from pymongo import MongoClient
import os

class MongoDBConnector:
    def __init__(self):
        # self.uri = os.getenv("MONGO_URI", "mongodb://mongodb:27017")
        self.uri = os.getenv("MONGO_URI", "mongodb://localhost:27017" if os.getenv("RUNNING_LOCALLY") else "mongodb://mongodb:27017")

        self.db_name = os.getenv("MONGO_DB", "scrapy_db")
        self.client = MongoClient(self.uri)
        self.db = self.client[self.db_name]
        self.collection = self.db["items"]

    def insert_item(self, item):
        if item:
            self.collection.insert_one(dict(item))

    def find_all(self):
        return list(self.collection.find())
