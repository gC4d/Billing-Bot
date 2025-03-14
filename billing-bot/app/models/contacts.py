from sqlalchemy import Column, Integer, String

class Contact:
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)