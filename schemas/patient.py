from pydantic import BaseModel
from decimal import Decimal

class Patient(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: Decimal
    height: Decimal
    phone: str

class CreatePatient(BaseModel):
    name: str
    age: int
    sex: str
    weight: Decimal
    height: Decimal
    phone: str

patients: list[Patient] = [
    Patient(id=0, name="Paul", age=23, sex="Male", weight=Decimal('34.5'), height=2.53, phone="08082998285"),
    Patient(id=1, name="Princess", age=34, sex="Female", weight=Decimal('56.35'), height=2.75, phone="08023047229")
]