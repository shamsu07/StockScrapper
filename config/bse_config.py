# config/bse_config.py
from pathlib import Path

BSE_CONFIG = {
    'base_url': 'https://www.bseindia.com/',
    'search_delay': 2,
    'page_load_delay': 5,
    'retry_attempts': 3,
    'retry_delay': 2
}

# Selectors for BSE website elements
BSE_SELECTORS = {
    'search': {
        'input': 'txt_Scrip_Code',  # ID of search input
        'suggestion_list': 'ul.ui-autocomplete',  # Class for search suggestions
        'suggestion_items': 'li.ui-menu-item'  # Class for individual suggestions
    },
    'stock_page': {
        'ltp': 'strong#idcrval',  # Last traded price
        'change': 'span#changeval',  # Price change
        'change_percent': 'span#changeprcntval',
        'volume': 'td#tdDataVolume',
        'value': 'td#tdDataValue',
        'day_high': 'td#tdDataDayHigh',
        'day_low': 'td#tdDataDayLow',
        'week_high_52': 'td#tdData52WH',
        'week_low_52': 'td#tdData52WL'
    },
    'error_messages': {
        'no_data': 'div.noDataMessage',
        'stock_not_found': 'div.scriptNotFound'
    }
}

# Headers required for BSE requests
BSE_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}

# API endpoints (if needed)
BSE_APIS = {
    'search_api': 'https://api.bseindia.com/Msource/1D/getQouteSearch.aspx',
    'stock_info': 'https://api.bseindia.com/BseIndiaAPI/api/StockReachGraph/w',
    'market_status': 'https://api.bseindia.com/Msource/1D/getMarketStatus.aspx'
}

# Rate limiting settings
BSE_RATE_LIMITS = {
    'max_requests_per_minute': 30,
    'max_concurrent_requests': 1
}

# BSE-specific cookie handling
BSE_COOKIES = {
    'required_cookies': [
        'ASP.NET_SessionId',
        'NSC_BSEINDIA',
        'bseData'
    ]
}