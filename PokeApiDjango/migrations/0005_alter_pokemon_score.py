# Generated by Django 5.0.6 on 2024-05-11 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PokeApiDjango', '0004_pokemon_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='score',
            field=models.FloatField(null=True),
        ),
    ]
