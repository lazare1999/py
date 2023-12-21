from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel

app = FastAPI()

redis = get_redis_connection(
    host="redis-11124.c250.eu-central-1-1.ec2.cloud.redislabs.com",
    port=11124,
    password="CEmnGutHWpI4JGwrScfnfQz8U7qi8yel",
    decode_responses=True
)


class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis


@app.post('/products')
def create(product: Product):
    return product.save()


@app.get('/products/{pk}')
def get(pk: str):
    try:
        return Product.get(pk)
    except Exception as e:
        print(str(e))
        return []


@app.get('/products')
def all_products():
    return [format_pr(pk) for pk in Product.all_pks()]


def format_pr(pk: str):
    product = Product.get(pk)

    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity
    }


@app.delete('/products/{pk}')
def delete(pk: str):
    return Product.delete(pk)


@app.put('products/{pk}/{q}')
def change(pk: str, q: int):
    product = Product.get(pk)
    product.quantity = q
    return product.save()
