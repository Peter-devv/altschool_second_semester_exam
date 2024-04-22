from fastapi import HTTPException, status
from schemas.patient import Patient, CreatePatient, patients

class Patient_Service:
    @staticmethod
    def create_patient(payload: CreatePatient):
        patient_id = len(patients) + 1
        patient = Patient(
            id=patient_id,
            name=payload.name, 
            age=payload.age,                                            
            sex=payload.sex,
            weight=payload.weight,
            height=payload.height,
            phone=payload.phone
        )
        patients.append(patient)
        return patient
    
    @staticmethod
    def get_patient(patient_id: int):
        patient = next((patient for patient in patients if patient.id == patient_id), None)
        if not patient:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="patient not found")
        return patient
    
    @staticmethod
    def update_patient(patient_id: int, payload: CreatePatient):
        patient = Patient_Service.get_patient(patient_id)
        patient.name = payload.name
        patient.age = payload.age
        patient.sex = payload.sex
        patient.weight = payload.weight
        patient.height = payload.height
        patient.phone = payload.phone
        return patient
    
    @staticmethod
    def delete_patient(patient_id: int):
        patient = Patient_Service.get_patient(patient_id)
        patients.remove(patient)