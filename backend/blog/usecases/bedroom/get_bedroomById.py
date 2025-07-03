from blog.domain.repositories.bedroom_repository import BedroomRepository
from blog.domain.entities.bedroom import Bedroom
from typing import Optional

class GetBedroomByIdUseCase:
    def __init__(self, repository: BedroomRepository):
        self.repository = repository

    def execute(self, bedroom_id: str) -> Optional[Bedroom]:
        return self.repository.get_by_id(bedroom_id)
