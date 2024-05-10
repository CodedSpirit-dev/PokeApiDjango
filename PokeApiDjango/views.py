from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests
from .models import PokemonTable

@api_view(['GET'])
def fetch_pokemon_data(request):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    pokemon_id = request.data.get('pokemon_id')

    if not pokemon_id:
        return Response({'error': 'pokemon_id is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        response = requests.get(f'{url}{pokemon_id}/')
        data = response.json()

        pokemon = PokemonTable(
            name=data['name'],
            pokemon_id=data['id'],
            types=[type_data['type']['name'] for type_data in data['types']],
            abilities=[ability_data['ability']['name'] for ability_data in data['abilities']],
            base_stats={
                'hp': next((stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'hp'), 0),
                'attack': next((stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'attack'), 0),
                'defense': next((stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'defense'), 0),
                'special-attack': next((stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'special-attack'), 0),
                'special-defense': next((stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'special-defense'), 0),
                'speed': next((stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'speed'), 0),
            },
            height=data['height'],
            weight=data['weight'],
            sprite_url=data['sprites']['front_default']
        )

        # Save the pokemon object to the database
        pokemon.save()
        return Response({'message': f'Pokemon {pokemon.name} added successfully'}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
