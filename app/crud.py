from sqlalchemy.orm import Session

from .models import Vehicle as VehicleModel
from .models import City as CityModel
from .models import Ubication as UbicationModel
from app.definitions.vehicle import Vehicle




def get_vehicles(db: Session, skip: int = 0, limit: int = 250):
    
    return db.query(VehicleModel).offset(skip).limit(limit).all()

def get_avaible_vehicle(db: Session, limit: int = 250):
    return db.query(VehicleModel).filter(VehicleModel.current_status==1).all()

def get_vehicle_by_id(db: Session, id: int, limit: int = 1):
     return db.query(VehicleModel).filter(VehicleModel.id == id).first()

def post_vehicle(db:Session, label, current_status):
    add_vehicle = VehicleModel(label=label, current_status=current_status)
    db.add(add_vehicle)
    db.commit()
    db.refresh(add_vehicle)

def get_cities(db: Session, skip: int = 0, limit: int = 250):
    return db.query(CityModel).offset(skip).limit(limit).all()

def get_last_city_id(db):
    city = db.query(CityModel).order_by(CityModel.id.desc()).first()
    if city is None:
        return None
    else:
        return city.id

def get_last_vehicle_id(db):
    vehicle = db.query(VehicleModel).order_by(VehicleModel.id.desc()).first()
    if vehicle is None:
        return None
    else:
        return vehicle.id

def get_city_by_name(db: Session, name: str):
    city = db.query(CityModel).filter(CityModel.name == name).first()
    if city is None:
        return None
    else:
        return city.id


def post_city(db:Session, name: str):
    add_city = CityModel(name = name)
    db.add(add_city)
    db.commit()
    db.refresh(add_city)

def get_ubications(db: Session, skip: int = 0, limit: int = 250):
    return db.query(UbicationModel).offset(skip).limit(limit).all()

def post_ubication(db:Session, latitude: float, longitude: float, vehicle_id: int, city_id: int):
    add_ubication = UbicationModel(latitude = latitude, longitude = longitude, vehicle_id = vehicle_id, city_id = city_id)
    db.add(add_ubication)
    db.commit()
    db.refresh(add_ubication)


def get_vehicle_id_by_label(db: Session, label: int):
    obj_vehicle = db.query(VehicleModel).filter(VehicleModel.label == label).first()
    if obj_vehicle is None:
        return None
    else:
        return obj_vehicle.id

def get_last_location_id(db: Session):
    ubication = db.query(UbicationModel).order_by(UbicationModel.id.desc()).first()
    if ubication is None:
        return None
    else:
        return ubication.id

def get_ubication_vehicle_by_id(db: Session, id: int):
    ubication = db.query(UbicationModel).filter(UbicationModel.vehicle_id == id).first()
    if ubication is None:
        return None
    else:
        return ubication
    
def get_avaible_cities(db: Session):
    vehicles = get_avaible_vehicle(db)
    cities = []
    for vehicle in vehicles:
        metrobus = Vehicle.from_instance(vehicle)
        cities.append(get_ubication_vehicle_by_id(db,metrobus.id))
    return cities

def get_vehicles_by_city(db: Session, id: int):
    return db.query(UbicationModel).filter(UbicationModel.city_id==id).all()
    



        
        
