"""
Weather service for fetching weather data
"""

import asyncio
from datetime import datetime
from typing import Optional, Dict, Any
from fastapi import HTTPException

from api.models.weather import WeatherRequest, WeatherResponse

class WeatherService:
    """Service for handling weather data operations"""
    
    def __init__(self):
        # Mock weather data for demonstration
        # In production, this would be replaced with actual API calls
        self.mock_data = {
            "new york": {
                "temperature": 22.5,
                "description": "Partly cloudy",
                "humidity": 65,
                "wind_speed": 12.5,
                "pressure": 1013,
                "feels_like": 24.0,
                "visibility": 10,
                "uv_index": 6.2
            },
            "london": {
                "temperature": 18.3,
                "description": "Light rain",
                "humidity": 78,
                "wind_speed": 8.2,
                "pressure": 1008,
                "feels_like": 16.5,
                "visibility": 8,
                "uv_index": 3.1
            },
            "tokyo": {
                "temperature": 26.8,
                "description": "Sunny",
                "humidity": 58,
                "wind_speed": 6.3,
                "pressure": 1020,
                "feels_like": 28.2,
                "visibility": 15,
                "uv_index": 8.7
            },
            "sydney": {
                "temperature": 20.1,
                "description": "Overcast",
                "humidity": 72,
                "wind_speed": 14.8,
                "pressure": 1016,
                "feels_like": 18.9,
                "visibility": 12,
                "uv_index": 4.5
            },
            "paris": {
                "temperature": 19.7,
                "description": "Clear sky",
                "humidity": 60,
                "wind_speed": 9.1,
                "pressure": 1015,
                "feels_like": 21.2,
                "visibility": 12,
                "uv_index": 5.3
            },
            "mumbai": {
                "temperature": 32.1,
                "description": "Hot and humid",
                "humidity": 85,
                "wind_speed": 15.3,
                "pressure": 1005,
                "feels_like": 38.5,
                "visibility": 6,
                "uv_index": 9.8
            },
            "delhi": {
                "temperature": 28.9,
                "description": "Hazy",
                "humidity": 72,
                "wind_speed": 11.2,
                "pressure": 1010,
                "feels_like": 33.1,
                "visibility": 4,
                "uv_index": 7.6
            }
        }
    
    async def get_weather(self, request: WeatherRequest) -> WeatherResponse:
        """
        Get weather data for a specific city
        
        Args:
            request: WeatherRequest object containing city and country
            
        Returns:
            WeatherResponse object with weather data
            
        Raises:
            HTTPException: If city is not found or API error occurs
        """
        # Simulate API delay
        await asyncio.sleep(0.3)
        
        city_key = request.city.lower().strip()
        
        if city_key in self.mock_data:
            data = self.mock_data[city_key]
            return WeatherResponse(
                city=request.city.title(),
                country=request.country.upper(),
                timestamp=datetime.now().isoformat(),
                **data
            )
        else:
            raise HTTPException(
                status_code=404,
                detail=f"Weather data for '{request.city}' not found. Try: {', '.join(self.mock_data.keys())}"
            )
    
    async def get_available_cities(self) -> Dict[str, Any]:
        """
        Get list of available cities
        
        Returns:
            Dictionary containing available cities
        """
        return {
            "cities": list(self.mock_data.keys()),
            "count": len(self.mock_data),
            "timestamp": datetime.now().isoformat()
        }
    
    # TODO: Implement real weather API integration
    async def _fetch_from_api(self, city: str, country: str) -> Optional[Dict[str, Any]]:
        """
        Fetch weather data from external API (to be implemented)
        
        Args:
            city: City name
            country: Country code
            
        Returns:
            Weather data dictionary or None if not found
        """
        # This would integrate with a real weather API like OpenWeatherMap
        # Example implementation:
        # 
        # import httpx
        # from config.settings import settings
        # 
        # async with httpx.AsyncClient() as client:
        #     response = await client.get(
        #         settings.WEATHER_API_URL,
        #         params={
        #             "q": f"{city},{country}",
        #             "appid": settings.WEATHER_API_KEY,
        #             "units": "metric"
        #         }
        #     )
        #     if response.status_code == 200:
        #         return response.json()
        #     return None
        pass

# Create global weather service instance
weather_service = WeatherService()