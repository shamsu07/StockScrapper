# src/utils/exceptions.py

class ScraperException(Exception):
    """Base exception for scraper errors"""
    pass

class NavigationError(ScraperException):
    """Raised when navigation fails"""
    pass

class DataExtractionError(ScraperException):
    """Raised when data extraction fails"""
    pass

class ValidationError(ScraperException):
    """Raised when data validation fails"""
    pass

class StockNotFoundError(ScraperException):
    """Raised when a stock is not found in an exchange"""
    pass

class ExchangeError(ScraperException):
    """Raised when there's an exchange-specific error"""
    pass