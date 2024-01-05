
import pandas as pd
import yfinance as yf

class YahooFinanceApi:
    
    """
    A class to interact with the Yahoo Finance API for retrieving market prices.

    Parameters:
    ----------
    - ticker (str): The stock symbol for the company.
    - period (int, optional): Number of years for which to retrieve market prices. Defaults to 10 years (written as "10y").


    Methods:
    -------
    - fetch_data(): Retrieves market prices for the specified number of years and returns a DataFrame.
    
    Returns
    -------
    - pd.DataFrame
        Columns are 'open', 'high', 'low', 'close', 'adj close' (depending on the ticker) and 'volume'.
        All columns are numeric.

    """
    
    def __init__(self, ticker, period = "10y"):
        self.ticker = ticker
        self.period = period
        
    def fetch_data(self):
        
        df = yf.download(self.ticker, period = self.period)
        
        df.columns = ["open","high","low", "close", "adj close", "volume"]
        
        df.index.name = "date"
        
        return df
    


def create_connection(database_name):
    
    """
    Creates a connection to a local SQL database.
    
    Parameters
    ----------
    database_name (str): The database name to connect to
    
    
    Returns
    -------
    sqlite3.Connection
        A connection to the database
    """
    
    import sqlite3    
    
    try:
        connection = sqlite3.connect(f"{database_name}.db", check_same_thread = False)
        
        return connection
        
    except:
        f"Error occurred"

        

class SQLRepository:
    
    def __init__(self, connection):
        
        self.connection = connection    
    
    def insert_table(self, table_name, records, if_exists = "fail"):
        """Insert DataFrame into SQLite database as table

        Parameters
        ----------
        table_name : str
        records : pd.DataFrame
        if_exists : str, optional
            How to behave if the table already exists.

            - 'fail': Raise a ValueError.
            - 'replace': Drop the table before inserting new values.
            - 'append': Insert new values to the existing table.

            Dafault: 'fail'

        Returns
        -------
        dict
            Dictionary has two keys:

            - 'transaction_successful', followed by bool
            - 'records_inserted', followed by int
        """
        
        n_inserted = records.to_sql(name = table_name, con = self.connection, if_exists = if_exists)
        
        
        return {
         'transaction_successful': True,
         'records_inserted': n_inserted
        }
        
    def read_table(self, table_name, limit = None):
        
        """Read table from database.

        Parameters
        ----------
        table_name : str
            Name of table in SQLite database.
        limit : int, None, optional
            Number of most recent records to retrieve. If `None`, all
            records are retrieved. By default, `None`.

        Returns
        -------
        pd.DataFrame
            Index is DatetimeIndex "date". Columns are 'open', 'high',
            'low', 'close', and 'volume'. All columns are numeric.
        """
        
        # Create SQL query (with optional limit)
        if limit:
            sql = f"SELECT * FROM '{table_name}' LIMIT {limit}"

        else:
            sql = f"SELECT * FROM '{table_name}'"


        # Retrieve data, read into DataFrame
        df = pd.read_sql(
            sql = sql,
            con = self.connection,
            parse_dates = ["date"],
            index_col = "date"
        )


        # Return DataFrame
        return df
    