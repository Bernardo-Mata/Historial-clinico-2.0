from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = "mysql+mysqlconnector://usuario:contraseña@localhost:3306/tu_basededatos"
    SECRET_KEY: str = "cambia_esto_por_un_valor_secreto"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALLOW_ORIGINS: list[str] = ["*"]  # Permite todas las conexiones CORS por defecto

    class Config:
        env_file = ".env"

settings = Settings()