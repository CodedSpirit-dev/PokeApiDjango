from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from PokeApiDjango.models import Pokemon
from PokeApiDjango.services.services import PokemonApiService, ScoreService


@api_view(['GET'])
def fetch_pokemon_data(request, pokemon_name_or_id):
    pokemon_data = PokemonApiService.get_pokemon_data(pokemon_name_or_id)
    if pokemon_data:
        return Response(pokemon_data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Pokemon not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def save_pokemon_data_in_db(request, pokemon_name_or_id):
    pokemon_data = PokemonApiService.get_pokemon_data(pokemon_name_or_id)
    if pokemon_data:
        # Calculate score
        score = ScoreService.calculate_score(pokemon_data)

        processed_data = {
            'name': pokemon_data['name'],
            'pokemon_id': pokemon_data['pokemon_id'],
            'types': pokemon_data['types'],
            'abilities': pokemon_data['abilities'],
            'base_stats': pokemon_data['base_stats'],
            'height': pokemon_data['height'],
            'weight': pokemon_data['weight'],
            'sprite_url': pokemon_data['sprite_url'],
            'score': score
        }

        # Save pokemon in database
        pokemon = Pokemon.objects

        if pokemon.filter(pokemon_id=pokemon_data['pokemon_id']).exists():
            return Response({'error': 'Pokemon already saved'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            pokemon = Pokemon(**processed_data)
            pokemon.save()

        return Response({'message': f'Pokemon {pokemon.name} saved successfully'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': 'Pokemon not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_pokemon_data_in_db(request, pokemon_name_or_id):
    try:
        pokemon = Pokemon.objects.get(pokemon_id=pokemon_name_or_id)
    except Pokemon.DoesNotExist:
        return Response({'error': 'Pokemon not found'}, status=status.HTTP_404_NOT_FOUND)

    # Obtain the updated data
    update_data = request.data

    # Calculate score
    score = ScoreService.calculate_score(update_data)

    update_data['score'] = score

    # Update the data
    for key, value in update_data.items():
        setattr(pokemon, key, value)

    pokemon.save()

    return Response({'message': f'Pokemon {pokemon.name} updated successfully'}, status=status.HTTP_200_OK)

