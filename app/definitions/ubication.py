import strawberry
from app.definitions.city import City
from app.definitions.vehicle import Vehicle
from app.models import Ubication as UbicationModel
from typing import Optional

@strawberry.type
class Ubication:
    id: strawberry.ID
    latitude: float
    longitude: float
    vehicle: Optional[Vehicle] = None
    city: Optional[City] = None

    @classmethod
    def from_instance(cls, model: UbicationModel):
        return cls(
            id=model.id,
            latitude=model.latitude,
            longitude=model.longitude,
            vehicle=Vehicle.from_instance(model.vehicle) if model.vehicle else None,
            city = City.from_instance(model.city) if model.city else None
        )