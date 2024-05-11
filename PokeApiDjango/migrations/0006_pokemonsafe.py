# Generated by Django 5.0.6 on 2024-05-11 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PokeApiDjango', '0005_alter_pokemon_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonSafe',
            fields=[
                ('pokemon_id', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('types', models.JSONField()),
                ('abilities', models.JSONField()),
                ('base_stats', models.JSONField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('sprite_url', models.URLField()),
                ('score', models.FloatField(null=True)),
            ],
        ),
    ]
