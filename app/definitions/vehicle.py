import strawberry
from typing import Optional

from app.models import Vehicle as VehicleModel


@strawberry.type
class Vehicle:
    id: strawberry.ID
    label: int
    current_status: int

    @classmethod
    def from_instance(cls, instance: VehicleModel):
        return cls(
            id=instance.id,
            label=instance.label,
            current_status=instance.current_status
        )