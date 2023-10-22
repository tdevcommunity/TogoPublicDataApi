import json

from models.demography.population import Census


def read_population():
    with open('data/demography/population.json', 'r') as file:
        data = json.load(file)
        # print(data['RGPH-5'])

        validated_data = Census(**data['RGPH-5'])

        return {'RGPH-5': validated_data}