
# https://carpentry.library.ucsb.edu/2021-08-23-ucsb-python-online/09-working-with-sql/index.html

import csv
import sqlite3
import pandas as pd

def retrieve_artist_trackID(path):
    con = sqlite3.connect(path)
    cur = con.cursor()
    df = pd.read_sql_query('SELECT artist_name,track_id FROM songs', con)
    df['artist_name'] = df['artist_name'].str.lower() #turn all artist names to lowercase
    df['artist_name'] = df['artist_name'].str.strip() #get rid of punctuation
    df.to_csv('MSD_artists_trackIDS.csv', index=False)

def retrieve_unique_artists(path):
    con = sqlite3.connect(path)
    cur = con.cursor()
    df = pd.read_sql_query('SELECT artist_name FROM songs', con)
    df.drop_duplicates(inplace= True)
    df['artist_name'] = df['artist_name'].str.lower() #turn all artist names to lowercase
    df['artist_name'] = df['artist_name'].str.strip() #get rid of punctuation
    df.to_csv('MSD_artists_unique.csv', index=False)

def reconstruct_lyrics(artists, lyrics):
    pass

def artist_intersection(msd, fma):
    pass
            
if __name__ == "__main__":

    #path variables
    PATH_METADATA = './track_metadata.db'
    PATH_LYRICS = './mxm_dataset.db'
    PATH_FMA = '../FMA/FMA_artists.csv'
    PATH_MSD = './MSD_artists_unique.csv'
    PATH_MSD_TRACKS = './MSD_artists_trackIDS.csv'

    retrieve_unique_artists(PATH_METADATA)
    retrieve_artist_trackID(PATH_METADATA)