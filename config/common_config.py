# config/common_config.py
from datetime import time

# Market timing configuration
MARKET_TIMINGS = {
    'market_open': time(9, 15),  # 9:15 AM
    'market_close': time(15, 30),  # 3:30 PM
    'pre_market_start': time(9, 0),  # 9:00 AM
    'post_market_end': time(16, 0)  # 4:00 PM
}

# Data validation settings
VALIDATION_RULES = {
    'price': {
        'min': 0.01,
        'max': 100000
    },
    'volume': {
        'min': 0,
        'max': 1000000000
    },
    'change_percent': {
        'min': -25,
        'max': 25
    }
}

# Retry configuration
RETRY_CONFIG = {
    'max_retries': 3,
    'retry_delay': 2,
    'retry_exponential_base': 2
}

# Output configuration
OUTPUT_CONFIG = {
    'excel': {
        'sheet_name': 'Stock Data',
        'date_format': 'YYYY-MM-DD HH:mm:ss',
        'float_precision': 2
    }
}