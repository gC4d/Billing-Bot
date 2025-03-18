from typing import Optional
from sqlmodel import Field, SQLModel


class CostumerBill(SQLModel, table=True):
    costumer_id : Optional[int] = Field(
        default=None, primary_key=True, foreign_key="costumer.id")
    
    bill_id : Optional[int] = Field(
        default=None, primary_key=True, foreign_key="bill.id")