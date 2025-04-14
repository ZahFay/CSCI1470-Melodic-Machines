# https://github.com/tbertinmahieux/MSongsDB/blob/master/Tasks_Demos/NamesAnalysis/list_all_artists.py

import hdf5_utils
import hdf5_getters as GETTERS

def retrieve_artist(path):
    h5 = hdf5_utils.open_h5_file_read(path)
    name = GETTERS.get_artist_name(h5)

def list_all(path):
    pass