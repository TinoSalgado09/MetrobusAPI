import strawberry

from app.models import City as CityModel




@strawberry.type
class City:
    id: strawberry.ID
    name: str

    @classmethod
    def from_instance(cls, instance: CityModel):
        return cls(
            id=instance.id,
            name=instance.name
        )