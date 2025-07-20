from sqlalchemy.orm import Session
from app.models.models import (
    Doctor, Paciente, HistorialClinico,
    Usuario, Consultorio, DoctorConsultorio
)
from app.schemas.schemas import (
    DoctorCreate, Doctor as DoctorSchema,
    PacienteCreate, Paciente as PacienteSchema,
    HistorialClinicoCreate, HistorialClinico as HistorialClinicoSchema
)
from app.security import hash_password, verify_password

# --- Doctor Auth y creación segura ---
def get_doctor_by_email(db: Session, email: str):
    return db.query(Doctor).filter(Doctor.correo_electronico == email).first()

def create_doctor(db: Session, doctor: DoctorCreate):
    hashed_pw = hash_password(doctor.password)
    db_doctor = Doctor(
        nombre=doctor.nombre,
        apellidos=doctor.apellidos,
        profesion=doctor.profesion,
        telefono_celular=doctor.telefono_celular,
        correo_electronico=doctor.correo_electronico,
        sexo=doctor.sexo,
        cedula_profesional=doctor.cedula_profesional,
        area_medica=doctor.area_medica,
        hashed_password=hashed_pw
    )
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def authenticate_doctor(db: Session, email: str, password: str):
    doctor = get_doctor_by_email(db, email)
    if doctor and verify_password(password, doctor.hashed_password):
        return doctor
    return None

# --- CRUD Paciente ---
def create_patient(db: Session, patient: PacienteCreate):
    db_patient = Paciente(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patient(db: Session, patient_id: int):
    return db.query(Paciente).filter(Paciente.id == patient_id).first()

def update_patient(db: Session, patient_id: int, patient: PacienteCreate):
    db_patient = db.query(Paciente).filter(Paciente.id == patient_id).first()
    if db_patient:
        for key, value in patient.dict().items():
            setattr(db_patient, key, value)
        db.commit()
        db.refresh(db_patient)
    return db_patient

def delete_patient(db: Session, patient_id: int):
    db_patient = db.query(Paciente).filter(Paciente.id == patient_id).first()
    if db_patient:
        db.delete(db_patient)
        db.commit()
    return db_patient

# --- CRUD Historial Clínico ---
def create_medical_history(db: Session, medical_history: HistorialClinicoCreate):
    db_history = HistorialClinico(**medical_history.dict())
    db.add(db_history)
    db.commit()
    db.refresh(db_history)
    return db_history

def get_medical_history(db: Session, history_id: int):
    return db.query(HistorialClinico).filter(HistorialClinico.id == history_id).first()

def update_medical_history(db: Session, history_id: int, medical_history: HistorialClinicoCreate):
    db_history = db.query(HistorialClinico).filter(HistorialClinico.id == history_id).first()
    if db_history:
        for key, value in medical_history.dict().items():
            setattr(db_history, key, value)
        db.commit()
        db.refresh(db_history)
    return db_history

def delete_medical_history(db: Session, history_id: int):
    db_history = db.query(HistorialClinico).filter(HistorialClinico.id == history_id).first()
    if db_history:
        db.delete(db_history)
        db.commit()
    return db_history

# --- CRUD Doctor (no reemplaza el create_doctor seguro de arriba) ---
def create_doctor_schema(db: Session, doctor: DoctorSchema):
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


