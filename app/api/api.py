from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.db.session import get_db
from app.schemas.schemas import (
    DoctorCreate, Doctor, Token,
    PacienteCreate, Paciente,
    HistorialClinicoCreate, HistorialClinico
)
from app.crud.crud import (
    create_doctor, authenticate_doctor, get_doctor,
    create_patient, get_patient, update_patient, delete_patient,
    create_medical_history, get_medical_history, update_medical_history, delete_medical_history
)
from app.security import create_access_token

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# --- Doctor Auth ---
@router.post("/register", response_model=Doctor)
def register(doctor: DoctorCreate, db: Session = Depends(get_db)):
    db_doctor = create_doctor(db, doctor)
    return db_doctor

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    doctor = authenticate_doctor(db, form_data.username, form_data.password)
    if not doctor:
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    access_token = create_access_token(data={"sub": doctor.correo_electronico})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/doctor/{doctor_id}", response_model=Doctor)
def read_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = get_doctor(db, doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    return doctor

# --- Paciente ---
@router.post("/patients/", response_model=Paciente)
def create_patient_endpoint(patient: PacienteCreate, db: Session = Depends(get_db)):
    return create_patient(db, patient)

@router.get("/patients/{patient_id}", response_model=Paciente)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = get_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return patient

@router.put("/patients/{patient_id}", response_model=Paciente)
def update_patient_endpoint(patient_id: int, patient: PacienteCreate, db: Session = Depends(get_db)):
    updated = update_patient(db, patient_id, patient)
    if not updated:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return updated

@router.delete("/patients/{patient_id}")
def delete_patient_endpoint(patient_id: int, db: Session = Depends(get_db)):
    deleted = delete_patient(db, patient_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return {"ok": True}

# --- Historial Clínico ---
@router.post("/medical_history/", response_model=HistorialClinico)
def create_medical_history_endpoint(medical_history: HistorialClinicoCreate, db: Session = Depends(get_db)):
    return create_medical_history(db, medical_history)

@router.get("/medical_history/{history_id}", response_model=HistorialClinico)
def read_medical_history(history_id: int, db: Session = Depends(get_db)):
    history = get_medical_history(db, history_id)
    if not history:
        raise HTTPException(status_code=404, detail="Historial clínico no encontrado")
    return history

@router.put("/medical_history/{history_id}", response_model=HistorialClinico)
def update_medical_history_endpoint(history_id: int, medical_history: HistorialClinicoCreate, db: Session = Depends(get_db)):
    updated = update_medical_history(db, history_id, medical_history)
    if not updated:
        raise HTTPException(status_code=404, detail="Historial clínico no encontrado")
    return updated

@router.delete("/medical_history/{history_id}")
def delete_medical_history_endpoint(history_id: int, db: Session = Depends(get_db)):
    deleted = delete_medical_history(db, history_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Historial clínico no encontrado")
    return {"ok": True}