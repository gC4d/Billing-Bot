from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class BillBase(BaseModel):
    description: Optional[str] = None
    amount: float
    payment_date: int
    billing_interval: int
    payment_cycles: int


class BillCreate(BillBase):
    pass


class BillUpdate():
    description: Optional[str] = None
    amount: Optional[float] = None
    payment_date: Optional[int] = None
    billing_interval: Optional[int] = None
    payment_cycles: Optional[int] = None


class BillInDBBase(BillBase):
    id: UUID

    class Config:
        orm_mode: True


class Bill(BillInDBBase):
    pass


class BillInDB(BillInDBBase):
    pass
