
from sqlalchemy.orm import Session
from app.models import Doctor
from app.schemas import DoctorCreate
from app.security import hash_password, verify_password

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