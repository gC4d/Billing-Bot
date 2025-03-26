from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional

from sqlmodel import UUID

T = TypeVar("T")


class BaseRepository(ABC, Generic[T]):
    @abstractmethod
    def get_by_id(self, entity_id: int | UUID) -> Optional[T]:
        """Retrieve a entity by its unique identifier."""
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        """Retrieve all entities."""
        pass

    @abstractmethod
    def create(self, entity: T) -> T:
        """Create a new entity."""
        pass

    @abstractmethod
    def update(self, entity: T) -> Optional[T]:
        """Update an existing entity."""
        pass

    @abstractmethod
    def delete(self, entity_id: int | UUID) -> None:
        """Delete an existing entity."""
        pass
