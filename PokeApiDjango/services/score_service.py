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

        score = (type_weight * types_count) + (stats_weight * stats_sum) + (abilities_weight * abilities_count) + (other_weight * other_factors)
        return score