from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    price: float = Field(..., gt=0)
    tax: float | None = None
    
@app.get("/")
def read_root():
    return {"Hello": "World"}

# NEW FEATURE
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items/")
def create_item(item: Item):
    total = item.price + (item.tax or 0)
    return {
        "name": item.name,
        "price": item.price,
        "tax": item.tax,
        "total": total,
    }