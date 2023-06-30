from pydantic import BaseModel


class User(BaseModel):
    uuid: str
    type: str
    name: str
    permissions: list[str]
