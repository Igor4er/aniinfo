from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException
from jose import jwt, JWTError
from pydantic import ValidationError

from aniinfo.settings import settings
from aniinfo.dto.user import User
import time


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)
    
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request=request)
        if credentials:
            if credentials.scheme != "Bearer":
                raise HTTPException(401, detail="Wrong auth sceme")
            user_dict = user_dict_if_valid(credentials.credentials)
            
            if user_dict is None:
                raise HTTPException(401, detail="Corrupted or expired token")
            return user_from_dict(user_dict)
        else:
            raise HTTPException(401, detail="Unset token")


def user_from_dict(user_dict: dict):
    try:
        user = User(**user_dict)
    except ValidationError:
        raise HTTPException(401, detail="Secret key was stolen or developer is idiot")
    return user
    

def user_dict_if_valid(token: str) -> dict | None:
    try:
        decoded = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        if int(decoded["expires"]) > int(time.time()):
            return decoded
    except:
        return None
    return None
        

if __name__ == "__main__":
    # Test token generator
    secret_key = input("Paste secret_key:")
    dt = {
        "uuid": "29670cf1-9738-4b58-b04b-7c73e829afc4",
        "type": "service",
        "name": "test_service",
        "expires": int(time.time()) + 30 * 60,
        "permissions": ["default", "diff_anime"]
    }
    edt = jwt.encode(dt, secret_key, algorithm=settings.JWT_ALGORITHM)
    print(edt)
