from __future__ import annotations
from typing import List
from sqlmodel import Relationship, SQLModel, Field
from app.domain.models.bill import Bill
from app.domain.models.costumer_bill import CostumerBill

class Costumer(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    phone: str = Field(nullable=False)
    
    bills: List[Bill] = Relationship(back_populates="costumer", link_model=CostumerBill)