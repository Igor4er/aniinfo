from pydantic import BaseSettings
from dotenv import load_dotenv


class Settings(BaseSettings):
    TORTOISE_CONFIG = {
        "config": {
            "connections": {
                "default": {
                    "engine": "tortoise.backends.sqlite",
                    "credentials": {"file_path": "db.sqlite3"},
                }
            },
            "apps": {
                "aniinfo": {"models": ["aniinfo.models"], "default_connection": "default"}
            },
        },
        "modules": {"models": ["aniinfo.models"]},
        "generate_schemas": True,
        "add_exception_handlers": True,
    }
    
    JWT_ALGORITHM = "HS512"
    JWT_SECRET = "SECRET_KEY"

    class Config:
        env_prefix: str = "ANIINFO_"


load_dotenv()
settings = Settings()
# print(settings)
