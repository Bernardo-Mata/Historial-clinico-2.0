from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(String)
    medical_histories = relationship("MedicalHistory", back_populates="patient")

class Doctor(Base):
    __tablename__ = 'doctors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    specialty = Column(String)
    clinic_id = Column(Integer, ForeignKey('clinics.id'))
    medical_histories = relationship("MedicalHistory", back_populates="doctor")

class MedicalHistory(Base):
    __tablename__ = 'medical_histories'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    description = Column(String)
    date = Column(String)  # Consider using Date type for better handling
    patient = relationship("Patient", back_populates="medical_histories")
    doctor = relationship("Doctor", back_populates="medical_histories")

class Clinic(Base):
    __tablename__ = 'clinics'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    doctors = relationship("Doctor", back_populates="clinic")