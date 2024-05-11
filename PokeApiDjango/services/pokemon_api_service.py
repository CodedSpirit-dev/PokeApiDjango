from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests
from ..models import Pokemon
from .score_service import ScoreService


def process_pokemon_data(pokemon_data):
    return {
        'name': pokemon_data['name'],
        'pokemon_id': pokemon_data['id'],  # Cambiado a pokemon_id
        'types': [type_data['type']['name'] for type_data in pokemon_data['types']],
        'abilities': [ability_data['ability']['name'] for ability_data in pokemon_data['abilities']],
        'base_stats': {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']},
        'height': pokemon_data['height'],
        'weight': pokemon_data['weight'],
        'sprite_url': pokemon_data['sprites']['front_default']
    }


@api_view(['GET'])
def fetch_all_pokemon_data(request):
    url = 'https://pokeapi.co/api/v2/pokemon/?limit=10277&offset=10127'
    response = requests.get(url)
    data = response.json()

    # Paso 1 y 2: Obtener y procesar los datos de todos los Pokémon
    for pokemon in data['results']:
        pokemon_data = requests.get(pokemon['url']).json()
        processed_data = process_pokemon_data(pokemon_data)

        # Paso 3: Guardar o actualizar cada Pokémon en la base de datos sin el puntaje
        Pokemon.objects.update_or_create(name=processed_data['name'], defaults=processed_data)

    # Paso 4 y 5: Calcular el puntaje para cada Pokémon y actualizar el registro en la base de datos
    for pokemon in Pokemon.objects.all():
        pokemon_data = {
            'name': pokemon.name,
            'types': pokemon.types,
            'abilities': pokemon.abilities,
            'base_stats': pokemon.base_stats,
            'height': pokemon.height,
            'weight': pokemon.weight
        }
        score = ScoreService.calculate_score(pokemon_data)
        pokemon.score = score
        pokemon.save()

    return Response({'message': 'Pokemons fetched, scored, and saved successfully'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def fetch_pokemon_data(request):
    pokemon_id = request.query_params.get('pokemon_id')  # Obtener pokemon_id de query_params
    if not pokemon_id:
        return Response({'error': 'pokemon_id is required'}, status=status.HTTP_400_BAD_REQUEST)

    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        processed_data = process_pokemon_data(pokemon_data)
        Pokemon.objects.update_or_create(pokemon_id=processed_data['pokemon_id'], defaults=processed_data)
        return Response({'message': f'Pokemon {processed_data["name"]} added successfully'},
                        status=status.HTTP_201_CREATED)
    else:
        return Response({'error': 'Failed to fetch pokemon data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
