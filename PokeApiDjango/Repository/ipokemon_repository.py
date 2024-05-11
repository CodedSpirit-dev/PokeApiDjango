from abc import abstractmethod, ABC
from typing import List

from PokeApiDjango.models import Pokemon


class IPokemonRepository(ABC):
    @abstractmethod
    def get_all_pokemon(self) -> List[Pokemon]:
        pass

    @abstractmethod
        # Get one pokemon by name or id
    def get_pokemon_from_localdb(self, pokemon_name: str) -> Pokemon:
        pass

    @abstractmethod
    def add_pokemon_to_localdb(self, pokemon: Pokemon) -> None:
        pass

    @abstractmethod
    def update_pokemon_in_localdb(self, pokemon: Pokemon) -> None:
        pass

    @abstractmethod
    def delete_pokemon_from_localdb(self, pokemon_name: str) -> None:
        pass

    @abstractmethod
    def get_details_from_pokemon(self, pokemon_name: str) -> Pokemon:
        pass

    @abstractmethod
    def get_pokemon_score(self, pokemon_name: str) -> float:
        pass

    @abstractmethod
    def get_all_pokemon_in_localdb(self) -> List[Pokemon]:
        pass

