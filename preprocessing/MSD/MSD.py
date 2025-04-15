
# https://carpentry.library.ucsb.edu/2021-08-23-ucsb-python-online/09-working-with-sql/index.html

import csv
import sqlite3
import pandas as pd

def retrieve_artist(path):
    con = sqlite3.connect(path)
    cur = con.cursor()
    df = pd.read_sql_query('SELECT artist_name,track_id FROM songs', con)
    df.to_csv('MSD_artists_trackIDS.csv', index=False)
            
if __name__ == "__main__":
    path = './track_metadata.db'
    retrieve_artist(path)