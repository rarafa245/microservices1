from typing import Type
from pymongo import MongoClient
from .mongo_config import mongo_setting


class MongoConnectionHandlere:
    def __init__(self):
        self.__client = None
        self.database = None
        self.collection = None

    @classmethod
    def get_client(cls) -> Type[MongoClient]:
        client = MongoClient(mongo_setting["host"], mongo_setting["port"])
        return client

    def create_index_ttl(
        self, attribute: str, database: str, collection: str, ttl: int
    ) -> None:
        client = self.get_client()
        self.database = client[mongo_setting[database]]
        self.collection = self.database[mongo_setting[collection]]
        client.create_index(attribute, expireAfterSeconds=ttl)

    def __enter__(self):
        self.__client = MongoClient(mongo_setting["host"], mongo_setting["port"])
        self.database = self.__client[mongo_setting["database"]]
        self.collection = self.database[mongo_setting["collection"]]
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__client.close()  # pylint: disable=no-member
        self.__client = None
        self.database = None
        self.collection = None
