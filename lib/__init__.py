# lib/config.py
import sqlite3

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()
CURSOR.execute("PRAGMA foreign_keys = ON")  
CONN.commit()