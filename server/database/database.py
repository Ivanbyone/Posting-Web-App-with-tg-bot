import datetime

from pymongo import MongoClient
from config.config import DB_NAME, DB_URL


client = MongoClient(DB_URL)
database = client[DB_NAME]
posts_collection = database.posts


def send_post_to_mongo(post: str) -> int:
    post = {
        "post_id": posts_collection.count_documents({})+1,
        "post": post,
        "date": str(datetime.datetime.now()),
        "liked": 0,
        "disliked": 0
    }

    posts_collection.insert_one(post)

    return post["post_id"]


def show_post_from_mongo(id: int):
    
    return dict(posts_collection.find_one({"post_id": id}))
    