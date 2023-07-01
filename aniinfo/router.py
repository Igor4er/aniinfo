from fastapi import APIRouter, Depends, HTTPException
from aniinfo.services.anime import get_anime_by_slug
from typing import Annotated
from dto.user import User
from auth.authentication import JWTBearer
from auth.authorization import require_permission, service_users_only

router = APIRouter(prefix="/a")


@router.get("/{slug}")
async def get_anime(slug: str, user: Annotated[User, Depends(JWTBearer())]):
    anime = await get_anime_by_slug(slug)
    return anime
