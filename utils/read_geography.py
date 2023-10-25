import json

from models.geography.location import Location
from models.geography.subdivision import Country


def read_location():
    with open('data/geography/location.json', 'r') as file:
        data = json.load(file)

        validated_data = Location(**data)

        return validated_data
    
def read_subdivisions():
    with open('data/geography/subdivisions.json', 'r') as file:
        data = json.load(file)

        validated_data = Country(**data)

        return validated_data