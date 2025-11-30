import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Charge le fichier .env
load_dotenv()  

# Récupération des variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")


def create_db_engine():
    url = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    return create_engine(url)
