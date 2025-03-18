from fastapi import APIRouter
from app.api.v1.endpoints import bill


router = APIRouter(prefix="/v1")

router.include_router(bill.router)