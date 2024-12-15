# src/scraper/browser.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.settings import BROWSER_SETTINGS
from src.utils.logger import setup_logger

logger = setup_logger(__name__)


class BrowserManager:
    def __init__(self):
        self.driver = None

    def setup_driver(self):
        """Initialize and configure Chrome WebDriver"""
        try:
            options = Options()
            if BROWSER_SETTINGS["headless"]:
                options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument(f"user-agent={BROWSER_SETTINGS['user_agent']}")

            self.driver = webdriver.Chrome(options=options)
            self.driver.implicitly_wait(BROWSER_SETTINGS["implicit_wait"])
            self.driver.set_page_load_timeout(BROWSER_SETTINGS["page_load_timeout"])

            return self.driver

        except Exception as e:
            logger.error(f"Failed to setup browser: {str(e)}")
            raise

    def close(self):
        """Close the browser"""
        if self.driver:
            self.driver.quit()