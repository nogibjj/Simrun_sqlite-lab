"""Query the database"""

import sqlite3


def query(the_query):
    """Query the database for all rows of the PatientDB table"""
    conn = sqlite3.connect("PatientDB.db")
    cursor = conn.cursor()
    sql_query = ''' 
    SELECT "Effectiveness of care national comparison", 
       "Readmission national comparison", 
       "Facility Name", 
       "State" FROM patientDB
       WHERE "State" = 'NC';
       '''
    cursor.execute(sql_query)
    for row in cursor.fetchall():
        print(row)
    conn.close()
    return 


