from fastapi import HTTPException, status
from schemas.doctor import doctors, CreateDoctor, Doctor

class Doctor_Service:
    @staticmethod
    def create_doctor(payload: CreateDoctor) -> Doctor:
        doctor_id = len(doctors) + 1
        doctor = Doctor(
            id=doctor_id,
            name=payload.name,
            specialization=payload.specialization,
            phone=payload.phone,
            is_available=payload.is_available
        )
        doctors.append(doctor)
        return doctor

    @staticmethod
    def get_doctor(doctor_id: int) -> Doctor:
        doctor = next((doctor for doctor in doctors if doctor.id == doctor_id), None)
        if not doctor:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="doctor not found")
        return doctor
    
    @staticmethod 
    def update_doctor(doctor_id: int, payload: CreateDoctor):
        doctor = Doctor_Service.get_doctor(doctor_id)
        doctor.name = payload.name
        doctor.specialization = payload.specialization
        doctor.phone = payload.phone
        doctor.is_available = payload.is_available
        return doctor

    @staticmethod 
    def delete_doctor(doctor_id: int):
        doctor = Doctor_Service.get_doctor(doctor_id)
        doctors.remove(doctor)

    @staticmethod
    def check_available_doctor() -> int:
        available_doctor_id: int = 0
        for doctor in doctors:
            if doctor.is_available:
                available_doctor_id = doctor.id
                break
        return available_doctor_id
    
    @staticmethod 
    def set_doctor_availability(doctor_id: int, is_available: bool) -> None:
        for doctor in doctors:
            if doctor.id == doctor_id:
                doctor.is_available = is_available
                break
