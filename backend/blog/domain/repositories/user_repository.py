from abc import ABC, abstractmethod
from typing import Optional # Importar Optional

from blog.domain.entities.user import User
from blog.domain.value_objects.email_vo import Email # Importar Email
from blog.domain.value_objects.password import Password # Importar Password

class UserRepository(ABC):
    @abstractmethod
    def login(self, email: Email, password: Password) -> Optional[User]: # Tipos de argumento e retorno atualizados
        pass

    @abstractmethod
    def register(self, user: User) -> User:
        pass

    @abstractmethod
    def logout(self) -> None:
        pass

    @abstractmethod
    def get_current_user(self) -> User | None:
        pass

    @abstractmethod
    def set_current_user(self, user: User) -> None:
        pass
