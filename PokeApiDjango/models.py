from django.db import models
import uuid


class Pokemon(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    pokemon_id = models.IntegerField(unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    types = models.JSONField()
    abilities = models.JSONField()
    base_stats = models.JSONField()
    height = models.IntegerField()
    weight = models.IntegerField()
    sprite_url = models.URLField()
    score = models.FloatField(null=True)

    def __str__(self):
        return self.name
        pass
