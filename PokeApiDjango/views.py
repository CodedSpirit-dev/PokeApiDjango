

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