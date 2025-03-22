from infra.mongodb_connector import MongoDBConnector

class MongoDBPipeline:
    def __init__(self):
        self.mongo = MongoDBConnector()

    def process_item(self, item, spider):
        self.mongo.insert_item(item)
        return item
