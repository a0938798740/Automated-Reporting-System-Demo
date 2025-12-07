import pandas as pd
import os
from datetime import datetime, timedelta
from utils.db_connector import DBConnector
import config

class DailyReportGenerator:
    def __init__(self):
        self.db = DBConnector()
        self.target_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    def generate(self):
        print(f"Generating Daily Report for {self.target_date}...")
        
        # 1. Fetch raw data (Simplified Query)
        query = f"""
            SELECT device_id, timestamp, kwh_consumption, peak_demand 
            FROM energy_logs 
            WHERE date(timestamp) = '{self.target_date}'
        """
        df = self.db.fetch_data(query)

        if df.empty:
            print("No data found.")
            return None

        # 2. Process Data (Aggregation)
        # Calculate daily total usage per device
        daily_summary = df.groupby('device_id').agg({
            'kwh_consumption': 'sum',
            'peak_demand': 'max'
        }).reset_index()

        # 3. Export to Excel
        filename = f"Daily_Report_{self.target_date}.xlsx"
        filepath = os.path.join(config.OUTPUT_DIR, filename)
        
        # Ensure directory exists
        os.makedirs(config.OUTPUT_DIR, exist_ok=True)
        
        daily_summary.to_excel(filepath, index=False)
        return filepath
