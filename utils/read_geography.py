import json

from models.geography.location import Location


def read_location():
    with open('data/geography/location.json', 'r') as file:
        data = json.load(file)

        validated_data = Location(**data)

        return validated_data