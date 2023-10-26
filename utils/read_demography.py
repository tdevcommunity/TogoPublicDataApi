import json

from models.demography.population import Census


def read_population():
    with open('data/demography/population.json', 'r') as file:
        data = json.load(file)

        validated_data = Census(**data['RGPH-5'])

        return validated_data