from aniinfo.dto.user import User
from fastapi import HTTPException
from functools import wraps


def is_service(user: User):
    if user.type == "service":
        return True
    return False


def user_permitted(user: User, permission_name: str):
    if permission_name in user.permissions:
        return True
    return False


def require_permission(permission_name: str):
    def decorator_func(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            user: User = kwargs["user"]
            if not user_permitted(user, permission_name):
                raise HTTPException(403, detail="Not Permitted")
            return await func(*args, **kwargs)
        return wrapper
    return decorator_func


def service_users_only(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        user: User = kwargs["user"]
        if user.type != "service":
            raise HTTPException(403, detail="Only service users allowed")
        return await func(*args, **kwargs)
    return wrapper

# user: Annotated[User, Depends(JWTBearer())]
