from datetime import datetime
from pydantic import BaseModel 

class Appointment(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    date: datetime

class CreateAppointment(BaseModel):
    patient_id: int
    doctor_id: int
    date: datetime

appointments: list[Appointment] = [
    Appointment(id=0, patient_id=1, doctor_id=0, date=datetime(2024, 4, 17)),
    Appointment(id=1, patient_id=0, doctor_id=1, date=datetime(2024, 4, 1))
]