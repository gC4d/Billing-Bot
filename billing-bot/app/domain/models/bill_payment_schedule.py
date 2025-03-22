from __future__ import annotations

from datetime import date
from sqlmodel import UUID, Field, Relationship, SQLModel
from app.domain.models.bill import Bill


class BillPaymentSchedule(SQLModel, table=True):
    id: UUID = Field(default=None, primary_key=True)
    bill_id: UUID = Field(foreign_key="bill.id")
    payment_date: date = Field(nullable=False)

    bill: Bill = Relationship(back_populates="payment_schedule")
