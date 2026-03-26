import pandas as pd
import sqlite3
import logging

logging.basicConfig(level=logging.INFO)

DB_PATH = "/home/unix16/airflow/data/infosys.db"

def load_data():
    logging.info("Data loading started")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # ✅ Make pipeline idempotent
    cursor.execute("DELETE FROM order_details")
    cursor.execute("DELETE FROM orders")
    cursor.execute("DELETE FROM sales_target")
    conn.commit()

    # ----------------------------
    # ORDERS
    # ----------------------------
    orders_df = pd.read_csv("/home/unix16/airflow/data/List of Orders.csv")
    orders_df.columns = ["order_id", "order_date", "customer_name", "state", "city"]
    orders_df.drop_duplicates(inplace=True)
    orders_df.to_sql("orders", conn, if_exists="append", index=False)
    logging.info("Orders table loaded successfully")

    # ----------------------------
    # ORDER DETAILS
    # ----------------------------
    details_df = pd.read_csv("/home/unix16/airflow/data/Order Details.csv")
    details_df.columns = ["order_id", "amount", "profit", "quantity", "category", "sub_category"]
    details_df.drop_duplicates(inplace=True)
    details_df.to_sql("order_details", conn, if_exists="append", index=False)
    logging.info("Order details table loaded successfully")

    # ----------------------------
    # SALES TARGET
    # ----------------------------
    target_df = pd.read_csv("/home/unix16/airflow/data/Sales target.csv")
    target_df.columns = ["month", "category", "target"]
    target_df.drop_duplicates(inplace=True)
    target_df.to_sql("sales_target", conn, if_exists="append", index=False)
    logging.info("Sales target table loaded successfully")

    conn.commit()
    conn.close()

    logging.info("Data loaded successfully")

if __name__ == "__main__":
    load_data()
