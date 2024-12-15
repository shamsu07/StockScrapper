# config/stocks.py
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Stock:
    name: str
    nse_symbol: Optional[str] = None
    bse_symbol: Optional[str] = None
    category: str = "GENERAL"


# Define stocks with their exchange-specific symbols
STOCKS = [
    # Defense stocks
    Stock("Astra Microwave", "ASTRAMICRO", "ASTRAMICRO", "DEFENSE"),
    Stock("Avantel", "AVANTEL", "AVANTEL", "DEFENSE"),
    Stock("BDL", "BDL", "BDL", "DEFENSE"),
    Stock("BEL", "BEL", "BEL", "DEFENSE"),
    Stock("Bharat Forge", "BHARATFORG", "BHARATFORG", "DEFENSE"),
    # Add other defense stocks...

    # Banking stocks
    Stock("Bank of Baroda", "BANKBARODA", "BANKBARODA", "BANKING"),
    Stock("Bank of India", "BANKINDIA", "BANKINDIA", "BANKING"),
    Stock("Maharashtra Bank", "MAHABANK", "MAHABANK", "BANKING"),
    # Add other banking stocks...
]


def get_stocks_by_category(category: str) -> List[Stock]:
    """Get stocks filtered by category"""
    return [stock for stock in STOCKS if stock.category == category]


def get_stocks_by_exchange(exchange: str) -> List[Stock]:
    """Get stocks available in a specific exchange"""
    if exchange.upper() == 'NSE':
        return [stock for stock in STOCKS if stock.nse_symbol]
    elif exchange.upper() == 'BSE':
        return [stock for stock in STOCKS if stock.bse_symbol]
    else:
        raise ValueError(f"Invalid exchange: {exchange}")


def get_alternate_symbol(stock: Stock, primary_exchange: str) -> tuple:
    """
    Get alternate exchange symbol if stock not found in primary exchange
    Returns: (exchange, symbol)
    """
    if primary_exchange.upper() == 'NSE':
        return ('BSE', stock.bse_symbol) if stock.bse_symbol else (None, None)
    elif primary_exchange.upper() == 'BSE':
        return ('NSE', stock.nse_symbol) if stock.nse_symbol else (None, None)
    else:
        raise ValueError(f"Invalid exchange: {primary_exchange}")