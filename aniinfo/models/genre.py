from tortoise import fields, models
from transliterate import translit


class Genre(models.Model):
    slug = fields.CharField(max_length=255, pk=True)
    name = fields.CharField(max_length=255)
    
    def __init__(self, **kwargs) -> None:
        if kwargs.get("pk", False):
            if "default" not in kwargs:
                kwargs["slug"] = translit(self.name, "uk")
        super().__init__(**kwargs)
