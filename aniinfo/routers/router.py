from fastapi import APIRouter, Depends, HTTPException
from aniinfo.services.anime import get_anime_by_uuid


router = APIRouter(prefix="/a")


@router.get("/{uuid}")
async def get_anime(uuid: str):
    anime = await get_anime_by_uuid(uuid)
    return anime
