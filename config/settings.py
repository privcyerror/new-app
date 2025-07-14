"""
Configuration settings for the Weather App
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    """Application settings"""
    
    # API Configuration
    API_HOST: str = os.getenv("API_HOST", "127.0.0.1")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    API_DEBUG: bool = os.getenv("API_DEBUG", "True").lower() == "true"
    
    # Weather API Configuration
    WEATHER_API_KEY: str = os.getenv("WEATHER_API_KEY", "")
    WEATHER_API_URL: str = os.getenv("WEATHER_API_URL", "https://api.openweathermap.org/data/2.5/weather")
    
    # GUI Configuration
    WINDOW_TITLE: str = "Weather App"
    WINDOW_SIZE: str = "800x600"
    THEME_COLOR: str = "#2c3e50"
    
    # Application Info
    APP_NAME: str = "Weather App"
    APP_VERSION: str = "1.0.0"
    
    @property
    def api_url(self) -> str:
        """Get the full API URL"""
        return f"http://{self.API_HOST}:{self.API_PORT}"

# Create global settings instance
settings = Settings()