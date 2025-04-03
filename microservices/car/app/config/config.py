from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://myuser:mypassword@localhost/car_db"
    auth0_domain: str = "your-auth0-domain"
    auth0_algorithms: list = ["RS256"]
    auth0_api_audience: str = "your-api-audience"
    auth0_issuer: str = "https://your-auth0-domain/"
    cors_origin: Optional[str] = "*"

settings = Settings()

def get_auth_settings():
    return settings

def get_cors_settings():
    return settings

def get_db_settings():
    return settings