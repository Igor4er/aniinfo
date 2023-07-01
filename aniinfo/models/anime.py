from tortoise import fields, models
from aniinfo.services.common import transliterate_from_uk
from aniinfo.models.genre import Genre


class Anime(models.Model):
    uuid = fields.UUIDField(pk=True)
    title = fields.CharField(max_length=255)
    year = fields.CharField(max_length=31)
    description = fields.TextField()
    image_url = fields.CharField(max_length=255)
    director = fields.CharField(max_length=63, null=True)
    studio = fields.CharField(max_length=127, null=True)
    genres: fields.ManyToManyRelation[Genre] = fields.ManyToManyField("aniinfo.Genre", related_name="animes", through="animes_genres")
    ongoing = fields.BooleanField()
