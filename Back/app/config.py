from pydantic import BaseSettings

class Settings(BaseSettings):
    TWITTER_API_KEY: str
    TWITTER_API_SECRET: str
    TWITTER_ACCESS_TOKEN: str
    TWITTER_ACCESS_TOKEN_SECRET: str
    OPENAI_API_KEY: str
    GOOGLE_API_KEY: str
    
    class Config:
        env_file = ".env"

settings = Settings()