from fastapi import FastAPI, HTTPException
from app.models import Item, UpdateItem
from app.db import items_collection, serialize_item
from bson.objectid import ObjectId

app = FastAPI()

@app.post("/items")
def create_item(item: Item):
    result = items_collection.insert_one(item.dict())
    return {"id": str(result.inserted_id)}

@app.get("/items")
def get_all_items():
    return [serialize_item(i) for i in items_collection.find()]

@app.get("/items/{item_id}")
def get_item(item_id: str):
    item = items_collection.find_one({"_id": ObjectId(item_id)})
    if item:
        return serialize_item(item)
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}")
def update_item(item_id: str, item: UpdateItem):
    result = items_collection.update_one({"_id": ObjectId(item_id)}, {"$set": item.dict(exclude_unset=True)})
    if result.modified_count == 1:
        return {"message": "Item updated"}
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    result = items_collection.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count == 1:
        return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
