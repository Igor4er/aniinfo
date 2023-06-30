from fastapi import APIRouter, HTTPException
from aniinfo.services.anime import get_anime_by_slug

router = APIRouter(prefix="/a")


@router.get("/{slug}")
async def get_anime(slug: str):
    anime = await get_anime_by_slug(slug)
    return anime
