from __future__ import annotations

from typing import List
from sqlmodel import UUID, Field, Relationship, SQLModel
from app.domain.models.costumer import Costumer
from app.domain.models.costumer_bill import CostumerBill

class Bill(SQLModel, table=True):
    
    id: UUID = Field(default=None, primary_key=True)
    description: str = Field(default=None)
    amount: float = Field(nullable=False)
    payment_date: int = Field(nullable=False)
    billing_interval: int = Field(nullable=False)
    payment_cycles: int = Field(nullable=False)
    
    costumers : List[Costumer] = Relationship(back_populates="bill", link_model=CostumerBill)