from abc import ABC, abstractmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExchangeScraper(ABC):
    """ Base class for all exchange scrappers. """

    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def navigate_to_home(self):
        """ Navigates to the home page. """
        pass

    @abstractmethod
    def search_stock(self, symbol):
        """ Searches for a stock symbol. """
        pass

    @abstractmethod
    def extract_stock_data(self, symbol):
        """ Extracts stock data. """
        pass

    @abstractmethod
    def validate_data(self, data):
        """ Validates extracted data. """
        pass

    def wait_for_element(self, by, value, timeout=10):
        """Wait for element to be present and visible"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located((by, value)))

    def wait_for_elements(self, by, value, timeout=10):
        """Wait for elements to be present"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_all_elements_located((by, value)))