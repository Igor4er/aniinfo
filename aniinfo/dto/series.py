from tortoise.contrib.pydantic import pydantic_model_creator
from aniinfo.models.series import Series

Anime = pydantic_model_creator(Series, name="Series"
