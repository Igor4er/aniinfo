from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from settings import settings
from router import router

app = FastAPI()

register_tortoise(
    app,
    **settings.TORTOISE_CONFIG
)

app.include_router(router)
