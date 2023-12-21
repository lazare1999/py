# This file is responsible for signing , encoding , decoding and returning JWTS
import time
from typing import Dict
import jwt
from decouple import config

# secret =79a35fd3c86e3a28c6bb859e856f1c000e87945f81467926ec132f7289abe8e0

# algorithm = HS256

JWT_SECRET = config("SECRET")
JWT_ALGORITHM = config("ALGORITHM")


def token_response(token: str):
    return {
        "access_token": token
    }


# function used for signing the JWT string
def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except Exception as e:
        print(str(e))
        return {}


print(signJWT("lazarekvirtia@gmail.com"))
print(decodeJWT(signJWT("lazarekvirtia@gmail.com")['access_token']))
