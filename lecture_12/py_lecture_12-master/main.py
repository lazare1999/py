from datetime import timedelta
from typing import List

from fastapi import FastAPI, Depends, status
from fastapi.exceptions import HTTPException
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "jonathan",
                "email": "jonathan@gmail.com",
                "password": "password"
            }
        }


class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "jonathan",
                "password": "password"
            }
        }


class Settings(BaseModel):
    authjwt_secret_key: str = '8879c30266309cff23acae1550633df9fbba4ed57dc4abebd9b72b7d331cc598'


ACCESS_TOKEN_EXPIRE_MINUTES = 1
access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)


@AuthJWT.load_config
def get_config():
    return Settings()


users = []

app = FastAPI()


@app.get("/")
def index(authorize: AuthJWT = Depends()):
    try:
        authorize.jwt_required()
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    return {"message": "Hello"}


# create a user
@app.post('/signup', status_code=201)
def create_user(user: User):
    new_user = {
        "username": user.username,
        "email": user.email,
        "password": user.password
    }

    users.append(new_user)

    return new_user


# getting all users
@app.get('/users', response_model=List[User])
def get_users(authorize: AuthJWT = Depends()):
    try:
        authorize.jwt_required()
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    return users


@app.post('/login')
def login(user: UserLogin, authorize: AuthJWT = Depends()):
    for u in users:
        if (u["username"] == user.username) and (u["password"] == user.password):
            access_token = authorize.create_access_token(subject=user.username,
                                                         expires_time=access_token_expires)
            refresh_token = authorize.create_refresh_token(subject=user.username)

            return {"access_token": access_token, "refresh_token": refresh_token}
        #            return {"access_token": access_token}

        raise HTTPException(status_code=401, detail="Invalid username or password")


@app.get('/protected')
def get_logged_in_user(authorize: AuthJWT = Depends()):
    try:
        authorize.jwt_required()
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    current_user = authorize.get_jwt_subject()

    return {"current_user": current_user}


@app.get('/new_token')
def create_new_token(authorize: AuthJWT = Depends()):
    try:
        authorize.jwt_refresh_token_required()
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    current_user = authorize.get_jwt_subject()

    access_token = authorize.create_access_token(subject=current_user,
                                                 expires_time=access_token_expires)

    return {"new_access_token": access_token}


@app.post('/fresh_login')
def fresh_login(user: UserLogin, authorize: AuthJWT = Depends()):
    for u in users:
        if (u["username"] == user.username) and (u["password"] == user.password):
            fresh_token = authorize.create_refresh_token(subject=user.username)

            return {"fresh_token": fresh_token}

        raise HTTPException(detail="Invalid Username or Password", status_code=status.HTTP_401_UNAUTHORIZED)


@app.get('/fresh_url')
def get_user(authorize: AuthJWT = Depends()):
    try:
        authorize.jwt_refresh_token_required()
    except Exception as e:
        print(str(e))
        raise HTTPException(detail="Invalid Token", status_code=status.HTTP_401_UNAUTHORIZED)

    current_user = authorize.get_jwt_subject()

    return {"current_user": current_user}
