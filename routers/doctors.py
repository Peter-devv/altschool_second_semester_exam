from fastapi import APIRouter, HTTPException, status
from schemas.doctor import CreateDoctor, doctors
from services.doctor import Doctor_Service

doctor_router = APIRouter()

@doctor_router.post("/", status_code=status.HTTP_201_CREATED)
def create_doctor(payload: CreateDoctor):
    doctor = Doctor_Service.create_doctor(payload) 
    return {"message": "Doctor successfully created", "data": doctor}

@doctor_router.get("/", status_code=status.HTTP_200_OK)
def get_all_doctors():
    return {"message": "success", "data": doctors}

@doctor_router.get("/{doctor_id}", status_code=status.HTTP_200_OK)
def get_student(doctor_id: int):
    doctor = Doctor_Service.get_doctor(doctor_id) 
    return {"message": "success", "data": doctor}

@doctor_router.put("/{doctor_id}", status_code=status.HTTP_200_OK)
def update_doctor(doctor_id: int, payload: CreateDoctor):
    doctor = Doctor_Service.update_doctor(doctor_id, payload)  
    return {"message": "Doctor successfully updated", "data": doctor}

@doctor_router.delete("/{doctor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_doctor(doctor_id: int):
    Doctor_Service.delete_doctor(doctor_id)

@doctor_router.put("/{doctor_id}/set_availability_status", status_code=status.HTTP_200_OK)
def set_availability_status(doctor_id: int, is_available: bool = False):
    doctor = Doctor_Service.get_doctor(doctor_id)
    doctor.is_available = is_available
    return {"message": "Doctor unavailable", "data": doctor}