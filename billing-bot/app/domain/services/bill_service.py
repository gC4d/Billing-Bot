from typing import Optional
from fastapi import Depends
from sqlmodel import UUID, Session
from app.infraestructure.database.session import get_db
from app.infraestructure.repositories.bill_repository import BillRepository
from app.domain.models.bill import Bill
from app.api.schemas.bill import BillCreate, BillUpdate


class BillService:

    def __init__(self, db: Session):
        self.bill_repo = BillRepository(db)

    def get_bill(self, bill_id: UUID) -> Optional[Bill]:
        return self.bill_repo.get_by_id(bill_id)

    def get_all_bills(self) -> list[Bill]:
        return self.bill_repo.get_all()

    def create_bill(self, bill_data: BillCreate) -> Bill:
        new_bill = Bill.model_validate(bill_data)
        return self.bill_repo.create(new_bill)

    def update_bill(self, bill_id: UUID, bill_data: BillUpdate) -> Bill:
        updated_bill = Bill.model_validate(bill_data)
        return self.bill_repo.update(bill_id, updated_bill)

    def delete_bill(self, bill_id: UUID) -> None:
        self.bill_repo.delete(bill_id)

    @staticmethod
    def get_instance(db: Session = Depends(get_db)):
        return BillService(db)
