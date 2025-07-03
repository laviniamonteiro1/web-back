
from blog.infra.repositories.in_memory_user_repository import InMemoryUserRepository
from blog.infra.repositories.in_memory_reservation_repository import InMemoryReservationRepository
from blog.infra.repositories.in_memory_bedroom_repository import (
    InMemoryBedroomRepository,
)

# Instâncias em memória para simulação
user_repo = InMemoryUserRepository()
reservation_repo = InMemoryReservationRepository()
bedroom_repo = InMemoryBedroomRepository()
