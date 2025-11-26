import sqlite3
from detetime import datetime

DB_file = 'student.db'
def get_connection():
    """Get database connection"""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  
    return conn
# def init_database():
#     """Intialize database and create tables"""
#     conn = get_connection()
