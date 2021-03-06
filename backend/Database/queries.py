from pymongo import DESCENDING, errors

from Database.mongoDB import db_collection
from lib.config import (
    PAGINATION_LIMIT,
)

def add_video(fetched_video):
    try:
        db_collection.insert_one(fetched_video)
    except errors.DuplicateKeyError:
        print('[Database] Error: Duplicate Key', flush=True)
        pass
    print('[Databse] Saved Video', flush=True)
    
def add_videos(fetched_videos):
    try:
        db_collection.insert_many(fetched_videos)
    except errors.BulkWriteError:
        print("[Database] Error: Write failed, continuing", flush=True)
        pass

def search_videos(query, skip_count):
    if query:
        search = {
            "$text": {
                "$search": query
            },
        }
    else:
        search = {}
    
    return (
        db_collection.find(search)
        .sort("published_at", DESCENDING)
        .skip(skip_count * PAGINATION_LIMIT)
        .limit(PAGINATION_LIMIT)
    )
