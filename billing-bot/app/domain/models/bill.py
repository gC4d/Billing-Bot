from __future__ import annotations

from typing import List
from sqlmodel import UUID, Field, Relationship, SQLModel
from app.domain.models.costumer import Costumer
from app.domain.models.costumer_bill import CostumerBill
from app.domain.models.bill_payment_schedule import BillPaymentSchedule

class BillFieldConfig:
    DESCRIPTION_MAX = 200
    DESCRIPTION_MIN = 10
    
    BILLING_MIN_INTERVAL = 1
    BILLING_MAX_INTERVAL = 12
    
    PAYMENT_CYCLES_MIN = 1

class Bill(SQLModel, table=True):
    
    id: UUID = Field(default=None, primary_key=True)
    description: str = Field(
        default=None, 
        max_length=BillFieldConfig.DESCRIPTION_MAX,
        min_length=BillFieldConfig.DESCRIPTION_MIN
    )
    amount: float = Field(nullable=False)
    billing_interval: int = Field(
        nullable=False,
        min_length=BillFieldConfig.BILLING_MIN_INTERVAL,
        max_length=BillFieldConfig.BILLING_MAX_INTERVAL
    )
    payment_cycles: int = Field(
        nullable=False,
        min_length=BillFieldConfig.PAYMENT_CYCLES_MIN
    )
    
    costumers: List[Costumer] = Relationship(back_populates="bill", link_model=CostumerBill)
    payment_schedule: List[BillPaymentSchedule] = Relationship(back_populates="bill")

