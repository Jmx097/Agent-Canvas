from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    BASE_DIR: Path = Path(__file__).parent.parent
    
    # LLM
    OPENAI_API_KEY: str = "mock_key"  # Set in .env
    LLM_MODEL: str = "gpt-4o"

    # Database
    DB_URL: str = "sqlite:///personal_os.db"

    # Logging
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()
