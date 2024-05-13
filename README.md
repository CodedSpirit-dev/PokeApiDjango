# PokeApiDjango
Este proyecto es una API REST desarrollada en Django Rest Framework que consume la API pública de Pokémon y almacena la información de los Pokémon en una base de datos SQLite. Además, se implementa un servicio para calcular un puntaje para cada Pokémon.

## Lista de tareas que este proyecto cumple:
- [x] Crear modelo de Django para almacenar información sobre los Pokémon.
- [x] Implementar un servicio para interactuar con la API pública de Pokémon.
- [x] Implementar un servicio para obtener un puntaje del Pokémon.
- [x] Crear un endpoint para obtener la información de un Pokémon por su ID o nombre.
- [x] Crear un endpoint para crear y guardar un Pokémon en la base de datos.
- [x] Crear un endpoint para actualizar la información de un Pokémon en la base de datos.
- [x] Crear un endpoint para eliminar un Pokémon de la base de datos.
- [x] Crear un endpoint para obtener toda la información de un Pokémon, incluyendo su puntaje.
- [x] Crear un endpoint para obtener la lista de Pokémon almacenados en la base de datos, incluyendo su puntaje y la URL de la imagen.
- [x] Crear un endpoint para calcular el puntaje de todos los Pokémon almacenados en la base de datos.

## Manual de uso de los endpoints
### 1. Obtener la información de un Pokémon por su ID o nombre
- **URL:** `/pokemon/<id_or_name>/`
- **Método:** GET
- **Parámetros:**
  - `id_or_name`: ID o nombre del Pokémon.
  - **Ejemplo:** `/pokemon/1/` o `/pokemon/bulbasaur/`
  - **Nota:** El nombre del Pokémon debe estar en minúsculas.
  - **Nota:** Este endpoint obtiene la información del Pokémon desde la API pública y posteriormente la almacena en la base de datos.
- **Respuesta:**
- **Código de estado:** 200
- **Cuerpo de la respuesta:**
```json
{
  "id": "b7701bbd-68ec-4f57-9c3e-29a807d28d06",
  "created_at": "2024-05-07T01:32:50.109162Z",
  "updated_at": "2024-05-07T01:32:50.109200Z",
  "name": "bulbasaur",
  "pokemon_id": 1,
  "types": [
	"grass",
	"poison"
  ],
  "abilities": [
	"overgrow",
	"chlorophyll"
  ],
  "base_stats": {
	"hp": 45,
	"attack": 49,
	"defense": 49,
	"special-attack": 65,
	"special-defense": 65,
	"speed": 45
  },
  "height": 7,
  "weight": 69,
  "sprite_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
  "score": 0
}
```

### 2. Crear y guardar un Pokémon en la base de datos
- **URL:** `/pokemon/`
- **Método:** POST
- **Nota:** Si no se usa un url de imagen, se usará la imagen por defecto de la API pública, que en este caso será la imagen de Pikachu.
- **Parámetros:**
  - **Cuerpo de la petición:** 
```json
{
  "name": "Motapod", //An unexisting pokemon
  "types": [
    "Electric",
    "Flying"
  ], //Custom types
  "abilities": [ //Custom abilities
    "sand-veil", 
    "sand-rush"
  ],
  "base_stats": { //Custom base stats
    "hp": 1,
    "attack": 3,
    "defense": 100,
    "special-attack": 0,
    "special-defense": 100,
    "speed": 3
  },
  "height": 4,
  "weight": 60,
  "sprite_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
}
```
- **Respuesta:**
- **Código de estado:** 200
- **Cuerpo de la respuesta:**
```json
{
  "name": "Motapod",
  "types": [
    "Electric",
    "Flying"
  ],
  "abilities": [
    "sand-veil",
    "sand-rush"
  ],
  "base_stats": {
    "hp": 1,
    "attack": 3,
    "defense": 100,
    "special-attack": 0,
    "special-defense": 100,
    "speed": 3
  },
  "height": 4,
  "weight": 60,
  "sprite_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
  "pokemon_id": 10286,
  "score": 69.69999999999999
}
```

### 3. Actualizar la información de un Pokémon en la base de datos
- **URL:** `/pokemon/<id_or_name>/`
- **Método:** PUT
- **Parámetros:**
  - `id_or_name`: ID o nombre del Pokémon.
  - **Ejemplo:** `/pokemon/1/` o `/pokemon/bulbasaur/`
  - **Nota:** El nombre del Pokémon debe estar en minúsculas.
  - **Cuerpo de la petición:** Mismo cuerpo de la petición que el endpoint de creación.
