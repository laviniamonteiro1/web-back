from blog.domain.entities.reservation import Reservation
from blog.domain.repositories.reservation_repository import ReservationRepository

class UpdateReservationUseCase:
    def __init__(self, repository: ReservationRepository):
        self.repository = repository

    def execute(self, user_id: str, reservation_data: dict) -> Reservation:
        reservation = Reservation(
            id=reservation_data['id'],
            user_id=user_id,
            title=reservation_data['title'],
            address=reservation_data['address'],
            check_in=reservation_data['check_in'],
            check_out=reservation_data['check_out'],
            status=reservation_data['status']
        )
        return self.repository.update(user_id, reservation)
