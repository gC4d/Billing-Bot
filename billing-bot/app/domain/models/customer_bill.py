from typing import Optional
from sqlmodel import UUID, Field, SQLModel


class CustomerBill(SQLModel, table=True):
    customer_id: Optional[UUID] = Field(
        default=None, primary_key=True, foreign_key="customer.id"
    )

    bill_id: Optional[UUID] = Field(
        default=None, primary_key=True, foreign_key="bill.id"
    )
