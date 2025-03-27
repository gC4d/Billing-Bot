from abc import ABC, abstractmethod
from typing import List

from sqlmodel import UUID
from app.domain.models.bill import Bill
from app.domain.models.customer import Customer
from app.domain.repositories.base_repository import BaseRepository


class IBillRepository(BaseRepository[Bill], ABC):

    @abstractmethod
    def get_costumers(self, id: int | UUID) -> List[Customer]:
        """Retrieve all costumers by a bill's unique identifier."""
        pass
