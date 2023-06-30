from tortoise import fields, models


class Series(models.Model):
    uuid = fields.UUIDField(pk=True)
    anime = fields.relational.ForeignKeyField(model_name="aniinfo.Anime")
    title = fields.CharField(max_length=255)
    season = fields.IntField()
    num = fields.IntField()
    source_url = fields.CharField(max_length=255)
