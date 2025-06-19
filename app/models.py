from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    name: str = Field(..., example="Laptop")
    description: Optional[str] = Field(None, example="Gaming Laptop")
    price: float = Field(..., gt=0, example=1499.99)

class UpdateItem(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
