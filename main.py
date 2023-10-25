from fastapi import FastAPI

from utils.read_demography import read_population
from utils.read_geography import read_location, read_subdivisions

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/demography/population")
def get_population():
    population = read_population()
    return population

@app.get("/geography/location")
def get_location():
    location = read_location()
    return location

@app.get("/geography/subdivisions")
def get_subdivisions():
    subdivisions = read_subdivisions()
    return subdivisions