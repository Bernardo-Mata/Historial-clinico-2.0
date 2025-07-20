from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_DB: str
    ALLOW_ORIGINS: list[str] = ["*"]  # Default to allow all origins

    @property
    def SQLALCHEMY_DATABASE_URL(self):
        return (
            f"mysql+mysqlconnector://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}"
            f"@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DB}"
        )

    class Config:
        env_file = ".env"

settings = Settings()