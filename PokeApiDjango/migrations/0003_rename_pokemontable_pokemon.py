# Generated by Django 5.0.6 on 2024-05-11 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PokeApiDjango', '0002_remove_pokemontable_id_alter_pokemontable_pokemon_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PokemonTable',
            new_name='Pokemon',
        ),
    ]