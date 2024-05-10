from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests
from .models import PokemonTable

class PokemonApiService:
    """
    A service class for fetching Pokemon data from the Pokemon API and saving it to the database.
    """

    @staticmethod
    @api_view(['GET'])
    def fetch_pokemon_data(request):
        """
        Fetches Pokemon data from the Pokemon API and saves it to the database.

        Args:
            request (HttpRequest): The request object.

        Returns:
            Response: A Response object with a success message and a 201 status code if the Pokemon data was fetched and saved successfully,
                      a Response object with an error message and a 400 status code if the 'pokemon_id' was not provided in the request data,
                      a Response object with an error message and a 500 status code if an error occurred while fetching the Pokemon data.
        """
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

            # Save the pokemon object to the database in case of the pokemon not existing
            if not PokemonTable.objects.filter(pokemon_id=pokemon.pokemon_id).exists():
                pokemon.save()
            else:
                return Response({'message': f'Pokemon {pokemon.name} already exists'}, status=status.HTTP_200_OK)

            return Response({'message': f'Pokemon {pokemon.name} added successfully'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        pass

class ScoreService:
    @staticmethod
    def calculate_score(pokemon_data):
        peso_tipo = 0.4
        peso_estadisticas = 0.3
        peso_habilidades = 0.2
        peso_otros = 0.1

        tipos = len(pokemon_data['types'])
        estadisticas = sum(pokemon_data['base_stats'].values())
        habilidades = len(pokemon_data['abilities'])
        otros = pokemon_data['height'] + pokemon_data['weight']

        score = (peso_tipo * tipos) + (peso_estadisticas * estadisticas) + (peso_habilidades * habilidades) + (peso_otros * otros)
        return score
    pass