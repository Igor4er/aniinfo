from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException
from jose import jwt, JWTError
from aniinfo.settings import settings
from aniinfo.dto.user import User
import time


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)
    
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(self, request=request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(401, detail="Wrong auth sceme")
            user_dict = user_dict_if_valid(credentials.credentials)
            if user_dict is None:
                raise HTTPException(401, detail="Corrupted or expired token")
            try:
                user = User(**user_dict)
            except:
                raise HTTPException(401, detail="Secret key was stolen or developer is idiot")
            return user
        else:
            raise HTTPException(401, detail="Invalid token")


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
        "permissions": ["default", "diff_anime"]
    }
    edt = jwt.encode(dt, secret_key, algorithm=settings.JWT_ALGORITHM)
    print(edt)
