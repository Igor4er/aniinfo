from tortoise.contrib.pydantic import pydantic_model_creator
from aniinfo.models.anime import Anime
from pydantic import BaseModel

Anime = pydantic_model_creator(Anime, name="Anime")


class ParsedAnime(BaseModel):
    url: str
    title: str
    year: str
    description: str
    image_url: str
    director: str | None
    studio: str | None
    genres: list[str]
    series: list | None
    ongoing: bool
