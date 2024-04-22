from pydantic import BaseModel

class Doctor(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    is_available: bool = True

class CreateDoctor(BaseModel):
    name: str
    specialization: str
    phone: str
    is_available: bool = True

doctors: list[Doctor] = [
    Doctor(id=0, name="Dr. James", specialization="Dentist", phone="08042452585", is_available=True),
    Doctor(id=1 , name="Dr. Phil", specialization="Surgeon", phone="09042527525", is_available=False)
]