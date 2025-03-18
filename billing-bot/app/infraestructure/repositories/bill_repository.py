from sqlmodel import Session, select
from typing import List, Optional
from app.domain.models.bill import Bill
from app.domain.models.costumer import Costumer
from app.domain.repositories.bill_repository import IBillRepository

class BillRepository(IBillRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, id: int) -> Optional[Bill]:
        statement = select(Bill).where(Bill.id == id)
        return self.db.exec(statement).first()

    def get_all(self) -> List[Bill]:
        statement = select(Bill)
        return self.db.exec(statement).all()

    def get_costumers(self, id: int) -> List[Costumer]:
        statement = select(Bill).where(Bill.id == id)
        bill = self.db.exec(statement).first()
        return bill.costumers if bill else []

    def create(self, bill: Bill) -> Bill:
        self.db.add(bill)
        self.db.commit()
        self.db.refresh(bill)
        return bill

    def update(self, bill: Bill) -> Bill:
        existing_bill = self.get_by_id(bill.id)
        if existing_bill:
            existing_bill.description = bill.description
            existing_bill.amount = bill.amount
            existing_bill.payment_date = bill.payment_date
            existing_bill.billing_interval = bill.billing_interval
            existing_bill.payment_cycles = bill.payment_cycles
            self.db.commit()
            self.db.refresh(existing_bill)
        return existing_bill

    def delete(self, id: int) -> None:
        bill = self.get_by_id(id)
        if bill:
            self.db.delete(bill)
            self.db.commit()