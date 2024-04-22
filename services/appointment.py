from datetime import date
from schemas.appointment import Appointment, appointments, CreateAppointment
from schemas.doctor import doctors

class Appointment_Service:

    @staticmethod
    def create_appointment(patient_id: int, available_doctor_id: int):
        appointment_id = len(appointments) + 1
        appointment = Appointment(
            id=appointment_id,
            patient_id= patient_id,
            doctor_id= available_doctor_id,
            date= date.today()
        )
        return appointment