from abc import ABC, abstractmethod
from typing import List

from sqlmodel import UUID
from app.domain.models.bill import Bill
from app.domain.models.costumer import Costumer
from app.domain.repositories.base_repository import BaseRepository

class IBillRepository(ABC, BaseRepository[Bill]):
    
    @abstractmethod
    def get_costumers(self, id: int) -> List[Costumer]:
        """Retrieve all costumers by a bill's unique identifier."""
        pass
