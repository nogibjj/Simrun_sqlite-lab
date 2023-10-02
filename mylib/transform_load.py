"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""
import sqlite3
import csv
import os


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/Jeopardy.csv"):
    """ "Transforms and Loads data into the local SQLite3 database"""

    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    print(payload)
    file = "JeopardyDB.db"
    conn = sqlite3.connect(file)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS JeopardyDB")
    c.execute(
        """
    CREATE TABLE JeopardyDB 
    ("Show Number", "Air Date", "Round", "Category", "Value", "Question", "Answer")"""
    )
    # insert
    c.executemany("INSERT INTO JeopardyDB VALUES (?, ?, ?, ?, ?, ?, ?)", payload)

    conn.commit()
    conn.close()
    return "JeopardyDB.db"
