import pandas as pd
import sqlite3
import logging

logging.basicConfig(level=logging.INFO)
DB_PATH = "/home/unix16/airflow/data/infosys.db"

def transform_data():
    raise Exception("Test Email Alert")
    logging.info("Transformation started")
    conn = sqlite3.connect(DB_PATH)

    # ----------------------------
    # CLEAN ORDERS
    # ----------------------------
    orders_df = pd.read_sql("SELECT * FROM WRONG_TABLE", conn)

    orders_df.dropna(subset=["order_id"], inplace=True)
    orders_df["order_date"] = pd.to_datetime(orders_df["order_date"], errors="coerce")
    orders_df["customer_name"] = orders_df["customer_name"].str.strip()
    orders_df["state"] = orders_df["state"].str.lower()
    orders_df["city"] = orders_df["city"].str.lower()

    orders_df.to_sql("clean_orders", conn, if_exists="replace", index=False)
    logging.info("Clean Orders table created!")

    # ----------------------------
    # CLEAN ORDER DETAILS
    # ----------------------------
    details_df = pd.read_sql("SELECT * FROM order_details", conn)

    details_df["amount"] = pd.to_numeric(details_df["amount"], errors="coerce")
    details_df["profit"] = pd.to_numeric(details_df["profit"], errors="coerce")

    details_df = details_df[details_df["quantity"] > 0]
    details_df = details_df[details_df["amount"] >= 0]

    details_df.dropna(inplace=True)

    details_df.to_sql("clean_order_details", conn, if_exists="replace", index=False)
    logging.info("Clean Order Details table created!")

    # ----------------------------
    # CLEAN SALES TARGET
    # ----------------------------
    target_df = pd.read_sql("SELECT * FROM sales_target", conn)

    target_df["target"] = pd.to_numeric(target_df["target"], errors="coerce")
    target_df["category"] = target_df["category"].str.lower()

    target_df.dropna(inplace=True)

    target_df.to_sql("clean_sales_target", conn, if_exists="replace", index=False)
    logging.info("Clean Sales Target table created!")

    conn.close()

    logging.info("Transformation completed")


if __name__ == "__main__":
    transform_data()
