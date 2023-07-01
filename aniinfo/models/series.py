from tortoise import fields, models
from aniinfo.models.anime import Anime


class Series(models.Model):
    uuid = fields.UUIDField(pk=True)
    anime: fields.ForeignKeyRelation[Anime] = fields.ForeignKeyField("aniinfo.Anime", related_name="series")
    title = fields.CharField(max_length=255)
    season = fields.IntField()
    num = fields.IntField()
    source_url = fields.CharField(max_length=255)
