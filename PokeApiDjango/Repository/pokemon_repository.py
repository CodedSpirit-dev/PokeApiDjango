from typing import List
from Repository.models import Pokemon
from ipokemon_repository import IPokemonRepository

class PokemonRepository(IPokemonRepository):
    def get_all_pokemon(self) -> List[Pokemon]:
        return Pokemon.objects.all()

    def get_pokemon_from_localdb(self, pokemon_name: str) -> Pokemon:
        try:
            return Pokemon.objects.get(name=pokemon_name)
        except Pokemon.DoesNotExist:
            return None

    def add_pokemon_to_localdb(self, pokemon: Pokemon) -> None:
        pokemon.save()

    def update_pokemon_in_localdb(self, pokemon: Pokemon) -> None:
        try:
            existing_pokemon = Pokemon.objects.get(pk=pokemon.id)
            existing_pokemon.name = pokemon.name
            # Actualiza otros campos si es necesario
            existing_pokemon.save()
        except Pokemon.DoesNotExist:
            pass

    def delete_pokemon_from_localdb(self, pokemon_name: str) -> None:
        try:
            pokemon = Pokemon.objects.get(name=pokemon_name)
            pokemon.delete()
        except Pokemon.DoesNotExist:
            pass

    def get_details_from_pokemon(self, pokemon_name: str) -> Pokemon:
        try:
            return Pokemon.objects.get(name=pokemon_name)
        except Pokemon.DoesNotExist:
            return None

    def get_pokemon_score(self, pokemon_name: str) -> float:
        pokemon = self.get_pokemon_from_localdb(pokemon_name)
        if pokemon:
            # Aquí puedes implementar lógica para calcular el puntaje del Pokémon
            return 0.0
        else:
            return 0.0

    def get_all_pokemon_in_localdb(self) -> List[Pokemon]:
        return Pokemon.objects.all()
