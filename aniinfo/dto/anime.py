from tortoise.contrib.pydantic import pydantic_model_creator
from aniinfo.models.anime import Anime

Anime = pydantic_model_creator(Anime, name="Anime")
