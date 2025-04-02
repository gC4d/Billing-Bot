from __future__ import annotations

from datetime import date
from typing import List
from sqlmodel import UUID, Field, Relationship, SQLModel
from app.domain.models.bill import Bill
from app.domain.models.customer import Customer
from app.domain.models.customer_bill import CustomerBill


class BillInstallment(SQLModel, table=True):
    id: UUID = Field(default=None, primary_key=True)
    bill_id: UUID = Field(foreign_key="bill.id")
    payment_date: date = Field(nullable=False)

    bill: Bill = Relationship(back_populates="bill_installment")
    
    customers: List[Customer] = Relationship(
        back_populates="bill_installment", link_model=CustomerBill
    )
