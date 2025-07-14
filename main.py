#!/usr/bin/env python3
"""
Main entry point for the Weather App
Starts both the FastAPI server and GUI application
"""

import threading
import time
import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from api.main import run_server
from gui.main import WeatherApp

def main():
    """Main function to run both API server and GUI"""
    print("🌤️  Starting Weather App...")
    print("🚀 Starting API server on http://127.0.0.1:8000")
    
    # Start API server in a separate thread
    api_thread = threading.Thread(target=run_server, daemon=True)
    api_thread.start()
    
    # Give server time to start
    print("⏳ Waiting for server to start...")
    time.sleep(3)
    
    # Start GUI
    print("🖥️  Starting GUI application...")
    try:
        app = WeatherApp()
        app.run()
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()