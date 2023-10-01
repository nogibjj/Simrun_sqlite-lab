"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""
import sqlite3
import csv
import os

#load the csv file and insert into a new sqlite3 database
def load(dataset="/workspaces/Simrun_sqlite-lab/data/patient.csv"):
    """"Transforms and Loads data into the local SQLite3 database"""

    #prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    conn = sqlite3.connect('PatientDB.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS PatientDB")
    c.execute(
    """
    CREATE TABLE PatientDB 
    (Facility ID,Facility Name,Address,City,State,ZIP Code,County Name,Phone Number,
    HCAHPS Measure ID,HCAHPS Question,HCAHPS Answer Description,Patient Survey Star Rating,
    Patient Survey Star Rating Footnote,HCAHPS Answer Percent,HCAHPS Answer Percent Footnote,
    HCAHPS Linear Mean Value,Number of Completed Surveys,Number of Completed Surveys Footnote,
    Survey Response Rate Percent,Survey Response Rate Percent Footnote,Start Date,End Date,Year,
    Hospital Type,Hospital Ownership,Emergency Services,Meets criteria for promoting interoperability of EHRs,
    Hospital overall rating,Hospital overall rating footnote,Mortality national comparison,
    Mortality national comparison footnote,
    Safety of care national comparison,Safety of care national comparison footnote,
    Readmission national comparison,Readmission national comparison footnote,Patient experience national comparison,
    Patient experience national comparison footnote,Effectiveness of care national comparison,
    Effectiveness of care national comparison footnote,Timeliness of care national comparison,
    Timeliness of care national comparison footnote,
    Efficient use of medical imaging national comparison,
    Efficient use of medical imaging national comparison footnote)"""
             )
    #insert
    c.executemany("INSERT INTO PatientDB VALUES "(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", payload)
    conn.commit()
    conn.close()
    return "PatientDB.db"

