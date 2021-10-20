import time
from typing import Dict

import jwt

secret=please_please_update_me_please
algorithm=HS256


def token_response(token: str):
    return {
        "access_token": token
    }

def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, secret, algorithm=algorithm)

    return token_response(token)

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, secret, algorithms=[algorithm])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}