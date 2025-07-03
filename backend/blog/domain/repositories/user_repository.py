from abc import ABC, abstractmethod
from blog.domain.entities.user import User

class UserRepository(ABC):
    @abstractmethod
    def login(self, email: str, password: str) -> User:
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
