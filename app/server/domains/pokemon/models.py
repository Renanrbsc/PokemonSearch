from typing import Optional

from pydantic import BaseModel, Field


class PokemonSchema(BaseModel):   

    pokedex_id: str = Field(...)
    name: str = Field(...)
    type: str = Field(...)
    height: float = Field(...)
    weight: float = Field(...)
    category: str = Field(...)
    first_skill: str = Field(...)
    second_skill: str = Field(...)
    first_weakness: str = Field(...)
    second_weakness: str = Field(...)
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
                "first_skill": "Growl",
                "second_skill": "Vine Whip",
                "first_weakness": 'Fire',
                "second_weakness": "Wate",
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
    first_skill: Optional[str]
    second_skill: Optional[str]
    first_weakness: Optional[str]
    second_weakness: Optional[str]
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
                "first_skill": "Growl",
                "second_skill": "Vine Whip",
                "first_weakness": 'Fire',
                "second_weakness": "Wate",
                "description": "A strange seed was planted on its back at birth." 
                               "The plant sprouts and grows with this Pokemon"
            }
        }


def Serialize():
    return {
        "pokedex_id": "",
        "name": "",
        "type": "",
        "height": "",
        "weight": "",
        "category": "",
        "first_skill": "",
        "second_skill": "",
        "first_weakness": '',
        "second_weakness": "",
        "description": ""
    }

    
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}









    