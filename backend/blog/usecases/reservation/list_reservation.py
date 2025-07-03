from blog.domain.repositories.reservation_repository import ReservationRepository
from typing import List
from blog.domain.entities.reservation import Reservation

class ListUserReservationsUseCase:
    def __init__(self, repository: ReservationRepository):
        self.repository = repository

    def execute(self, user_id: str) -> List[Reservation]:
        return self.repository.get_all(user_id)
