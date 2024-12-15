# main.py
from src.scraper.browser import BrowserManager
from src.scraper.factory import ScraperFactory
from src.data.storage import DataStorage
from config.stocks import STOCKS, get_alternate_symbol
from src.utils.logger import setup_logger
from src.utils.exceptions import StockNotFoundError

logger = setup_logger(__name__)


def scrape_stock(stock, exchange, scraper, browser_manager):  # Added browser_manager parameter
    """Scrape individual stock data"""
    try:
        symbol = (
            stock.nse_symbol if exchange == 'NSE'
            else stock.bse_symbol
        )

        if not symbol:
            raise StockNotFoundError(
                f"No {exchange} symbol for {stock.name}"
            )

        scraper.search_stock(symbol)
        return scraper.extract_stock_data(stock)

    except StockNotFoundError as e:
        logger.warning(str(e))
        # Get alternate exchange and symbol
        alt_exchange, alt_symbol = get_alternate_symbol(stock, exchange)
        if alt_exchange and alt_symbol:
            logger.info(
                f"Attempting to fetch {stock.name} from {alt_exchange}"
            )
            # Create new scraper for alternate exchange
            alt_scraper = ScraperFactory.get_scraper(
                alt_exchange,
                browser_manager.setup_driver()
            )
            alt_scraper.navigate_to_home()
            return scrape_stock(stock, alt_exchange, alt_scraper, browser_manager)  # Pass browser_manager
        else:
            logger.error(
                f"Stock {stock.name} not available in any exchange"
            )
            return None

    except Exception as e:
        logger.error(
            f"Failed to scrape {stock.name} from {exchange}: {str(e)}"
        )
        return None


def main():
    browser_manager = BrowserManager()
    storage = DataStorage()
    stock_data_list = []

    try:
        # Start with NSE as primary exchange
        primary_exchange = 'NSE'
        driver = browser_manager.setup_driver()
        scraper = ScraperFactory.get_scraper(primary_exchange, driver)
        scraper.navigate_to_home()

        for stock in STOCKS:
            data = scrape_stock(stock, primary_exchange, scraper, browser_manager)  # Pass browser_manager
            if data:
                stock_data_list.append(data)

        # Save all collected data
        storage.save_to_excel(stock_data_list)

    except Exception as e:
        logger.error(f"Script execution failed: {str(e)}")
        raise

    finally:
        browser_manager.close()


if __name__ == "__main__":
    main()