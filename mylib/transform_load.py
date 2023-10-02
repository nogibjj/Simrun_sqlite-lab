"""
Transforms and Loads data into the local SQLite3 database
Example:
"Show Number", "Air Date", "Round", "Category", "Value", "Question", "Answer"
"""
import sqlite3
import pandas as pd
from pprint import pprint

def load(the_query):
    dataset = "data/Jeopardy.csv"
    df = pd.read_csv(dataset)
    connect = sqlite3.connect("JeopardyDB.db")

    df.to_sql("table1", connect, if_exists="replace", index=False)
    cursor = connect.cursor()
    cursor.execute(the_query)
    connect.commit()
    connect.close()
  
