import requests


def process_pokemon_data(pokemon_data):
    return {
        'name': pokemon_data['name'],  # Keep the original case
        'pokemon_id': pokemon_data['id'],
        'types': [type_data['type']['name'] for type_data in pokemon_data['types']],  # Keep the original case
        'abilities': [ability_data['ability']['name'] for ability_data in pokemon_data['abilities']],  # Keep the original case
        'base_stats': {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']},
        'height': pokemon_data['height'],
        'weight': pokemon_data['weight'],
        'sprite_url': pokemon_data['sprites']['front_default']
    }


class PokemonApiService:
    @staticmethod
    def get_pokemon_data(pokemon_name_or_id):
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name_or_id}/'
        response = requests.get(url)
        pokemon_data = response.json()
        processed_data = process_pokemon_data(pokemon_data)
        return processed_data


class ScoreService:
    @staticmethod
    def calculate_score(pokemon_data):
        type_weight = 0.4
        stats_weight = 0.3
        abilities_weight = 0.2
        other_weight = 0.1

        types_count = len(pokemon_data['types'])
        stats_sum = sum(pokemon_data['base_stats'].values())
        abilities_count = len(pokemon_data['abilities'])
        other_factors = pokemon_data['height'] + pokemon_data['weight']

        score = (type_weight * types_count) + (stats_weight * stats_sum) + (abilities_weight * abilities_count) + (
                    other_weight * other_factors)
        return score
