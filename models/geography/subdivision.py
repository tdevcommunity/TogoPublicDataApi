from pydantic import BaseModel
from typing import Dict


class Municipality(BaseModel):
    capital: str

class Prefecture(BaseModel):
    municipalities: Dict[str, Municipality]

class Region(BaseModel):
    prefectures: Dict[str, Prefecture]

class Country(BaseModel):
    regions: Dict[str, Region]