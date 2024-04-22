from datetime import datetime
from fastapi import APIRouter, HTTPException, status

from schemas.appointment import appointments, Appointment
from schemas.doctor import doctors
from schemas.patient import patients
from services.patient import Patient_Service 
from services.doctor import Doctor_Service 
from services.appointment import Appointment_Service 

appointment_router = APIRouter()

@appointment_router.post("/{patient_id}", status_code=status.HTTP_201_CREATED)
def create_appointment(patient_id: int):
    patient = Patient_Service.get_patient(patient_id)
    available_doctor_id = Doctor_Service.check_available_doctor()
    if available_doctor_id == 0:  #check available doctors
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No available doctors")
    appointment = Appointment_Service.create_appointment(patient_id, available_doctor_id)
    appointments.append(appointment)
    Doctor_Service.set_doctor_availability(available_doctor_id, False)
    return {"message": "Appointment created succesfully", "data": appointment}

@appointment_router.post("/{appointment_id}/complete", status_code=status.HTTP_201_CREATED)
def complete_appointment(appointment_id: int):
    new_appointment = None
    for appointment in appointments:
        if appointment.id == appointment_id:
            new_appointment = appointment
    if not new_appointment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,  detail= "Appointment not found") 
    Doctor_Service.set_doctor_availability(new_appointment.doctor_id, True)
    appointments.remove(appointment)
    return {"message": "Appointment completed."}

@appointment_router.delete("/{appointment_id}/cancel", status_code=status.HTTP_201_CREATED)
def cancel_appointment(appointment_id: int):
    new_appointment = None
    for appointment in appointments:
        if appointment.id == appointment_id:
            new_appointment = appointment
    if not new_appointment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,  detail= "Appointment not found") 
    Doctor_Service.set_doctor_availability(new_appointment.doctor_id, True)
    appointments.remove(appointment)
    return {"message": "Appointment cancelled."}
    