from __future__ import annotations
from typing import List
from sqlmodel import UUID, Relationship, SQLModel, Field
from app.domain.models.bill import Bill
from app.domain.models.customer_bill import CustomerBill


class CustomerFieldConfig:
    NAME_MAX = 100
    NAME_MIN = 5


class Customer(SQLModel, table=True):
    id: UUID = Field(default=None, primary_key=True)
    name: str = Field(
        nullable=False,
        max_length=CustomerFieldConfig.NAME_MAX,
        min_length=CustomerFieldConfig.NAME_MIN,
    )
    phone: str = Field(nullable=False)

    bills: List[Bill] = Relationship(back_populates="customer", link_model=CustomerBill)
