from blog.domain.repositories.bedroom_repository import BedroomRepository
from blog.domain.entities.bedroom import Bedroom
from typing import List

class InMemoryBedroomRepository(BedroomRepository):
    def __init__(self):
        self._bedrooms = {}

    def get_all(self) -> List[Bedroom]:
        return list(self._bedrooms.values())

    def get_by_id(self, bedroom_id: str) -> Bedroom | None:
        return self._bedrooms.get(bedroom_id, None)
