from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://host.docker.internal:27017/")  # Works inside Docker on Windows
db = client["crud_db"]
items_collection = db["items"]

def serialize_item(item):
    item["_id"] = str(item["_id"])
    return item
