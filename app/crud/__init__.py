from sqlalchemy.orm import Session
from app.models import Patient, Doctor, MedicalHistory, Clinic
from app.schemas import PatientSchema, DoctorSchema, MedicalHistorySchema

def create_patient(db: Session, patient: PatientSchema):
    db_patient = Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patient(db: Session, patient_id: int):
    return db.query(Patient).filter(Patient.id == patient_id).first()

def update_patient(db: Session, patient_id: int, patient: PatientSchema):
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if db_patient:
        for key, value in patient.dict().items():
            setattr(db_patient, key, value)
        db.commit()
        db.refresh(db_patient)
    return db_patient

def delete_patient(db: Session, patient_id: int):
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if db_patient:
        db.delete(db_patient)
        db.commit()
    return db_patient

def create_medical_history(db: Session, medical_history: MedicalHistorySchema):
    db_history = MedicalHistory(**medical_history.dict())
    db.add(db_history)
    db.commit()
    db.refresh(db_history)
    return db_history

def get_medical_history(db: Session, history_id: int):
    return db.query(MedicalHistory).filter(MedicalHistory.id == history_id).first()

def update_medical_history(db: Session, history_id: int, medical_history: MedicalHistorySchema):
    db_history = db.query(MedicalHistory).filter(MedicalHistory.id == history_id).first()
    if db_history:
        for key, value in medical_history.dict().items():
            setattr(db_history, key, value)
        db.commit()
        db.refresh(db_history)
    return db_history

def delete_medical_history(db: Session, history_id: int):
    db_history = db.query(MedicalHistory).filter(MedicalHistory.id == history_id).first()
    if db_history:
        db.delete(db_history)
        db.commit()
    return db_history

def create_doctor(db: Session, doctor: DoctorSchema):
    db_doctor = Doctor(**doctor.dict())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def get_doctor(db: Session, doctor_id: int):
    return db.query(Doctor).filter(Doctor.id == doctor_id).first()

def update_doctor(db: Session, doctor_id: int, doctor: DoctorSchema):
    db_doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if db_doctor:
        for key, value in doctor.dict().items():
            setattr(db_doctor, key, value)
        db.commit()
        db.refresh(db_doctor)
    return db_doctor

def delete_doctor(db: Session, doctor_id: int):
    db_doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if db_doctor:
        db.delete(db_doctor)
        db.commit()
    return db_doctor