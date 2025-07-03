from blog.domain.repositories.bedroom_repository import BedroomRepository
from typing import List
from blog.domain.entities.bedroom import Bedroom

class ListBedroomsUseCase:
    def __init__(self, repository: BedroomRepository):
        self.repository = repository

    def execute(self) -> List[Bedroom]:
        return self.repository.get_all()
