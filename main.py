from enum import Enum

from fastapi import FastAPI

from models import Census, Location, Country
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

@app.get("/geography/location", tags=[Tags.geography], response_model=Location)
def get_location():
    location = read_location()
    return location

@app.get("/geography/subdivisions", tags=[Tags.geography], response_model=Country)
def get_subdivisions():
    subdivisions = read_subdivisions()
    return subdivisions