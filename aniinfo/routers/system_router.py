from fastapi import APIRouter, Depends
from aniinfo.auth.authentication import JWTBearer
from aniinfo.auth.authorization import require_permission, service_users_only
from typing import Annotated
from aniinfo.dto.user import User
from aniinfo.dto.anime import ParsedAnime
from aniinfo.services.anime import insert_from_parsed

router = APIRouter(prefix="/system")


@router.post("/insert_diff")
@service_users_only
@require_permission("diff_anime")
async def insert_diff(animes: list[ParsedAnime], user: Annotated[User, Depends(JWTBearer())]):
    print(len(animes))
    for anime in animes:
        await insert_from_parsed(anime)
    return {"ok": True}
