from sqlmodel import SQLModel, Session, select
from app.models.contacts import Contact

class ContactRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_contact(self, contact_id: int):
        statement = select(Contact).where(Contact.id == contact_id)
        return self.db.exec(statement).first()

    def get_all_contacts(self):
        statement = select(Contact)
        return self.db.exec(statement).all()

    def create_contact(self, name: str, phone: str):
        new_contact = Contact(name=name, phone=phone)
        self.db.add(new_contact)
        self.db.commit()
        self.db.refresh(new_contact)
        return new_contact

    def update_contact(self, contact_id: int, name: str = None, phone: str = None):
        statement = select(Contact).where(Contact.id == contact_id)
        contact = self.db.exec(statement).first()
        if contact:
            if name:
                contact.name = name
            if phone:
                contact.phone = phone
            self.db.add(contact)
            self.db.commit()
            self.db.refresh(contact)
        return contact

    def delete_contact(self, contact_id: int):
        statement = select(Contact).where(Contact.id == contact_id)
        contact = self.db.exec(statement).first()
        if contact:
            self.db.delete(contact)
            self.db.commit()
        return contact