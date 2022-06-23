from lib.config import (
    MONGODB_URI,
    MONGODB_DATABASE,
    MONGODB_COLLECTION
)
from pymongo import MongoClient, DESCENDING

client = MongoClient(MONGODB_URI)
database = client[MONGODB_DATABASE]

db_collection = database.get_collection(MONGODB_COLLECTION)

#Indexing
db_collection.create_index(
    [
        ("title", DESCENDING),
        ("description", DESCENDING)
    ]
)