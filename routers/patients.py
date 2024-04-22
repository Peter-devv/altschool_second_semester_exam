from fastapi import APIRouter, HTTPException, status

from schemas.patient import CreatePatient, patients
from services.patient import Patient_Service

patient_router = APIRouter()

@patient_router.post("/", status_code=status.HTTP_201_CREATED)
def create_patient(payload: CreatePatient):
    patient = Patient_Service.create_patient(payload)
    return {"message": "Patient successfully created", "data": patient}

@patient_router.get("/{patient_id}", status_code=status.HTTP_200_OK)
def get_patient(patient_id: int):
    patient = Patient_Service.get_patient(patient_id)
    return {"message": "success", "data": patient}

@patient_router.get("/", status_code=status.HTTP_200_OK)
def get_all_patients():
    return {"message": "success", "data": patients}
    
@patient_router.put("/{patient_id}", status_code=status.HTTP_200_OK)
def update_patient(patient_id: int, payload: CreatePatient):
    patient = Patient_Service.update_patient(patient_id, payload) 
    return {"message": "Patient successfully updated", "data": patient}

@patient_router.delete("/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(patient_id: int):
    Patient_Service.delete_patient(patient_id)