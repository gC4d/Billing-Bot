from sqlalchemy.orm import Session
from app.models.bill import Bill

class BillRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_bill(self, bill_id: int):
        return self.db.query(Bill).filter(Bill.id == bill_id).first()

    def get_all_bills(self):
        return self.db.query(Bill).all()

    def create_bill(self, bill: Bill):
        self.db.add(bill)
        self.db.commit()
        self.db.refresh(bill)
        return bill

    def update_bill(self, bill_id: int, updated_bill: Bill):
        bill = self.get_bill(bill_id)
        if bill:
            bill.description = updated_bill.description
            bill.amount = updated_bill.amount
            self.db.commit()
            self.db.refresh(bill)
        return bill

    def delete_bill(self, bill_id: int):
        bill = self.get_bill(bill_id)
        if bill:
            self.db.delete(bill)
            self.db.commit()
        return bill