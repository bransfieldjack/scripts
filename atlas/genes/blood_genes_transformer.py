import numpy as np
import pandas as pd
import functools 
import csv
import pymongo
from pymongo import MongoClient


"""
Converts the existing atlas blood genes file to a mongo collection.
"""

def main():

    MONGO_URI='mongodb://localhost:27017'

    """
    blood_atlas_samples_v7.1.tsv
    Construct a dataframe from the text file dump and convert into a new format with new column/fields. 
    """

    blood_genes_df = pd.read_csv('data/blood/blood_atlas_genes_v7.1.tsv', sep='\t', index_col=0)
    blood_genes_df.reset_index(level=0, inplace=True)

    _dicts = blood_genes_df.to_dict('records')
   
    myclient = pymongo.MongoClient(MONGO_URI) # Mongon container name is 'mongo'. # local mongodb server.   # Connects to the mongodb daabase and returns everything.
    database = myclient["blood_v1"]
    collection = database["genes"]
    result = collection.insert_many(_dicts)

    print("Operation complete")


if __name__ == "__main__":
    main()


