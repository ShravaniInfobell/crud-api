import mongomock
from bson.objectid import ObjectId

client = mongomock.MongoClient()
db = client["crud_db"]
items_collection = db["items"]

def serialize_item(item):
    item["_id"] = str(item["_id"])
    return item
