from __future__ import annotations

from typing import List
from sqlmodel import UUID, Field, Relationship, SQLModel
from app.domain.models.costumer import Costumer
from app.domain.models.costumer_bill import CostumerBill

class FieldConfig:
    DESCRIPTION_MAX = 200
    DESCRIPTION_MIN = 10

class Bill(SQLModel, table=True):
    
    id: UUID = Field(default=None, primary_key=True)
    description: str = Field(
        default=None, 
        max_length=FieldConfig.DESCRIPTION_MAX,
        min_length=FieldConfig.DESCRIPTION_MIN
    )
    amount: float = Field(nullable=False)
    payment_date: int = Field(nullable=False,) # NORMALIZAR - IMPLEMENTAR UM MODELO QUE ARMAZENE AS DATAS DE PAGAMENTO
    billing_interval: int = Field(nullable=False)
    payment_cycles: int = Field(nullable=False)
    
    costumers : List[Costumer] = Relationship(back_populates="bill", link_model=CostumerBill)
    