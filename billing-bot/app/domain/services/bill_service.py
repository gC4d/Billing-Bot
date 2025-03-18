from typing import Optional
from fastapi import Depends
from sqlmodel import Session
from app.infraestructure.database.session import get_db
from app.infraestructure.repositories import BillRepository
from app.domain.models.bill import Bill, BillCreate, BillUpdate


class BillService:

    def __init__(self, db: Session):
        self.bill_repo = BillRepository(db)

    def get_bill(self, bill_id: int) -> Optional[Bill]:
        return self.bill_repo.get_bill(bill_id)

    def get_all_bills(self) -> list[Bill]:
        return self.bill_repo.get_all_bills()

    def create_bill(self, bill_data: BillCreate) -> Bill:
        new_bill = Bill.model_validate(bill_data)
        return self.bill_repo.create_bill(new_bill)

    def update_bill(self, bill_id: int, bill_data: BillUpdate) -> Bill:
        updated_bill = Bill.model_validate(bill_data)
        return self.bill_repo.update_bill(bill_id, updated_bill)

    def delete_bill(self, bill_id: int) -> Bill:
        return self.bill_repo.delete_bill(bill_id)
    
    @staticmethod
    def get_instance(db: Session = Depends(get_db)):
        return BillService(db)