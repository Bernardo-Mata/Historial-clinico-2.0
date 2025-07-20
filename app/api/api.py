from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.db.session import SessionLocal
from app.schemas import DoctorCreate, Doctor, Token
from app.crud import create_doctor, authenticate_doctor
from app.security import create_access_token
from app.models import Doctor as DoctorModel

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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