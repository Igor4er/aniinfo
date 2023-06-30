from tortoise.contrib.pydantic import pydantic_model_creator
from aniinfo.models.genre import Genre

Anime = pydantic_model_creator(Genre, name="Genre")
