from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.db import items_collection, serialize_item
from bson import ObjectId

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

@app.post("/items")
def create_item(item: Item):
    result = items_collection.insert_one(item.dict())
    return {"id": str(result.inserted_id)}

@app.get("/items")
def get_items():
    items = list(items_collection.find())
    return [serialize_item(item) for item in items]

@app.get("/items/{item_id}")
def get_item(item_id: str):
    item = items_collection.find_one({"_id": ObjectId(item_id)})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return serialize_item(item)

@app.put("/items/{item_id}")
def update_item(item_id: str, item: Item):
    result = items_collection.update_one({"_id": ObjectId(item_id)}, {"$set": item.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item updated"}

@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    result = items_collection.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}
