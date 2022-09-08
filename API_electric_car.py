from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

class car_model(BaseModel):
    Name: str
    Subtitle: str
    Acceleration: str
    TopSpeed: str
    Range: str
    Efficiency: str
    FastChargeSpeed: str
    Drive: str
    NumberofSeats: str
    PriceinGermany: str
    PriceinUK: str

    class Config:
        orm_mode = True


json_cars = open('electric_car.json')
cars_database = json.load(json_cars)



app = FastAPI()


@app.get('/')
def home():
    return {'data':'Cheapest Electric Cars in 2022 - API'}


@app.get('/cars')
def cars():
    return cars_database


@app.get('/cars/{car_id}')
def cars(car_id: int):
    if car_id+1 <= len(cars_database):
        return cars_database[car_id]
    else:
        raise HTTPException(status_code=404, detail=f"{car_id}. car id doesn't exist!")


@app.get('/cars/name/{car_name}')
def cars_by_name(car_name: str):

    found_ids = []
    for id in range(len(cars_database)):
        car_name_db = cars_database[id]['Name'].lower()
        if car_name_db.find(car_name.lower()) >= 0:
            found_ids.append(id)
    
    if len(found_ids) > 0:
        searched = []
        for id in found_ids:
            searched.append(cars_database[id])        
        return {f'{len(searched)} car found!': searched}

    else:
        raise HTTPException(status_code=404, detail=f'{car_name} not found!')

@app.post('/cars')
def new_car(item: car_model):

    cars_database.append(

    {"Name": item.Name,
    "Subtitle": item.Subtitle,
    "Acceleration": item.Acceleration,
    "TopSpeed": item.TopSpeed,
    "Range": item.Range,
    "Efficiency": item.Efficiency,
    "FastChargeSpeed": item.FastChargeSpeed,
    "Drive": item.Drive,
    "NumberofSeats": item.NumberofSeats,
    "PriceinGermany": item.PriceinGermany,
    "PriceinUK": item.PriceinUK })
    json.dump(cars_database, open('electric_car.json', 'w'))

    return {'successfully posted': cars_database[-1]}


@app.put('/cars/{car_id}')
def car_put(item: car_model, car_id: int):

    if car_id+1 <= len(cars_database):
        cars_database[car_id].update(item)
        json.dump(cars_database, open('electric_car.json', 'w'))
        return {'successfully updated': cars_database[car_id]}

    else:
        raise HTTPException(status_code=404, detail=f"{car_id}. car id doesn't exist!")
    
    


@app.delete('/cars/{car_id}')
def car_delete(car_id: int):

    if car_id+1 <= len(cars_database):
        car_name = cars_database[car_id]["Name"]
        del cars_database[car_id]
        json.dump(cars_database, open('electric_car.json', 'w'))

        return {'deleted successfully': f'{car_name} deleted!'}
    else:
        raise HTTPException(status_code=404, detail=f"{car_id}. car id doesn't exist!")

