from fastapi import HTTPException
from aniinfo.models.anime import Anime as AnimeModel


async def get_anime_by_slug(slug: str):
    x = await AnimeModel.filter(slug=slug)
    if len(x) == 1:
        return x[0]
    else:
        raise HTTPException(404)
