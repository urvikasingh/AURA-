from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQL Server connection (Windows Authentication)
DATABASE_URL = (
    "mssql+pyodbc://DESKTOP-1D8S0U8\SQLEXPRESS/"
    "aura_db?"
    "driver=ODBC+Driver+17+for+SQL+Server&"
    "trusted_connection=yes"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
