from blog.domain.repositories.reservation_repository import ReservationRepository

class DeleteReservationUseCase:
    def __init__(self, repository: ReservationRepository):
        self.repository = repository

    def execute(self, user_id: str, reservation_id: str) -> None:
        self.repository.delete(user_id, reservation_id)
