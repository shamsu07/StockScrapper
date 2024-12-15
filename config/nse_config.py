# config/nse_config.py
from pathlib import Path

NSE_CONFIG = {
    'base_url': 'https://www.nseindia.com/',
    'search_delay': 2,  # Delay between searches in seconds
    'page_load_delay': 5,  # Delay for page load in seconds
    'retry_attempts': 3,  # Number of retry attempts for failed requests
    'retry_delay': 2,  # Delay between retries in seconds
}

# Selectors for NSE website elements
NSE_SELECTORS = {
    'search': {
        'input': 'header-search-input',  # ID of search input
        'suggestion_list': 'ul.search_list',  # Class for search suggestions
        'suggestion_items': 'li.search_list_item'  # Class for individual suggestions
    },
    'stock_page': {
        'ltp': 'div[data-test-id="lastPrice"]',  # Last traded price
        'change': 'div[data-test-id="priceChange"]',  # Price change
        'change_percent': 'div[data-test-id="priceChangePercentage"]',
        'volume': 'div[data-test-id="totalVolume"]',
        'value': 'div[data-test-id="totalValue"]',
        'day_high': 'div[data-test-id="dayHigh"]',
        'day_low': 'div[data-test-id="dayLow"]',
        'week_high_52': 'div[data-test-id="52WeekHigh"]',
        'week_low_52': 'div[data-test-id="52WeekLow"]'
    },
    'error_messages': {
        'no_data': 'div.no-data-message',
        'stock_not_found': 'div.stock-not-found'
    }
}

# Headers required for NSE requests
NSE_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}

# API endpoints (if needed)
NSE_APIS = {
    'search_api': 'https://www.nseindia.com/api/search/autocomplete',
    'stock_info': 'https://www.nseindia.com/api/quote-equity',
    'market_status': 'https://www.nseindia.com/api/marketStatus'
}

# Rate limiting settings
NSE_RATE_LIMITS = {
    'max_requests_per_minute': 30,
    'max_concurrent_requests': 1
}