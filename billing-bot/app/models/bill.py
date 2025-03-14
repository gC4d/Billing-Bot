from sqlalchemy import Column, Float, Integer, String

class Bill:
    
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    