from fastapi import APIRouter

router = APIRouter()

@router.get("/patients")
async def get_patients():
    return {"message": "List of patients"}

@router.post("/patients")
async def create_patient(patient_data: dict):
    return {"message": "Patient created", "data": patient_data}

@router.get("/doctors")
async def get_doctors():
    return {"message": "List of doctors"}

@router.post("/doctors")
async def create_doctor(doctor_data: dict):
    return {"message": "Doctor created", "data": doctor_data}

@router.get("/medical_histories")
async def get_medical_histories():
    return {"message": "List of medical histories"}

@router.post("/medical_histories")
async def create_medical_history(history_data: dict):
    return {"message": "Medical history created", "data": history_data}