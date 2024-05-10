from django.db import models
import uuid


class Pokemon(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    pokemon_id = models.IntegerField(unique=True)
    types = models.JSONField()
    abilities = models.JSONField()
    base_stats = models.JSONField()
    height = models.IntegerField()
    weight = models.IntegerField()
    sprite_url = models.URLField()

    def __str__(self):
        return self.name
