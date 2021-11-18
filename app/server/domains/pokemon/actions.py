from server.database.connection import pokemon_collection
# from utils.convert_txt import convert_txt_for_json

from bson.objectid import ObjectId
        

def pokemon_helper(pokemon) -> dict:
        return {
                "id": str(pokemon["_id"]),    
                "pokedex_id": pokemon["pokedex_id"],
                "name": pokemon["name"],
                "type": pokemon["type"],
                "height": pokemon["height"],
                "weight": pokemon["weight"],
                "category": pokemon["category"],
                "ability": pokemon["ability"],
                "ability_two": pokemon["ability_two"],
                "weakness": pokemon["weakness"],
                "weakness_two": pokemon["weakness_two"],
                "description": pokemon["description"]
                }


# Retrieve all pokemons present in the database
async def retrieve_pokemons():
    pokemons = []
    async for pokemon in pokemon_collection.find():
        pokemons.append(pokemon_helper(pokemon))
    return pokemons


# Add a new pokemon into to the database
async def add_pokemon(pokemon_data: dict) -> dict:
    pokemon = await pokemon_collection.insert_one(pokemon_data)
    new_pokemon = await pokemon_collection.find_one({"_id": pokemon.inserted_id})
    return pokemon_helper(new_pokemon)


# Retrieve a pokemon with a matching ID
async def retrieve_pokemon(id: str) -> dict:
    pokemon = await pokemon_collection.find_one({"_id": ObjectId(id)})
    if pokemon:
        return pokemon_helper(pokemon)


# Update a pokemon with a matching ID
async def update_pokemon(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    pokemon = await pokemon_collection.find_one({"_id": ObjectId(id)})
    if pokemon:
        updated_pokemon = await pokemon_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_pokemon:
            return True
        return False


# Delete a pokemon from the database
async def delete_pokemon(id: str):
    pokemon = await pokemon_collection.find_one({"_id": ObjectId(id)})
    if pokemon:
        await pokemon_collection.delete_one({"_id": ObjectId(id)})
        return True


# Add a new pokemon into to the database
async def add_all_pokemon(pokemon_list: list) -> dict:
    count_save = 0
    for pokemon_data in pokemon_list:
        await pokemon_collection.insert_one(pokemon_data)
        count_save = count_save + 1
    return f"{count_save} Pokemons saves."

# def import_txt(text: str) -> List[Pokemon]:
#     pokemon: Pokemon = Pokemon()
#     list_models: List[Pokemon] = list()

#     dictionary_list = convert_txt_for_json(text, pokemon.serialize())
#     for data in dictionary_list:
#         model: Pokemon = Pokemon(
#                                  id=data['id'],
#                                  name=data['name'],
#                                  type=data['type'],
#                                  height=data['height'],
#                                  weight=data['weight'],
#                                  category=data['category'],
#                                  ability=data['ability'],
#                                  ability_two=data['ability_two'],
#                                  weakness=data['weakness'],
#                                  weakness_two=data['weakness_two'],
#                                  description=data['description']
#                                  )
#         list_models.append(model)

#     for model in list_models:
#         "save(model)"

#     return list_models
