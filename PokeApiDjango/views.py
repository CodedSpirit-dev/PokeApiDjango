from rest_framework import viewsets

from PokeApiDjango.models import Pokemon
from PokeApiDjango.serializers import PokemonSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer