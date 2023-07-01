from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from settings import settings
from routers.router import router
from routers.system_router import router as system_router

app = FastAPI()

register_tortoise(
    app,
    **settings.TORTOISE_CONFIG
)

app.include_router(router)
app.include_router(system_router)
