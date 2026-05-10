import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

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
            host=host,
            user=user,
            password=password,
            database=db,
            port=int(port) if port else 3306,
            charset='utf8mb4'
        )

   
    return create_engine("mysql+pymysql://", creator=connector)