from pydantic import BaseModel


class Location(BaseModel):
    id: str
    name: str


class LocationPokemon(BaseModel):
    id: int
    name: str
    types: list[str]
    image: str