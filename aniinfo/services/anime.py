from fastapi import HTTPException
from aniinfo.models.anime import Anime as AnimeModel
from aniinfo.dto.anime import ParsedAnime
from aniinfo.services.common import transliterate_from_uk
from aniinfo.services.genre import genres_by_parsed


async def get_anime_by_uuid(uuid: str):
    x = await AnimeModel.filter(uuid=uuid)
    if len(x) == 1:
        return x[0]
    else:
        raise HTTPException(404)


async def insert_from_parsed(anime: ParsedAnime):
    probably_slug = transliterate_from_uk(anime.title)
    genres = await genres_by_parsed(anime)
    query = await AnimeModel.update_or_create(
        title=anime.title,
        year=anime.year,
        description=anime.description,
        image_url=anime.image_url,
        director=anime.director,
        studio=anime.studio,
        ongoing=anime.ongoing,
    )
    q = query[0]
    await q.genres.clear()
    await q.genres.add(*genres)
    await q.save()
