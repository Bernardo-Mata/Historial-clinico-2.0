from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UsuarioBase(BaseModel):
    nombre: str
    apellidos: str
    correo_electronico: EmailStr
    profesion: Optional[str] = None
    telefono_celular: Optional[str] = None

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int
    created_at: Optional[datetime]
    usuario_id: Optional[int]
    class Config:
        orm_mode = True

class DoctorBase(BaseModel):
    nombre: str
    apellidos: str
    profesion: Optional[str] = None
    telefono_celular: Optional[str] = None
    correo_electronico: EmailStr
    sexo: Optional[str] = None
    cedula_profesional: Optional[str] = None
    area_medica: Optional[str] = None

class DoctorCreate(DoctorBase):
    password: str

class Doctor(DoctorBase):
    id: int
    class Config:
        orm_mode = True

class PacienteBase(BaseModel):
    nombre: str
    apellidos: str
    genero: Optional[str] = None
    edad: Optional[int] = None
    its: Optional[bool] = False
    problemas_cardiacos: Optional[bool] = False
    diabetes: Optional[bool] = False
    telefono: Optional[str] = None
    correo_electronico: Optional[EmailStr] = None
    fecha_nacimiento: Optional[datetime] = None

class PacienteCreate(PacienteBase):
    pass

class Paciente(PacienteBase):
    id: int
    class Config:
        orm_mode = True

class HistorialClinicoBase(BaseModel):
    paciente_id: int
    doctor_id: int
    medicamento: Optional[str] = None
    tratamiento: Optional[str] = None
    diagnostico: Optional[str] = None
    notas: Optional[str] = None
    fecha: Optional[datetime] = None

class HistorialClinicoCreate(HistorialClinicoBase):
    pass

class HistorialClinico(HistorialClinicoBase):
    id: int
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None