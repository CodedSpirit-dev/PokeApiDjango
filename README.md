## Instrucciones del ejercicio para el Candidato:

Desarrollar una aplicación web utilizando Django REST Framework para el backend y React para el frontend. La aplicación debe permitir a los usuarios buscar información sobre Pokémon utilizando la Poke API (https://pokeapi.co/), agregar Pokémon a una base de datos local (SQLite), ver una lista de los Pokémon agregados, ver detalles específicos de un Pokémon y calcular y mostrar su puntaje.

### Desarrollo del Backend (Django REST Framework):

Implementa la funcionalidad requerida en el backend utilizando Django REST Framework.

1. Crear modelo de Django para almacenar información sobre los Pokémon, incluyendo su nombre, ID, tipos, habilidades, estadísticas base, altura, peso y URL de la imagen. Ejemplo de los campos y formato requerido:
```json
{
  "id": "b7701bbd-68ec-4f57-9c3e-29a807d28d06",
  "created_at": "2024-05-07T01:32:50.109162Z",
  "updated_at": "2024-05-07T01:32:50.109200Z",
  "name": "zapdos",
  "pokemon_id": 145,
  "types": [
    "electric",
    "flying"
  ],
  "abilities": [
    "pressure",
    "static"
  ],
  "base_stats": {
    "hp": 90,
    "attack": 90,
    "defense": 85,
    "special-attack": 125,
    "special-defense": 90,
    "speed": 100
  },
  "height": 16,
  "weight": 526,
  "sprite_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/145.png"
}
```
2. Crear los siguientes servicios:

	2.1. Pokemon API Service: Implementar un servicio para interactuar con la API pública de Pokémon. Este servicio es el encargado de procesar las peticiones a la API publica.
	
	```python
	class PokemonApiService:
	    @staticmethod
	    def get_pokemon_data(pokemon_name_or_id):
		    # Hacer llamada a la api publica
	        ...

	    @staticmethod
	    def process_pokemon_data(pokemon_data):
	        # Procesar y transformar la data publica para ajustrla a como lo requiere el modelo
	        ...
	```
	2.2. Score Service: implementar un servicio para obtener un puntaje del Pokemon (ver detalles)
	
	
	```python
	class ScoreService:
	    @staticmethod
	    def calculate_score(pokemon):
	        ...
	```
	
	```
	Cálculo del Puntaje: El puntaje de un Pokémon se calcula sumando diferentes factores, cada uno multiplicado por un peso:

	Puntaje=(PesoTipo×Tipos)+(PesoEstadisticas×Estadisticas)+(PesoHabilidades×Habilidades)+(PesoOtros×Otros)Puntaje=(PesoTipo×Tipos)+(PesoEstadisticas×Estadisticas)+(PesoHabilidades×Habilidades)+(PesoOtros×Otros)

	Los pesos son 0.4 para tipos, 0.3 para estadisticas, 0.2 para habilidades y 0.1 para otros

	Por ejemplo, si un Pokémon tiene 2 tipos, 3 habilidades, una suma de estadísticas base de 300, una altura de 0.5 m y un peso de 10 kg, el cálculo del puntaje sería:

	Puntaje=(0.4×2)+(0.3×300)+(0.2×3)+(0.1×(0.5+10))=0.8+90+0.6+1.05=92.45Puntaje=(0.4×2)+(0.3×300)+(0.2×3)+(0.1×(0.5+10))=0.8+90+0.6+1.05=92.45
	```	


	
	
3. Crear los siguientes endpoints:
	* 3.1 Endpoint para buscar y obtener datos un Pokemon usando el Servicio.
	* 3.2 Endpoint para crear/guardar pokemon en la base de datos.
	* 3.3 Endpoint para editar/actualizar pokemon.
	* 3.4 Endpoint para eliminar un Pokémon de la base de datos.
	* 3.5 Endpoint para  obtener información detallada de Pokémon guardado en la base de datos.
	* 3.6 Endpoint para  la lista de Pokemones guardados en la base de datos.	
	* 3.7 Endpoint para obtener el cálculo de puntajes de Pokémon guardado en la base de datos.

### Desarrollo del Frontend (Opcional, para evaluar la habilidad con React):
1. Desarrolla una interfaz frontal básica para interactuar con las APIs del backend.
2. Enfócate en características fundamentales del frontend como mostrar un formulario para buscar Pokémon y agregarlos a la base de datos, listar Pokémon almacenados en la base de datos, mostrar información detallada sobre Pokémon seleccionados y agregar un botón para calcular y mostrar puntajes de Pokémon.
3. Utiliza React o cualquier framework JavaScript moderno de tu elección para construir la aplicación frontend.

### Integración:
1. Asegura una integración fluida entre los componentes frontend y backend.
2. Maneja las solicitudes y respuestas de la API de manera adecuada, incluyendo manejo de errores y validación.
3. Demuestra cómo la aplicación frontend interactúa con las APIs de Django REST para realizar operaciones CRUD en los datos de Pokémon y calcular puntajes.

En resumen, concéntrate más en el desarrollo del backend utilizando Django REST Framework, mientras que opcionalmente demuestras habilidades en desarrollo frontend con React o cualquier framework JavaScript preferido. Asegura una integración sin problemas entre los componentes frontend y backend para mostrar comprensión y habilidad integral en desarrollo full-stack.

