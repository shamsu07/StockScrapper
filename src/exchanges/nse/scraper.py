from src.exchanges.base import ExchangeScraper
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class NSEScraper(ExchangeScraper):
    def navigate_to_home(self):
        """ NSE Specific homepage Navigation"""
        pass

    def search_stock(self, symbol):
        """
        Search for a stock on NSE using the search box

        Args:
            symbol (str): The stock symbol/company name to search for

        Returns:
            None: Navigates to the stock page if found
        """
        try:
            # Wait for search box to be present and visible
            search_box = self.wait_for_element(By.ID, "header-search-input")

            # Clear any existing text and enter the symbol
            search_box.clear()
            search_box.send_keys(symbol)

            # Wait for autocomplete results to appear
            auto_complete = self.wait_for_element(By.ID, "autoComplete")

            # Wait for search results to populate
            search_results = self.wait_for_elements(By.CSS_SELECTOR, "#autoCompleteBlock li")

            # Click the first matching result
            if search_results:
                for result in search_results:
                    if symbol.upper() in result.text.upper():
                        result.click()
                        break

        except TimeoutException:
            print(f"Timeout while searching for symbol {symbol}")
        except Exception as e:
            print(f"Error searching for symbol {symbol}: {str(e)}")
    def extract_stock_data(self, symbol):
        """ Extract stock data from NSE """
        pass