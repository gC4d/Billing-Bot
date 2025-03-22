import pytest
from app.domain.models.bill import Bill, BillFieldConfig
from app.infraestructure.database.session import get_db
from app.infraestructure.repositories.bill_repository import BillRepository


@pytest.fixture(name="session")
def session_fixture():
    with next(get_db()) as session:
        yield session


def test_should_create_bill_with_valid_parameters(session):
    bill_repository = BillRepository(session)
    bill = Bill(
        description="Monthly subscription",
        amount=29.99,
        billing_interval=1,
        payment_cycles=12,
    )
    created_bill = bill_repository.create(bill)

    assert created_bill.id is not None
    assert created_bill.description == "Monthly subscription"
    assert created_bill.amount == 29.99
    assert created_bill.billing_interval == 1
    assert created_bill.payment_cycles == 12


def test_should_create_bill_with_valid_minimum_values(session):
    bill_repository = BillRepository(session)
    bill = Bill(description="Basic", amount=0.01, billing_interval=1, payment_cycles=1)
    created_bill = bill_repository.create(bill)

    assert created_bill.id is not None
    assert created_bill.description == "Basic"
    assert created_bill.amount == 0.01
    assert created_bill.billing_interval == 1
    assert created_bill.payment_cycles == 1


def test_should_create_bill_with_valid_maximum_values(session):
    bill_repository = BillRepository(session)
    bill = Bill(
        description="L" * BillFieldConfig.DESCRIPTION_MAX,
        amount=999999.99,
        billing_interval=12,
        payment_cycles=120,
    )
    created_bill = bill_repository.create(bill)

    assert created_bill.id is not None
    assert created_bill.description == "L" * BillFieldConfig.DESCRIPTION_MAX
    assert created_bill.amount == 999999.99
    assert created_bill.billing_interval == 12
    assert created_bill.payment_cycles == 120


def test_should_not_create_bill_with_invalid_amount(session):
    BillRepository(session)
    with pytest.raises(ValueError):
        Bill(
            description="Invalid amount",
            amount=-10.00,
            billing_interval=1,
            payment_cycles=12,
        )


def test_should_not_create_bill_with_invalid_description(session):
    BillRepository(session)
    with pytest.raises(ValueError):
        Bill(description="", amount=29.99, billing_interval=1, payment_cycles=12)
