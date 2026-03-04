import os
from dotenv import load_dotenv

load_dotenv()

# URLs
BASE_URL = os.getenv("BASE_URL", "https://www.mercadolibre.com.mx")

# Browser settings
BROWSER = os.getenv("BROWSER", "chrome")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
WINDOW_SIZE = os.getenv("WINDOW_SIZE", "1920,1080")

# Wait timeouts (en segundos)
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "15"))

# Directorios
SCREENSHOTS_DIR = os.getenv("SCREENSHOTS_DIR", "screenshots")
