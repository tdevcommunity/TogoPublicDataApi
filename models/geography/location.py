from pydantic import BaseModel
from typing import Dict


class Measurement(BaseModel):
    value: float
    unit: str

class Boundary(BaseModel):
    name: str
    country: bool
    borderLength: Measurement

class Location(BaseModel):
    continent: str
    # capital_city: str
    continentRegion: str
    latitude: str
    longitude: str
    boundaries: Dict[str, Boundary]
    area: Measurement