# src/data/models.py
from dataclasses import dataclass
from datetime import datetime

@dataclass
class StockData:
    symbol: str
    timestamp: datetime = datetime.now()
    # Add other fields based on your requirements