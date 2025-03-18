from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.models.bill import Bill


class IBillRepository(ABC):
    
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Bill]:
        """Retrieve a bill by its unique identifier."""
        pass

    @abstractmethod
    def get_all(self) -> List[Bill]:
        """Retrieve a bill by its unique identifier."""
        pass
    
    @abstractmethod
    def create(self, bill: Bill) -> Bill:
        """Create a new bill."""
        pass

    @abstractmethod
    def update(self, bill: Bill) -> Bill:
        """Update an existing bill."""
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        """Delete an existing bill."""
        pass