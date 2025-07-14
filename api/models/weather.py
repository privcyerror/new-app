"""
Pydantic models for weather data
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class WeatherRequest(BaseModel):
    """Weather request model"""
    city: str = Field(..., min_length=1, max_length=100, description="City name")
    country: str = Field(default="US", min_length=2, max_length=5, description="Country code")
    
    class Config:
        schema_extra = {
            "example": {
                "city": "New York",
                "country": "US"
            }
        }

class WeatherResponse(BaseModel):
    """Weather response model"""
    city: str = Field(..., description="City name")
    country: str = Field(..., description="Country code")
    temperature: float = Field(..., description="Temperature in Celsius")
    description: str = Field(..., description="Weather description")
    humidity: int = Field(..., ge=0, le=100, description="Humidity percentage")
    wind_speed: float = Field(..., ge=0, description="Wind speed in km/h")
    pressure: int = Field(..., ge=0, description="Atmospheric pressure in hPa")
    feels_like: float = Field(..., description="Feels like temperature in Celsius")
    visibility: int = Field(..., ge=0, description="Visibility in km")
    uv_index: Optional[float] = Field(None, ge=0, le=15, description="UV index")
    timestamp: str = Field(..., description="Data timestamp")
    
    class Config:
        schema_extra = {
            "example": {
                "city": "New York",
                "country": "US",
                "temperature": 22.5,
                "description": "Partly cloudy",
                "humidity": 65,
                "wind_speed": 12.5,
                "pressure": 1013,
                "feels_like": 24.0,
                "visibility": 10,
                "uv_index": 6.2,
                "timestamp": "2024-01-15T14:30:00"
            }
        }

class ErrorResponse(BaseModel):
    """Error response model"""
    error: str = Field(..., description="Error message")
    detail: Optional[str] = Field(None, description="Detailed error information")
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())
    
    class Config:
        schema_extra = {
            "example": {
                "error": "City not found",
                "detail": "The requested city could not be found in our database",
                "timestamp": "2024-01-15T14:30:00"
            }
        }

class HealthResponse(BaseModel):
    """Health check response model"""
    status: str = Field(..., description="Service status")
    timestamp: str = Field(..., description="Response timestamp")
    version: str = Field(..., description="API version")
    
    class Config:
        schema_extra = {
            "example": {
                "status": "healthy",
                "timestamp": "2024-01-15T14:30:00",
                "version": "1.0.0"
            }
        }