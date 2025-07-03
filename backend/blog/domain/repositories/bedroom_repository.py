from abc import ABC, abstractmethod
from blog.domain.entities.bedroom import Bedroom

class BedroomRepository(ABC):
    
    @abstractmethod
    def get_all(self) -> list[Bedroom]:
        pass
    
    @abstractmethod
    def get_by_id(self, bedroom_id: str) -> Bedroom | None:
        pass
