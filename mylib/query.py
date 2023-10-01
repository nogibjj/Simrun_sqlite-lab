"""Query the database"""

import sqlite3


def query(the_query):
    """Query the database for all rows of the PatientDB table"""
    conn = sqlite3.connect("PatientDB.db")
    cursor = conn.cursor()
    cursor.execute(the_query)
    rows = cursor.fetchall()
    print(rows)
    conn.close()
    return rows


