from fastapi import FastAPI, Body, Depends

import jwt_handler
from jwt_bearer import JWTBearer
from models import PostSchema, UserSchema, UserLoginSchema

from passlib.hash import sha256_crypt

posts = [
    {
        "id": 1,
        "title": "Penguins ",
        "text": "Penguins are a group of aquatic flightless birds."
    },
    {
        "id": 2,
        "title": "Tigers ",
        "text": "Tigers are the largest living cat species and a memeber of the genus panthera."
    },
    {
        "id": 3,
        "title": "Koalas ",
        "text": "Koala is arboreal herbivorous maruspial native to Australia."
    },
]

users = []

app = FastAPI()


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and sha256_crypt.verify(data.password, user.password):
            return True
    return False


# route handlers

# testing
@app.get("/", tags=["test"])
def greet():
    return {"hello": "world!."}


# Get Posts
@app.get("/posts", tags=["posts"])
def get_posts():
    return {"data": posts}


@app.get("/posts/{id}", tags=["posts"])
def get_single_post(id: int):
    if id > len(posts):
        return {
            "error": "No such post with the supplied ID."
        }

    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }


@app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["posts"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "data": "post added."
    }


@app.post("/user/signup", tags=["user"])
def create_user(user: UserSchema = Body(...)):
    user.password = sha256_crypt.encrypt(user.password)
    users.append(user)  # replace with db call, making sure to hash the password first
    return jwt_handler.signJWT(user.email)


@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return jwt_handler.signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }