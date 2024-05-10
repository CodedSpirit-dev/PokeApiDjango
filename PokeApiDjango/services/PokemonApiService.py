from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests
from PokeApiDjango.models import PokemonTable


class PokemonApiService:
    @staticmethod
    def get_pokemon_data(pokemon_name_or_id):
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name_or_id}/'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @staticmethod
    def process_pokemon_data(pokemon_data):
        processed_data = {
            'name': pokemon_data['name'],
            'pokemon_id': pokemon_data['id'],
            'types': [type_data['type']['name'] for type_data in pokemon_data['types']],
            'abilities': [ability_data['ability']['name'] for ability_data in pokemon_data['abilities']],
            'base_stats': {
                'hp': next((stat['base_stat'] for stat in pokemon_data['stats'] if stat['stat']['name'] == 'hp'), 0),
                'attack': next((stat['base_stat'] for stat in pokemon_data['stats'] if stat['stat']['name'] == 'attack'), 0),
                'defense': next((stat['base_stat'] for stat in pokemon_data['stats'] if stat['stat']['name'] == 'defense'), 0),
                'special_attack': next((stat['base_stat'] for stat in pokemon_data['stats'] if stat['stat']['name'] == 'special-attack'), 0),
                'special_defense': next((stat['base_stat'] for stat in pokemon_data['stats'] if stat['stat']['name'] == 'special-defense'), 0),
                'speed': next((stat['base_stat'] for stat in pokemon_data['stats'] if stat['stat']['name'] == 'speed'), 0),
            },
            'height': pokemon_data['height'],
            'weight': pokemon_data['weight'],
            'sprite_url': pokemon_data['sprites']['front_default']
        }
        return processed_data
