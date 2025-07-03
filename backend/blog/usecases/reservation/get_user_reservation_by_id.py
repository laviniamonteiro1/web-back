from blog.domain.repositories.reservation_repository import ReservationRepository
from blog.domain.entities.reservation import Reservation
from typing import Optional

class GetUserReservationByIdUseCase:
    def __init__(self, repository: ReservationRepository):
        self.repository = repository

    def execute(self, user_id: str, reservation_id: str) -> Optional[Reservation]:
        return self.repository.get_by_id(user_id, reservation_id)