# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapy.exceptions import DropItem

class MongoDbPipeline(object):
    collection = ''

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri # obtained from settings.py
        self.mongo_db = mongo_db # obtained from settings.py

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.collection = spider.collection

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if self.db[self.collection].count_documents({'$and': [
            {'date': item.get('date')},
            {'team_away_city': item.get('team_away_city')},
            {'team_away_name': item.get('team_away_name')},
            {'team_away_score': item.get('team_away_score')},
            {'team_home_city': item.get('team_home_city')},
            {'team_home_name': item.get('team_home_name')},
            {'team_home_score': item.get('team_home_score')}
            ]
            }
            ) == 1:
            raise DropItem("Item dropped")

        else:
            self.db[self.collection].insert_one(dict(item))
            return item
