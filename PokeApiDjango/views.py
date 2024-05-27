from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from PokeApiDjango.models import Pokemon
from PokeApiDjango.services.services import PokemonApiService, ScoreService


@api_view(['GET'])
def fetch_pokemon_data(request, pokemon_name_or_id):
    """
    Fetches data for a specified Pokemon by name or ID from an external API, calculates its score,
    and returns a simplified set of data to the front end. If the Pokemon already exists in the database,
    it returns the existing data instead of fetching from the external API again.

    Args:
        request: The HTTP request object.
        pokemon_name_or_id: The name or ID of the Pokemon to fetch.

    Returns:
        A Response object containing the Pokemon's name, ID, types, and score.
    """
    # Initialize data_to_show
    data_to_show = {}

    if pokemon_name_or_id.isdigit():
        # Convert to integer
        pokemon_id = int(pokemon_name_or_id)
        # Attempt to fetch the Pokemon by ID
        existing_pokemon = Pokemon.objects.filter(pokemon_id=pokemon_id).first()
    else:
        # Attempt to fetch the Pokemon by name
        existing_pokemon = Pokemon.objects.filter(name__iexact=pokemon_name_or_id).first()

    if existing_pokemon:
        # Prepare data to return if the Pokemon exists
        data_to_show = {
            'name': existing_pokemon.name,
            'pokemon_id': existing_pokemon.pokemon_id,
            'types': existing_pokemon.types,
            'score': existing_pokemon.score,
            'sprite_url': existing_pokemon.sprite_url
        }
    else:
        # Fetch new Pokemon data from the external API if it doesn't exist in the database
        pokemon_data = PokemonApiService.get_pokemon_data(pokemon_name_or_id)
        if not pokemon_data:
            return Response({'error': 'Pokemon not found in the API'}, status=status.HTTP_404_NOT_FOUND)

        score = ScoreService.calculate_score(pokemon_data)

        # Prepare the data to be saved in the database
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

        # Save the new Pokemon data in the database
        pokemon = Pokemon(**processed_data)
        pokemon.save()

        # Prepare data to return for the new Pokemon
        data_to_show = {
            'name': pokemon_data['name'],
            'pokemon_id': pokemon_data['pokemon_id'],
            'types': pokemon_data['types'],
            'score': score,
            'sprite_url': pokemon_data['sprite_url']
        }

    return Response(data_to_show, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_custom_pokemon_data(request):
    """
    Add custom Pokemon data to the database.
    If the Pokemon already exists in the database, return the existing data.

    Args:
        request: The request object.

    Returns:
        A Response object with the Pokemon data or an error message.
    """
    last_official_pokemon_id = 10277
    num_custom_pokemon = Pokemon.objects.filter(pokemon_id__gt=last_official_pokemon_id).count()
    new_pokemon_id = last_official_pokemon_id + num_custom_pokemon + 1

    # Obtener los datos del Pokemon del cuerpo de la solicitud
    pokemon_data = request.data

    # Personalizar el nombre del Pokemon si se proporciona en la solicitud, de lo contrario, utilizar 'Custom'
    if 'name' in pokemon_data:
        name = pokemon_data['name']
    else:
        name = f'Custom{num_custom_pokemon + 1}'

    # Completar los datos del nuevo Pokemon
    pokemon_data.update({
        'name': name,
        'pokemon_id': new_pokemon_id,
        'sprite_url': pokemon_data.get('sprite_url',
                                       'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png')
    })

    # Calcular el puntaje
    score = ScoreService.calculate_score(pokemon_data)
    pokemon_data['score'] = score

    # Guardar los datos en la base de datos
    if Pokemon.objects.filter(pokemon_id=pokemon_data['pokemon_id']).exists():
        pokemon = Pokemon.objects.get(pokemon_id=pokemon_data['pokemon_id'])
        pokemon_data = {
            'unique_id': pokemon.unique_id,
            'name': pokemon.name,
            'pokemon_id': pokemon.pokemon_id,
            'types': pokemon.types,
            'abilities': pokemon.abilities,
            'base_stats': pokemon.base_stats,
            'height': pokemon.height,
            'weight': pokemon.weight,
            'sprite_url': pokemon.sprite_url,
            'score': pokemon.score
        }

        return Response({'pokemon_data': pokemon_data, 'error': 'Pokemon already exists in the database'},
                        status=status.HTTP_400_BAD_REQUEST)
    else:
        pokemon = Pokemon(**pokemon_data)
        pokemon.save()
        return Response(pokemon_data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_pokemon_data_in_db(request, pokemon_name_or_id):
    try:
        pokemon = Pokemon.objects.get(pokemon_id=pokemon_name_or_id)
    except Pokemon.DoesNotExist:
        return Response({'error': 'Pokemon not found'}, status=status.HTTP_404_NOT_FOUND)

    update_data = request.data
    score = ScoreService.calculate_score(update_data)
    update_data['score'] = score

    for key, value in update_data.items():
        setattr(pokemon, key, value)

    pokemon.save()

    return Response({'message': f'Pokemon {pokemon.name} updated successfully'}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_pokemon_data_in_db(request, pokemon_name_or_id):
    try:
        # Verify if the input is a number or a string
        if pokemon_name_or_id.isdigit():
            # If it is a number, search by id
            pokemon = Pokemon.objects.get(pokemon_id=pokemon_name_or_id)
        else:
            # If it is a string, search by name, and filter by the first result
            pokemon = Pokemon.objects.filter(name__iexact=pokemon_name_or_id).first()
    except Pokemon.DoesNotExist:
        return Response({'error': 'Pokemon not found'}, status=status.HTTP_404_NOT_FOUND)

    pokemon.delete()

    return Response({'message': f'The pokemon {pokemon_name_or_id} with id {pokemon.pokemon_id} was deleted'},
                    status=status.HTTP_200_OK)


@api_view(['GET'])
def get_pokemon_data_from_db(request, pokemon_name_or_id):
    try:
        if pokemon_name_or_id.isdigit():
            pokemon = Pokemon.objects.get(pokemon_id=pokemon_name_or_id)
        else:
            # If it is a string, search by name, and filter by the first result
            pokemon = Pokemon.objects.filter(name__iexact=pokemon_name_or_id).first()
    except Pokemon.DoesNotExist:
        return Response({'error': 'Pokemon not found'}, status=status.HTTP_404_NOT_FOUND)

    pokemon_data = {
        'name': pokemon.name,
        'pokemon_id': pokemon.pokemon_id,
        'types': pokemon.types,
        'abilities': pokemon.abilities,
        'base_stats': pokemon.base_stats,
        'height': pokemon.height,
        'weight': pokemon.weight,
        'sprite_url': pokemon.sprite_url,
        'score': pokemon.score
    }

    return Response(pokemon_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_list_of_pokemon_saved_in_db(request):
    pokemons = Pokemon.objects.all()
    pokemons_data = []
    for pokemon in pokemons:
        pokemon_data = {
            'name': pokemon.name,
            'pokemon_id': pokemon.pokemon_id,
            'types': pokemon.types,
            'abilities': pokemon.abilities,
            'base_stats': pokemon.base_stats,
            'height': pokemon.height,
            'weight': pokemon.weight,
            'sprite_url': pokemon.sprite_url,
            'score': pokemon.score
        }
        pokemons_data.append(pokemon_data)

    return Response(pokemons_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def calculate_pokemon_score(request, pokemon_name_or_id):
    pokemon_data = PokemonApiService.get_pokemon_data(pokemon_name_or_id)
    if pokemon_data:
        score = ScoreService.calculate_score(pokemon_data)
        name = pokemon_data['name']
        pokemon_id = pokemon_data['pokemon_id']

        return Response({'pokemon_name': name, 'pokemon_id': pokemon_id, 'score': score}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Pokemon not found'}, status=status.HTTP_404_NOT_FOUND)
