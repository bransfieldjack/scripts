import numpy as np
import pandas as pd
import functools 
import csv
import pymongo
from pymongo import MongoClient


"""
iMac atlas PCA coordinates conversion script. 
"""

def main():

    MONGO_URI='mongodb://localhost:27017'

    """
    imac_atlas_coordinates.tsv
    """
    imac_coords_df = pd.read_csv('imac_atlas_coordinates.tsv', sep='\t', index_col=0)
    imac_coords_df.reset_index(level=0, inplace=True)
    imac_coords_df.columns = ['index', 'x', 'y', 'z']
    temp = imac_coords_df.to_dict('records')   # List of dictionaries. 
    myclient = pymongo.MongoClient(MONGO_URI) # Mongon container name is 'mongo'. # local mongodb server.   # Connects to the mongodb daabase and returns everything.
    database = myclient["imac_v1"]
    collection = database["pca_coordinates"]
    result = collection.insert_many(temp)
    print("Operation complete")

if __name__ == "__main__":
    main()



