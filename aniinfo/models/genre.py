from tortoise import fields, models
from transliterate import translit
from aniinfo.services.common import transliterate_from_uk


class Genre(models.Model):
    uuid = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=255)

