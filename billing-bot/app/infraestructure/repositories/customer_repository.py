from typing import List, Optional
from sqlmodel import UUID, Session, select
from app.domain.models.customer import Customer
from app.domain.repositories.base_repository import BaseRepository


class CustomerRepository(BaseRepository[Customer]):

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, id: int | UUID) -> Optional[Customer]:
        statement = select(Customer).where(Customer.id == id)
        return self.db.exec(statement).first()

    def get_all(self) -> List[Customer]:
        statement = select(Customer)
        return list(self.db.exec(statement).all())

    def create(self, customer: Customer) -> Customer:
        self.db.commit()
        self.db.refresh(customer)
        return customer

    def update(self, customer: Customer) -> Optional[Customer]:
        existing_customer = self.get_by_id(customer.id)
        if existing_customer:
            existing_customer.name = customer.name
            existing_customer.phone = customer.phone

            self.db.commit()
            self.db.refresh(existing_customer)
        return existing_customer

    def delete(self, id: int | UUID) -> None:
        customer = self.get_by_id(id)
        if customer:
            self.db.delete(customer)
            self.db.commit()
