from re import I
from typing import List, Optional
import strawberry
from strawberry.extensions import Extension
from app.db import SessionLocal
from .definitions.vehicle import Vehicle
from .definitions.city import City
from .definitions.ubication import Ubication
from app.crud import get_avaible_cities, get_ubication_vehicle_by_id, get_ubications, get_vehicles, get_vehicle_by_id, get_avaible_vehicle, get_cities, get_vehicles_by_city


class SQLAlchemySession(Extension):
    def on_request_start(self):
        self.execution_context.context["db"] = SessionLocal()

    def on_request_end(self):
        self.execution_context.context["db"].close()

@strawberry.type
class Query:



    @strawberry.field
    def all_vehicles(self, info) -> List[Vehicle]:
        """Get all vehicles
        Args:
            db (Session): database session/connection
        Returns:
            The list of all vehicles or an empty array if no book is registered
        """
        db = info.context["db"]
        vehicles = get_vehicles(db)
        return [Vehicle.from_instance(vehicle) for vehicle in vehicles]
    



    @strawberry.field
    def get_vehicle_by_id(self,info, id: int) -> Vehicle:
        """Get vehicle by ID
        Args:
            db (Session): database session/connection
            id (int): vehicle id sent as query parameter
        Returns:
            The vehicle or an empty array if no vehicle is registered
        """
        db = info.context["db"]
        vehicle = get_vehicle_by_id(db, id)
        return Vehicle.from_instance(vehicle)





    @strawberry.field
    def get_avaible_vehicle(self, info) -> List[Vehicle]:
        """Get available vehicles
            db (Session): database session/connection
        Returns:
            The list of all available vehicles or an empty array if no available vehicle is registered
        """
        db = info.context["db"]
        vehicles = get_avaible_vehicle(db)
        return [Vehicle.from_instance(vehicle) for vehicle in vehicles]




    @strawberry.field
    def all_cities(self, info) -> List[City]:
        """Get all cities
            db (Session): database session/connection
        Returns:
            The list of all cities or an empty array if no city is registered
        """
        db = info.context["db"]
        cities = get_cities(db)
        return [City.from_instance(city) for city in cities]


 

    @strawberry.field
    def all_ubications(self, info) -> List[Ubication]: 
        """Get all locations
            db (Session): database session/connection
        Returns:
            The list of all locations or an empty array if no locations is registered
        """  
        db = info.context["db"]
        ubications = get_ubications(db)
        return ubications



  

    @strawberry.field
    def ubication_vehicle_by_id(self, info, id:int) -> Ubication:
        """Get vehicle location by vehicle
            db (Session): database session/connection
            id (int): vehicle id sent as query parameter
        Returns:
            The  vehicle location or an none value if no vehicle location is registered
        """ 
        db = info.context["db"]
        ubication = get_ubication_vehicle_by_id(db, id)
        return Ubication.from_instance(ubication)




    @strawberry.field
    def get_available_cities(self, info) -> List[Ubication]:
        """Get available cities
            db (Session): database session/connection
        Returns:
            The available cities or an none value if no available city is registered
        """   
        db = info.context["db"]
        ubications = get_avaible_cities(db)
        return [Ubication.from_instance(ubication) for ubication in ubications]



 

    @strawberry.field
    def get_vehicles_by_city(self, info, id: int) -> List[Ubication]:
        """Get vehicles by city
            db (Session): database session/connection
            id (int): city id sent as query parameter
        Returns:
            The vehicles in city or an none value if no vehicle in city is registered
        """  
        db = info.context["db"]
        ubications = get_vehicles_by_city(db, id)
        return [Ubication.from_instance(ubication) for ubication in ubications]



schema = strawberry.Schema(Query, extensions=[SQLAlchemySession])