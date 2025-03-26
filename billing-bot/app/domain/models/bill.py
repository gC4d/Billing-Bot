from __future__ import annotations

from datetime import datetime, timezone
from typing import List
from sqlmodel import UUID, Enum, Field, Relationship, SQLModel
from app.domain.models.costumer import Costumer
from app.domain.models.costumer_bill import CostumerBill
from app.domain.models.bill_payment_schedule import BillPaymentSchedule


class BillingInterval(str, Enum):
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    BIANNUALLY = "biannually"
    ANNUALLY = "annually"


class BillStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    OVERDUE = "overdue"


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
        min_length=BillFieldConfig.DESCRIPTION_MIN,
    )
    amount: float = Field(nullable=False)
    billing_interval: BillingInterval = Field(
        default=BillingInterval.MONTHLY, nullable=False
    )
    payment_cycles: int = Field(
        default=1, nullable=False, ge=BillFieldConfig.PAYMENT_CYCLES_MIN
    )
    status: BillStatus = Field(default=BillStatus.PENDING, nullable=False)
    created_at: datetime = Field(default=datetime.now(timezone.utc), index=True)
    updated_at: datetime = Field(
        default=datetime.now(timezone.utc),
        sa_column_kwargs={"onupdate": datetime.now(timezone.utc)}
    )

    costumers: List[Costumer] = Relationship(
        back_populates="bill", link_model=CostumerBill
    )
    payment_schedule: List[BillPaymentSchedule] = Relationship(back_populates="bill")
