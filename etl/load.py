import pandas as pd
from .preprocessing import get_address
from app.db import SessionLocal
from app.crud import get_last_city_id, get_last_vehicle_id, get_vehicle_id_by_label, post_city, post_ubication, post_vehicle, get_city_by_name

db = SessionLocal()

def load(data: pd.DataFrame):
    """Add to database the vehicle, city and location foreach element of open data Metrobus CDMX System
    Args:
        data (pd.DataFrame): data open data Metrobus CDMX System
    Returns:
        Does not return any value
    """
        
    for i in data.index:
        latitude = float( data.iloc[i]['position_latitude'] )
        longitude = float(data.iloc[i]['position_longitude'])
        city = get_address(latitude, longitude)
        if city is None:
            print("invalid location")
        else:
            city_id = get_city_by_name(db, city)
            if city_id is None:
                post_city(db, city)
                city_id = get_last_city_id(db)
            
            vehicle_label = int( data.iloc[i]['vehicle_label'] )
            vehicle_current_status = int( data.iloc[i]['vehicle_current_status'] )
            vehicle_id = get_vehicle_id_by_label(db, vehicle_label)

            if vehicle_id is None:
                post_vehicle(db, vehicle_label, vehicle_current_status)
                vehicle_id = get_last_vehicle_id(db)
            
            post_ubication(db, latitude, longitude, vehicle_id, city_id)
            print("Record added successfully")








