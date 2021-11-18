from typing import Optional

from pydantic import BaseModel, Field


class PokemonSchema(BaseModel):   

    pokedex_id: str = Field(...)
    name: str = Field(...)
    type: str = Field(...)
    height: float = Field(...)
    weight: float = Field(...)
    category: str = Field(...)
    ability: str = Field(...)
    ability_two: str = Field(...)
    weakness: str = Field(...)
    weakness_two: str = Field(...)
    description: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "pokedex_id": "20",
                "name": "Bulbasaur",
                "type": "Grass",
                "height": 1.73,
                "weight": 90,
                "category": "Earth",
                "ability": "Growl",
                "ability_two": "Vine Whip",
                "weakness": 'Fire',
                "weakness_two": "Wate",
                "description": "A strange seed was planted on its back at birth." 
                               "The plant sprouts and grows with this POKéMON"
            }
        }


class UpdatePokemonModel(BaseModel):

    pokedex_id: Optional[str]
    name: Optional[str]
    type: Optional[str]
    height: Optional[float]
    weight: Optional[float]
    category: Optional[str]
    ability: Optional[str]
    ability_two: Optional[str]
    weakness: Optional[str]
    weakness_two: Optional[str]
    description: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "pokedex_id": "20",
                "name": "Bulbasaur",
                "type": "Grass",
                "height": 1.73,
                "weight": 90,
                "category": "Earth",
                "ability": "Growl",
                "ability_two": "Vine Whip",
                "weakness": 'Fire',
                "weakness_two": "Wate",
                "description": "A strange seed was planted on its back at birth." 
                               "The plant sprouts and grows with this Pokemon"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}









    