# config/settings.py
from pathlib import Path

# Base project directory
BASE_DIR = Path(__file__).parent.parent

# Output directory for Excel files
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# Logs directory
LOGS_DIR = BASE_DIR / "logs"
LOGS_DIR.mkdir(exist_ok=True)

# Browser settings
BROWSER_SETTINGS = {
    "headless": False,  # Set to True for production
    "user_agent": "Mozilla/5.0 ...",  # Add appropriate user agent
    "page_load_timeout": 30,
    "implicit_wait": 10,
}

# NSE Website settings
BASE_URL = "https://www.nseindia.com"
SEARCH_DELAY = 2  # Delay between searches in seconds
PAGE_LOAD_DELAY = 5  # Delay for page load in seconds