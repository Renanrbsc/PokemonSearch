from fastapi import Body
from fastapi.encoders import jsonable_encoder
from utils.convert_txt import convert_txt_for_json, open_txt

from server.domains.pokemon.actions import (
    add_pokemon,
    add_all_pokemon,
    delete_pokemon,
    retrieve_pokemon,
    retrieve_pokemons,
    update_pokemon,
)
from server.domains.pokemon.models import (
    ErrorResponseModel,
    ResponseModel,
    PokemonSchema,
    UpdatePokemonModel,
    Serialize
)
from server.domains import router


@router.post("/pokemon", response_description="Pokemon data added into the database")
async def add_pokemon_data(pokemon: PokemonSchema = Body(...)):
    pokemon = jsonable_encoder(pokemon)
    new_pokemon = await add_pokemon(pokemon)
    return ResponseModel(new_pokemon, "Pokemon added successfully.")


@router.post("/allpokemon", response_description="Pokemon data added into the database")
async def add_all_pokemon_data():
    url = 'app/server/database/data/pokemons.txt'
    all_pokemon = convert_txt_for_json(open_txt(url), Serialize())
    new_pokemon = await add_all_pokemon(all_pokemon)
    return ResponseModel(new_pokemon, "Pokemon added successfully.")


@router.get("/", response_description="Pokemons retrieved")
async def get_pokemons():
    pokemons = await retrieve_pokemons()
    if pokemons:
        return ResponseModel(pokemons, "Pokemons data retrieved successfully")
    return ResponseModel(pokemons, "Empty list returned")


@router.get("/{id}", response_description="Pokemon data retrieved")
async def get_pokemon_data(id):
    pokemon = await retrieve_pokemon(id)
    if pokemon:
        return ResponseModel(pokemon, "Pokemon data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "pokemon doesn't exist.")


@router.put("/{id}")
async def update_pokemon_data(id: str, req: UpdatePokemonModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_pokemon = await update_pokemon(id, req)
    if updated_pokemon:
        return ResponseModel(
            "Pokemon with ID: {} name update is successful".format(id),
            "Pokemon name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the pokemon data.",
    )


@router.delete("/{id}", response_description="Pokemon data deleted from the database")
async def delete_pokemon_data(id: str):
    deleted_pokemon = await delete_pokemon(id)
    if deleted_pokemon:
        return ResponseModel(
            "Pokemon with ID: {} removed".format(id), "Pokemon deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Pokemon with id {0} doesn't exist".format(id)
    )











# @app_pokemons.route('/pokemons:import_txt_pokemon', methods=['POST'])
# def post_txt_pokemons():
#     content = request.files['file']
#     text = content.stream.read().decode("utf-8")

#     list_data = import_txt_pokemon(text)
#     return jsonify([pokemon.serialize() for pokemon in list_data]), 201

