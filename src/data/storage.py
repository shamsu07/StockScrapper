# src/data/storage.py
import pandas as pd
from pathlib import Path
from datetime import datetime
from src.utils.logger import setup_logger
from config.settings import OUTPUT_DIR

logger = setup_logger(__name__)


class DataStorage:
    def __init__(self):
        self.output_dir = OUTPUT_DIR

    def save_to_excel(self, data_list, filename=None):
        """Save stock data to Excel file"""
        try:
            if filename is None:
                filename = f"stock_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

            filepath = self.output_dir / filename

            df = pd.DataFrame([vars(data) for data in data_list])
            df.to_excel(filepath, index=False)

            logger.info(f"Data saved successfully to {filepath}")
            return filepath

        except Exception as e:
            logger.error(f"Failed to save data: {str(e)}")
            raise