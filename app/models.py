from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Float
from typing import Optional


Base = declarative_base()

""" This class allow create a model base for Vehicle.
    
    Features:
        id (int): unique identifier for each vehicle
        label (int): indicate the economic number of the vehicle
        current_status: indicates the current status of the vehicle
"""
class Vehicle(Base):
    __tablename__ = "vehicle"
    id: int = Column(Integer, primary_key=True, index=True)
    label: int = Column(Integer, nullable=False, unique=True)
    current_status: int = Column(Integer, nullable=False)

    ubication = relationship("Ubication")




""" This class allow create a model base for City.
    
    Features:
        id (int): unique identifier for each city
        name (str): indicates the name of the city
"""
class City(Base):
    __tablename__ = "city"
    id: int = Column(Integer, primary_key=True, index=True)
    name: int = Column(String, nullable=False, unique=True)

    ubication = relationship("Ubication")



""" This class allow create a model base for Location.
    
    Features:
        id (int): unique identifier for each location
        latitude (float): indicate the latitude of a geographic point
        longitude (float): indicate the longitude of a geographic point
        vehicle_id: foreign key that identifies which vehicle this location belongs to
        city_id: foreign key that identifies which city this location belongs to
"""
class Ubication(Base):
    __tablename__ = "ubication"
    id: int = Column(Integer, primary_key=True, index=True)
    latitude: float = Column(Float, nullable=False)
    longitude: float = Column(Float, nullable=False)
    vehicle_id: Optional[int] = Column(Integer, ForeignKey(Vehicle.id), nullable=False)
    vehicle = relationship("Vehicle", back_populates="ubication")

    city_id: Optional[int] = Column(Integer, ForeignKey(City.id), nullable=False)
    city = relationship("City", back_populates="ubication")



    