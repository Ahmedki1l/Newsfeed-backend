import mysql.connector
from config import db_config

def get_db_connection():
    """Establishes a connection to the database."""
    conn = mysql.connector.connect(**db_config)
    return conn
