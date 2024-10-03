# lib.py

import sqlite3
import pandas as pd

def my_load(db_path='data/nasdaq.db', csv_path='data/NASDAQ_100_Data_From_2010.csv', nrows=None):
    """
    Load data from a CSV file into a SQLite database.
    """
    with sqlite3.connect(db_path) as conn:
        # Read data from the CSV file
        df = pd.read_csv(csv_path, nrows=nrows, sep='\t')
        # Drop the 'Adj Close' column if it exists
        if 'Adj Close' in df.columns:
            df = df.drop(columns=['Adj Close'])
        # Write the DataFrame to the 'stocks' table
        df.to_sql('stocks', conn, if_exists='replace', index=False)

def my_create(db_path='data/nasdaq.db', record=None):
    """
    Insert a new record into the 'stocks' table.
    """
    if record is None:
        record = ('2021-10-01', 100, 110, 90, 105, 1000000, 'Imaginary AAPL')
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO stocks (Date, Open, High, Low, Close, Volume, Name)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, record)
        conn.commit()

def my_read(db_path='data/nasdaq.db', name='Imaginary AAPL'):
    """
    Read records from the 'stocks' table where Name matches.
    Returns the result as a list of tuples.
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM stocks WHERE Name = ?", (name,))
        results = cursor.fetchall()
    return results

def my_update(db_path='data/nasdaq.db', name='Imaginary AAPL', new_close=200):
    """
    Update the 'Close' value of a record in the 'stocks' table.
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE stocks SET Close = ? WHERE Name = ?", (new_close, name))
        conn.commit()

def my_delete(db_path='data/nasdaq.db', name='Imaginary AAPL'):
    """
    Delete records from the 'stocks' table where Name matches.
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM stocks WHERE Name = ?", (name,))
        conn.commit()