```json
{
  "name": "Motapod",
  "types": [
    "Electric",
    "Flying"
  ],
  "abilities": [
    "sand-veil",
    "sand-rush"
  ],
  "base_stats": {
    "hp": 1,
    "attack": 3,
    "defense": 100,
    "special-attack": 0,
    "special-defense": 100,
    "speed": 3
  },
  "height": 4,
  "weight": 60,
  "sprite_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
}

```
- **Respuesta:**
- **Código de estado:** 200
- **Cuerpo de la respuesta:**
```json
{
  "name": "Motapod",
  "types": [
    "Electric",
    "Flying"
  ],
  "abilities": [
    "sand-veil",
    "sand-rush"
  ],
  "base_stats": {
    "hp": 1,
    "attack": 3,
    "defense": 100,
    "special-attack": 0,
    "special-defense": 100,
    "speed": 3
  },
  "height": 4,
  "weight": 60,
  "sprite_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
  "pokemon_id": 10286,
  "score": 69.69999999999999
}
```

### 4. Eliminar un Pokémon de la base de datos
- **URL:** `/pokemon/<id_or_name>/`
- **Método:** DELETE
- **Parámetros:**
  - `id_or_name`: ID o nombre del Pokémon.
  - **Ejemplo:** `/pokemon/1/` o `/pokemon/bulbasaur/`
  - **Nota:** El nombre del Pokémon debe estar en minúsculas.
- **Respuesta:**
- **Código de estado:** 200
- **Cuerpo de la respuesta:**
```json
{
  "message": "The pokemon Motapod with id 10287 deleted successfully" //The information of the deleted pokemon changes depending on the pokemon deleted
}
```

### 5. Obtener toda la información de un Pokémon, incluyendo su puntaje
- **URL:** `/pokemon/<id_or_name>/full/`
- **Método:** GET
- **Parámetros:**
  - `id_or_name`: ID o nombre del Pokémon.
  - **Ejemplo:** `/get_pokemon_data_from_db/14/` o `/get_pokemon_data_from_db/kakuna/`
  - **Nota:** El nombre del Pokémon debe estar en minúsculas.
  - **Nota:** Este endpoint obtiene la información del Pokémon desde la base de datos, no desde la API pública.
  - **Respuesta:**
  - **Código de estado:** 200
  - **Cuerpo de la respuesta:**
```json
{
    "name": "kakuna",
    "pokemon_id": 14,
    "types": [
        "bug",
        "poison"
    ],
    "abilities": [
        "shed-skin"
    ],
    "base_stats": {
        "hp": 45,
        "attack": 25,
        "defense": 50,
        "special-attack": 25,
        "special-defense": 25,
        "speed": 35
    },
    "height": 6,
    "weight": 100,
    "sprite_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/14.png",
    "score": 73.1
}
```

### 6. Obtener la lista de Pokémon almacenados en la base de datos, incluyendo su puntaje y la URL de la imagen
- **URL:** `/get_list_of_pokemon_saved_in_db/`
- **Método:** GET
- **Nota:** Este endpoint obtiene la información de todos los Pokémon almacenados en la base de datos.
- **Respuesta:**
- **Código de estado:** 200
- **Cuerpo de la respuesta**
```json
[
    {
        "name": "weedle",
        "pokemon_id": 13,
        "types": [
            "bug",
            "poison"
        ],
        "abilities": [
            "shield-dust",
            "run-away"
        ],
        "base_stats": {
            "hp": 40,
            "attack": 35,
            "defense": 30,
            "special-attack": 20,
            "special-defense": 20,
            "speed": 50
        },
        "height": 3,
        "weight": 32,
        "sprite_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/13.png",
        "score": 63.199999999999996
    },
    {
        "name": "kakuna",
        "pokemon_id": 14,
        "types": [
            "bug",
            "poison"
        ],
        "abilities": [
            "shed-skin"
        ],
        "base_stats": {
            "hp": 45,
            "attack": 25,
            "defense": 50,
            "special-attack": 25,
            "special-defense": 25,
            "speed": 35
        },
        "height": 6,
        "weight": 100,
        "sprite_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/14.png",
        "score": 73.1
    }
]
```
### 7. Calcular el puntaje de un Pokémon
- **URL:** `/calculate_score_of_pokemon/`
- **Método:** GET
- **Parámetros:**
  - `id_or_name`: ID o nombre del Pokémon.
  - **Ejemplo:** `/calculate_score_of_pokemon/14/` o `/calculate_score_of_pokemon/kakuna/`
  - **Nota:** El nombre del Pokémon debe estar en minúsculas.
- **Nota:** Este endpoint calcula el puntaje de un Pokémon en base a sus estadísticas base.
- **Respuesta:**
- **Código de estado:** 200
- **Cuerpo de la respuesta:**
```json
{
  "pokemon_name": "kakuna",
  "pokemon_id": 14,
  "score": 73.1
}
```

## Instalación
1. Clonar el repositorio:
```bash
git clone
```
2. Crear un entorno virtual:
```bash
python -m venv venv
```
3. Activar el entorno virtual:
```bash
source venv/bin/activate
```
4. Instalar las dependencias:
```bash
pip install -r requirements.txt
```
5. Realizar las migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```
6. Iniciar el servidor:
```bash
python manage.py runserver
```
7. Una vez iniciado, iniciar el proyecto de el cual se encuentra en el siguiente enlace: [Frontend](https://github.com/CodedSpirit-dev/PokeApi_React)
8. Listo, ya puedes empezar a usar la API.



