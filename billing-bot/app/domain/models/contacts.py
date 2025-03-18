from sqlmodel import SQLModel, Field

class Contact(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    phone: str = Field(nullable=False)
    
    bill : int = Field(default=None, foreign_key="bill.id")