from sqlmodel import Session, select
from app.domain.models.bill import Bill

class BillRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_bill(self, bill_id: int) -> Bill:
        statement = select(Bill).where(Bill.id == bill_id)
        return self.db.exec(statement).first()

    def get_all_bills(self) -> list[Bill]:
        statement = select(Bill)
        return self.db.exec(statement).all()

    def create_bill(self, bill: Bill) -> Bill:
        self.db.add(bill)
        self.db.commit()
        self.db.refresh(bill)
        return bill

    def update_bill(self, bill_id: int, updated_bill: Bill) -> Bill:
        bill = self.get_bill(bill_id)
        if bill:
            bill.description = updated_bill.description
            bill.amount = updated_bill.amount
            bill.payment_date = updated_bill.payment_date
            bill.billing_interval = updated_bill.billing_interval
            bill.payment_cycles = updated_bill.payment_cycles
            self.db.commit()
            self.db.refresh(bill)
        return bill

    def delete_bill(self, bill_id: int) -> Bill:
        bill = self.get_bill(bill_id)
        if bill:
            self.db.delete(bill)
            self.db.commit()
        return bill