import pymysql
import pandas as pd
import logging
from config import DB_HOST, DB_USER, DB_PASS, DB_NAME

class DBConnector:
    """
    Handles database connections and query execution using Pandas.
    """
    def __init__(self):
        self.connection_str = {
            'host': DB_HOST,
            'user': DB_USER,
            'password': DB_PASS,
            'database': DB_NAME,
            'charset': 'utf8mb4'
        }

    def fetch_data(self, query):
        """Executes a SQL query and returns a Pandas DataFrame."""
        try:
            connection = pymysql.connect(**self.connection_str)
            df = pd.read_sql(query, connection)
            connection.close()
            return df
        except Exception as e:
            logging.error(f"Database Error: {e}")
            return pd.DataFrame() # Return empty DF on error
