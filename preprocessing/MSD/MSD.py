
# https://carpentry.library.ucsb.edu/2021-08-23-ucsb-python-online/09-working-with-sql/index.html

import csv
import sqlite3
import pandas as pd
from os import listdir
from os.path import isfile, join

def retrieve_artist_trackID(path):
    con = sqlite3.connect(path)
    df = pd.read_sql_query('SELECT artist_name,track_id FROM songs', con)
    df['artist_name'] = df['artist_name'].str.lower().str.strip() #turn all artist names to lowercase and get rid of punctuation
    df.to_csv('MSD_artists_trackIDS.csv', index=False)

def retrieve_unique_artists(path):
    con = sqlite3.connect(path)
    df = pd.read_sql_query('SELECT artist_name FROM songs', con)
    df.drop_duplicates(inplace= True)
    df['artist_name'] = df['artist_name'].str.lower().str.strip() 
    df.to_csv('MSD_artists_unique.csv', index=False)

def reconstruct_lyrics(artists, lyrics):
    pass

def artist_intersection(msd, fma):
    msd_df = pd.read_csv(msd)
    msd_df.rename(columns={'artist_name': 'name'}, inplace=True) #rename column to merge
    fma_df = pd.read_csv(fma)
    df_merged = pd.concat([msd_df, fma_df], ignore_index=True)
    duplicates = df_merged[df_merged.duplicated()]
    duplicates.to_csv('MSD_FMA_artists.csv', index=False)

def merge_famous_artists(path):
    #https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    mainframe = pd.DataFrame(columns=['artist','lyric'])
    for file in onlyfiles:
        file_path = path + "/" + file
        df = pd.read_csv(file_path, index_col=0)
        df.columns = df.columns.str.lower()
        df.drop(columns=['title','album','year','date'], inplace=True)
        df['artist'] = df['artist'].str.lower().str.strip() 
        df['lyric'] = df['lyric'].str.lower().str.strip()
        mainframe = pd.concat([mainframe, df], ignore_index= True)
    mainframe.to_csv('famous_artist_lyrics.csv', index=False)
            
if __name__ == "__main__":
    #path variables
    PATH_METADATA = './track_metadata.db'
    PATH_LYRICS = './mxm_dataset.db'
    PATH_FMA = '../FMA/FMA_artists.csv'
    PATH_MSD = './MSD_artists_unique.csv'
    PATH_MSD_TRACKS = './MSD_artists_trackIDS.csv'
    PATH_FAMOUS_LYRICS = './famous artists/csv'

    # retrieve_unique_artists(PATH_METADATA)
    # retrieve_artist_trackID(PATH_METADATA)
    # artist_intersection(PATH_MSD, PATH_FMA)
    merge_famous_artists(PATH_FAMOUS_LYRICS)