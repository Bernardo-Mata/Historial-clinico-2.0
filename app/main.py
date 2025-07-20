from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.api import router as api_router
from app.core.config import settings

app = FastAPI(
    title="Sistema de Historiales Clínicos",
    description="API para gestión segura de historiales clínicos",
    version="1.0.0"
)

# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Medical History App API!"}