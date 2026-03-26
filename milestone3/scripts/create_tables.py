import sqlite3
import os
import logging

logging.basicConfig(level=logging.INFO)

def create_tables():
    logging.info("Creating tables started")

    # Make sure data folder exists
    os.makedirs("/home/unix16/airflow/data", exist_ok=True)

    conn = sqlite3.connect("/home/unix16/airflow/data/infosys.db")
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    # Orders Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id TEXT PRIMARY KEY,
        order_date TEXT,
        customer_name TEXT,
        state TEXT,
        city TEXT
    )
    """)

    # Order Details Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS order_details (
        order_id TEXT,
        amount REAL,
        profit REAL,
        quantity INTEGER,
        category TEXT,
        sub_category TEXT,
        FOREIGN KEY(order_id) REFERENCES orders(order_id)
    )
    """)

    # Sales Target Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales_target (
        month TEXT,
        category TEXT,
        target REAL
    )
    """)

    conn.commit()
    conn.close()

    logging.info("Tables created successfully")

if __name__ == "__main__":
    create_tables()
