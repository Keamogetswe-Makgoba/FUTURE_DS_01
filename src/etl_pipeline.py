import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from data_cleaner import clean_sales_data 

load_dotenv()

def get_db_engine():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")

    def connector():
        import pymysql
        return pymysql.connect(
            host=host, user=user, password=password,
            database=db, port=int(port) if port else 3306,
            charset='utf8mb4'
        )
    return create_engine("mysql+pymysql://", creator=connector)

def run_etl():
    print("--- Starting ETL Process ---")
    
    # We extract the data
    file_path = 'data/raw/Sample - Superstore.csv'
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return
    df = pd.read_csv(file_path, encoding='latin1')

    #  Now we standardize the data
    df.columns = [c.lower().replace(' ', '_').replace('-', '_') for c in df.columns]
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['ship_date'] = pd.to_datetime(df['ship_date'])

    # Transform
    print("Executing advanced cleaning...")
    df = clean_sales_data(df)

    # LOAD
    try:
        engine = get_db_engine()
        print(f"Loading data into {os.getenv('DB_NAME')}...")
        df.to_sql('sales_data_clean', con=engine, if_exists='replace', index=False)
        print("ETL Job Finished Successfully!")
    except Exception as e:
        print(f"Database Error: {e}")

if __name__ == "__main__":
    run_etl()