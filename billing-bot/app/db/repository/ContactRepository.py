from sqlalchemy.orm import Session
from app.models.contacts import Contact

class ContactRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_contact(self, contact_id: int):
        return self.db.query(Contact).filter(Contact.id == contact_id).first()

    def get_all_contacts(self):
        return self.db.query(Contact).all()

    def create_contact(self, name: str, phone: str):
        new_contact = Contact(name=name, phone=phone)
        self.db.add(new_contact)
        self.db.commit()
        self.db.refresh(new_contact)
        return new_contact

    def update_contact(self, contact_id: int, name: str = None, phone: str = None):
        contact = self.db.query(Contact).filter(Contact.id == contact_id).first()
        if contact:
            if name:
                contact.name = name
            if phone:
                contact.phone = phone
            self.db.commit()
            self.db.refresh(contact)
        return contact

    def delete_contact(self, contact_id: int):
        contact = self.db.query(Contact).filter(Contact.id == contact_id).first()
        if contact:
            self.db.delete(contact)
            self.db.commit()
        return contact