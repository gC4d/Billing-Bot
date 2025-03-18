from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.db.session import get_db
from app.services.bill_service import BillService
from app.models.bill import Bill, BillCreate, BillUpdate

router = APIRouter()

def get_bill_service(db: Session = Depends(get_db)):
    return BillService(db)

@router.get("/bills/{bill_id}", response_model=Bill)
def get_bill(bill_id: int, bill_service: BillService = Depends(get_bill_service)):
    
    bill = bill_service.get_bill(bill_id)
    if not bill:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bill not found")
    return bill

@router.get("/bills", response_model=list[Bill])
def get_all_bills(bill_service: BillService = Depends(get_bill_service)):
    return bill_service.get_all_bills()

@router.post("/bills", response_model=Bill, status_code=status.HTTP_201_CREATED)
def create_bill(bill_data: BillCreate, bill_service: BillService = Depends(get_bill_service)):
    return bill_service.create_bill(bill_data)

@router.put("/bills/{bill_id}", response_model=Bill)
def update_bill(bill_id: int, bill_data: BillUpdate, bill_service: BillService = Depends(get_bill_service)):
    bill_service: BillService = Depends(get_bill_service)
    return bill_service.update_bill(bill_id, bill_data)

@router.delete("/bills/{bill_id}", response_model=Bill)
def delete_bill(bill_id: int, bill_service: BillService = Depends(get_bill_service)):
    return bill_service.delete_bill(bill_id)