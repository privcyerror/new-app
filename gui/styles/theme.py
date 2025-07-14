"""
Theme configuration for the GUI application
"""

import tkinter as tk
from tkinter import ttk

class AppTheme:
    """Application theme configuration"""
    
    # Color scheme
    COLORS = {
        'primary': '#2c3e50',        # Dark blue-grey
        'secondary': '#34495e',      # Lighter blue-grey
        'accent': '#3498db',         # Blue
        'danger': '#e74c3c',         # Red
        'warning': '#f39c12',        # Orange
        'success': '#27ae60',        # Green
        'light': '#ecf0f1',          # Light grey
        'white': '#ffffff',          # White
        'dark': '#2c3e50'            # Dark
    }
    
    # Fonts
    FONTS = {
        'title': ('Arial', 24, 'bold'),
        'header': ('Arial', 16, 'bold'),
        'body': ('Arial', 12),
        'small': ('Arial', 10),
        'temperature': ('Arial', 48, 'bold'),
        'search': ('Arial', 14)
    }
    
    # Spacing
    SPACING = {
        'small': 5,
        'medium': 10,
        'large': 20,
        'xlarge': 30
    }
    
    # Window settings
    WINDOW = {
        'width': 800,
        'height': 600,
        'min_width': 600,
        'min_height': 400,
        'resizable': True
    }

def configure_styles(style: ttk.Style):
    """
    Configure custom styles for the application
    
    Args:
        style: ttk.Style instance
    """
    theme = AppTheme()
    
    # Configure theme
    style.theme_use('clam')
    
    # Title label
    style.configure('Title.TLabel',
                   font=theme.FONTS['title'],
                   foreground=theme.COLORS['white'],
                   background=theme.COLORS['primary'])
    
    # Header label
    style.configure('Header.TLabel',
                   font=theme.FONTS['header'],
                   foreground=theme.COLORS['accent'],
                   background=theme.COLORS['primary'])
    
    # Body text label
    style.configure('Body.TLabel',
                   font=theme.FONTS['body'],
                   foreground=theme.COLORS['light'],
                   background=theme.COLORS['primary'])
    
    # Info label
    style.configure('Info.TLabel',
                   font=theme.FONTS['body'],
                   foreground=theme.COLORS['light'],
                   background=theme.COLORS['secondary'])
    
    # Temperature label
    style.configure('Temperature.TLabel',
                   font=theme.FONTS['temperature'],
                   foreground=theme.COLORS['danger'],
                   background=theme.COLORS['secondary'])
    
    # Search entry
    style.configure('Search.TEntry',
                   font=theme.FONTS['search'],
                   fieldbackground=theme.COLORS['secondary'],
                   foreground=theme.COLORS['white'],
                   borderwidth=1,
                   relief='solid',
                   bordercolor=theme.COLORS['accent'])
    
    # Search button
    style.configure('Search.TButton',
                   font=theme.FONTS['body'],
                   background=theme.COLORS['accent'],
                   foreground=theme.COLORS['white'],
                   borderwidth=0,
                   padding=(theme.SPACING['medium'], theme.SPACING['small']))
    
    # Hover effect for search button
    style.map('Search.TButton',
              background=[('active', theme.COLORS['accent']),
                         ('pressed', '#2980b9')])
    
    # Loading label
    style.configure('Loading.TLabel',
                   font=theme.FONTS['header'],
                   foreground=theme.COLORS['warning'],
                   background=theme.COLORS['secondary'])
    
    # Error label
    style.configure('Error.TLabel',
                   font=theme.FONTS['body'],
                   foreground=theme.COLORS['danger'],
                   background=theme.COLORS['secondary'])
    
    # Success label
    style.configure('Success.TLabel',
                   font=theme.FONTS['body'],
                   foreground=theme.COLORS['success'],
                   background=theme.COLORS['secondary'])
    
    # Small text label
    style.configure('Small.TLabel',
                   font=theme.FONTS['small'],
                   foreground=theme.COLORS['light'],
                   background=theme.COLORS['secondary'])

def create_gradient_frame(parent, color1, color2, height=2):
    """
    Create a gradient frame (simple implementation)
    
    Args:
        parent: Parent widget
        color1: Start color
        color2: End color
        height: Frame height
        
    Returns:
        Frame widget
    """
    frame = tk.Frame(parent, bg=color1, height=height)
    return frame

def get_weather_icon(description: str) -> str:
    """
    Get weather icon based on description
    
    Args:
        description: Weather description
        
    Returns:
        Unicode weather icon
    """
    description = description.lower()
    
    icons = {
        'sunny': '☀️',
        'clear': '☀️',
        'partly cloudy': '⛅',
        'cloudy': '☁️',
        'overcast': '☁️',
        'rainy': '🌧️',
        'light rain': '🌦️',
        'heavy rain': '⛈️',
        'thunderstorm': '⛈️',
        'snowy': '❄️',
        'snow': '❄️',
        'foggy': '🌫️',
        'hazy': '🌫️',
        'windy': '💨'
    }
    
    for key, icon in icons.items():
        if key in description:
            return icon
    
    return '🌤️'  # Default icon

def get_color_by_temperature(temp: float) -> str:
    """
    Get color based on temperature
    
    Args:
        temp: Temperature in