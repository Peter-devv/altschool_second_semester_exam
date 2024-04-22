from fastapi import FastAPI
from routers.patients import patient_router
from routers.doctors import doctor_router
from routers.appointments import appointment_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to MedAppoint Hub"}

app.include_router(patient_router, prefix="/patients", tags=["Patient"])
app.include_router(doctor_router, prefix="/doctors", tags=["Doctor"])
app.include_router(appointment_router, prefix="/appointments", tags=["Appointment"])
