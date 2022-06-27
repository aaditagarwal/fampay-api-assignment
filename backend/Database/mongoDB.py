from lib.config import (
    MONGODB_URI,
    MONGODB_DATABASE,
    MONGODB_COLLECTION
)
from pymongo import MongoClient

client = MongoClient(MONGODB_URI)
database = client[MONGODB_DATABASE]

db_collection = database.get_collection(MONGODB_COLLECTION)

#Indexing
db_collection.create_index(
    [
        ("title", 'text'),
        ("description", 'text')
    ]
)