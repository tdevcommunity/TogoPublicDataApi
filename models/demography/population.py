from pydantic import BaseModel
from typing import Dict

class Population(BaseModel):
    female: str
    male: str
    total: str

class Region(Population):
    prefectures: Dict[str, Population]

class Census(BaseModel):
    date: str
    general: Population
    regions: Dict[str, Region]

class Demography(BaseModel):
    Dict[str, Census]