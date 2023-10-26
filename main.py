from enum import Enum

from fastapi import FastAPI, HTTPException

from models import Census, Region, Location, Country, Population
from utils import read_population, read_location, read_subdivisions


app = FastAPI()


class Tags(Enum):
    demography = "demography"
    geography = "geography"


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/demography/population", tags=[Tags.demography], response_model=Census)
def get_population():
    population = read_population()
    return population


@app.get("/demography/population/region/{region}", tags=[Tags.demography], response_model=Region)
def get_population_by_region(region: str):
    population = read_population()

    if region not in population.regions:
        raise HTTPException(status_code=404, detail=f"Region '{region}' not found. Make sure the region's name is spelled correctly.")
    
    return population.regions[region]


@app.get("/demography/population/prefecture/{prefecture}", tags=[Tags.demography], response_model=Population)
def get_population_by_prefecture(prefecture: str):
    population = read_population()

    for region in population.regions.values():
        if prefecture in region.prefectures:
            return region.prefectures[prefecture]

    raise HTTPException(status_code=404, detail=f"Prefecture '{prefecture}' not found. Make sure the prefecture's name is spelled correctly.")


@app.get("/geography/location", tags=[Tags.geography], response_model=Location)
def get_location():
    location = read_location()
    return location


@app.get("/geography/subdivisions", tags=[Tags.geography], response_model=Country)
def get_subdivisions():
    subdivisions = read_subdivisions()
    return subdivisions
