from typing import Union
from fastapi import FastAPI, HTTPException
from enum import Enum

app = FastAPI()

class AvailableCuisine(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"

food_items = {
    "indian": ["samosa", "dosa"],
    "american": ["hot dog", "apple pie"],
    "italian": ["pizza", "ravioli"]
}

coupon_code = {
    1: '10%',
    2: '20%',
    3: '30%'
}

@app.get("/get_items/{cuisine}")
def get_item(cuisine: AvailableCuisine):
    # The cuisine is already validated by FastAPI using Enum
    if cuisine not in food_items:
        raise HTTPException(status_code=404, detail="Cuisine not found")
    return {"food_items": food_items[cuisine]}

@app.get("/get_coupon/{code}")
def get_coupon(code: int):
    # Handle case when coupon code is not valid
    discount = coupon_code.get(code)
    if not discount:
        raise HTTPException(status_code=404, detail="Coupon code not found")
    return {'discount_amount': discount}
