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
        tok = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        if int(tok["expires"]) > int(time.time()):
            return tok
    except:
        return None
    return None
        
