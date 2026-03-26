import sqlite3
import logging

logging.basicConfig(level=logging.INFO)

def check_data():
    logging.info("Checking data started")

    conn = sqlite3.connect("/home/unix16/airflow/data/infosys.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM orders")
    logging.info(f"Total Orders: {cursor.fetchone()[0]}")

    cursor.execute("SELECT COUNT(*) FROM order_details")
    logging.info(f"Total Order Details: {cursor.fetchone()[0]}")

    cursor.execute("SELECT COUNT(*) FROM sales_target")
    logging.info(f"Total Sales Targets: {cursor.fetchone()[0]}")

    conn.close()

    logging.info("Checking completed")

if __name__ == "__main__":
    check_data()
