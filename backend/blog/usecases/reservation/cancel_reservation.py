from blog.domain.entities.reservation import Reservation
from blog.domain.repositories.reservation_repository import ReservationRepository

class CancelReservationUseCase:
    def __init__(self, repository: ReservationRepository):
        self.repository = repository

    def execute(self, user_id: str, reservation_id: str) -> Reservation:
        return self.repository.cancel(user_id, reservation_id)
