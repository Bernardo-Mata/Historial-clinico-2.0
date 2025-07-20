from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text, Time
from sqlalchemy.orm import relationship
from app.db.session import Base

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    apellidos = Column(String(255), nullable=False)
    correo_electronico = Column(String(255), unique=True, index=True, nullable=False)
    profesion = Column(String(255))
    telefono_celular = Column(String(20))
    created_at = Column(DateTime)
    usuario_id = Column(Integer)

class Doctor(Base):
    __tablename__ = "doctor"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    apellidos = Column(String(255), nullable=False)
    profesion = Column(String(255))
    telefono_celular = Column(String(20))
    correo_electronico = Column(String(255), unique=True, index=True, nullable=False)
    sexo = Column(String(10))
    cedula_profesional = Column(String(50))
    area_medica = Column(String(100))
    hashed_password = Column(String(255), nullable=False)
    consultorios = relationship("DoctorConsultorio", back_populates="doctor")

class Consultorio(Base):
    __tablename__ = "consultorio"
    id = Column(Integer, primary_key=True, index=True)
    nombre_consultorio = Column(String(255), nullable=False)
    direccion = Column(String(255))
    capacidad_doctores = Column(Integer)
    horario = Column(Time)
    numero_contacto = Column(String(20))
    doctores = relationship("DoctorConsultorio", back_populates="consultorio")

class DoctorConsultorio(Base):
    __tablename__ = "doctor_consultorio"
    id = Column(Integer, primary_key=True, index=True)
    consultorio_id = Column(Integer, ForeignKey("consultorio.id"))
    doctor_id = Column(Integer, ForeignKey("doctor.id"))
    consultorio = relationship("Consultorio", back_populates="doctores")
    doctor = relationship("Doctor", back_populates="consultorios")

class Paciente(Base):
    __tablename__ = "paciente"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    apellidos = Column(String(255), nullable=False)
    genero = Column(String(10))
    edad = Column(Integer)
    its = Column(Boolean, default=False)
    problemas_cardiacos = Column(Boolean, default=False)
    diabetes = Column(Boolean, default=False)
    telefono = Column(String(20))
    correo_electronico = Column(String(255))
    fecha_nacimiento = Column(DateTime)

class HistorialClinico(Base):
    __tablename__ = "historial_clinico"
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("paciente.id"))
    doctor_id = Column(Integer, ForeignKey("doctor.id"))
    medicamento = Column(Text)
    tratamiento = Column(Text)
    diagnostico = Column(Text)
    notas = Column(Text)
    fecha = Column(DateTime)
    paciente = relationship("Paciente")
    doctor = relationship("Doctor")

class Cita(Base):
    __tablename__ = "cita"
    id = Column(Integer, primary_key=True, index=True)
    fecha_cita = Column(DateTime)
    doctor_id = Column(Integer, ForeignKey("doctor.id"))
    paciente_id = Column(Integer, ForeignKey("paciente.id"))
    motivo = Column(Text)
    telefono = Column(String(20))
    correo_electronico = Column(String(255))
    fecha_nacimiento = Column(DateTime)