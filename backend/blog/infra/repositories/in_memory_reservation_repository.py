from blog.domain.repositories.reservation_repository import ReservationRepository
from blog.domain.entities.reservation import Reservation
from typing import List, Optional

class InMemoryReservationRepository(ReservationRepository):
    def __init__(self):
        self._reservations = {}

    def create(self, user_id: str, reservation: Reservation) -> Reservation:
        self._reservations[reservation.id] = reservation
        return reservation

    def update(self, user_id: str, reservation: Reservation) -> Reservation:
        existing_reservation = self._reservations.get(reservation.id)
        if not existing_reservation or existing_reservation.user_id != user_id:
            raise ValueError("Reserva não encontrada para este usuário.")
        
        self._reservations[reservation.id] = reservation
        return reservation

    def delete(self, user_id: str, reservation_id: str) -> None:
        reservation = self._reservations.get(reservation_id)
        if reservation and reservation.user_id == user_id:
            self._reservations.pop(reservation_id)
        else:
            raise ValueError("Reserva não encontrada para este usuário.")

    def get_all(self, user_id: str) -> List[Reservation]:
        return [reservation for reservation in self._reservations.values() if reservation.user_id == user_id]

    def get_by_id(self, user_id: str, reservation_id: str) -> Optional[Reservation]:
        reservation = self._reservations.get(reservation_id)
        if reservation and reservation.user_id == user_id:
            return reservation
        return None

    def cancel(self, user_id: str, reservation_id: str) -> Reservation:
        reservation = self._reservations.get(reservation_id)
        if not reservation or reservation.user_id != user_id:
            raise ValueError("Reserva não encontrada para este usuário.")
        
        if reservation.status == "Cancelada":
            raise ValueError("Reserva já está cancelada.")
        
        reservation.status = "Cancelada"
        return reservation