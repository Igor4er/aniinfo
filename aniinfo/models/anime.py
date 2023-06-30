from tortoise import fields, models
from transliterate import translit


class Anime(models.Model):
    slug = fields.CharField(max_length=255, pk=True)
    title = fields.CharField(max_length=255)
    year = fields.CharField(max_length=4)
    description = fields.TextField()
    image_url = fields.CharField(max_length=255)
    director = fields.CharField(max_length=63)
    studio = fields.CharField(max_length=127)
    genres = fields.relational.ManyToManyField(model_name="aniinfo.Genre")
    ongoing = fields.BooleanField()

    def __init__(self, **kwargs) -> None:
        if kwargs.get("pk", False):
            if "slug" not in kwargs:
                kwargs["slug"] = translit(self.title, "uk")
        super().__init__(**kwargs)
