from abc import ABC, abstractmethod
from blog.domain.entities.reservation import Reservation
from typing import List, Optional

class ReservationRepository(ABC):

    @abstractmethod
    def create(self, user_id: str, reservation: Reservation) -> Reservation:
        pass

    @abstractmethod
    def update(self, user_id: str, reservation: Reservation) -> Reservation:
        pass

    @abstractmethod
    def delete(self, user_id: str, reservation_id: str) -> None:
        pass

    @abstractmethod
    def get_all(self, user_id: str) -> List[Reservation]:
        pass

    @abstractmethod
    def get_by_id(self, user_id: str, reservation_id: str) -> Optional[Reservation]:
        pass

    @abstractmethod
    def cancel(self, user_id: str, reservation_id: str) -> Reservation:
        pass