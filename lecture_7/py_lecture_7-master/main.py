from typing import Optional
from typing import Union
from enum import Enum

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# items
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.get("/items_q/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=5)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


# items

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# payments
class Payment(BaseModel):
    date: str
    amount: float
    ReceiverAcc: str
    description: Optional[str] = None


Payments = {}


@app.get("/payments")
def read_payments():
    return Payments


@app.get("/payments/{payment_id}")
def read_payment(payment_id: int):
    return Payments.get(payment_id)


@app.put("/payments/{payment_id}")
def update_payment(payment_id: int, payment: Payment):
    Payments[payment_id] = payment.dict()
    return payment.dict()


@app.delete("/payments/{payment_id}")
def delete_payment(payment_id: int):
    if Payments[payment_id]:
        Payments.pop(payment_id)
        return {"ok": True}
    return {"ok": False}


@app.post("/payments")
async def payments():
    return Payments
# payments
