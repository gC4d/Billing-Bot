from sqlmodel import Field, SQLModel

class Bill(SQLModel, table=True):
    
    id: int = Field(default=None, primary_key=True)
    description: str = Field(default=None)
    amount: float = Field(nullable=False)
    payment_date: int = Field(nullable=False)
    billing_interval: int = Field(nullable=False)
    payment_cycles: int = Field(nullable=False)