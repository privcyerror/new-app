"""
Weather API routes
"""

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from datetime import datetime

from api.models.weather import WeatherRequest, WeatherResponse, ErrorResponse, HealthResponse
from api.services.weather_service import weather_service
from config.settings import settings

# Create router
router = APIRouter(
    prefix="/api/v1",
    tags=["weather"],
    responses={
        404: {"model": ErrorResponse, "description": "City not found"},
        500: {"model": ErrorResponse, "description": "Internal server error"}
    }
)

@router.get("/", response_model=dict)
async def root():
    """Root endpoint with API information"""
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "message": "Weather API is running!",
        "endpoints": {
            "health": "/health",
            "weather": "/weather",
            "cities": "/cities",
            "docs": "/docs"
        },
        "timestamp": datetime.now().isoformat()
    }

@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now().isoformat(),
        version=settings.APP_VERSION
    )

@router.post("/weather", response_model=WeatherResponse)
async def get_weather(request: WeatherRequest):
    """
    Get weather data for a specific city
    
    - **city**: City name (required)
    - **country**: Country code (optional, defaults to US)
    
    Returns weather information including temperature, humidity, wind speed, etc.
    """
    try:
        weather_data = await weather_service.get_weather(request)
        return weather_data
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )

@router.get("/cities")
async def get_available_cities():
    """
    Get list of available cities
    
    Returns a list of cities for which weather data is available
    """
    try:
        cities_data = await weather_service.get_available_cities()
        return cities_data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )

@router.get("/weather/{city}", response_model=WeatherResponse)
async def get_weather_by_city(city: str, country: str = "US"):
    """
    Get weather data by city name (GET endpoint)
    
    - **city**: City name (path parameter)
    - **country**: Country code (query parameter, defaults to US)
    """
    request = WeatherRequest(city=city, country=country)
    return await get_weather(request)

# Error handlers
@router.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    """Custom HTTP exception handler"""
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            error=exc.detail,
            detail=f"HTTP {exc.status_code}",
            timestamp=datetime.now().isoformat()
        ).dict()
    )

@router.exception_handler(Exception)
async def general_exception_handler(request, exc: Exception):
    """General exception handler"""
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=ErrorResponse(
            error="Internal server error",
            detail=str(exc),
            timestamp=datetime.now().isoformat()
        ).dict()
    )