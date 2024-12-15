from src.exchanges.nse.scraper import NSEScraper
from src.exchanges.bse.scraper import BSEScraper


class ScraperFactory:
    @staticmethod
    def get_scraper(exchange, driver):
        """Factory method to create appropriate scraper"""
        scrapers = {
            'NSE': NSEScraper,
            'BSE': BSEScraper
        }

        if exchange not in scrapers:
            raise ValueError(f"Unsupported exchange: {exchange}")

        return scrapers[exchange](driver)