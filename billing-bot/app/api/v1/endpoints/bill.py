from fastapi import APIRouter, Depends, status
from sqlmodel import UUID
from app.domain.services.bill_service import BillService
from app.domain.models.bill import Bill
from app.api.schemas.bill import BillCreate, BillUpdate

router = APIRouter()


@router.get("/bills/{bill_id}", response_model=Bill)
def get_bill(
    bill_id: int | UUID, bill_service: BillService = Depends(BillService.get_instance)
):
    """
    Retrieve a bill by its ID.
    Args:
        bill_id (int | UUID): The unique identifier of the bill.
        bill_service (BillService, optional): The service instance to handle bill operations. Defaults to BillService.get_instance.
    Returns:
        Bill: The bill object corresponding to the provided ID.
    """
    return bill_service.get_bill(bill_id)


@router.get("/bills", response_model=list[Bill])
def get_all_bills(bill_service: BillService = Depends(BillService.get_instance)):
    """
    Retrieve all bills.

    This endpoint retrieves a list of all bills.

    Returns:
        list[Bill]: A list of all bills.

    Dependencies:
        bill_service (BillService): The service used to retrieve the bills.
    """
    return bill_service.get_all_bills()


@router.post("/bills", response_model=Bill, status_code=status.HTTP_201_CREATED)
def create_bill(
    bill_data: BillCreate, bill_service: BillService = Depends(BillService.get_instance)
):
    """
    Create a new bill.
    Args:
        bill_data (BillCreate): The data required to create a new bill.
        bill_service (BillService, optional): The service used to handle bill creation. Defaults to an instance of BillService.
    Returns:
        Bill: The created bill object.
    """
    return bill_service.create_bill(bill_data)


@router.put("/bills/{bill_id}", response_model=Bill)
def update_bill(
    bill_id: int | UUID,
    bill_data: BillUpdate,
    bill_service: BillService = Depends(BillService.get_instance),
):
    """
    Update an existing bill.

    This endpoint allows updating the details of an existing bill identified by its ID.

    Args:
        bill_id (int | UUID): The unique identifier of the bill to be updated.
        bill_data (BillUpdate): The new data for the bill.
        bill_service (BillService, optional): The service instance to handle bill operations. Defaults to BillService.get_instance.

    Returns:
        Bill: The updated bill object.
    """
    return bill_service.update_bill(bill_id, bill_data)


@router.delete("/bills/{bill_id}", response_model=Bill)
def delete_bill(
    bill_id: int | UUID, bill_service: BillService = Depends(BillService.get_instance)
):
    """
    Delete a bill by its ID.

    Args:
        bill_id (int | UUID): The ID of the bill to be deleted. Can be an integer or a UUID.
        bill_service (BillService, optional): The service instance used to delete the bill. Defaults to an instance of BillService.

    Returns:
        bool: True if the bill was successfully deleted, False otherwise.
    """
    return bill_service.delete_bill(bill_id)
