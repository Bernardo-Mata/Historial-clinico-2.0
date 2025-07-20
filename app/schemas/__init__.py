from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class PatientSchema(BaseModel):
    id: int
    name: str
    date_of_birth: datetime
    medical_history: List['MedicalHistorySchema'] = []

class DoctorSchema(BaseModel):
    id: int
    name: str
    specialty: str
    clinic_id: int

class MedicalHistorySchema(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    diagnosis: str
    treatment: str
    date: datetime

class ClinicSchema(BaseModel):
    id: int
    name: str
    address: str
    doctors: List[DoctorSchema] = []